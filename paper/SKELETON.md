# Paper skeleton + component map — for owner review (writing step 2)

> Date 2026-06-22. Structure-clone target: **Altschuler–Tikhomirov, "A threshold for online balancing of sparse i.i.d.
> vectors" (arXiv:2509.02432)** — the closest in-area SODA-style exemplar (same model, threshold-characterization shape).
> Adapted to carry: an OFFLINE tight characterization (the technical centerpiece) + an ONLINE fixed-k result + the
> online-vs-offline SEPARATION (the conceptual headline) + a shelved growing-k open problem. Full statements/guards:
> `paper/FROZEN_RESULTS.md`; verification: `paper/VERIFICATION_CAMPAIGN.md`. **This is for your review before I expand full proofs.**

## Proposed title (pick one / steer)
- **A1.** "A Multicolor Threshold for Online Balancing of Sparse i.i.d. Vectors" (mirrors A-T; foregrounds the extension)
- **A2.** "Multicolor Discrepancy of Sparse Random Vectors: An Occupancy Threshold and an Online–Offline Separation"
- **A3.** "How Many Colors Help? Online vs. Offline Multicolor Discrepancy in the Sparse Regime"

## Target venue note
SODA 2027 (deadline 2026-07-09 AoE; re-confirm CFP format/blind). If a referee reads it as "in-area but incremental over
A-T," SoCG/ESA is the honest sibling home (the result is solid-strong regardless). Decide at the venue gate.

---

## SECTION SKELETON (≈10pp body + long proof appendix, no hard page limit)

**§1 Introduction.** The (average-case online) Beck–Fiala / vector-balancing model; the A-T `k=2` anchor (`Θ(loglog n)`,
d-independent); the question "what does the number of colors `k` do?"; **our three results** (T1 offline, T2 online fixed-k,
T3 separation) + the growing-k frontier; the conceptual headline = *more colors collapse the OFFLINE discrepancy to an
occupancy-entropy threshold `Ψ`, while ONLINE stays `Θ(loglog n)` for fixed k — a multicolor online–offline separation*;
related work; technical overview (the 3 custom ingredients of the offline upper; the multicolor A-T extension).

**§2 Preliminaries.** Model, `ondisc_k/offdisc_k`, `λ,L,H,Ψ`, the rank `ρ`, negative association / strongly-Rayleigh,
Lovett–Meka partial coloring (statement), Poisson tails (Bennett). State the over-claim-safe conventions.

**§3 The offline characterization `offdisc_k=Θ(Ψ)` [T1 — technical centerpiece].**
- §3.1 the occupancy-entropy LOWER `Ω(Ψ)` (Poissonization + extreme-value of k Poisson(λ); the 3 regimes).
- §3.2 the all-subsets negative-association **structural lemma**.
- §3.3 the density-sensitive **exact-cardinality Lovett–Meka splitting lemma**.
- §3.4 the **recursive color-tree** ⇒ the matching `O(Ψ)` upper (no extra log loss).

**§4 The online fixed-k result `ondisc_k=Θ(loglog n)` [T2].**
- §4.1 the `Ω(loglog n/k)` lower [P2: two-block projection, even & odd k].
- §4.2 the multicolor A-T upper `O(loglog n)` ∀k (seed + min-load repair + **the category recursion, reproduced in full** +
  the double-exponential decay). ⇒ fixed-k `Θ(loglog n)`.

**§5 The separation + the growing-k bracket [T3].** `ondisc_k=Θ(loglog n) ≫ offdisc_k=Θ(√d)=o(loglog n)` for fixed k
(cite Bansal–Meka for the fixed-k offline value, NOT T1); the bracket `max{Ψ,loglog n/k} ≤ ondisc_k ≤ loglog n`.

**§6 The growing-k frontier (open problem).** The reduction to the ranked-broadening lemma RB; why the two natural routes
fail — the symmetric `(R,s)` route gives `loglog n/log k` [B4], the naive expectation/quenched route is refuted by the phase
conveyor [B5]; the corrected truncated `PF_tr` / fold-or-Fibonacci target. (A clean, well-mapped open problem — off critical path.)

**Appendices.** Full proofs of §3–§4 (the long offline construction; the reproduced A-T recursion); BC lemma; deferred calcs.

---

