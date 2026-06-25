# Component map (structure-clone) — NSW SODA'25 → our paper. For OWNER ALIGNMENT before drafting body.

> Date (resume). Step 3 of the SODA writing pipeline = structure-clone, NOT free writing. Target exemplar:
> **Naor–Srinivasan–Wajc, "Online Dependent Rounding Schemes for Bipartite Matchings, with Applications", SODA 2025
> (arXiv:2301.08680)** — read section-by-section below. (It even uses negative-association / strong-Rayleigh in its
> preliminaries — the same tool as our offline structural lemma, so the clone is genuinely apt.) Supersedes the section-org
> in `paper/SKELETON.md` (which used A-T as the topical anchor; A-T stays the *content* anchor, NSW is the *structural* template).

## VERIFIED length / proof / bibliography model (SODA = THEORY class, no page limit)
- **SODA 2025: NO page limit** — submit the full version with appendices containing full proofs (SIAM template). 192/655
  accepted (~29%). [verified: SODA25 submissions page + Barna Saha].
- **NSW structure (the baseline):** §1 Intro (results + applications + techniques + related work, all folded in) → §2
  Preliminaries (incl. §2.1 NA / strong Rayleigh) → §3–§4 main techniques (warm-up → overview/intuition → core → full) →
  §5 Applications → §6 Lower Bounds → §7 Summary & Open Questions → **Appendices A (extra prelims), B/C/D (deferred full
  proofs of §3/§4/§6)**. ~20 body theorems/lemmas + substantial appendix proofs. **~86 references.** No figures (pseudocode boxes).
- **Our targets (verified-anchored):** total **~50–60 pp** (body ~10–12 + long proof appendix); **~50–70 references**
  (NSW=86; ours is a more focused single-characterization paper, so ~50–70 is honest coverage, not padding); **every claim's
  FULL proof exists (appendix)**; **double-blind** (2024+ SODA — anonymous, no first-person self-citation; re-confirm CFP).

---

## SECTION SKELETON (cloned from NSW org)
- **§1 Introduction** — `Our results` (T1/T2/T3 formal statements upfront) · §1.1 `The separation & the growing-k regime`
  (the consequence/“applications” slot) · §1.2 `Techniques` (offline: the 3 ingredients; online: the multicolor A-T extension)
  · §1.3 `Related work` (folded in — paging/online-balancing/A-T/random-set-system discrepancy/NA tools).
- **§2 Preliminaries** — model & `ondisc_k/offdisc_k`; `λ,L,H,Ψ`, the rank `ρ`; §2.1 `Negative association & strong Rayleigh`;
  Lovett–Meka partial coloring (statement); Poisson/Bennett tails. (Mirror NSW §2 depth.)
- **§3 The offline characterization `offdisc_k=Θ(Ψ)`** (clone NSW §3 warm-up→overview→core→full) — §3.1 the occupancy lower
  `Ω(Ψ)` (warm-up + Poissonization) · §3.2 overview/intuition of the upper · §3.3 the all-subsets NA structural lemma ·
  §3.4 the exact-cardinality Lovett–Meka splitting lemma · §3.5 the recursive color-tree ⇒ `O(Ψ)`. (sketches in body, full→App B.)
- **§4 The online fixed-k result `ondisc_k=Θ(loglog n)`** (clone NSW §4) — §4.1 the `Ω(loglog n/k)` lower (two-block
  projection) · §4.2 the multicolor A-T upper (seed + min-load repair + the category recursion + double-exp). (full→App C.)
- **§5 The separation & growing-k bracket** (NSW §5 “Applications” slot) — fixed-k separation `ondisc_k≫offdisc_k`
  (🔴 cite Bansal–Meka for fixed-k offline `Θ(√d)`, NOT T1); the bracket `max{Ψ,loglog n/k}≤ondisc_k≤loglog n`.
- **§6 Summary & open problems** (clone NSW §7) — the growing-k frontier: RB ⟸ truncated `PF_tr` ⟸ fold-or-Fibonacci;
  why both natural routes fail (symmetric `(R,s)`→`loglog n/log k` [B4]; naive expectation refuted by the phase conveyor [B5]).
- **Appendices** — **A** additional prelims (NA closure, Lovett–Meka exact-equality form, Poisson tails). **B** deferred full
  proofs of §3 (structural lemma; splitting; color-tree path-sums; the `Ω(Ψ)` lower). **C** deferred full proofs of §4 (**the
  A-T category recursion in full** — reproduce per V1; seed tail; double-exp). **D** the BC lemma (P13) + growing-k details.

## PROOF-PLACEMENT / COMPONENT-COMPLETENESS TABLE (one row per claim — full proof MUST exist)
| claim | body form | full proof | verified by |
|---|---|---|---|
| Thm 1 (T1) `offdisc_k=Θ(Ψ)` | statement §1, overview §3.2 | App B (upper) + §3.1/App B (lower) | V2 88% + V3 88% + round-4 3 blind |
| Lem (structural NA, P11-A) | statement §3.3 | App B.1 | V2 88% + round-4 Audit B |
| Lem (splitting LM, P11-B) | statement §3.4 | App B.2 | V2 88% + round-4 Audit C |
| Lem (color-tree, P11-C) | §3.5 | App B.3 | V2 88% |
| Lem (occupancy lower, →Ψ) | §3.1 | App B.4 | V3 88% |
| Thm 2 (T2) `ondisc_k=Θ(loglog n)` fixed k | statement §1, §4 | §4.1 (lower) + App C (upper) | V1 90% |
| Lem (multicolor A-T upper, P12) | overview §4.2 | App C.1 (**category recursion in full**) | V1 90% (reproduced) |
| Lem (two-block projection, P2) | §4.1 | App C.2 (even+odd k) | V3 88% |
| Thm 3 (T3) separation + bracket | §5 | §5 (short; cites Bansal–Meka) | V3 88% |
| BC lemma (P13) | §6/App D | App D | round-6 audit 88% |
| growing-k open problem | §6 | — (open) | round-6/7 audits |

## OVER-CLAIM GUARDS (carry into the text; from `FROZEN_RESULTS.md` §guards)
AI-verified-status (internal; the paper states proofs, full); MATCH ruled out small-k only; d-independence is OFFLINE-only
(online upper is itself d-independent); separation needs `Ψ=o(loglog n)` under the cap; `K_1` stays a bracket; "decreasing
in k" is rate-level; cite Bansal–Meka (not T1) for fixed-k offline `√d`; **no Limitations/Future-Work** (defensive-writing rule).

## DEVIATIONS from NSW (flag for owner)
- NSW has a rich §5 Applications; we have no external applications — we use that slot for the **separation + bracket** (a
  consequence of T1+T2). Honest and on-theme; not padded.
- NSW interleaves a standalone §6 Lower Bounds; our lower bounds are interleaved into §3.1 (offline) and §4.1 (online) — cleaner
  for a characterization paper. (No standalone lower-bounds section.)
- We are a single-characterization paper (narrower than NSW's multi-application sweep) ⇒ ~50–60pp / ~50–70 refs is the honest
  target, below NSW's breadth but full-proof-complete.
