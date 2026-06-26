# TRIM_PROGRESS — SODA freeze-phase finalization

> Re-read this + re-measure the PDF (pdfinfo, pdftoppm first ~12pp, section→page map from main.aux)
> before each step on long context. Trim = editing, never weakening (no claim/hypothesis/bound/scope change).

## Baseline (entering trim, 2026-06-25)
- 40pp, compiles clean (0 undefined, 0 multiply-defined), 69 verified refs, 0 banned tokens / em-dash glue.
- **Problem to fix:** full offline proof (§5, pp.12–19) + online proof (§7, pp.22–24) are in the BODY,
  pushing T2→p20, T3→p25. The three theorems do not fit the first ~10 pages.
- Owner decision: **sink full proofs to `\appendix`** (Option A).

## First-10-page merits inventory (baseline, from main.aux)
| merit | currently at | target |
|---|---|---|
| problem + model | p1 | ≤ p10 ✓ |
| prior positioning (tab:results) | p2 | ≤ p10 ✓ |
| Technical Overview (sketches) | p4–5 | ≤ p10 ✓ |
| T1 statement | p8 | ≤ p10 ✓ |
| **T2 statement** | **p20** | **→ ≤ p10 (needs sink)** |
| **T3 separation** | **p25** | **→ ≤ p12 (needs sink)** |
| growing-k open problem | p28 | front narrative |
| Discussion | p29 | front narrative |

## Protect-list (from R2 panel) — do NOT delete/compress these during trimming
From RW2 (sketches), 20 load-bearing intuition items:
- sec-overview: NA-affords-2^T-union (l19); the binom(T,s)=e^{sℓ} vs e^{-cBsℓ} balance (l22); LM locally-tuned
  thresholds (l30); all-ones equality keeps sizes exact (l32); O(1/q) attenuation (l39); occupancy lower-tail
  q=k^Ω(1) (l52); heavy/light dichotomy (l53).
- sec3-offline: "key accounting fact is attenuation" (l156); path-sum display (l176); Bennett-summand split at
  q=√(log k/λ) (l181).
- sec4-online: min-load can't raise spread (l65,l72); category uses only future-support indep + seed sparsity
  + actual≠seed⇒exceptional (l80,l81).
- sec6-open: permutation-invariant (range,maxmult) (l29); bracket allows j up to loglog n/k (l36); "gap not
  slack in bookkeeping" (l38); asymmetric approach (l45); expectation tail is false (l51); conveyor is fragile (l54).
- (also protect, general): abstract single takeaway; tab:results; §2 obstacle→idea maps; the worked Ψ-regime
  reading in sec2-prelims; section headers.

## R2 findings + fixes
- RW2 BLOCKER-1 (sec3:56 "range ≥ Θ(Ψ) with constant probability beats e^{Θ(n log k)}") = FALSE → FIXED:
  now states per-coordinate rate e^{-k^Ω(1)} (lem:occ-spread), cross-coord independence via Bernoulli rows
  (not NA), beats union because k≥C₀log⁵(dk).
- RW2 BLOCKER-2 (sec-overview:68 "seed tail scopes to k≤poly(d)" vs "holds for all k") → FIXED: variance
  2Td/(nk) shrinks with k, worst case k=2, so upper bound holds for all k.