## PROOF-COMPONENT MAP (theorem → constituent lemmas → status → section)
| theorem / step | lemmas used | verification | section |
|---|---|---|---|
| **T1 upper** `offdisc_k=O(Ψ)` | structural NA lemma (P11-A) → splitting lemma (P11-B, Lovett–Meka) → color-tree (P11-C) | V2 88% (re-derived+numeric) + round-4 3 blind | §3.2–3.4 |
| **T1 lower** `offdisc_k=Ω(Ψ)` | Poissonization + k-Poisson extreme value (P9→Ψ) | V3 88% + round-3/4 audits | §3.1 |
| **T2 upper** `ondisc_k=O(loglog n)` ∀k | seed tail (Bernstein) + **A-T category recursion** + double-exp decay (P12) | V1 90% (**reproduced**) + round-5 Audit A | §4.2 |
| **T2 lower** `ondisc_k=Ω(loglog n/k)` | two-block projection, even & odd k (P2) → A-T `k=2` lower (P1) | V3 88% | §4.1 |
| **T3 separation** (fixed k) | T2 (online) + `offdisc_k=Θ(√d)` [Bansal–Meka + routine ext] + `Ψ=o(loglog n)` cap | V3 88% | §5 |
| **growing-k bracket** | T1 (`online≥offline`) + P2 + T2 | — | §5 |
| **growing-k open problem** | RB ⟸ `PF_tr` ⟸ fold-or-Fibonacci; B4 + B5 (both routes dead); BC (P13) | round-6/7 audits | §6 |

> Supporting/context (cite, not re-prove): P1 (A-T `k=2` `Θ(loglog n)`), P3 (fresh-color), Bansal–Meka/Ezra–Lovett/Hoberg–
> Rothvoss (offline `k=2` `√d`), Bansal/HPVX (generic online multicolor), Manurangsi–Meka/2502.10516 (offline worst-case contrast).

---

## DRAFT — §1 Introduction + results (prose, for framing review)

**[Opening]** Online vector balancing asks: vectors `v_1,…,v_T ∈ R^n` arrive one at a time and each must be irrevocably
assigned a sign (or, here, a color) so as to keep every prefix's coordinate-wise imbalance small. In the average-case
(stochastic) regime where the `v_t` are i.i.d. uniform exactly-`d`-sparse 0/1 vectors with `T=Θ(n)`, Altschuler and
Tikhomirov [A-T 2025] proved a striking threshold: the optimal online two-color prefix discrepancy is `Θ(loglog n)`,
*independent of the sparsity `d`* (for `2 ≤ d ≤ (loglog n)²/logloglog n`) — an exponential separation from the `Θ(√d)`
offline (Beck–Fiala) value. We ask the natural next question: **how does the number of colors `k` change this picture?**

**[Results]** We give an essentially complete answer in two of the three regimes, and reduce the third to a single
crisply-stated lemma. Let `λ := Td/(nk) = Θ(d/k)` (the per-color occupancy), `L := log(ek)`, `H := loglog n`, and
`Ψ(λ,L) := 1 + √(λL) + L/log(e+L/λ)`.

> **Theorem 1 (offline, tight).** For `k → ∞` with `k ≤ d` and `d,k = (log n)^{o(1)}`, the optimal offline multicolor
> discrepancy is `offdisc_k = Θ(Ψ(λ, log k))` w.h.p. — a balls-into-bins occupancy-entropy threshold (three regimes:
> `√(λ log k)`, `log k/log((log k)/λ)`, `log k/loglog k`).

> **Theorem 2 (online, fixed k).** For every fixed `k ≥ 2`, the optimal online multicolor prefix discrepancy is
> `ondisc_k = Θ(loglog n)`, independent of `d` — extending the A-T `k=2` phenomenon to all fixed `k`.

> **Theorem 3 (separation).** Consequently, for every fixed `k`, online is exponentially worse than offline:
> `ondisc_k = Θ(loglog n) ≫ offdisc_k = Θ(√d) = o(loglog n)` (under the sparsity cap). For growing `k`,
> `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n`, and pinning the exact order reduces to the ranked-broadening lemma (§6).

**[Why it's interesting]** Offline, more colors *help* — the discrepancy collapses from `Θ(√d)` to the much smaller
occupancy threshold `Ψ`. Online, more colors do *not* help in the fixed-`k` regime — the `Θ(loglog n)` barrier of A-T
persists, d-independently. The contrast is the multicolor face of the online–offline gap, and (unlike the offline `k=2`
`√d`, which is classical) the offline multicolor threshold `Ψ` and its matching construction are new.

**[Technical overview]** The offline upper (Theorem 1) is the technical heart: a single draw of the random incidence
matrix is shown, via an *all-subsets negative-association* structural lemma, to be simultaneously well-behaved for every
column subset (so an adaptive partial-coloring recursion never destroys randomness); a *density-sensitive
exact-cardinality* Lovett–Meka splitting lemma then halves any color class with the occupancy-scale error; and a
*recursive color-tree* composes these with no loss beyond the threshold `Ψ`. Theorem 2 extends the A-T seed-and-repair
argument to `k` colors — its category / double-exponential machinery is genuinely color-blind, which we make precise.

**[Honesty notes to keep in the text]** results are stated for the regimes proven (fixed `k` for the separation; `k→∞`
for `Ψ`); the growing-`k` exact order is open; "online stays `loglog n`" is the fixed-`k` statement.
