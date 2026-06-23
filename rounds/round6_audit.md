# Round-6 audit — independent adversarial verifier(s) on `round6_response.md` (PENDING)

> **Status: NOT STARTED** (depends on `round6_response.md`). Convention (`rounds/README.md`): a claimed CLOSURE of RB (or a
> fully-matched online lower bound) → 3 blind audits. The broadening-cost / drift control (the within-level Δρ=+1 transitions,
> all-prefixes, whp over n×T) and any online lower (must hold vs EVERY online algorithm) are the hardest points — audit them
> adversarially. Classify FATAL/GAP/MINOR; end with OUTCOME.

## Auditor verdict (one focused audit; verdict = OPEN, so 1 audit proportionate). **All claims CORRECT (88%).**
- **BC lemma: CORRECT.** (a) the certificate step (every range-`r` invisible broadening forces TWO distinct range-≥`r` rows in
  the support) — rank arithmetic verified, genuinely needs `r≥2` (the min-load color `M_i−r ≤ M_i−2 ∉ F_{i,q}`); (b) collision
  prob `≤ 2d²η/n` (numerically verified `d∈[2,50], η∈[.01,.9]`); (c) the falling-factorial / ordered-tuple bound
  `nη(Tp)^a ≤ nη(2τ_+ d²η)^a` valid; (d) uniform over adaptive stopping times (future supports stay iid uniform `d`-sets). ✓
- **Exponent mismatch: CORRECT.** (3) `#{R_i=r, s_i≥s}/n ≲ η_r(Cd²η_r)^{s−1}` follows by Markov on BC (the `(s−1)!` only helps);
  the `η_r^s·η_r^{k−s}=η_r^k` balance is right ⇒ `η_{r+1} ≲ (Aη_r)^k` ⇒ `η ≤ exp(−c k^j)` ⇒ union-over-n needs `j ≳ loglog n/log k
  = H/log k`, an extra `log k` vs the `H/k` RB needs. **The symmetric `(R,s)`/`H_{r,a}` route provably cannot prove RB.** At
  `k=2` both `H/log2` and `H/2` are `Θ(H)` (the A-T anchor can't distinguish) — confirmed. ✓
- **Skip obstruction: VALID AS STATED.** The narrow-rainbow (a visible raise skips all `k−2` intermediate phases ⇒ the `k^r`
  mechanism) is a legitimate **proof obstruction for symmetric-rank methods only** — correctly **NOT** a stochastic lower bound
  vs arbitrary online algorithms (an asymmetric color-staggering rule can break the simultaneous-`k`-copies configuration). ✓
- −12%: unaudited dependencies taken as given (the cover certificate; the P8 `η_r^{k−s}` cost; `τ_+`/horizon defs); the
  obstruction is an argument, not a formal impossibility proof.

## Classification — VERIFIED. RB OPEN (not closed).
- **Banked: P13 (BC)** + **B4** (symmetric route dead ⇒ `H/log k`). RB neither proved nor refuted; narrowed to **PF via LeftGap**
  (asymmetric, staggered-Fibonacci; UNPROVEN, GPT 60%). Unconditional bracket unchanged `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n`.
  The two complete results (P11, P12 fixed-k) are untouched.
- **No FATAL.** Not a stall in the "no new lemma" sense (BC is new+verified), but RB did NOT close, and the *natural* route is now
  provably excluded — so further symmetric-route rounds are worthless; only the harder asymmetric PF/LeftGap remains.

## OUTCOME (what the orchestrator did)
1. Banked P13 (BC) + B4 (symmetric-route obstruction) into the substrate.
2. **Per the pre-committed plan (owner "attack RB first, else write" + the milestone health-check): RB didn't close ⇒ surfaced
   the PIVOT-TO-WRITING decision to the owner** — (A) write now (P11+P12+separation; RB→PF as the open-problem section, now a
   richer frontier) [recommended], vs (B) one PF/LeftGap round (the 60% asymmetric path) then write. Owner decides; agent does
   not auto-run another round (the symmetric route is dead; PF is a single harder lemma; the binding risk is writing +
   human-verification time vs the 07-09 deadline).

