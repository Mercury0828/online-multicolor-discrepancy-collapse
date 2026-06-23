# Solver-Exchange Archive — `online-multicolor-discrepancy-collapse`

> Append-only archive of the external-solver attack/audit loop (orchestrator ⇄ web GPT-5.5-Pro, owner relays).
> Mirrors the archival mode of the sibling project `dynamic-weighted-mis-fat-objects`. **Every brief sent, every
> reply received, and every audit run is filed here — nothing is discarded, nothing is faked.** Owner-facing
> summaries are Chinese; all archive files are English (guide §language).

## Why this exists
The orchestrator (Claude) is the **referee/archivist, NOT the prover**. The math is attacked by GPT-5.5-Pro;
Claude writes method-free briefs, files the replies verbatim, and runs independent adversarial audits. This
folder is the audit trail: anyone (or a future session, post-context-summary) can reconstruct exactly what was
asked, what was answered, and what was found wrong — **re-read from here + `../LEDGER_collapse.md`, never from memory.**

## File-naming convention (per round `n`)
| file | what | format |
|---|---|---|
| `round{n}_brief.md` | the brief SENT to GPT-5.5-Pro | `# Brief for GPT-5.5 Pro — round n, <topic>`; freeze-FACTS/free-METHODS code-fence; "what we need back". The code fence is the exact paste-to-Pro payload. |
| `round{n}_response.md` | the reply RECEIVED | §1 verbatim reply (raw, unedited, for provenance) → §2 orchestrator faithful restatement (CANDIDATE, UNVERIFIED) + **Audit points** → §3 disposition. |
| `round{n}_audit.md` | the adversarial AUDIT(s) | fresh-context verifier verdict verbatim → FATAL/GAP/MINOR classification → **OUTCOME**. Claimed-closure ⇒ 3 blind audits (`_audit.md`, `_audit_b.md`, `_audit_c.md`). |
| `round{n}_brief.md` (rebuttal) | a follow-up/rebuttal brief is the NEXT round's `round{n+1}_brief.md` | same brief format; references the GAP it targets. |

Topical variants (when a round forks into parallel sub-attacks) follow the sibling's style:
`round{n}_brief_<angle>.md` (e.g. `_fast`, `_cascade`, `_fresh` for a fresh-context attacker).

## Status table
| round | topic | brief | response | audit | classification | confidence (cascade/fast/plateau/other) |
|---|---|---|---|---|---|---|
| 1 | `HS-core`: prove/refute `(★)`; fast-first | [`round1_brief.md`](round1_brief.md) ✅ sent | [`round1_response.md`](round1_response.md) ✅ non-closure + progress | [`round1_audit.md`](round1_audit.md) ✅ 2 blind audits + numeric | **GAP/PROGRESS (not FATAL)**: P6 verified; literal `(★)` refuted; FAST over-claim caught | 0.45 / 0.33 / 0.04 / 0.18 |
| 2 | FAST floor / CASCADE stretch | [`round2_brief.md`](round2_brief.md) ✅ sent | [`round2_response.md`](round2_response.md) ✅ contribution-altering | [`round2_audit.md`](round2_audit.md) ✅ **3 blind audits** + numeric | **MAJOR PROGRESS + scope change (not kill)**: P7 offline `√(d/k)` floor refutes clean forms; P8 aggregate cover; monotonicity refuted → **HUMAN GATE (c)** | reframed — see ledger |

| 3 | Matching ONLINE upper (A: `√(d/k)` regime; B: `d=O(1)` `F_online`) | [`round3_brief.md`](round3_brief.md) ✅ sent | [`round3_response.md`](round3_response.md) ✅ **A1/A2 refuted; P9 floor** | [`round3_audit.md`](round3_audit.md) ✅ 2 blind + numeric | **STRATEGIC INFLECTION**: P9 occupancy floor (>√(d/k)) refutes A1/A2; P10 (L2); 3 rounds, no upper anywhere → owner touch | P(SODA by deadline) ≈ 0.10–0.15 |

