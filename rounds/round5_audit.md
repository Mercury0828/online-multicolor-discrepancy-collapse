# Round-5 audit — independent blind verifiers on `round5_response.md`

> Date 2026-06-22. Two blind fresh-context adversarial audits. **Audit B DONE** (bracket / fixed-k / MATCH / L2 no-go / RB).
> **Audit A (the §1 `O(loglog n)` online upper — the load-bearing new result) IN PROGRESS.** Convention: `rounds/README.md`.

## Audit A — §1 the multicolor `O(loglog n)` online upper bound (the A-T extension). **VERDICT: CORRECT (85%).**
- **The flagged crux (seed-tail at small k / large d) HOLDS with a 9× margin.** The prompt's "fails for small k" worry was an
  arithmetic slip (dropped the `32²` factor): with deviation `32H`, the Bernstein numerator is `512H²`, so at k=2, `d=H²/logH`
  the exponent is `512·logH` vs the needed `≈56·logH` for `d^{-28}` ⇒ margin ≈9×. Verified numerically across H and k. **The
  seed tail is the strongest, not the weakest, link.**
- **Algorithm online-valid; the key invariant airtight:** an upcrossing of an exceptional row certifies a *distinct*
  exceptional helper in the support (any supported row with range ≥64H is itself exceptional; the "unique strict max among
  `S_t∩E` vs among all `S_t`" gap closes itself; repair never raises `i*`'s range; no future knowledge). ✓
- **Categories/pigeonhole k-INDEPENDENT:** the linchpin "actual≠seed ⇒ a previously-exceptional row in the column" is true of
  this algorithm and k-free; category depth is indexed by columns, not colors; `16H` modified incidences into `≤6H` categories
  ⇒ promotion; `n·d^{-28} → n·d^{-5}` slack consistent. ✓ **Double-exp recurrence** `|M(T,r)| ≤ n(log n)^{-2·2^r}` drops below 1
  at `r≈1.44H < 2H` ⇒ `max range < 80H`; union over r `= O((loglog n)²/log n) → 0`. No hidden n/log-n loss. ✓
- **No collision with P11:** `Ψ ≤ √((d/k)log k) < H` for all k≥2, so the offline floor stays below `80H` — consistent.
- **Most fragile (residual) step:** the **imported A-T category high-moment recursion** (not reproduced line-by-line). Its
  *interface* (k-free hypotheses) + *bookkeeping* verified; the internal recursion taken on the structural argument. −10% for
  this + −5% asymptotic-only whp constants. **The nominated kill-shot (seed tail) was refuted with margin.**
- ⇒ **`ondisc_k = O(loglog n)` for all k is VALID** (P12). With P2: **`ondisc_k = Θ(loglog n)` for every fixed k (CLOSED).**

## Audit B — bracket / fixed-k / MATCH / L2 no-go / RB reduction. **VERDICT: all CORRECT (88%), 2 corrections.**
- **CLAIM 1 (bracket `c·max{Ψ, loglog n/k} ≤ ondisc_k ≤ C loglog n`): CORRECT** — lower = max of P11 (`online≥offline=Ω(Ψ)`) +
  P2 (`Ω(loglog n/k)`); upper = the (separately-audited) `O(loglog n)`. A genuine bracket with a gap (asserts a bracket, not
  tightness). ✓
- **CLAIM 2 (fixed-k CLOSED `Θ(loglog n)`): CORRECT, airtight** — P2 lower `Ω(loglog n/k)=Ω(loglog n)` for constant k +
  the `O(loglog n)` upper squeeze. The `Ψ` term is dominated/capped. ✓
- 🔴 **CLAIM 3 (MATCH ruled out): CORRECT-BUT-INCOMPLETE.** `ondisc_k ≥ max{Ψ, loglog n/k}`; where `loglog n/k ≫ Ψ`
  (**small/fixed k**, and k=2 via P1) the online value strictly exceeds the offline `Ψ` ⇒ MATCH (`ondisc_k=Θ(Ψ)`) is FALSE
  there. **BUT it is NOT globally ruled out** — for growing k with `loglog n/k ≲ Ψ` (e.g. `k=Θ(loglog n)` and beyond) MATCH
  remains OPEN. **Correct statement: "MATCH ruled out in the small-k slice; open for growing k."** (Do not state a blanket
  "MATCH ruled out".)
- **CLAIM 4 (L2→L∞ no-go): CORRECT.** `R_i≥D ⇒ Σ_c z² ≥ D²/2` (from `M²+m²≥(M−m)²/2`, all reals) ⇒ `#{R_i≥D} ≤ O(nd/D²)`,
  which is `≥ n` at `D≍Ψ` (regime arithmetic verified: λ≳L ⇒ `nk/L > n` since `k/log(ek)>1 ∀k≥2`; λ=Θ(1) ⇒ `k(log L)²/L²·n →∞`).
  The mean-square (P10) provably gives NO useful L∞ control at the entropy scale. (Caveat: rules out the *direct* L2/Markov
  promotion, not every conceivable L∞ argument — but that's all it claims.) ✓
- **CLAIM 5 (RB reduction): CORRECT-BUT-INCOMPLETE.** `R ≤ 1+ρ/(k−1)` ✓; range-raise `Δρ=k−s`, broadening `Δρ=+1` ✓; RB
  (`max ρ ≤ C(kΨ+H)`) ⇒ `ondisc_k = O(Ψ+loglog n/k)` ⇒ (with P2,P11) `Θ(max{Ψ, loglog n/k})` ✓. RB is the **exact sufficient
  missing lemma** (sufficient + calibrated — neither term slack). **INCOMPLETE: RB is UNPROVEN** (the open hard step — exactly
  the L2→L∞/within-level-broadening control the Claim-4 no-go shows the greedy route cannot supply). Soft spots not fully
  discharged: the "other transitions leave ρ non-increasing" case; the whp/union constants in RB.

## Classification — VERIFIED (both audits CORRECT: A 85%, B 88%)
- **Banked: P12** (`ondisc_k = O(loglog n)` ∀k) + **fixed-k CLOSED `Θ(loglog n)`** + the bracket + the L2 no-go. MATCH refuted
  **for small k only** (not global). Growing-k OPEN at the **ranked-broadening lemma (RB)** — the new attack target.
- **🟢🟢 TWO COMPLETE RESULTS** (pending human verification): offline `offdisc_k=Θ(Ψ)` (P11) + online fixed-k `ondisc_k=Θ(loglog n)`
  (P12) — a coherent paper with a genuine **multicolor online-vs-offline separation**. The round-3 "no upper anywhere"
  inflection is **RESOLVED**.
- 🔴 Honesty: NOT "MATCH ruled out" globally — only small-k. "AI-verified ≠ proved": P12 pending human check of the A-T
  category recursion; P11 pending the NA-union + exact-LM.

## OUTCOME (what the orchestrator did)
1. Banked P12 + fixed-k closure + the corrections (ledger). Confidence: P(SODA-worthy paper) ↑ ≈ 0.55–0.65.
2. Ran a milestone health-check (`docs/HEALTH_CHECK_milestone_r5.md`): is this a SODA paper now; attack RB (close growing-k)
   vs start writing vs both.
3. Reported the milestone + the decision to the owner (attack RB / write the two complete results / both). The two results
   are "closed pending human verification" (names the steps needing independent human checking — gate (b) honesty rail).
