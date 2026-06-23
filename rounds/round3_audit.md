# Round-3 audit — 2 independent blind verifiers + numeric on `round3_response.md`

> Date 2026-06-22. Two blind fresh-context adversarial audits + audit-side numerics. Convention: `rounds/README.md`.
> **Convergent verdict: VERIFIED.** P9 occupancy-entropy floor holds (cleaner 2-regime form); A1/A2 refuted; the
> mean-square lemma is correct (L2-only); the "folklore" record needs correcting (multicolor offline upper is open).

## Audit A — P9 occupancy-entropy floor (§1). **VERDICT: CORRECT-with-imprecise-regime-split (88%).**
- Master inequality (Poissonization + multinomial→Poisson Stirling + `k^T` union) is the standard first-moment bound;
  all error terms (`d²`, `k log(nd)`, Stirling) are `polylog(n) ≪ n log k`. ✓
- Core insight correct: forcing `k` (≈iid) Poisson(λ) occupancies into a width-D window ⇒ `D ≳` the **extreme-value
  spread of k Poissons**. Anti-concentration engine valid.
- **Cleanest correct bound (audit-sharpened, STRONGER than GPT's 3-regime):**
  `offdisc_k ≳ √(λ log k)` for all `λ≫1`, and `≳ log k/loglog k` for `λ=Θ(1)`. GPT's "moderate regime `Ω(λ)`" is true
  but **slack** — `√(λ log k) ≥ λ` for `λ≲log k`, so the Gaussian bound the proof already gives dominates it. (Numerics:
  `max of k Poisson(1) ≈ log k/loglog k`; `√(λ log k)` dominant for `1≪λ≲log k`; both confirmed.)
- **Beats `√(d/k)=√λ` by `√(log k)` (or `log k/loglog k`) → ∞** for all `k→∞, k≤d`. ✓ ⇒ **A2 (offline O(√(d/k)))
  refuted; A1 (online) refuted a fortiori** (online ≥ offline). **Matching offline UPPER is OPEN.**
- −12% caveat: the constant-occupancy `k^{1−δ+o(1)}` margin converges only at rate `loglog log k/loglog k` — asymptotically
  valid, thin at finite scale.

## Audit B — mean-square lemma + folklore + P8 scope (§5, §3, §6.2). **VERDICTS below.**
- **P10 mean-square lemma: CORRECT (95%).** Recomputed the drift with the FULL update (`z_{i,c}+=1−1/k`, `z_{i,a}−=1/k`):
  `Δ(Σ_a z_{i,a}²) = 2z_{i,c} + 1 − 1/k` exactly (the `(2/k)z_{i,c}` cross-term cancels). Telescopes to `Φ(t) ≤ td(1−1/k)
  ≤ td`; `(1/nk)Σz² = O(d/k)`. 🔴 **Genuinely L2-ONLY** — `Φ≤td` is compatible with one coordinate carrying `Θ(√(nd))`;
  says nothing about `max_i R_i`. A legitimate but weak (second-moment) tool, NOT a discrepancy bound.
- **Folklore correction: YES, "folklore" was too hasty (70%).** Bansal–Meka / Ezra–Lovett / Hoberg–Rothvoss are **2-color
  (±1) only**; none states a `k`-color `O(√(d/k))` upper. Doerr–Srivastav multicolor reductions do NOT give the `1/√k`
  improvement for free. ⇒ **the multicolor random offline UPPER is OPEN** (not on the shelf) — though *possibly* a routine
  partial-coloring (Lovett–Meka) extension, so do not over-claim deep novelty. (The 2-color `√d` IS folklore.)
- **P8-scope limitation: VALID & important (80%).** P8 bounds only **level-RAISING** covers; it is silent on **within-level
  broadening** (`(r,r−1,…)→(r,…,r,0)` growing `|F_r|` via safe updates, manufacturing uncharged `C(|F_r|,a)` mass). ⇒ the
  cascade upper needs an additional **broadening-cost** lemma; the drift shape `ΔH_{r,a} ≤ −γH_{r,a} + C(k,a)η^a` is
  reasonable (modulo `C(k,a)η^a` summability over `a` + uniform `γ`).

## Orchestrator numerics (`code/verify_round3.py`)
- **Mean-square `Φ(t) ≤ td`:** confirmed — `Φ(T)/(Td)` stays `≤ 1` (≈`1−1/k`) across `(d,k)`; `(1/nk)Σz²` tracks `O(d/k)`.
- **Poisson extreme-value spread:** `E[max−min of k Poisson(λ)]` tracks `log k/loglog k` at `λ=Θ(1)` and `√(λ log k)` at
  `λ≫1` — both `≫ √λ` — corroborating P9's two-regime floor and that it exceeds `√(d/k)`.

## Classification
- **VERIFIED PROGRESS (stronger lower bound + a positive L2 tool) BUT closure-prospect DROP.** Bank **P9** (2-regime
  floor, supersedes P7 as tighter), **P10** (mean-square, L2-only), **N7** (A1/A2 refuted). Correct the folklore record.
  Sharpen P8 scope.
- **No proof-of-death ⇒ no kill.** But: **3 rounds, all lower bounds + refutations, no matching upper anywhere, target
  reshaped 3×.** Sustained closure-prospect drop ⇒ **first-class escalation signal** (fresh attacker / re-aim), and the
  contribution shape changed again ⇒ owner touch (gate-(a)/(c)-adjacent).

## Single biggest risk
**No matching UPPER bound exists in any regime after 3 rounds.** The most reachable candidate = the **offline
entropy-saturation upper** (a random-CSP existence theorem, no adaptivity); if it closes, the **offline occupancy-threshold
characterization** is a self-contained novel result. The online side (does online match offline?) and all of bounded-d
remain harder/open.

## OUTCOME (what the orchestrator did)
1. Banked P9/P10/N7; corrected the folklore record; sharpened P8 scope (ledger).
2. Ran a STRATEGY health-check (`docs/HEALTH_CHECK_strategy_r3.md`).
3. Brought a **candid trajectory assessment + options** to the owner (escalate a fresh attacker on the offline saturation
   upper / re-aim the headline at the offline occupancy-threshold characterization / reassess scope-venue) — NO silent
   downgrade, NO kill. Owner decides the next attack direction.
