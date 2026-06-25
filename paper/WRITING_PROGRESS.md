# WRITING_PROGRESS — SODA draft

> Update after every section. On resume / long context: re-read this + `paper/COMPONENT_MAP.md` + `paper/FROZEN_RESULTS.md`
> + the relevant frozen proof (`rounds/round{4,5,6,7}_*`, `LEDGER_collapse.md`) before writing — never from memory.
> Drafting order (theory venue): prelims → theorems+proofs → techniques → related work → intro → conclusion → abstract (last).
> Style gate after each section (`.agent/AI_STYLE_CHECKLIST.md`): zero AI-tokens, 说人话, NO defensive prose, "rather than" banned,
> no em-dash glue, every bound pulled from the frozen proof, cross-section number echo.

## LENGTH + REFS (2026-06-25, FINAL — 40pp / 69 refs)
- **40 pages**, compiles clean (0 undefined, 0 multiply-defined). Structure: intro+results-table → Technical Overview →
  prelims → T1 statements (≈ first 10pp = extended abstract) → full offline proof → full online proof → separation →
  open problem → **Sec 7 Discussion** (online overhead, offline-monotonicity corollary, why the color-tree loses no log,
  what the online transplant uses); appendix = NA/Poisson facts + broadening-cost/conveyor.
- **refs.bib: 69 entries, all web-verified, all cited.**
- Proofs deepened to full self-verifiable derivations (color-tree path-sum per regime; LM budget; Freedman seed-tail;
  NA closure facts; fixed-k offline Theta(sqrt d) with anticoncentration; BC charging + conveyor invariant).
- Offline lower-bound lemma `lem:occ-spread` is now **fully self-contained** (GPT-5.5-Pro resolution typeset): reverse
  Cramér `lem:reverse-cramer` + comparable-mean spread `lem:comparable` + heavy/no-heavy reduction, rate `e^{−ck^{1/4}}`.
  Necessary correction applied: added hypothesis **`λ≥1`** (the lemma is false for `λ≪1`; `λ≥1` ⟺ `k≤Td/n`, holds for all
  `k≤d` once `T≥n`) to T1 / intro / `cor:bracket`. The paper no longer has any cited-as-standard step. Relay archived
  at `rounds/RELAY_occupancy_lemma.md` (marked RESOLVED).
- CAVEAT: the deepening passes added new explicit derivations around the (preserved) statements; these merit one more
  Codex correctness pass before submission.


- **Now 32 pages**, compiles clean (0 undefined). Restructured per SODA's "first 10pp must convey the core ideas":
  intro (+results table) → **Technical Overview** (new: proof ideas of T1/T2/T3 + growing-k obstruction) → prelims →
  T1 statements ≈ first ~10pp (extended-abstract part); then **full proofs in the body** (offline, online), separation,
  open problem; appendix = deferred NA/Poisson facts + broadening-cost/conveyor.
- **refs.bib: 18 → 44 entries, every one web-verified (arXiv/DOI/DBLP) and every one cited** in the four-lineage §1.3.
- Style gate clean: 0 "rather than", 0 em-dash glue. Target band 30–40pp met.
- Relay prompt for the one cited-as-standard occupancy lemma: `rounds/RELAY_occupancy_lemma.md` (hand to GPT-5.5-Pro).

## ACCEPTANCE STATUS (2026-06-25) — full draft + Codex review convergence
- **Compiles clean**: `latexmk main.tex` → 17pp, exit 0, 0 undefined refs/citations after bibtex.
- **All sections + full-proof appendices + intro + abstract written.** Title/headline/structure as decided below.
- **Codex review (gpt-5.5 xhigh) BLOCKERs resolved** through iterated re-checks (R1 correctness, R5 completeness):
  - Prefix-vs-final: `offdisc`=final, `ondisc`=prefix (Altschuler–Tikhomirov split). FIXED §2/§3/appB/§5.
  - Online upper (§4/appC): reframed as a **black-box reduction** to A-T's exceptional-set + level-set lemmas; we prove
    only the k-free transplant (repair range-non-increasing for any k; actual≠seed ⇒ exceptional coord present). RESOLVED.
  - Offline lower (appB): rewritten as **Lemma `lem:occ-spread` (occupancy spread lower tail)**, q≥k^{1/5}; heavy/light
    on the *relative* threshold k^{1/4}λ; comparable-mean extreme-value law cited (ABKU/BCSV) as the one occupancy input.
    Reviewer verdict: **LB-SHOULDFIX** = correct modulo the cited standard law (no remaining false sub-claim).
  - Hypothesis `k ≥ C₀ log⁵(dk)` now carried in Thm 1, intro T1, and `cor:bracket` (the loglog n/k floor needs no lower-k).
  - Compile blocker `\whp` in display math, `\newtheorem{problem}`, odd-k signing sign (−(a+1)/a, zero-sum). FIXED.
