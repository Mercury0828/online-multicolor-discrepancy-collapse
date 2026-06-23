# Paper-Orientation Health-Check — post-Round-5 milestone (independent subagent)

> Date 2026-06-22. Independent blind reviewer. **Verdict up front: this is a SODA paper NOW — write it. Run one RB round
> in parallel, but do NOT gate the submission on RB. The binding risk is HUMAN VERIFICATION of P11/P12, not RB.**

## ① SODA paper now (RB unproven)? — YES. P(SODA-acceptable as-is) ≈ 0.55.
The bundle is a self-contained SODA-shaped paper: (1) complete tight OFFLINE `offdisc_k=Θ(Ψ)` (non-trivial construction —
the load-bearing piece); (2) complete tight ONLINE fixed-k `ondisc_k=Θ(loglog n)` (extends A-T); (3) a genuine **multicolor
online-vs-offline separation** (the conceptual headline — extends a 2025 prestige result into the color axis); (4) a growing-k
bracket reduced to one clean named lemma (RB). **An open sub-regime presented as a clean bracket + named conjecture reads as a
FRONTIER, not incompleteness** — SODA routinely accepts complete-main-theorems + isolated stated open problem. The danger would
be thin closed results; these are not thin (two complete tight theorems + a separation + a proven L2→L∞ no-go telling the reader
exactly why the gap is hard). **0.55 not higher because:** P11/P12 are AI-verified, human-verification pending (a hole there is
fatal to the headline); strong SODA pool; the separation's novelty leans on A-T being recent (foreground the non-mechanical
multicolor extension — B1 collapse, no power-of-k analogy).

## ② Attack RB vs write vs both — (c) BOTH, ~80% writing / 20% one RB round. WRITING is the critical path.
- **Start writing immediately** — the paper exists today (offline + online fixed-k + separation + bracket + RB-as-conjecture).
- 🔴 **The highest-value use of remaining cycles is NOT RB — it is HUMAN VERIFICATION of P11 and P12** (the headline; AI-only-
  verified = the biggest acceptance AND retraction risk). Spend cycles hardening P11/P12 before RB.
- **Run exactly ONE more RB round in background, short clock.** RB closing upgrades growing-k from bracket → tight (bonus,
  ~30–40%). Do NOT let it consume writing time; do NOT run a 2nd/3rd RB round (diminishing returns vs deadline).
- Day plan: 1–10 write full draft (offline construction = longest section) + 1 background RB round + human-verify P11/P12
  (co-critical: writing those sections IS verification); 11–14 integrate RB if landed, polish the separation; buffer to 07-09.

## ③ If RB doesn't close — still SODA-grade, NOT ESA/RANDOM, provided P11/P12 survive human check.
Offline tight + online fixed-k tight + a genuine separation + a sharply-bracketed open regime with a proven no-go = SODA-grade.
The round-3 "offline-only → ESA" worry no longer holds (online fixed-k + separation are now in the bundle). **The real demotion
trigger is "P11 or P12 fails human verification," NOT "RB open."** Venue floor is governed by verification.

## ④ Over-claim guards for the WRITEUP (must surface in the paper text, not just the ledger)
1. 🔴 **AI-verified ≠ proved (P11, P12).** Top risk. Named unverified steps: P11 = the all-subsets NA-union + exact-cardinality
   Lovett–Meka + m=O(1) tail; P12 = the imported A-T category high-moment recursion (NOT reproduced line-by-line — **reproduce
   it during writing**; a referee may demand it). Do not submit headline theorems no human has checked.
2. **"MATCH ruled out" is SMALL-k ONLY.** Never write "online ≠ offline" / "MATCH ruled out" without the qualifier; the
   separation headline is rigorously true *for fixed k* — state it that way; growing-k MATCH is open.
3. **d-independence-breaking is OFFLINE-only.** `Ψ` depends on `λ=Td/(nk)` (offline, d-dependent); the ONLINE upper P12 is
   itself d-INDEPENDENT (`O(loglog n)` ∀k). Don't blur "we break d-independence" across the online/offline boundary.
4. **The separation needs `Ψ=o(loglog n)` under the sparsity cap** `d ≤ (loglog n)²/logloglog n` — state the cap every time the
   separation is claimed; it is not unconditional.
5. **Name lower-bound components by source.** Keep `K_1` a bracket `[Ω(loglog n), O(log n/loglog n)]` (B3 — never headline
   `K_1=Θ(M)`); "decreasing in k" is rate-level, not per-k monotone (N6 hard-refuted, exact 11/9,13/9,1). Foreground the novelty
   as the **threshold form `Ψ` + the construction's 3 custom ingredients**, not the mere existence of a multicolor bound.

## Recommended next action
Freeze results and begin the full SODA draft today (offline characterization = technical centerpiece; the multicolor
online-vs-offline separation = conceptual headline; RB = clean conjecture/open problem). In parallel: (i) ONE background RB round,
short clock; (ii) HUMAN verification of P11 and P12 as co-equal critical path. Integrate RB only if it lands; do not gate on it.
P(strong SODA submission by 07-09) ≈ 0.55, → ~0.65 if RB closes and/or human verification completes cleanly. **Binding risk =
verification of P11/P12, not RB.**

## Orchestrator disposition
- This is the **AI-convergence milestone → human gate (b)** for the two complete sub-results: they are "closed PENDING HUMAN
  VERIFICATION" — the handoff names the exact steps needing independent human checking (P11: NA-union + exact-LM + m=O(1) tail;
  P12: the A-T category recursion). I surface this + the write/RB/verify decision to the owner; the owner is the decider/verifier.
- I do NOT over-index on one reviewer, but its read is consistent with the banked confidence (0.55–0.65) and the constitution
  (write when proofs frozen; the writing pipeline `venue-prompts/soda/` runs at this stage). I present the recommendation and the
  three live options without pre-deciding the owner's risk/time tradeoff.