- RW2 SHOULD-FIX (sec3:173 wrong \eqref{eq:rank} in offline color-tree; deg_t→deg) → FIXED (now "offline
  discrepancy is range of final loads", deg(i)).
- RW2 SHOULD-FIX sec4:79 "verbatim" already qualified by "uses only ..." — adequate, left.

## Reference re-verification result (web-recheck subagent, all 69)
- 68/69 fully accurate, NO fabricated/wrong-paper entries.
- 1 FIX applied: BansalDadushGargLovett2018 pages 1269--1282 → 587--597 (STOC'18). Done.

## R2 panel RW1 (front-10) + RW3 (consistency) findings + fixes
- RW1 BLOCKER (front matter not contiguous; T2→p20, T3→p25) → resolved by STEP 4 (sink proofs).
- RW1 BLOCKER (sec5 "adversary feeds columns" vs i.i.d. model) → FIXED: average-case wording, cites def:model.
- RW1 BLOCKER (sec5 fixed-k offline Θ(√d) lower bound not self-contained for adaptive coloring) → FIXED:
  T3 offline restated as O(√d) via offdisc_k ≤ offdisc_2 = Θ(√d) [cite] (all the separation needs); intro
  T3 + table fixed-k row + tab caption updated to O(√d).
- RW1+RW3 BLOCKER (sec5 crossover used Ψ=Θ(√log k) at λ=Θ(1); correct is Θ(log k/loglog k)) → FIXED:
  removed the wrong precise crossover, replaced with correct qualitative statement.
- RW3 BLOCKER (appB λ scaling "Θ(dk/n)/k") → FIXED to Td/(nk)=Θ(d/k).
- RW3 BLOCKER (sec5 "rank-greedy rule" undefined) → FIXED (now cites lem:online-upper / seed-and-repair).
- RW3 BLOCKER (growing-k hypotheses not echoed) → FIXED: added λ≥1 to table row + intro bracket; sec7
  monotonicity corollary now carries C₀, λ≥1, d,k=(log n)^{o(1)} and no longer mixes the fixed-k endpoint.
- RW3 SHOULD-FIX symbol collisions → FIXED: \rank macro \rho→\mathrm{rk}; appB color-set H→G; appC Freedman
  λ→u; sec7 overhead \rho_k→\kappa_k; SDP expanded on first use; bare Ψ in table/sec7 → Ψ(λ,log k); L=log(ek)
  clarified in intro; "determines exactly"→"up to constant factors, in the growing-palette regime".
- RW2 BLOCKERs (sec3 false "constant probability"; overview seed-tail "all k" inconsistency) → FIXED earlier.
- Deferred (accepted, non-blocking): appC local R_i shorthand (defined at use); "exceptional coordinate" in
  intro before E_t (acceptable for intro); sec4 pre-sampled-seed online-ness appositive (optional).
- Anonymity: clean (RW3 confirmed no author/institution/self-cite leak).

## Step status (update)
- [x] 1. writing recheck — done.
- [x] 2. reference re-verification — done (1 fix).
- [x] 3. R2 panel + protect-list + BLOCKER/SHOULD-FIX — done. Recompiles clean, 40pp, 0 undefined.
- [x] 4. SINK proofs to appendix — done. New page map: T1 p8, T2 p12, T3 p14, cor:bracket p15, open p16,
       discussion p17; full proofs in appendix p25+. All proof \Cref pointers resolve as Appendix B/C.
       NOTE on merits window: all three results are STATED in the intro list + results table on pp.1-2 and
       the proof ideas in the overview pp.4-5, so the merits are conveyed in the first ~5 pages; the formal
       restatements T2/T3 sit at p12/p14. If R3 wants the formal statements within p10, tighten §2/§3 prose
       (escalate-in-report; do not cut protect-list).
- [~] 5. trim — LIGHT (no length pressure; SODA uncapped): abstract 190w (in range), caption within norm,
       protect-list constrains cutting. Added sec4 "private randomness ... stays online" appositive (RW1 SF5).
- [~] 6. exit gate: R3 Codex panel LAUNCHED (background). Joint fixed point pending its verdict.

## Step status
- [x] 0. tracking file (this)
- [~] 1. writing recheck: static scan CLEAN (0 banned tokens, 0 defensive prose, 0 em-dash glue, 0 self-cite
       leaks); bound-echo across intro list / AT-background / theorem statements consistent (Θ(Ψ), Θ(loglog n),
       Θ(√d)); fixed 1 acronym nit (appA double-defined "(NA)" → now refs def:NA). RW3 (Codex) deep-checks.
- [~] 2. reference re-verification: web-recheck subagent LAUNCHED (background, all 69 entries). self-audit of
       in-text bound attributions pending agent return (watch HPVX2025 "Θ(√log T)", MulticolorLB2025 "√n").
- [~] 3. R2 Codex cold-reader panel: RW1(front-10)/RW2(sketches)/RW3(consistency) LAUNCHED (background). Awaiting
       BLOCKER/SHOULD-FIX + protect-list.
- [ ] 4. sink full proofs to appendix; verify T1/T2/T3 < p~10
- [ ] 5. trim (caption / restatement prose / component lengths)
- [ ] 6. exit gate: R3 Codex panel; joint fixed point; commit+push

## Owner decisions
- 2026-06-25: sink full proofs to appendix (Option A).

## Notes
- Codex smoke test OK (panels go via Codex; if Codex fails → STOP + report, no Claude fallback).
- abstract currently 203 words (target 150–200; trim lightly in step 5C).
