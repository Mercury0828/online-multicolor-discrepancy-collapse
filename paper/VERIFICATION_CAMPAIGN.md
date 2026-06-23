# Verification campaign — A/B/C (owner-mandated, multi-agent adversarial) → READY TO WRITE

> Date 2026-06-22. Owner directive: "verify A/B/C with multiple strong adversarial agents; if no problem, treat as fine;
> real human verification = post-submission reviewers; drive to the ready-to-write stage." **Outcome: all results VERIFIED;
> no FATAL, no GAP found by any agent. Ready to write.** This is the running record of that campaign; it also lists the
> residual *prose-completeness* items (NOT logic gaps) for the writeup.

## Verification standard (per owner)
AI-audit-pass is treated as pass; the genuine human check is deferred to the peer-review community post-submission. The
campaign therefore demands: multiple INDEPENDENT fresh-context adversarial agents per load-bearing component, each tasked to
REPRODUCE imported steps (not just sanity-check) and to find a hole or confirm. Prior rounds already gave 1–3 audits each;
this campaign adds independent re-derivations focused on the steps flagged "pending human verification."

## Results
| component | agent verdict | what was done | residual (prose-completeness only) |
|---|---|---|---|
| **T2** online fixed-k `Θ(loglog n)` (P12) | **VERIFIED 90%** (V1) | **Reproduced the A-T category high-moment recursion from scratch** (`β_w ≤ (Cd²/H)^{16H}·β_{w−1}^{(·)}` ⇒ `|E_T| ≤ n d^{−5}`); confirmed genuine **k-independence** (the invariant "actual≠seed ⇒ a prior exceptional row in the support" is control-flow, not k; the min-load repair is range-non-increasing for any k); seed tail 9× margin; double-exp closes at `r*≈1.443H<2H`. **Closes the one gap flagged "imported, not reproduced."** | the exact A-T column-counting constant in the step-3 squaring (soundness-robust: any super-geometric contraction closes it) |
| **T1 upper** offline `O(Ψ)` (P11) | **VERIFIED 88%** (V2) | **Independently re-derived every inequality + numerically stress-tested** all 3 parts: the all-subsets NA structural lemma (NA via strongly-Rayleigh + JDP P6/P7, correct MGF direction; the union converges for an absolute `B`); the exact-cardinality Lovett–Meka splitting (budget `m≥22`, stage-sums (3.4) C≈5.3 / (3.5) rebasing ≤1.04); the recursive color-tree (`1/q` attenuation; path-sums reassemble EXACTLY into `Ψ`, ratio stays in `[1.0,1.9]` — NO per-level / `log d` / `loglog n` loss). | the limiting/subspace-constrained LM exact-equality formalization; the `O(1)` cleanup-swap rigor (both standard, no counterexample) |
| **T1 lower** offline `Ω(Ψ)` (P9→Ψ) | **VERIFIED 88%** (V3) | Poisson tail inversion `t*≍√(λL)+L/log(e+L/λ)` confirmed analytically + numerically (exact Bennett `I(t*)/L∈[0.64,1.07]`); the 3 regimes + continuity; k=2 silence (no clash with A-T). | the Poissonization/conditioning error bookkeeping vs `n log k` (constant-level, standard) |
| **T3 separation** (fixed k) | **VERIFIED 88%** (V3) | `Ψ=Θ(√d)=o(loglog n)` UNIFORMLY under the cap (`√d ≤ H/√log H`, `1/√log H→0`); correctly scoped to fixed k. | 🔴 **writing guard:** cite the fixed-k offline `Θ(√d)` to **Bansal–Meka / Ezra–Lovett / Hoberg–Rothvoss + the routine multicolor extension, NOT to the `k→∞` T1** (they agree on the overlap). |
| **P2** online lower `Ω(loglog n/k)` | **VERIFIED 88%** (V3) | two-block projection = a valid online 2-coloring ⇒ A-T's online `Ω(loglog n)` ⇒ `Ω(loglog n/k)`; odd-k asymmetric variant preserves the recurrence (const ≤2); tightness corroborated by B2. | the A-T recurrence's insensitivity to the `ρ∈[1/2,1]` asymmetry (mechanism sound) |

## Net verdict
🟢 **A/B/C VERIFIED to the agreed standard. No FATAL, no GAP across V1/V2/V3 (90/88/88%) — on top of the prior per-round
audits (T1: 3 blind; T2: 1; lowers/P13: audited).** All residuals are prose-completeness / constant-level bookkeeping, NOT
logic holes; none yielded a counterexample. The one genuine gap (reproduce the A-T category recursion) is now reproduced.
**Per the owner's standard, this is "verified" — the genuine human check is the post-submission referees.** **READY TO WRITE.**

## Writeup checklist (carry the residuals into the prose — they are where a referee will want full detail)
1. Write the **A-T category recursion in full** (T2) — reproduce, don't import (V1 gives the derivation to expand).
2. Write the **all-subsets NA union bound** + the **limiting-LM exact-equality** + the **`O(1)` cleanup** in full (T1 upper, V2).
3. Write the **Poissonization/conditioning error** bound explicitly (T1 lower, V3).
4. **Cite Bansal–Meka et al. for the fixed-k offline `Θ(√d)`** in the separation, not T1 (V3 guard).
5. State all over-claim guards in the text (FROZEN_RESULTS §guards): AI-verified-status note; MATCH small-k only; d-independence
   offline-only; `Ψ=o(loglog n)` needs the cap; `K_1` bracket; rate-level monotonicity.
6. The growing-k regime is the **shelved frontier / open problem** (RB ⟸ `PF_tr` ⟸ fold-or-Fibonacci; B4 + B5 both dead) — a
   clean "open problem" section, off the critical path.