**Verified gains:** P6 (block-compression), P7 (`√(d/k)` floor), P8 (aggregate cover), **P9 (occupancy-entropy floor)**, **P10 (mean-square, L2)** — five banked tools; all LOWER-bound/structural, **zero matching UPPER**.
**STRATEGIC INFLECTION (post-round-3):** strategy health-check (`docs/HEALTH_CHECK_strategy_r3.md`) → SODA-by-deadline ≈ 10–15%. **Owner decision (gate a/c): KEEP SODA full-force (no venue downgrade — NO-RETREAT); Round 4 = a FRESH-context attacker on the offline saturation UPPER (#1) ONLY**, ~5-day binary clock. Bank the complete offline occupancy-threshold characterization first; online-localization stays the SODA-grade prize.

| 4 | FRESH-context: the offline entropy-saturation UPPER | [`round4_brief.md`](round4_brief.md) ✅ sent | [`round4_response.md`](round4_response.md) ✅ **CLOSURE (corrected order)** | [`round4_audit.md`](round4_audit.md) ✅ **3 blind audits** + numeric | 🟢 **CLOSED**: `offdisc_k=Θ(Ψ(λ,log k))` (P11), first matching result; corrected P9 | P(SODA paper) ↑ ≈ 0.40–0.50 |

| 5 | ONLINE localization (full regime) | [`round5_brief.md`](round5_brief.md) ✅ sent | [`round5_response.md`](round5_response.md) ✅ **online upper + fixed-k closed** | [`round5_audit.md`](round5_audit.md) ✅ 2 blind audits | 🟢🟢 **P12** `ondisc_k=O(loglog n)` ∀k ⇒ **fixed-k `Θ(loglog n)` CLOSED**; growing-k OPEN at RB; MATCH ruled out small-k only | P(SODA paper) ↑ ≈ 0.55–0.65 |

**🟢🟢 TWO COMPLETE RESULTS (after Round 5):** (offline) `offdisc_k = Θ(Ψ(λ, log k))` (P11) + (online, fixed k) `ondisc_k = Θ(loglog n)` (P12) — audit-verified, pending human verification — a genuine multicolor online-vs-offline separation. Verified tools/results P6–P12.
**Growing-k** is the one open gap, reduced to the **ranked-broadening lemma (RB)** ⇒ conjectured `Θ(max{Ψ, loglog n/k})`.

| 6 | RB — close growing-k OR an online lower bound | [`round6_brief.md`](round6_brief.md) ✅ sent | [`round6_response.md`](round6_response.md) ✅ **OPEN (not closed)** | [`round6_audit.md`](round6_audit.md) ✅ 1 audit (88%) | RB **OPEN**; banked **P13 (BC)** + **B4** (symmetric route dead → `H/log k`); narrowed to **PF via LeftGap** (60%) | bracket unchanged |

| 7 | PF — close growing-k OR an online lower bound | [`round7_brief.md`](round7_brief.md) ✅ sent | [`round7_response.md`](round7_response.md) ✅ **PF refuted (not closed)** | [`round7_audit.md`](round7_audit.md) ✅ 1 audit (93%) | displayed **PF FALSE** (phase conveyor, B5) but NOT a lower bound ⇒ RB still OPEN; → WRITE | bracket unchanged |

**Verified tools/results P6–P13** (+ B1–B5, N1–N7). **ATTACK LOOP CLOSED at Round 7.** The two owner-authorized RB/PF rounds (6,7) did NOT close growing-k: B4 (symmetric route dead → `H/log k`) + B5 (displayed PF refuted, but not a lower bound — RB still open). The open problem is sharply mapped (RB ⟸ truncated `PF_tr` ⟸ fold-or-Fibonacci). **→ PIVOT TO WRITING** (per the pre-committed plan): the two complete results (P11 offline + P12 fixed-k) + the separation + the bracket + the mapped open problem. Writing in `paper/` (step 1 = `paper/FROZEN_RESULTS.md`). 🔴 Binding venue risk = **human verification of T1/T2/P13**.

## Related Phase-0 archive (outside the round loop, cross-referenced)
- Literature kill-scan: [`../lit/SCAN_REPORT.md`](../lit/SCAN_REPORT.md) (GREEN, no scoop) + independent second
  opinion [`../lit/SCAN_SECOND_OPINION.md`](../lit/SCAN_SECOND_OPINION.md) (82% no-scoop).
- `(★)` de-risk: [`../code/DERISK_REPORT.md`](../code/DERISK_REPORT.md) (Sim A Γ-statistic + Sim B curve; not refuted)
  + raw `../code/phase0_results.json`.
- Paper-orientation health-check: [`../docs/HEALTH_CHECK_phase0.md`](../docs/HEALTH_CHECK_phase0.md)
  (on-track; fast-first sequencing; cascade-lower-bound gap named).
- Frozen ledger / state / decisions: `../LEDGER_collapse.md`, `../PROJECT_STATE.md`, `../DESIGN_DECISIONS.md`.

## Honesty rails carried into every round
- "AI-verified ≠ proved" — a claimed closure is "pending human verification"; the response file stays CANDIDATE/UNVERIFIED until ≥3 blind audits find no FATAL.
- P2 `Ω(loglog n/k)` is the matching lower for the **fast** fork ONLY; cascade needs `HS-lower` (B2-gated). Never conflate.
- `K_1` stays a bracket (B3); "decreasing in k" is rate-level; "P2 + algorithm" alone ≠ SODA.
- No-retreat: difficulty ⇒ escalate (codex-xhigh → web-Pro → fresh-context attacker), never downgrade the contribution. Only proof-of-death goes to the human gate.
