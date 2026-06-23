# Round-2 audit — 3 independent blind verifiers + numeric triangulation on `round2_response.md`

> Date 2026-06-22. THREE blind fresh-context adversarial audits (contribution-altering reply ⇒ full 3-audit
> treatment) + orchestrator numerics (`code/verify_round2.py`). **Convergent verdict: GPT's round-2 results are
> VERIFIED.** The clean FAST/CASCADE forms are refuted by a correct offline `√(d/k)` floor; the contribution is
> RESHAPED (richer, d-dependent), **not killed**. Convention: `rounds/README.md`.

---

## Audit A — offline `Ω(√(d/k))` lower bound (§1). **VERDICT: THEOREM CORRECT (93%).**
Every step recomputed: **Step 1** balance `|m_c−m_{c'}|≤nD/d` ⇒ `m_c≥αn/2k` for `D≤αd/2k` ✓ (and `m_c` is
*deterministic* given the coloring, which cleanly resolves the Step1↔Step3 junction). **Step 2** the Bernoulli→
exactly-d conditioning identity ✓, `Pr(C)≥(c0/√d)^T` ✓, divide-by-Pr(C) direction ✓; **the load-bearing point —
rows of B are independent given the coloring because the union bound is over DETERMINISTIC colorings, so χ⊥B —
holds** ✓ (an adaptive/offline coloring is covered exactly because the `k^T` union bound spans every deterministic
χ). **Step 3** `Var(Y_c)=Θ(d/k)` ✓, max-atom `≤C√(k/d)` valid since `mp(1−p)=Θ(d/k)→∞` ✓, `u^{k−1}` row bound ✓.
**Step 4** `u=Θ(c)<1` const ✓, exponent `exp(O(n log dk)−Ω(nk))` ✓, gating `k≥C log(dk)` exact ✓. **Application**
at `d=Θ(L²/log L),k=Θ(L)`: `k≥C log(dk)` holds (`L≫log L`), `d/k=Θ(L/log L)→∞`, `√(d/k)=Θ(√(L/log L))→∞` ✓.
**No contradiction with P1** (k=2 excluded by the gating hypothesis `2≥C log(2d)` fails). **Refutes** `ondisc_k=O(max{1,L/k})`
at that parameter box (offline ≤ online). Cleanest form: *∃ c,C(α,β): if `αn≤T≤βn`, `k≥C log(dk)`, `d≤n/2`, then
`Pr[offdisc_k ≥ c√(d/k)] ≥ 1−exp(−Ω(nk))`.*

## Audit B — aggregate cover lemma (§5, eqs 16–19). **VERDICT: CLAIM 1 & 2 CORRECT (97%), BANKABLE.**
(a) cover ⟹ ∃φ, indicator ≤ #φ ✓; (b) `Pr(∀c)=Π_j q^h(A_j)` by independence, empty-block `q(∅)=1` ✓; (c) the
relaxation to `Σ_{Σa_j=k}Π_j E_{a_j}=[z^k](Σ_a E_a z^a)^d` is a valid UPPER bound (drops disjointness/cover, all
terms `≥0`, so relaxed ≥ true termwise) ✓ (auditor numerics: 400/400 instances `LHS≤RHS`, equality at d=1); (d)
`E_a≤C(k,a)ρ^a ⇒ Σ E_a z^a ⪯ (1+ρz)^k` coefficientwise ⇒ `[z^k](·)^d ≤ C(kd,k)ρ^k ≤ (ed)^k ρ^k` ⇒ `(edρ)^k` ✓
(`C(kd,k)≤(ed)^k` numerically ✓). **(e) aggregate moments `E_a` genuinely suffice — `max_{|A|=a} q(A)` appears
NOWHERE.** ⇒ **max-cylinder control is UNNECESSARY.** Caveat (flagged, non-blocking): iid sampling; without-
replacement costs the asserted `O(d²/n)` coupling; and the hypothesis must include `a=k` (`E_k=(1/n)#{F(i)=[k]}≤ρ^k`).

## Audit C — monotonicity, regime logic, HS-lower (§2,3,7). **VERDICT: all CONFIRMED (93%).**
- **(1a)** the `d=2` stream `D_m=1 < D_{m+1}≥2` is a valid pathwise non-monotonicity ✓. **(1b)** independent backward-
  induction reproduces **`ondisc_2=11/9, ondisc_3=13/9, ondisc_4=1` EXACTLY**; max-disc∈{1,2} so `EV=1+Pr(fail)`,
  `Pr(fail)=2/9,4/9,0`; **`ondisc_2<ondisc_3` is ROBUST ⇒ non-monotone (more colors strictly worse)** ✓. (Minor: GPT's
  k=3 verbal failure-decomposition mislabels *which* sequences give the 2nd `2/9`, but the count/total are exact.)
