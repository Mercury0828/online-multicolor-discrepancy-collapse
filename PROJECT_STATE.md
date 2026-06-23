# PROJECT_STATE — `online-multicolor-discrepancy-collapse`

> Live progress file. Update every step/round. **Re-read this + `LEDGER_collapse.md` + frozen artifacts when
> context grows long — never from memory.** Owner-facing summaries are Chinese; this file is English.

---

## ❄️ COLD-START / RESUME (read FIRST — frozen 2026-06-22)
**FROZEN here by owner decision; resume WRITING after Thursday 2026-06-25 (token budget tight). Pushed to GitHub.**

**One line:** The research/attack loop is CLOSED. Two complete tight theorems + a separation are **VERIFIED** (multi-agent
adversarial campaign — owner's standard = AI-verified, human check deferred to referees). We are at the **writing** stage;
the paper SKELETON is done and awaiting owner review of framing/title/venue; next is expanding the full proofs.

**The results (all VERIFIED, no FATAL/GAP — `paper/FROZEN_RESULTS.md`, `paper/VERIFICATION_CAMPAIGN.md`):**
- **T1 (offline, tight):** `offdisc_k = Θ(Ψ(λ, log k))`, `Ψ=1+√(λL)+L/log(e+L/λ)`, `λ=Θ(d/k)`, `L=log(ek)` — for `k→∞, k≤d`.
- **T2 (online, fixed k):** `ondisc_k = Θ(loglog n)`, d-independent (extends A-T `k=2` to all fixed k).
- **T3 (separation):** for fixed k, `ondisc_k=Θ(loglog n) ≫ offdisc_k=Θ(√d)=o(loglog n)` (under the sparsity cap).
- **growing-k:** bracket `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n`; exact order OPEN = **SHELVED** (owner) as a frontier
  (RB ⟸ truncated `PF_tr` ⟸ fold-or-Fibonacci; symmetric route B4 + naive route B5 both proven dead).

**TO RESUME, read in order:** (1) this block + `## Current phase`; (2) `paper/SKELETON.md` (skeleton + component-map + draft
intro — **owner to review framing/title/venue first**); (3) `paper/FROZEN_RESULTS.md` (exact statements + over-claim guards +
the writeup checklist); (4) `paper/VERIFICATION_CAMPAIGN.md` (what's verified + residual prose items); (5) `LEDGER_collapse.md`
(substrate P1–P13, barriers B1–B5, the full round history R1–R7).

**NEXT ACTION (after the owner reviews `paper/SKELETON.md`):** expand the full proofs — §3 the offline construction (longest:
NA structural lemma → exact-cardinality Lovett–Meka splitting → recursive color-tree + the Poisson lower), §4 reproduce the
A-T category recursion (V1's derivation), §5 the separation (🔴 cite Bansal–Meka for the fixed-k offline `Θ(√d)`, NOT T1),
§6 the growing-k open problem. Carry ALL over-claim guards (FROZEN_RESULTS §guards). Deadline SODA27 **2026-07-09 AoE**
(re-confirm CFP format/blind). Solver = web GPT-5.5-Pro (owner relays); audits = subagents.

**Owner decisions still pending (from `paper/SKELETON.md`):** title (A1/A2/A3); confirm the "more colors: offline helps,
online doesn't" headline; SODA vs SoCG/ESA venue; whether to add any "lift" content (recommend: keep current scope, write the
three results solidly). Cross-project dedup vs the two siblings = CLEAN (`lit/DEDUP_sibling_projects.md`).

---

## Current phase
**📝 WRITING.** (attack loop closed at Round 7 — see below.)

 Standing — **TWO complete tight results** (offline `offdisc_k=Θ(Ψ)` P11;
online fixed-k `ondisc_k=Θ(loglog n)` P12) + the **online-vs-offline separation** (T3) + the growing-k bracket
`[max{Ψ, loglog n/k}, loglog n]`. Rounds 6–7 (the two owner-authorized RB/PF rounds) did NOT close growing-k: banked **P13 (BC)**,
**B4** (symmetric route dead → `H/log k`), **B5** (the displayed PF refuted by a phase conveyor — but NOT a lower bound, RB still
open). The open problem is sharply mapped (RB ⟸ truncated `PF_tr` ⟸ a fold-or-Fibonacci incidence-excess lemma; both natural
routes proven dead). **Per the pre-committed plan ⇒ PIVOT TO WRITING. No further RB/PF rounds.** Writing step 1 done:
`paper/FROZEN_RESULTS.md` (exact statements + status + over-claim guards + the human-verification checklist).
**VERIFICATION CAMPAIGN COMPLETE (owner-mandated, multi-agent):** A/B/C all **VERIFIED**, no FATAL/GAP —
V1 (T2: reproduced the A-T category recursion, 90%) + V2 (T1 offline construction re-derived + numerically checked, 88%) +
V3 (T1 lower Ω(Ψ) + separation + P2, 88%), on top of the prior per-round audits. Residuals are prose-completeness only.
Owner standard: AI-multi-agent-verified = "verified"; human check = post-submission referees. Cross-project dedup CLEAN
(`lit/DEDUP_sibling_projects.md`). 🟢 **READY TO WRITE.** (`paper/FROZEN_RESULTS.md`, `paper/VERIFICATION_CAMPAIGN.md`.)
**P(SODA-worthy paper by 07-09) ≈ 0.55–0.65.** **WRITING — skeleton done, awaiting owner review.** `paper/SKELETON.md` =
structure-clone (A-T exemplar) + section skeleton + proof-component map + draft §1 intro/results/separation framing + 3 title
options. **NEXT:** owner reviews framing/title/venue → I expand the full proofs (offline construction §3 longest; T2 reproduce
A-T recursion §4; separation §5; growing-k open problem §6).

## Progress

- [x] Read `guide.md` (read-only constitution) in full + README + bootstrap.
- [x] Scaffold: `code/`, `lit/`, `docs/`, `rounds/`; day-0 artifacts created.
- [x] Literature kill-scan = **GREEN** (`lit/SCAN_REPORT.md`); P1 quantifier + d-independence verified vs A-T source.
- [x] Second-opinion subagent = **AGREE-GREEN, 82% no-scoop** (`lit/SCAN_SECOND_OPINION.md`).
- [x] `(★)` de-risk: Sim A (Γ-statistic) + Sim B (curve) = **NOT refuted, mildly cascade-favorable** (`code/DERISK_REPORT.md`).
- [x] Paper-orientation health-check subagent (`docs/HEALTH_CHECK_phase0.md`) — on-track + fast-first sequencing + cascade-lower gap.
- [x] **Phase-0 verdict = GREEN** → human gate (awaiting owner confirmation to start the attack loop).

## Frozen results + numbers + artifact paths

- Substrate `P1–P12` (P6 block-compression, P7 `√(d/k)`, P8 aggregate cover, P9 occupancy floor [→P11], P10 mean-square L2,
  **P11 = OFFLINE `offdisc_k=Θ(Ψ)`**, **P12 = ONLINE `ondisc_k=O(loglog n)` ∀k** — all audit-verified), `B1–B3`, `N1–N7`: see ledger.
- 🟢🟢 **BANKED (matching, pending human verification):** **(offline) `offdisc_k = Θ(Ψ(λ, log k))`** (P11); **(online, fixed k)
  `ondisc_k = Θ(loglog n)`** (P12 upper + P2 lower). `Ψ=1+√(λL)+L/log(e+L/λ)`, `λ=Θ(d/k)`, `L=log(ek)`. A genuine multicolor
  **online-vs-offline separation** (online `loglog n` ≫ offline `Ψ` for fixed k).
- **Growing-k (open):** `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n`; the gap = the **ranked-broadening lemma (RB)** ⇒ conjectured
  `ondisc_k = Θ(max{Ψ, loglog n/k})`. RB is the exact sufficient reduction (verified); UNPROVEN. MATCH (online=Ψ) ruled out for
  small k only. L2→L∞ no-go proven (P10 can't reach `Ψ`).
- **Open (remaining):** growing-k tightness, now narrowed to the **Profile-Fibonacci lemma (PF)** via the asymmetric **LeftGap**
  rule (UNPROVEN, 60%). 🔴 The **symmetric `(R,s)` route is DEAD (B4)** — gives `H/log k` not `H/k`; banked **P13 (BC)**.
- Both complete results (P11, P12) + P13 pending human verification of the named steps (P11: NA-union + exact-LM + m=O(1) tail;
  P12: A-T category recursion; P13: cover-certificate + P8-cost dependencies).
- **P1 verified vs source:** A-T 2509.02432 v3 Def 1.4 (disc = max-over-prefixes ℓ∞ partial sum) + Thm 1.1
  (lower `max(⅛ loglog n, Ω(√d))`, upper `35 loglog n` for `d≤(loglog n)²/logloglog n`); d-independent. Quantifier
  matches ours exactly.
- 🔴 `K_fresh = Θ(M) = Θ(log n/loglog n)` is the PROVEN *sufficient* collapse scale (P3); the true threshold
  `K_1` is NOT proven `Θ(M)` — only `Ω(loglog n) ≤ K_1 ≤ O(log n/loglog n)` (B3). Do not write `K_1=Θ(M)`.
- 🔴 **Cascade-fork lower gap:** P2 `Ω(loglog n/k)` is the matching lower for the FAST fork only; the CASCADE
  fork (`loglog n/log k`) needs a NEW stronger lower `HS-lower` (P2 is not it). Name the fork when claiming "tight".
- **De-risk numbers (`code/phase0_results.json`):** Sim B d=2 n=2e5: ondisc_k = 3,3,2,2,2,2,1,1 for k=2..20 (collapse
  ~k≈2–3·M). Sim A binding level r=D: mean |F|≈1.0–1.08, Γ(q) increasing (k=4 r=2: 1.31→2.14→2.15, stable n=2e5/1e6).
  Code: `code/sim_collapse.py`, `code/run_phase0.py`. Player = `lookahead` (heuristic, NOT optimal).

## Confidence trend

| Date | cascade | fast | plateau | other |
|---|---|---|---|---|
| 2026-06-22 | 0.40 | 0.35 | 0.10 | 0.15 |

## TODO + pending-human-decisions

- 🔴 **PENDING HUMAN GATE (c) — SCOPE/CONTRIBUTION (Round-2 reshaping):** the clean forms are refuted; owner chooses the
  scope: **(A)** full d-range richer theorem `Θ(max{1,F_online,√(d/k)})` (needs the matching online upper across all
  regimes — most novel, most work); **(B)** restrict `d` so `√(d/k)=o(1)` and recover a clean online phase-transition
  (cleaner but narrower, and tension with A-T's d-independence ethos); **(C)** offline multicolor `√(d/k)` + the small-k
  online behavior. Plus: confirm SODA still the venue. Fold in `docs/HEALTH_CHECK_gate_c.md`. Agent does NOT pick scope.
- (Resolved earlier) Phase-0 GREEN gate passed; attack loop running, GPT-5.5-Pro, fast-first.
- **Sequencing note for the owner (gate (c)-adjacent, NOT a downgrade):** recommended attack ordering = bank the
  **FAST `O(loglog n/k)` upper (`HS-alt`) first** as a guaranteed SODA floor (it makes P2 a complete tight theorem,
  no adaptivity-stability needed), THEN gamble on `(★)`/cascade. NO-RETREAT intact (still targeting the matching
  characterization; the fast tight theorem IS a matching characterization, the cascade is the stretch upgrade).
- On GREEN confirmation: dispatch `rounds/round1_brief.md` to codex GPT-5.5-xhigh (or write-to-file +
  owner relays). Re-confirm SODA double-blind/page policy at writing time (carried YELLOW).

## Notes / honesty rails active

- "AI-verified ≠ proved"; no "optimal" without a matching lower bound; `(★)` is the single load-bearing crux.
- **Cascade-fork lower gap:** P2 `Ω(loglog n/k)` matches the FAST fork only; cascade (`loglog n/log k`) lower is
  zero-proven (needs `HS-lower`, B2-gated). Never present P2 as "the matching lower" without naming the fork.
- **K_1 stays a bracket** `Ω(loglog n) ≤ K_1 ≤ O(log n/loglog n)` (B3); phrase collapse as "for `k ≥ Θ(M)`".
- **"Decreasing in k" is RATE-level**, not a strict per-k monotonicity theorem (Sim B flat stretches;
  not in P1–P3). Per-sequence non-monotonicity B-note still holds (`disc_{k+1} ≤ disc_k` FALSE per-sequence).
- **"P2 + fresh-color algorithm" alone is NOT a SODA paper** (= the RANDOM/ESA downgrade) — the floor is the
  FAST tight theorem.
- Balls-into-bins folklore risk: if `HS-upper` is balls-and-bins-style, foreground novelty on `HS-lower` + A-T anchoring.
