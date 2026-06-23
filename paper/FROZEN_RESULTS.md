# FROZEN RESULTS — results self-check (writing step 1) + human-verification checklist

> Date 2026-06-22. The exact, frozen statements for the SODA draft, separating PROVEN-pending-human-verification from OPEN,
> with the over-claim guards and the human-verification checklist. **Status of all theorems: "AI-verified (multi-round
> adversarial audit), PENDING HUMAN VERIFICATION."** This doc is also the verification worklist (the venue-floor determinant).
> Sources: `LEDGER_collapse.md` (P1–P13, B1–B5, N1–N7), `rounds/round{4,5,6,7}_*`.

## Model (state once, precisely)
`R^n`; arrivals `v_1,…,v_T` i.i.d. uniform over EXACTLY-`d`-ones 0/1 vectors, `d ∈ [2, (loglog n)²/logloglog n]`, `T = Θ(n)`.
A `k`-coloring assigns each `v_t` a color in `[k]` (ONLINE = irrevocable, no future knowledge; OFFLINE = full knowledge).
Color-class load `S_c(t)=Σ_{s≤t,χ(s)=c} v_s`; coordinate `i` has loads `x_{i,c}`; pairwise range `R_i = max_c x_{i,c} − min_c x_{i,c}`.
`ondisc_k` / `offdisc_k` = optimal online / offline value of `max_{t,i} R_i` (whp). `λ := Td/(nk) = Θ(d/k)`, `L := log(ek)`,
`H := loglog n`. `Ψ(λ,L) := 1 + √(λL) + L/log(e + L/λ)`.

---

## THE THEOREMS (frozen)

### T1 (offline characterization — the technical centerpiece). [P11]
For `k → ∞`, `k ≤ d`, `d,k = (log n)^{o(1)}`:  **`offdisc_k = Θ(Ψ(λ, log k))` w.h.p.**
Three regimes: `√(λ log k)` (`λ ≳ log k`); `log k/log((log k)/λ)` (`1 ≪ λ ≪ log k`); `log k/loglog k` (`λ = Θ(1)`).
*Lower:* first-moment + Poissonization + the extreme-value spread of `k` Poisson(`λ`) (balls-into-bins). *Upper:* an
all-subsets negative-association structural lemma + a density-sensitive exact-cardinality Lovett–Meka partial-coloring
splitting lemma + a recursive color-tree (no extra `log d / √log d / loglog n` loss).

### T2 (online, fixed k). [P12 + P2]
For every FIXED `k ≥ 2`:  **`ondisc_k = Θ(loglog n)`, independent of `d`.**
*Upper:* `ondisc_k = O(loglog n)` for ALL `k` — a multicolor extension of Altschuler–Tikhomirov (seed colors + min-load
repair of the uniquely-largest exceptional row + the `k`-free category / double-exponential machinery). *Lower:* `Ω(loglog n/k)` [P2].

### T3 (multicolor online-vs-offline separation — the conceptual headline).
For every fixed `k`, under the sparsity cap `d ≤ (loglog n)²/logloglog n`:  **`ondisc_k = Θ(loglog n) ≫ offdisc_k = Θ(Ψ) = o(loglog n)`.**
Extends A-T's `k=2` online-vs-offline gap to all fixed `k`. (Online stays `loglog n`; offline drops to the occupancy threshold `Ψ`.)