- **(2a–2d)** all algebra/asymptotics confirmed: `√(d/k)=√(L/log L)→∞` at `(d,k)=(Θ(L²/log L),Θ(L))`; crossover
  `√(d/k)≥L/k ⟺ k≥L²/d=Θ(log L)` at max d; `√(d/k)=o(L)` at k=2 (consistent with P1); floor `<1 ⟺ k>d`, `d≪M`, so the
  floor reaches 1 at `k≍d∈(L,M)⊆` B3's bracket — **pins the disc-1 threshold near `k≍d` at max d** ✓.
- **(2e) SCOPE: RESHAPES, does NOT kill.** Target → `Θ(max{1, L/k (or L/log k), √(d/k)})`; the floor bites only in the
  window `log L ≲ k ≲ d`; outside it the original survives. Still a clean, matching-able/tight characterization, and
  it **ADDS novelty by breaking A-T's d-independence for k>2**. **Contingency: the payoff now hinges on a matching
  ONLINE upper across the new `√(d/k)`-dominated regime** (the lower alone doesn't kill).
- **(3) HS-lower obstruction VALID** against the subset-counting class; `O(kdp_r)=o(1)` first-moment is right; agrees
  with **B1** (forbidden sets share history) and **B2** (can't beat the fixed-projection `Ω(L/k)` cap by this branching).
  HS-lower (`Ω(L/log k)`) remains **OPEN**, not refuted.

## Orchestrator numerics (`code/verify_round2.py`)
- **Monotonicity (exact DP):** `ondisc_2=11/9, ondisc_3=13/9, ondisc_4=1` — reproduced exactly; non-monotone confirmed.
- **Offline floor:** aggressive local-search offline minimization (an UPPER bound on `offdisc_k`) never collapses to
  `O(1)` when `d/k≫1` and grows with `d/k` (e.g. `d=64,k=4→13`; `d=144,k=12→18`); achieved `≈ (3–6)·√(d/k) > √(d/k)` —
  consistent with `offdisc_k ≥ c√(d/k)`, `c≤1` (local search is a weak optimizer, so this is supportive, not tight;
  the rigorous support is Audit A).

---

## Classification & banking
- **MAJOR VERIFIED PROGRESS + a contribution-altering REFUTATION — NOT a kill.** Bank:
  - **P7 (NEW)** offline floor `offdisc_k ≥ c√(d/k)` (hence `ondisc_k ≥ c√(d/k)`) for `k≥C log(dk)`, `d/k→∞` — Audit A.
  - **P8 (NEW)** aggregate cover lemma: `Pr(level-r cover|h) ≤ (edρ)^k + O(d²/n)` under the AGGREGATE condition
    `(AM): (1/n)Σ_{i:R_i=r} C(|F_r(i)|,a) ≤ C(k,a)ρ^a ∀a` — Audit B. (max-cylinder unnecessary.)
  - **N5 (NEW refuted):** the clean forms `Θ(max{1,L/k})` (fast) and `Θ(max{1,L/log k})` (cascade) as the FULL answer —
    refuted by P7 at the top of the d-range. The corrected answer carries a `√(d/k)` term.
  - **Monotonicity of `ondisc_K` in K: REFUTED** (record alongside the B-note) — no monotonicity lemma usable.
- **No proof-of-death ⇒ no kill.** But the **contribution shape + the k-regime change ⇒ HUMAN GATE (c)** (scope).
- **Confidence (reshaped):** see ledger — the cascade/fast forks now describe only the small-k online-term regime
  (`k ≲ log L` at max d); the overall tight result additionally needs a matching ONLINE upper for the `√(d/k)` regime.

## Single biggest risk going forward
The **matching ONLINE upper bound for the `√(d/k)`-dominated middle regime** (`log L ≲ k ≲ d`) is unproven — even the
offline `O(√(d/k))` upper must be (re)confirmed and then achieved online. Without it, we have a sharper LOWER bound
but not a tight characterization.

## OUTCOME (what the orchestrator did)
1. Banked P7, P8, N5 + the monotonicity refutation into the ledger substrate.
2. Ran the mandatory paper-orientation health-check (`docs/HEALTH_CHECK_gate_c.md`).
3. **Fired HUMAN GATE (c)** — presented the corrected `Θ(max{1, online-term, √(d/k)})` characterization, the relocated
   constant-disc target (`k≍d∨L`), the new matching-upper risk, and the (richer, more novel, NOT dead) reframing for
   the owner's scope decision. Did NOT silently proceed (contribution altitude changed).
