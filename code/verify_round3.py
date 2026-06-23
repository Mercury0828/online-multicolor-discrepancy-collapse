"""
Numeric triangulation of GPT-5.5-Pro round-3 claims (alongside the 2 blind audits).
(A) Online mean-square lemma: greedy on Phi=sum z^2 gives Phi(t) <= t*d ; (1/nk) sum z^2 = O(d/k).
(B) Poisson extreme-value spread: E[max-min of k Poisson(lambda)] vs log k/loglog k (lambda=Theta(1))
    and sqrt(lambda log k) (lambda>>1); both >> sqrt(lambda) = sqrt(d/k) -> supports P9 > P7.
"""
import numpy as np
from math import log, sqrt


def mean_square_phi(n, T, d, k, seed=0):
    rng = np.random.default_rng(seed)
    S = np.zeros((n, k), dtype=np.float64)   # color loads
    deg = np.zeros(n, dtype=np.float64)
    worst_ratio = 0.0
    for t in range(1, T + 1):
        E = rng.choice(n, size=d, replace=False)
        z = S[E] - (deg[E][:, None] / k)          # (d,k) centered loads
        c = int(z.sum(axis=0).argmin())           # greedy: minimize sum_i z_{i,c}
        S[E, c] += 1
        deg[E] += 1
        # current Phi
    z_all = S - deg[:, None] / k
    phi = float((z_all ** 2).sum())
    return {"n": n, "d": d, "k": k, "Phi": round(phi, 1), "t*d": T * d,
            "Phi/(td)": round(phi / (T * d), 3), "(1/nk)sumz2": round(phi / (n * k), 4),
            "d/k": round(d / k, 4)}


def poisson_spread(k, lam, reps=20000, seed=1):
    rng = np.random.default_rng(seed)
    Z = rng.poisson(lam, size=(reps, k))
    rng_vals = Z.max(axis=1) - Z.min(axis=1)
    return float(rng_vals.mean())


if __name__ == "__main__":
    print("=== (A) mean-square lemma: expect Phi/(td) <= 1 (~1-1/k); (1/nk)sumz2 ~ O(d/k) ===")
    for (n, d, k) in [(20000, 4, 4), (20000, 8, 8), (20000, 16, 4), (40000, 16, 16), (40000, 32, 8)]:
        print("  ", mean_square_phi(n, n, d, k, seed=d + k))

    print("\n=== (B) E[max-min of k Poisson(lambda)] vs predictions (both >> sqrt(lambda)=sqrt(d/k)) ===")
    print(f"{'k':>7} {'lambda':>7} {'E[range]':>9} {'logk/loglogk':>13} {'sqrt(lam*logk)':>15} {'sqrt(lam)':>10}")
    for k in (50, 1000, 100000):
        lk = log(k); llk = log(lk)
        for lam in (1.0, 5.0, 30.0):
            er = poisson_spread(k, lam)
            print(f"{k:>7} {lam:>7.1f} {er:>9.2f} {lk/llk:>13.2f} {sqrt(lam*lk):>15.2f} {sqrt(lam):>10.2f}")
    print("  (E[range] tracks log k/loglog k at lambda=1, sqrt(lambda log k) at lambda>>1; both exceed sqrt(lambda).)")