### Growing-k bracket + the OPEN problem.
**`max{Ψ(λ,log k), loglog n/k} ≤ ondisc_k ≤ loglog n` w.h.p.** (lower: P11 `online≥offline` + P2; upper: T2's `O(loglog n)`).
**OPEN:** the exact growing-`k` order. Conjectured `Θ(max{Ψ, loglog n/k})` (the "ranked-broadening lemma" RB ⇒ this). Reduced to
a sharply-specified probabilistic lemma — the truncated **`PF_tr`** via a **fold-or-Fibonacci incidence-excess** count for the
asymmetric LeftGap rule. Both natural routes are PROVEN DEAD: the symmetric `(R,s)` route [B4] gives only `loglog n/log k`; the
naive expectation / quenched-factorization route [B5] is refuted by the phase conveyor. ⇒ a clean, well-mapped frontier.

---

## STATUS TABLE (post multi-agent verification campaign — `paper/VERIFICATION_CAMPAIGN.md`)
| result | status | verification | residual (prose-completeness only) |
|---|---|---|---|
| T1 offline `Θ(Ψ)` (P11) | ✅ **VERIFIED** (AI multi-agent; human=referees) | 3 blind (92/88/88%) + V2 re-derivation (88%) + V3 lower (88%) | the limiting-LM exact-equality + `O(1)` cleanup + Poissonization-error bookkeeping (write in full) |
| T2 online fixed-k `Θ(loglog n)` (P12) | ✅ **VERIFIED** | Audit A (85%) + **V1 reproduced the A-T category recursion (90%)** | the exact step-3 column-counting constant (soundness-robust) |
| T3 separation (fixed k) | ✅ **VERIFIED** | V3 (88%) | cite fixed-k offline `Θ(√d)` to Bansal–Meka, NOT T1 (guard #6) |
| growing-k bracket | ✅ **VERIFIED** | (P2,P11,P12) | — |
| P2 / BC (P13) | ✅ **VERIFIED** | V3 / round-6 audit (88%) | the A-T `ρ`-asymmetry insensitivity / cover-cert + P8-cost (mechanism sound) |
| growing-k EXACT order | **OPEN (shelved frontier)** | — | RB ⟸ `PF_tr` ⟸ fold-or-Fibonacci (research-open; off critical path) |

> 🟢 **READY TO WRITE.** No FATAL/GAP found by any agent; residuals are prose-completeness, not logic holes. Per the owner's
> standard, AI-multi-agent-verified = "verified"; the genuine human check is the post-submission referee community.

---

## OVER-CLAIM GUARDS (must surface in the paper text — from `docs/HEALTH_CHECK_milestone_r5.md`)
1. 🔴 **"AI-verified ≠ proved."** Do NOT submit headline theorems no human has checked. Reproduce the A-T category recursion
   (T2); human-check the NA-union + exact-LM (T1). State the proof-provenance honestly if time forces submission before full check.
2. **"MATCH ruled out" is SMALL-k ONLY.** The separation (T3) is rigorous **for fixed k**; for growing `k` with `loglog n/k ≲ Ψ`,
   whether `ondisc_k = Θ(Ψ)` is OPEN. Never write a blanket "online ≠ offline".
3. **d-independence-breaking is OFFLINE-only.** `Ψ` depends on `λ = Td/(nk)` (offline, d-dependent); the ONLINE upper (T2) is
   itself d-INDEPENDENT (`O(loglog n)` ∀k). Do not blur this across the online/offline boundary.
4. **The separation needs `Ψ = o(loglog n)` under the sparsity cap** `d ≤ (loglog n)²/logloglog n` — state the cap every time.
5. **Keep `K_1` a bracket** `[Ω(loglog n), O(log n/loglog n)]` (B3 — never headline `K_1=Θ(M)`); "decreasing in k" is rate-level,
   not per-k monotone (N6: exact `ondisc_2=11/9 < ondisc_3=13/9`, `ondisc_4=1`). Foreground the novelty as **`Ψ`'s threshold form
   + the construction's 3 custom ingredients**, NOT the mere existence of a multicolor bound.
6. 🔴 **The fixed-k offline value `offdisc_k=Θ(√d)` in the SEPARATION (T3) must be cited to Bansal–Meka (1810.03374) /
   Ezra–Lovett / Hoberg–Rothvoss (2-color `√d`) + the routine multicolor small-ball extension — NOT to T1.** T1 (`offdisc_k=Θ(Ψ)`)
   is proven only for `k→∞`; it agrees with `Θ(√d)` on the overlap (`Ψ=Θ(√d)` at fixed k) but is NOT the *source* of the fixed-k
   value. (Verification V3 flagged this scoping; the over-claim guard #2 already covers it.)

## POSITIONING / related work (for the intro)
- **Anchor:** Altschuler–Tikhomirov (arXiv:2509.02432, 2025) — `k=2` online sparse i.i.d. discrepancy `Θ(loglog n)`, d-independent.
  We extend to multicolor (the color axis): T2 (online, all fixed k) + T1 (offline tight) + T3 (separation).
- **Offline random-set-system discrepancy (k=2, known):** Bansal–Meka (1810.03374); Ezra–Lovett; Hoberg–Rothvoss — `Θ(√d)`. Our
  T1 is the **multicolor** occupancy-entropy threshold `Ψ` (the `k`-color upper at the threshold is NOT on the shelf).
- **Generic online multicolor:** Bansal (2007.10622) polylog; HPVX (2502.14624) general unit vectors `Θ(√log T)` — neither gives
  the sparse entropy-scale statement. Offline worst-case multicolor LBs (2504.18489 `Ω(√n)`, 2502.10516) = the contrast.

## WRITING PLAN (manual pipeline; `venue-prompts/soda/` not present in this repo)
1. **(this doc) results self-check** ✅ — exact statements, status, guards, verification checklist.
2. **Component map + structure-clone** an in-area SODA exemplar (recent discrepancy / online-algorithms paper); build the
   proof-component table (which of P1–P13 proves which theorem step).
3. **Draft** — intro + the separation headline; the offline construction (T1, longest section — writing it IS verification);
   T2 (reproduce the A-T category recursion); the growing-k bracket + the open-problem section (RB → `PF_tr` → fold-or-Fibonacci).
4. **Trim ↔ writing-reviewer JOINT convergence** (owner rule); **pre-submission check** (lightweight double-blind — re-confirm
   the live SODA27 CFP; deadline 2026-07-09 AoE).
- 🔴 **Co-critical path: HUMAN verification of T1/T2/P13** (the venue floor) — run alongside writing.