- **Remaining (honest, non-blocking for a review draft):** (a) refs ~18 → grow to ~50–70 + verify; (b) prose density —
  proofs are tight; expanding to full SODA exposition would grow length; (c) the comparable-mean occupancy law is invoked
  as a cited standard fact (the one spot to hand the external solver if a referee wants it self-contained).

## Decisions (owner-aligned)
- Title = **A2**: "Multicolor Discrepancy of Sparse Random Vectors: An Occupancy Threshold and an Online–Offline Separation".
- Headline = "more colors: offline helps, online doesn't" + the multicolor online–offline separation.
- Venue = **SODA** (THEORY class; ~50–60pp; full proofs in appendix; double-blind/anonymized). Structure-clone = NSW SODA'25.
- Scope = the three results (T1/T2/T3) solid; growing-k = open-problem section (§6), off critical path.
- Pacing = section-by-section; all review panels (6 reviewers + 3 cold-readers) via **Codex** (`gpt-5.5`, xhigh), not Claude.

## Status by section (`paper/tex/`)
| file | section | status |
|---|---|---|
| `main.tex` | document skeleton (SIAM-ready, anonymized; \input section files) | ✅ done |
| `notation.tex` | macros (single source; symbol discipline) | ✅ done |
| `refs.bib` | bibliography | 🟡 ~18 core anchors seeded; grow to ~50–70 per-section + verify (check_refs --online) |
| `sec2-prelims.tex` | §2 Preliminaries (model, scales+Ψ, NA/strong-Rayleigh, Lovett–Meka, Poisson tails) | ✅ **done** (full) |
| `sec3-offline.tex` | §3 offline `Θ(Ψ)` (centerpiece) — 3.1 lower / 3.2 overview / 3.3 NA lemma / 3.4 LM splitting / 3.5 color-tree | ⬜ NEXT (sketches in body; full→appB) |
| `sec4-online.tex` | §4 online fixed-k `Θ(loglog n)` — P2 lower / multicolor A-T upper | ⬜ (full→appC) |
| `sec5-separation.tex` | §5 separation + growing-k bracket | ⬜ |
| `sec6-open.tex` | §6 growing-k open problem | ⬜ |
| `sec1-intro.tex` | §1 intro (results/separation/techniques/related work) | ⬜ LATE (after the theorems exist) |
| `sec0-abstract.tex` | abstract | ⬜ LAST |
| `appA–appD` | full deferred proofs | ⬜ (B=§3, C=§4 incl. the A-T category recursion in full, D=BC lemma) |

## Source of each result (pull bounds from here, not memory)
- T1 upper: `rounds/round4_response.md` §2–5 + `round4_audit.md` + `paper/VERIFICATION_CAMPAIGN.md` (V2).
- T1 lower (Ψ, 3 regimes): `rounds/round3_response.md` §1 + `round4_response.md` (correction) + V3.
- T2: `rounds/round5_response.md` §1 + V1 (the A-T category recursion reproduced — expand it in appC).
- P2 / separation / BC: `LEDGER_collapse.md` (P2, P13); V3; round-6/7 for the open problem.

## NEXT ACTION
**FULL FIRST DRAFT COMPLETE** (all body §1–§6 + appendices A–D + abstract). Now: style gate + **Codex review panels**
(6 reviewers + 3 cold-readers via `codex exec -m gpt-5.5 -c model_reasoning_effort="xhigh"`, per the routing red line),
then fix BLOCKERs and converge on (a) proofs complete, (b) length, (c) refs, (d) readability.

## DRAFT STATUS (all written)
`sec0-abstract` ✅ · `sec1-intro` ✅ · `sec2-prelims` ✅ · `sec3-offline` ✅ (+`appB` full proofs) ·
`sec4-online` ✅ (+`appC` full proofs incl. the A-T category recursion reproduced) · `sec5-separation` ✅ ·
`sec6-open` ✅ (+`appD` BC lemma + phase conveyor) · `appA-prelims` ✅. `refs.bib` ~18 anchors (grow to ~50–70 + verify).
Honest length note: a focused single-characterization paper; with the full proofs present it is more compact than NSW's
multi-application ~50–60pp. Expand proof detail / add a worked example / grow refs to reach the SODA density at the review stage.
