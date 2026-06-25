# WRITING_PROGRESS — SODA draft

> Update after every section. On resume / long context: re-read this + `paper/COMPONENT_MAP.md` + `paper/FROZEN_RESULTS.md`
> + the relevant frozen proof (`rounds/round{4,5,6,7}_*`, `LEDGER_collapse.md`) before writing — never from memory.
> Drafting order (theory venue): prelims → theorems+proofs → techniques → related work → intro → conclusion → abstract (last).
> Style gate after each section (`.agent/AI_STYLE_CHECKLIST.md`): zero AI-tokens, 说人话, NO defensive prose, "rather than" banned,
> no em-dash glue, every bound pulled from the frozen proof, cross-section number echo.

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
Write §3 (the offline characterization): §3.1 the `Ω(Ψ)` lower (Poissonization + k-Poisson extreme value, the three
regimes), §3.2 overview, §3.3 the all-subsets NA structural lemma, §3.4 the exact-cardinality Lovett–Meka splitting,
§3.5 the recursive color-tree ⇒ `O(Ψ)`. Body = statements + intuition + proof entry points; **full proofs in appB**.
Then §4, §5, §6, intro, abstract. Push after each major section.
