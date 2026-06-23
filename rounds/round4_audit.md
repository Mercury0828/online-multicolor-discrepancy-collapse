# Round-4 audit — 3 independent blind verifiers + numeric on `round4_response.md`

> Date 2026-06-22. THREE blind fresh-context adversarial audits (claimed CLOSURE ⇒ full treatment) + audit-side numerics.
> **Convergent verdict: the OFFLINE characterization is CLOSED** (audit-verified). `offdisc_k = Θ(Ψ(λ, log k))`. This is the
> project's FIRST matching (tight) result. Convention: `rounds/README.md`.

## Audit A — corrected Poisson scale Ψ (lower side, §1). **VERDICT: CORRECT (92%).**
- Poisson tail rate `−log Pr(P≥λ+t) ≍ t²/λ (t≲λ), t log(1+t/λ) (t≳λ)` — standard, correct. Inverting `rate=L=log k` gives
  `t ≍ √(λL) + L/log(e+L/λ)`. ✓
- **The round-3 P9 2-regime form is genuinely WRONG in `1≪λ≪log k`** — the correct scale there is `log k/log((log k)/λ)`,
  bigger than `√(λ log k)`. **Counterexample at `λ=√(log k)` verified:** claimed `(log k)^{3/4}` vs true `≍ log k/loglog k`,
  ratio `(log k)^{1/4}/loglog k → ∞`. ✓ Boundaries continuous; `λ=Θ(1) → log k/loglog k`, `λ≍log k → log k`. ✓
- ⇒ `ondisc_k ≥ offdisc_k = Ω(Ψ(λ, log k))` (corrected lower). −8%: the `≍`-on-the-rate hides a `Θ(log)` prefactor (absorbed
  at `Θ`-order); the first-moment/union machinery was taken as given.

## Audit B — uniform structural lemma (§2, the all-subsets NA union — flagged crux #1). **VERDICT: CORRECT (88%).**
- **NA holds:** each column = uniform `d`-subset indicator = strongly Rayleigh ⇒ NA; independent concatenation over `s`
  columns (JDP P7) ⇒ NA vector `W` on `n·s` entries; row-sums `r_i=Σ_t A_{it}` are increasing functions of **disjoint**
  coordinate blocks `{(i,t):t}` (JDP P6) ⇒ `{r_i(S)}` NA. The "same column ⇒ dependent" worry is a non-issue (P6 needs
  disjoint *entries*, not independent ones). **Used in the correct direction:** the `exp(−c/r)·1{r>0}` summand in (2.3) is
  genuinely *nondecreasing* in `r`, so the upper-tail MGF factorization is exactly what NA grants. ✓
- **All-subsets union bound converges:** `ℓ_s=log(eT/s)≥1`; per-`S` failure `e^{−cBsℓ_s}` vs count `C(T,s)≤e^{sℓ_s}` ⇒
  `Σ_s e^{−(cB−1)sℓ_s} = o(1)` for `B` large. ✓ The `(2.3)/(2.4)` binomial tails are correct (split-at-`bμ`, order `b`
  then `K`; the Bennett `ℓ/log(e+ℓ/μ)` term exactly cancels the Poisson `log(t/μ)` amplification → exponent `≥Bℓ`). ✓
- Caveats (non-fatal): needs `T/n=Θ(1)` (holds); prose looseness, not substance.

## Audit C — splitting lemma (§3) + recursion (§4, exact-cardinality LM — flagged crux #2). **VERDICT: CORRECT (88%).**
- **Splitting lemma CORRECT** modulo two cosmetic clauses (absorbed by the `+1` in Ψ): (i) stop LM at `m=O(1)` (budget
  `1+m/64≤m/16` fails below `m≈22`) and finish brute-force; (ii) exact cardinality only after an `O(1)` cleanup swap (≤1
  per `r_i`). Dense per-iteration drift `K√(μ_A ℓ_A)` (i-independent) ✓; sparse release `≤2U_A` ✓; stage-sums **(3.4)**
  `Σ√(μ_A ℓ_A)≤C√(μ_0ℓ_0)` (numeric C≈5.3) and **(3.5)** `sup Ψ ≤ CΨ` incl. rebasing `ℓ_0+log(μ_0/ℓ_0)≤C√(μ_0ℓ_0)`
  (numeric ratio 1.197) ✓.
- **Recursion CORRECT:** `1/q` attenuation ✓; **(4.4)** `Σ√(λq ℓ_q)/q = O(√(λL))` ✓; **(4.5)** `Σ ℓ_q/(q log(e+ℓ_q/(λq))) ≤
  C(√(λL)+L/log(e+L/λ))` (numeric worst ratio 2.02 at the `q*=√(L/λ)` split) ✓. The two path-sums **reassemble exactly into
  `Ψ(λ,log k)`**; **NO extra `log d / √log d / loglog n / per-level-log` loss.** The deterministic construction adds no second
  union (the `for-all-S` structural lemma covers the adaptively-chosen alive sets). ✓
- **Most fragile step:** the `for-all-S` universality of §2 (covered by Audit B); within the core, the (3.5) rebasing (little
  slack but holds). −12%: the `for-all-S` achievability at `s/64` + the `O(1)` tail rigor are stated, not fully proven here.

## Orchestrator numerics (`code/verify_round3.py` extension + audit-side)
- Audit A: `max of k Poisson(Θ(1)) ≍ log k/loglog k`; the intermediate-band Bennett term dominates `√(λL)`. Audit C: the
  stage-sums (3.4)/(3.5)/(4.4)/(4.5) all numerically bounded. (Orchestrator's own confirmatory Poisson-spread run is
  redundant with these and non-load-bearing.)

## Classification & banking
- **CLOSURE CONFIRMED — bank P11:** `offdisc_k = Θ(Ψ(λ, log k))`, the project's first matching characterization. **Correct
  P9** (intermediate band). 🔴 **"AI-verified ≠ proved":** pending human verification of (i) the all-subsets NA union bound,
  (ii) the exact-cardinality limiting Lovett–Meka + the `m=O(1)` tail/cleanup.
- **No FATAL across 3 audits.** Per the convergence convention this offline SUB-result is "pending human verification".
- **Strategic:** the round-3 "no upper anywhere" inflection is **partly resolved** — a non-trivial matching upper now exists.
  The SODA-grade upgrade still hinges on the ONLINE side (does `ondisc_k` match `Ψ`?).

## OUTCOME (what the orchestrator did)
1. Banked **P11** (offline characterization); corrected **P9**; updated confidence (P(SODA-worthy paper) ↑ ≈ 0.40–0.50).
2. Reported the milestone to the owner (the authorized binary test came back POSITIVE within the clock) + the next decision:
   pursue the ONLINE side (the SODA-grade prize: does `ondisc_k` match the offline `Ψ`?) and/or start writing the offline
   characterization. Honesty rail flagged: P11 is conditional pending human verification of the two named steps.
