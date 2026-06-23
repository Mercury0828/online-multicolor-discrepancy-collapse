"""
Numeric triangulation of GPT-5.5-Pro round-2 claims (alongside the 3 blind audits).

(A) Offline sqrt(d/k) floor: aggressive offline local-search minimization of max coordinate range; check the
    best achievable max-range scales like ~ c*sqrt(d/k) and does NOT go below it (supports the LOWER bound).
(B) Exact n=3,d=2,T=4 optimal-online expected discrepancy via full expectimax DP; check ondisc_2=11/9,
    ondisc_3=13/9, ondisc_4=1 and the NON-monotonicity ondisc_2 < ondisc_3.
"""
import numpy as np
from itertools import product
from fractions import Fraction


# ---------- (A) offline sqrt(d/k) floor -------------------------------------
def offline_min_range(n, T, d, k, seed=0, sweeps=40):
    """Heuristic offline minimizer of max_i range. Start balanced-random; local search: repeatedly recolor the
       arrival that most reduces the current global max range. Returns achieved max range (an UPPER bound on
       offdisc_k; if it plateaus ~ sqrt(d/k) that supports the floor)."""
    rng = np.random.default_rng(seed)
    supports = [rng.choice(n, size=d, replace=False) for _ in range(T)]
    col = rng.integers(0, k, size=T)                      # current coloring
    S = np.zeros((n, k), dtype=np.int64)
    for t in range(T):
        S[supports[t], col[t]] += 1

    def coord_range(rows):
        sub = S[rows]
        return (sub.max(axis=1) - sub.min(axis=1)).max()

    def global_max():
        return int((S.max(axis=1) - S.min(axis=1)).max())

    order = np.arange(T)
    for _ in range(sweeps):
        rng.shuffle(order)
        improved = False
        gm = global_max()
        for t in order:
            rows = supports[t]
            # only bother if this arrival touches a near-max coordinate
            if coord_range(rows) < gm - 1:
                continue
            best_c, best_val = col[t], None
            S[rows, col[t]] -= 1
            for c in range(k):
                S[rows, c] += 1
                v = coord_range(rows)
                S[rows, c] -= 1
                if best_val is None or v < best_val:
                    best_val, best_c = v, c
            S[rows, best_c] += 1
            if best_c != col[t]:
                col[t] = best_c
                improved = True
        if not improved:
            break
    return global_max()


def run_offline_floor():
    print("=== (A) offline min max-range vs sqrt(d/k)  (best of 3 seeds; expect ~ c*sqrt(d/k), c<1) ===")
    print(f"{'n':>6} {'d':>4} {'k':>4} {'sqrt(d/k)':>10} {'offline_min':>12} {'ratio':>7}")
    for (n, d, k) in [(4000, 16, 4), (4000, 32, 4), (4000, 64, 4), (4000, 64, 8),
                      (4000, 64, 16), (8000, 100, 10), (8000, 100, 25), (8000, 144, 12)]:
        T = n
        vals = [offline_min_range(n, T, d, k, seed=s) for s in range(3)]
        best = min(vals)                                   # best coloring found = tightest upper bound
        sq = (d / k) ** 0.5
        print(f"{n:>6} {d:>4} {k:>4} {sq:>10.2f} {best:>12} {best/sq:>7.2f}   runs={vals}")
    print("  (If offline_min tracks sqrt(d/k) and never collapses to O(1) when d/k>>1, the floor is supported.)")


# ---------- (B) exact n=3,d=2,T=4 optimal-online expected discrepancy --------
EDGES = [(0, 1), (0, 2), (1, 2)]   # triangle on vertices {0,1,2}, d=2

def ondisc_exact(k, T=4, n=3):
    """Optimal-online expected (prefix-max) discrepancy via expectimax DP with exact Fraction arithmetic.
       State: loads = tuple over vertices of tuple over colors; plus running max so far.
       At each step: edge ~ uniform(EDGES); player sees it, picks color minimizing expected future max."""
    from functools import lru_cache

    def vrange(loadv):
        return max(loadv) - min(loadv)

    # loads as nested tuple; use memo keyed by (loads, t, curmax)
    memo = {}

    def value(loads, t, curmax):
        if t == T:
            return Fraction(curmax)
        key = (loads, t, curmax)
        if key in memo:
            return memo[key]
        total = Fraction(0)
        for (a, b) in EDGES:                               # uniform edge
            best = None
            for c in range(k):                              # player minimizes (online: sees edge, then colors)
                nl = [list(v) for v in loads]
                nl[a][c] += 1
                nl[b][c] += 1
                m2 = max(curmax, vrange(nl[a]), vrange(nl[b]))
                nlt = tuple(tuple(v) for v in nl)
                val = value(nlt, t + 1, m2)
                if best is None or val < best:
                    best = val
            total += best
        res = total / len(EDGES)
        memo[key] = res
        return res

    init = tuple(tuple(0 for _ in range(k)) for _ in range(n))
    return value(init, 0, 0)


def run_monotonicity():
    print("\n=== (B) exact ondisc_k on n=3,d=2,T=4 (expect 11/9, 13/9, 1; NON-monotone 11/9<13/9) ===")
    for k in (2, 3, 4):
        v = ondisc_exact(k)
        print(f"   ondisc_{k} = {v} = {float(v):.4f}")
    v2, v3 = ondisc_exact(2), ondisc_exact(3)
    print(f"   monotone non-increasing? ondisc_2<=ondisc_3 ?  {v2} vs {v3}  ->  "
          f"{'NON-MONOTONE (k=2->3 increases)' if v2 < v3 else 'monotone here'}")


if __name__ == "__main__":
    run_monotonicity()
    run_offline_floor()
