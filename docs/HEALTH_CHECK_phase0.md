# Paper-Orientation Health-Check — Phase 0 (independent subagent, mandatory at every gate)

> Date: 2026-06-22. Reviewer: independent fresh-context subagent, blind to the orchestrator's reasoning.
> Verbatim conclusions + the orchestrator's disposition. (Guide §Workflow: every gate runs one of these.)

## ① On track for SODA? — YES conditionally; the real story is a LOWER-BOUND GAP
- Model/question/contrast framing are SODA-appropriate. A submittable paper IF the crux closes — in either fork,
  *provided the matching bound is genuinely two-sided.*
- 🔴 **Critical correction to the project's own framing:** "P2 lower + matching upper = tight" holds **only for the
  FAST fork.** P2 gives `Ω(loglog n/k)`; the cascade target is `Θ(loglog n/log k)`, and for `k≥3`,
  `loglog n/log k ≫ loglog n/k`. So **P2 does NOT lower-bound the cascade form** — in the cascade fork BOTH bounds
  are open, and the cascade lower rides on the SAME nonlinear subset-entropy machinery as `(★)` (B2: no fixed
  projection can reach it). The cascade lower (Profile-Branching) is *simultaneously the missing piece AND the sole
  novelty-defense* against the balls-into-bins folklore charge ⇒ doubly load-bearing, currently zero proof.
- **Reachability:** the **fast fork is the more honestly-reachable tight theorem** — P2 already owns half of it;
  it only needs the `O(loglog n/k)` star/junta upper, a fixed-structure argument with NO adaptivity-stability
  requirement. Cascade is higher-prestige but doubly-open + folklore-exposed. Prior cascade 0.40/fast 0.35 slightly
  over-weights cascade given fast is half-proven and cascade's lower is zero-proven.

## ② Drift? — NO scope creep; but the next-move PRIORITIZATION is arguably wrong
- Frozen state is disciplined (fixed model/quantity, explicit barriers + fork tree, pre-registered sims, honest
  de-risk caveats). Not drifting into nice-stories.
- 🟡 **Sequencing flag:** attacking `(★)` FIRST is high-variance (it must hold for the OPTIMAL player AND be stable
  under adaptive evolution — the sim cannot touch this). More paper-rational: **prove the fast `O(loglog n/k)` upper
  FIRST** → converts P2 into a complete tight theorem (guaranteed SODA floor), THEN attack `(★)`/Profile-Branching
  to upgrade fast→cascade. Going for `(★)` cold risks ending with only "P2 + an algorithm" (the ESA downgrade).

## ③ Other problems
- (a) **Balls-into-bins folklore risk is real and currently under-defended** — `loglog n/log k` IS the d-choice
  max-load `loglog m/log d` law. If cascade is the target, the Profile-Branching lower is the ENTIRE novelty claim,
  not a completeness item; must be load-bearing-proven, not bracketed.
- (b) **`K_1=Θ(M)` correctly flagged NOT proven (B3)** — keep `Ω(loglog n) ≤ K_1 ≤ O(log n/loglog n)` as a bracket
  everywhere, including the contribution list. Phrase the collapse headline as "for `k ≥ Θ(M)`" (upper-bracket,
  P3-proven), never as a tight `K_1` characterization.
- (c) **Monotonicity:** "decreasing in k" is NOT in the proven substrate. Sim B shows flat stretches (k=4..8 all =2)
  ⇒ consistent with RATE-monotone, not strict per-k. State as rate-level (the Θ-rate decreases), never as a strict
  monotonicity theorem (also recall the per-sequence non-monotonicity B-note).
- (d) **Thin-contribution failure mode is real:** "P2 + fresh-color algorithm" alone is NOT a SODA paper (the
  P2 `loglog n/k` ↔ P3 `~M/k` gap is wide & open) — it IS the RANDOM/ESA downgrade. The floor must be the FAST
  tight theorem, not P2+algorithm.
- (e) **Double-blind/positioning:** clean. Cite A-T anchor (P1) as THEIR theorem, not folded into the contribution.

## Orchestrator's disposition (recorded → DESIGN_DECISIONS + the round-1 brief)
1. **Adopt the fast-first sequencing** as the *recommended* attack-loop ordering: the round-1 brief's "what we need
   back" now prioritizes the FAST `O(loglog n/k)` upper (`HS-alt`) as the bankable floor, pursued in parallel with /
   ahead of the cascade gamble (`HS-upper`+`HS-lower`). Still "prove or refute `(★)`" — but bank the floor first.
   (Surfaced to the human at the gate as a scope/sequencing note, gate (c)-adjacent — NOT a contribution downgrade.)
2. **Cascade-lower gap** already in the ledger (2026-06-22 entry) — reinforced: never call P2 "the matching lower"
   without naming the fork; cascade needs `HS-lower` as load-bearing novelty.
3. **Over-claim watches** (K_1 bracket, rate-level monotonicity, "P2+algorithm ≠ SODA") → added to PROJECT_STATE
   honesty rails + the SODA writing constraints.
4. Net: **does not change the GREEN verdict** (science is green; these are prioritization + framing fixes).
