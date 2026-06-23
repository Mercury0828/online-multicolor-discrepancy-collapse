"""
Phase-0 de-risk simulations for `online-multicolor-discrepancy-collapse`.

Model (Altschuler-Tikhomirov stochastic online Beck-Fiala):
  arrivals v_1..v_T i.i.d. uniform over EXACTLY-d-sparse 0/1 vectors in R^n, T = Theta(n).
  Online k-coloring: each v_t -> chi(t) in [k], irrevocable.
  Color load S_c(t) in Z_{>=0}^n. Coordinate profile x_i = (S_{i,1..k}).
  Pairwise range R_i = max_c x_{i,c} - min_c x_{i,c}.   ondisc_k = max_{t,i} R_i.

We CANNOT settle the optimal-online value (that is theory, HS-core). We use a strong
near-optimal heuristic player to probe the STRUCTURE of forbidden sets (Sim A, the
Gamma-statistic = the (star) lemma discriminator) and the curve shape (Sim B).

Pre-registration (frozen BEFORE running, guide ?Evaluation):
  Sim A:  Gamma_r(q) = -(1/q) log Pr_{A~Unif(C([k],q))}( A subset F_r(v) ), F_r = argmax-color set.
     flat-in-q Gamma  => Q_r(A) ~ rho^|A|  => (star) PLAUSIBLE => CASCADE-favorable.
     Gamma dropping fast in q => big forbidden sets compressed => (star) FALSE => FAST/PLATEAU.
  Sim B:  D(k_j) for k_j = floor(M^{1/j}).  cascade => D ~ j ; fast => ~1 ; plateau => ~loglog n.

Honesty: probes an ALGORITHM + STRUCTURE, NOT the optimal-online matching. Directional only;
loglog n ~ 3-4 and M ~ 5 at feasible n. Fixed seeds; report over-coordinate max.
"""

import numpy as np
from math import comb, log


# ----------------------------------------------------------------------------- player
def run_player(n, T, d, k, rng, lam=1.0, player="lookahead"):
    """
    Online k-coloring. Returns:
      S            : (n,k) final color loads
      ondisc       : max pairwise range over ALL (t, i in support touched) -- prefix max
    Players:
      'lookahead'  : assign v to the color minimizing the resulting max pairwise range over
                     its support, tie-broken by an exponential (soft min-load) potential.
                     Strong near-optimal heuristic for the max-range objective.
      'exp'        : pure exponential potential (soft least-loaded) -- smoother, slightly weaker.
      'greedy'     : assign to the globally-least-loaded color on the support (sum). weak baseline.
    """
    S = np.zeros((n, k), dtype=np.int32)
    ondisc = 0
    for _ in range(T):
        E = rng.choice(n, size=d, replace=False)      # support of the arrival
        sub = S[E]                                     # (d,k) current loads on the support
        if player == "greedy":
            c = int(sub.sum(axis=0).argmin())
        elif player == "exp":
            mean_i = sub.mean(axis=1, keepdims=True)
            w = np.exp(lam * (sub - mean_i)).sum(axis=0)   # (k,) push to soft-least-loaded
            c = int(w.argmin())
        else:  # lookahead: minimize resulting max range on the support, tie-break by exp potential
            best_c, best_key = 0, None
            mean_i = sub.mean(axis=1, keepdims=True)
            expw = np.exp(lam * (sub - mean_i)).sum(axis=0)  # (k,)
            for c in range(k):
                t = sub.copy()
                t[:, c] += 1
                rng_after = (t.max(axis=1) - t.min(axis=1)).max()  # max range over support after
                key = (rng_after, expw[c])
                if best_key is None or key < best_key:
                    best_key, best_c = key, c
            c = best_c
        S[E, c] += 1
        # prefix discrepancy: max range on the just-touched support coordinates
        sub2 = S[E]
        r = int((sub2.max(axis=1) - sub2.min(axis=1)).max())
        if r > ondisc:
            ondisc = r
    return S, ondisc


# ----------------------------------------------------------------------------- Sim A
def gamma_statistic(S, k, levels=(None,)):
    """
    For each discrepancy level r (range value), among coordinates whose range == r,
    compute F = argmax-color set, its size f, then for q=1..k:
        Q(q) = mean over stressed coords of  C(f,q)/C(k,q)      (= Pr_{|A|=q}(A subset F))
        Gamma(q) = -(1/q) log Q(q)
    Returns dict: level r -> {'count', 'fsizes' (hist), 'gamma' (list over q), 'Q' (list)}
    `levels`: iterable of r values; None means "the top two achieved levels".
    """
    rng_per_coord = S.max(axis=1) - S.min(axis=1)            # (n,)
    D = int(rng_per_coord.max())
    out = {}
    target_levels = [L for L in levels if L is not None]
    if not target_levels:
        target_levels = [D, D - 1] if D >= 2 else [D]
    for r in target_levels:
        if r < 1:
            continue
        idx = np.where(rng_per_coord == r)[0]
        if len(idx) == 0:
            out[r] = {"count": 0}
            continue
        mx = S[idx].max(axis=1, keepdims=True)
        fsizes = (S[idx] == mx).sum(axis=1)                  # |argmax| per stressed coord
        # histogram of forbidden-set sizes
        hist = {int(f): int((fsizes == f).sum()) for f in np.unique(fsizes)}
        gamma, Qs = [], []
        for q in range(1, k + 1):
            ckq = comb(k, q)
            # Pr_{|A|=q}(A subset F) = C(f,q)/C(k,q); mean over stressed coords
            vals = np.array([comb(int(f), q) for f in fsizes], dtype=float) / ckq
            Q = float(vals.mean())
            Qs.append(Q)
            gamma.append(float("nan") if Q <= 0 else -(1.0 / q) * log(Q))
        out[r] = {"count": int(len(idx)), "fsizes": hist, "gamma": gamma, "Q": Qs,
                  "mean_fsize": float(fsizes.mean())}
    return out, D


# ----------------------------------------------------------------------------- drivers
def sim_A(n, T, d, k, seed=0, lam=1.0, player="lookahead"):
    rng = np.random.default_rng(seed)
    S, ondisc = run_player(n, T, d, k, rng, lam=lam, player=player)
    stats, D = gamma_statistic(S, k)
    return {"n": n, "T": T, "d": d, "k": k, "seed": seed, "player": player,
            "ondisc": ondisc, "D_final": D, "levels": stats}


def sim_B(n, d, ks, seed=0, lam=1.0, player="lookahead", reps=1):
    """ondisc_k over a sweep of k (max over reps with different seeds = adversarial-over-runs)."""
    T = n
    res = {}
    for k in ks:
        vals = []
        for rep in range(reps):
            rng = np.random.default_rng(seed + 1000 * rep + k)
            _, ondisc = run_player(n, T, d, k, rng, lam=lam, player=player)
            vals.append(ondisc)
        res[k] = {"ondisc_max": int(max(vals)), "ondisc_runs": vals}
    return res


def M_scale(n):
    """M = Theta(log n / loglog n) (natural log), the proven sufficient collapse scale K_fresh."""
    ln = log(n)
    return ln / log(ln)
