# `(★)` De-risk Report — Phase 0 (Sim A Γ-statistic + Sim B curve)

> Date: 2026-06-22. Code: `code/sim_collapse.py`, `code/run_phase0.py`; raw: `code/phase0_results.json`.
> Fixed seeds. Player = `lookahead` (1-step min-max-range, exp-potential tie-break) — a strong near-optimal
> heuristic, NOT provably optimal. **Honesty: probes an ALGORITHM + STRUCTURE; does NOT settle the optimal-
> online matching (the SODA crux `HS-core`).** loglog n (nat) ≈ 2.0–2.5 and M ≈ 3.8–4.9 at feasible n ⇒ COARSE,
> directional only. Pre-registration was frozen before running (guide §Evaluation; reproduced below).

## Pre-registration (frozen before running)
- **Sim A:** `Γ_r(q) = −(1/q) log Pr_{A~Unif(C([k],q))}(A ⊆ F_r(v))`, `F_r` = argmax-color set on stressed coords.
  **flat-in-q Γ ⇒ Q_r(A) ≈ ρ^|A| ⇒ `(★)` PLAUSIBLE ⇒ CASCADE-favorable; Γ dropping fast in q ⇒ big forbidden
  sets compressed ⇒ `(★)` FALSE ⇒ FAST/PLATEAU.**
- **Sim B:** `D(k_j)` for `k_j=⌊M^{1/j}⌋`. cascade ⇒ `D≈j`; fast ⇒ `≈1`; plateau ⇒ `Θ(loglog n)`.

---

## Result 1 — Sim B (curve shape): decreasing + collapse CONFIRMED (directional)

`ondisc_k` (max over 3 reps, prefix max-over-coords range), player=lookahead:

| | k=2 | 3 | 4 | 5 | 6 | 8 | 12 | 20 | M |
|---|---|---|---|---|---|---|---|---|---|
| d=2, n=20 000 | 2 | 2 | 2 | 2 | 2 | 2 | **1** | 1 | 4.32 |
| d=2, n=200 000 | 3 | 3 | 2 | 2 | 2 | 2 | **1** | 1 | 4.88 |
| d=3, n=20 000 | 3 | 3 | 3 | 3 | 2 | 2 | **1** | – | 4.32 |
| d=3, n=200 000 | 4 | 3 | 3 | 3 | 2 | 2 | 2 | – | 4.88 |

- **Monotone decreasing in k and collapses to 1** — P5's qualitative picture holds. Collapse to `disc 1` occurs
  around `k ≈ 2M..3M` (k=12 vs M≈4.9) for d=2; later for d=3 (denser ⇒ higher anchor, slower collapse).
- **NOT a plateau** hugging small k (which would have stayed `≈loglog n` across all k) — this **pushes the
  plateau outcome down**.
- **Cascade vs fast: INDISTINGUISHABLE here** (as pre-registered): `D(2)=3 → D(4)=2 → D(12)=1`; both
  `loglog n/log k` and `loglog n/k` predict `D(4)≈1.5` (observed 2) — the integer levels are too coarse
  (`loglog n ≈ 2.5`) to separate the two forms. **This is the known limitation, not a refutation.**

## Result 2 — Sim A (the `(★)` discriminator): NOT refuted; mildly CASCADE-favorable

The lemma matters at the **binding / stressed top levels** `r = D, D−1` (the coordinates that realize the
discrepancy). Γ(q) and forbidden-set sizes there (d=2):

| n | k | level r | #coords | mean |F| | Γ(q=1,2,3,…) | shape |
|---|---|---|---|---|---|---|
| 200 000 | 4 | **r=2 (top)** | 2 537 | 1.08 | 1.31 → 2.14 → 2.15 | **increasing** |
| 1 000 000 | 4 | **r=2 (top)** | 12 848 | 1.08 | 1.31 → 2.15 → 2.28 | **increasing** (stable across n) |
| 200 000 | 5 | **r=2 (top)** | 656 | 1.05 | 1.56 → 2.68 | increasing |
| 200 000 | 6 | **r=2 (top)** | 77 | 1.01 | 1.78 → 3.53 | increasing |
| 1 000 000 | 6 | **r=2 (top)** | 412 | 1.08 | 1.72 → 2.60 → 2.64 | increasing |
| 200 000 | 4 | r=1 (bulk) | 154 257 | 1.84 | 0.78 → 0.86 → 0.94 | increasing |
| 200 000 | 6 | r=1 (bulk) | 170 458 | 2.23 | 0.99 → 1.01 → 0.98 → 0.96 → 0.99 | ~flat |
| 200 000 | 8 | r=1 (=top, collapsed) | 172 771 | 2.31 | 1.24 → … → 1.08 | mild **decrease** |

**Reading (vs pre-registration):**
- At the **binding stressed levels** `r=D` (r=2,3), forbidden sets are **small — a single leader dominates**
  (mean |F| ≈ 1.0–1.08; histogram overwhelmingly |F|=1). The feared **B1 compression** profile `(D,…,D,0)`
  with `|F|=k−1` does **NOT** dominate the stressed population. Γ(q) is **increasing** ⇒ `Q_r(A)` decays at
  **least geometrically** ⇒ **consistent with `(★)`** (`(★)` allows ≤ ρ^|A|; increasing-Γ is even stronger).
- The only place Γ flattens / mildly drops is the **trivial level r=1** in the **already-collapsed regime**
  (k≥6–8, where `ondisc_k`→1). There r=1 IS the max level, many colors sit tied at 0/1, so |argmax| grows
  with k mechanically. This is the *trivial* collapse, **not** the cascade/fast-deciding stressed regime.
- **Verdict on the lemma:** the de-risk **does not refute `(★)`**; the binding-level structure (small forbidden
  sets, geometric-or-faster Q-decay) is **mildly cascade-favorable**.

## Honesty caveats (do not over-read)
1. **Heuristic player**, not provably optimal. `(★)` must hold for the *optimal* online player and be **stable
   under adaptive online evolution** — the single hardest part of `HS-core`, and exactly what a static-snapshot
   sim cannot certify. The sim shows the *binding-level structure a good player produces* is `(★)`-shaped; it
   does not prove the optimal player cannot induce compression.
2. **Thin top-level statistics**: r=2 has only 77–656 coords at k=5,6; r=3 has 2 coords at k=3. The increasing-Γ
   signal at the very top is real but low-N.
3. **Coarse scale**: `loglog n ≈ 2.5`, `D ≤ 3` ⇒ cannot see an asymptotic tower; cascade vs fast unresolved.
4. The sim is over `μ_{d,n}` (the actual i.i.d. model — legitimate evidence) but probes the structure under an
   algorithm; the optimal-online matching is theory (`HS-core`).

## Net de-risk conclusion
`(★)` survives the Phase-0 probe: decreasing+collapse confirmed (Sim B), and the binding-level forbidden-set
structure is `(★)`-consistent / mildly cascade-favorable (Sim A), with the B1-compression failure mode NOT
observed at stressed levels. **No refutation ⇒ no RED on the science.** Two-of-three outcomes (cascade, fast)
remain live; the plateau outcome is weakly down-weighted. Cascade-vs-fast is for the attack loop, not the sim.
