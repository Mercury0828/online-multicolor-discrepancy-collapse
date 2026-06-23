"""
Independent numeric cross-check of GPT-5.5-Pro round-1 load-bearing arithmetic.
(Triangulates the two adversarial audits — NOT a substitute for them.)

1. Block-compression lemma (eq.1): ondisc_k(merge) ≤ q · (virtual range).  Empirical: for random instances,
   run an online kq-coloring, apply the fixed block-merge to k colors, check real_range ≤ q · virtual_range
   at EVERY prefix.
2. Mixture-law correlations (eq.8-10): the color-symmetric law 1/2·perm(r,0..0) + 1/2·perm(r,..,r,0).
   Check Q({c})=1/2, Q({c,c'})=(k-2)/(2k), Q(|A|=a)=(k-a)/(2k), and ρ_min=(2k)^{-1/(k-1)}.
3. Marginal-violation ratio (eq.11): (t-1)/t · k/(k-1) vs a direct Monte-Carlo of the symmetrized disc-1 process.
"""
import numpy as np
from math import comb
from itertools import combinations


# ---------- 1. block-compression inequality (eq.1) ----------------------------
def check_block_compression(n=3000, T=3000, d=2, k=3, q=4, seed=0, player="exp", lam=1.0):
    K = k * q
    rng = np.random.default_rng(seed)
    Y = np.zeros((n, K), dtype=np.int64)            # virtual loads
    blocks = np.repeat(np.arange(k), q)             # virtual color -> real block
    worst_virtual, worst_real, worst_ratio = 0, 0, 0.0
    viol = 0
    for _ in range(T):
        E = rng.choice(n, size=d, replace=False)
        sub = Y[E]                                  # (d,K)
        mean = sub.mean(axis=1, keepdims=True)
        w = np.exp(lam * (sub - mean)).sum(axis=0)  # soft least-loaded virtual color
        a = int(w.argmin())
        Y[E, a] += 1
        subY = Y[E]
        vr = int((subY.max(axis=1) - subY.min(axis=1)).max())          # virtual range on support
        # real loads on support via block sums
        realsub = np.add.reduceat(subY[:, np.argsort(blocks, kind="stable")],
                                  np.arange(0, K, q), axis=1)           # (d,k) block sums
        rr = int((realsub.max(axis=1) - realsub.min(axis=1)).max())     # real range on support
        worst_virtual = max(worst_virtual, vr)
        worst_real = max(worst_real, rr)
        if rr > q * vr:                              # the lemma asserts this never happens
            viol += 1
        if vr > 0:
            worst_ratio = max(worst_ratio, rr / vr)
    return {"k": k, "q": q, "K": K, "worst_virtual": worst_virtual, "worst_real": worst_real,
            "q*worst_virtual": q * worst_virtual, "max_ratio_rr_over_vr": round(worst_ratio, 3),
            "violations_rr>q*vr": viol}


# ---------- 2. mixture-law correlations (eq.8-10) -----------------------------
def mixture_law_Q(k, a):
    # F = single uniform color (prob 1/2) or [k]\{uniform z} (prob 1/2). Q(A)=Pr(A ⊆ F), |A|=a.
    if a == 1:
        return 0.5 * (1.0 / 1) * 1 + 0.5 * (k - 1) / k   # |F|=1: A(single) ⊆ F iff that color is the one: 1/k... careful
    return None

def mixture_law_exact(k, a):
    # |F|=1 branch: A⊆F with |A|=a≥1 requires F⊇A, but |F|=1 so only possible if a=1 AND F=A.
    #   Pr over uniform single color = (a==1) * (1/k)  ... but we want Pr(A⊆F) for FIXED A.
    # |F|=k-1 branch: F=[k]\{z}, z uniform. A⊆F iff z∉A, prob (k-a)/k.
    p_small = (1.0 / k) if a == 1 else 0.0
    p_broad = (k - a) / k
    return 0.5 * p_small + 0.5 * p_broad

def check_mixture(ks=(5, 6, 8, 12)):
    out = {}
    for k in ks:
        Qs = {a: mixture_law_exact(k, a) for a in range(1, k)}
        # singleton
        Q1 = Qs[1]
        Q2 = Qs[2]
        rho_marginal = Q1            # = max_c Q({c})
        # required rho from the |A|=k-1 constraint: Q(k-1) ≤ rho^{k-1}
        Qmax_a = Qs[k - 1]
        rho_needed = Qmax_a ** (1.0 / (k - 1))
        out[k] = {"Q({c})": round(Q1, 4), "Q({c,c'})": round(Q2, 4),
                  "Q1^2": round(Q1 * Q1, 4), "Q2>Q1^2": Q2 > Q1 * Q1,
                  "Q(a=k-1)": round(Qmax_a, 5), "rho_needed=(2k)^-1/(k-1)": round(rho_needed, 4),
                  "(2k)^-1/(k-1)": round((2 * k) ** (-1.0 / (k - 1)), 4)}
    return out


# ---------- 3. marginal-violation ratio (eq.11) Monte-Carlo -------------------
def check_marginal_ratio(n=20000, d=2, k=40, t=200, seed=1, reps=4000):
    """
    Symmetrized disc-1 fresh-color process proxy: each coordinate's 'used colors' = a uniform random
    size-N subset of [k] where N=deg (degrees from a random d-sparse process up to time t). We test the
    correlation ratio Q({c,c'})/Q({c})^2 against the predicted (t-1)/t * k/(k-1).
    """
    rng = np.random.default_rng(seed)
    # build degrees by throwing t edges of size d onto n coords, count a fixed coordinate's degree dist via sampling
    # Monte-Carlo over coordinate I and history: deg N ~ Binomial(t, d/n)
    pred = (t - 1) / t * k / (k - 1)
    # sample N, then a uniform N-subset, indicator c in F and c,c' in F for fixed c=0,c'=1
    p = d / n
    Ns = rng.binomial(t, p, size=reps)
    c_in = 0; cc_in = 0
    for N in Ns:
        N = min(int(N), k)
        if N == 0:
            continue
        S = rng.choice(k, size=N, replace=False)
        s = set(S.tolist())
        if 0 in s: c_in += 1
        if 0 in s and 1 in s: cc_in += 1
    Q1 = c_in / reps
    Q2 = cc_in / reps
    ratio = (Q2 / (Q1 * Q1)) if Q1 > 0 else float("nan")
    return {"k": k, "t": t, "pred_ratio=(t-1)/t*k/(k-1)": round(pred, 4),
            "MC_Q1": round(Q1, 5), "MC_Q2": round(Q2, 6),
            "MC_ratio_Q2/Q1^2": round(ratio, 4), "t>k": t > k}


if __name__ == "__main__":
    print("=== 1. block-compression lemma  ondisc_k(merge) <= q*virtual_range  (violations must be 0) ===")
    for (k, q) in [(2, 3), (3, 4), (4, 3), (5, 2), (3, 8)]:
        print("  ", check_block_compression(k=k, q=q, seed=k * 10 + q))
    print("\n=== 2. mixture law (eq.8-10): expect Q2>Q1^2 True for k>=5; rho_needed->1 ===")
    for k, v in check_mixture().items():
        print(f"   k={k}: {v}")
    print("\n=== 3. marginal-violation ratio (eq.11): MC ratio ~= pred, both >1 for t>k ===")
    for (k, t) in [(40, 200), (40, 41), (20, 100), (60, 600)]:
        print("  ", check_marginal_ratio(k=k, t=t))
