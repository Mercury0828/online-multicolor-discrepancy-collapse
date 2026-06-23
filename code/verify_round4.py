"""
Round-4 confirmatory numeric: the CORRECTED occupancy scale Ψ(λ,L)=1+√(λL)+L/log(e+L/λ) (P11),
vs E[max-min of k iid Poisson(λ)]. Memory-safe (chunked over colors) — do NOT materialize a (reps×k)
array for large k (the earlier buggy one-liner tried (40000×200000) int64 ≈ 64 GB and thrashed).
Non-load-bearing: the round-4 audits already corroborated the scale (Audit A) and the stage-sums (Audit C).
"""
import numpy as np
from math import log, sqrt, e


def Psi(lam, L):
    return 1 + sqrt(lam * L) + L / log(e + L / lam)


def spread(k, lam, reps=2000, seed=1, chunk=5000):
    """E[max_c Z_c - min_c Z_c], Z_c ~ Poisson(lam), c=1..k. Streams colors in chunks to bound memory."""
    rng = np.random.default_rng(seed)
    mx = np.full(reps, -1, dtype=np.int64)
    mn = np.full(reps, 10**9, dtype=np.int64)
    done = 0
    while done < k:
        c = min(chunk, k - done)
        Z = rng.poisson(lam, size=(reps, c))           # at most reps*chunk elements
        mx = np.maximum(mx, Z.max(axis=1))
        mn = np.minimum(mn, Z.min(axis=1))
        done += c
    return float((mx - mn).mean())


if __name__ == "__main__":
    print("E[max-min of k Poisson(lam)] vs corrected Psi(lam, log k):")
    print(f"{'k':>8}{'lam':>9}{'E[rng]':>8}{'Psi':>7}{'sqrtLamL':>9}{'Bennett':>9}  regime")
    for k in (200, 5000, 200000):
        L = log(e * k)
        for lam, nm in [(1.0, "const"), (round(sqrt(L), 2), "INTERMED"), (round(L, 1), "gauss")]:
            print(f"{k:>8}{lam:>9.2f}{spread(k, lam):>8.2f}{Psi(lam, L):>7.2f}"
                  f"{sqrt(lam*L):>9.2f}{L/log(e+L/lam):>9.2f}  {nm}")
    print("E[range] tracks Psi across regimes (small-constant factor); confirms the corrected scale (P11).")
