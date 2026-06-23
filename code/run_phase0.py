"""
Phase-0 de-risk experiment driver. Runs Sim A (Gamma) + Sim B (curve), prints a report,
saves JSON. Fixed seeds. Directional only (loglog n ~ 3-4, M ~ 5 at feasible n).
"""
import json, time
from math import log
from sim_collapse import sim_A, sim_B, M_scale

OUT = {}

def banner(s):
    print("\n" + "=" * 78 + "\n" + s + "\n" + "=" * 78)

# --- scales we can afford ---------------------------------------------------
# n, loglog n (nat), M = log n/loglog n
for n in (2000, 20000, 200000):
    ln = log(n); print(f"n={n:>7}  ln n={ln:5.2f}  loglog n(nat)={log(ln):4.2f}  M={M_scale(n):4.2f}")

banner("SIM B  --  ondisc_k curve (player=lookahead, d=2 random graph; max over 3 reps)")
simB = {}
for n in (20000, 200000):
    ks = [2, 3, 4, 5, 6, 8, 12, 20]
    t0 = time.time()
    res = sim_B(n, d=2, ks=ks, seed=7, lam=1.0, player="lookahead", reps=3)
    simB[n] = res
    M = M_scale(n)
    print(f"\n n={n}  M~{M:.2f}   (k : ondisc_k  [runs])")
    for k in ks:
        print(f"   k={k:<3d} ondisc={res[k]['ondisc_max']}   runs={res[k]['ondisc_runs']}")
    print(f"   [{time.time()-t0:.1f}s]")
OUT["simB_d2"] = {str(n): {str(k): v for k, v in r.items()} for n, r in simB.items()}

banner("SIM B  --  d=3 (denser support) for contrast")
simB3 = {}
for n in (20000, 200000):
    ks = [2, 3, 4, 5, 6, 8, 12]
    res = sim_B(n, d=3, ks=ks, seed=11, lam=1.0, player="lookahead", reps=3)
    simB3[n] = res
    print(f"\n n={n} d=3 M~{M_scale(n):.2f}")
    for k in ks:
        print(f"   k={k:<3d} ondisc={res[k]['ondisc_max']}   runs={res[k]['ondisc_runs']}")
OUT["simB_d3"] = {str(n): {str(k): v for k, v in r.items()} for n, r in simB3.items()}

banner("SIM A  --  Gamma-statistic / forbidden-set structure (the (star) discriminator)")
# moderate k where cascade/fast differ (2..M); d=2; large n for more stressed coords.
simA = []
for (n, k) in [(200000, 3), (200000, 4), (200000, 5), (200000, 6),
               (200000, 8), (1000000, 4), (1000000, 6)]:
    t0 = time.time()
    r = sim_A(n, T=n, d=2, k=k, seed=3, lam=1.0, player="lookahead")
    simA.append(r)
    print(f"\n n={n} k={k}  ondisc={r['ondisc']} D_final={r['D_final']}  [{time.time()-t0:.1f}s]")
    for lvl, st in sorted(r["levels"].items(), reverse=True):
        if st.get("count", 0) == 0:
            print(f"   level r={lvl}: (no coords)"); continue
        g = st["gamma"]
        gstr = "  ".join(f"q{q+1}:{g[q]:.3f}" for q in range(len(g)) if g[q] == g[q])
        print(f"   level r={lvl}: #coords={st['count']:>6}  mean|F|={st['mean_fsize']:.2f}"
              f"  |F|-hist={st['fsizes']}")
        print(f"       Gamma(q): {gstr}")
OUT["simA"] = simA

with open("phase0_results.json", "w") as f:
    json.dump(OUT, f, indent=1, default=str)
print("\nsaved -> code/phase0_results.json")
