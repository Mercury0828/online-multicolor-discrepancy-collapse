# Literature Kill-Scan Report — Phase 0 (`online-multicolor-discrepancy-collapse`)

> Date: 2026-06-22. Scanner: Claude Code (orchestrator). Kill criteria FROZEN before scanning (guide §Literature).
> Verdict at bottom. A second-opinion audit is archived separately (`lit/SCAN_SECOND_OPINION.md`).

---

## 1. Queries run (every query recorded)

| # | Query | Engine | Notable hits |
|---|---|---|---|
| Q1 | Altschuler Tikhomirov online prefix discrepancy sparse iid vectors loglog threshold | WebSearch | A-T 2509.02432 (the anchor); Bansal 2007.10622; 2308.01406 (optimal online disc); 2111.07049 (prefix disc/smoothed) |
| Q2 | online multicolor discrepancy sparse threshold k-partition prefix | WebSearch | 2504.18489 (tight multicolor LB); HPVX 2502.14624; 2502.10516 (multicolor LB fair division); 2102.02765 |
| Q3 | arxiv 2509.02432 online Beck-Fiala stochastic discrepancy | WebSearch | A-T 2509.02432 (v1/v2/v3); 2102.07342 (phase transition disc random hypergraphs); 2602.09948 (Feb-2026 Beck-Fiala coverage) |
| Q4 | online k-coloring random hypergraph local imbalance loglog discrepancy 2025 2026 | WebSearch | 2511.16100 (online graph coloring k-colorable, Nov-2025/Apr-2026); conflict-free hypergraph coloring; 1811.01491 (disc random hypergraph models) |
| Q5 | Altschuler Tikhomirov multicolor k-color online balancing follow-up 2026 | WebSearch | A-T author page (dylanaltschuler.github.io); A-T 2509.02432; HPVX 2502.14624 (binary-tree weighted reduction) |
| Q6 | SODA 2027 call for papers submission deadline | WebSearch | callforpaper.org/SODA27; wikicfp SODA27; SIAM SODA27 page (403 on fetch) |
| Q7 | frequency of frequencies online estimation species occupancy adversary discrepancy | WebSearch | only ecology / Good-Turing statistics — NO CS scoop (the "frequency-of-frequencies" structure is an analogy, not a competing paper) |
| Q8 | multicolor prefix discrepancy loglog n online sparse phase transition 2026 | WebSearch | NO matching paper — only Bansal 2007.10622, 1601.03311 (sparse set systems offline), clinical-trial noise. **Line appears OPEN.** |
| Q9 | SODA 2026/2027 double-blind anonymous submission policy | WebSearch | SODA26 hotcrp + SIAM submissions page (403 on fetch); policy not text-confirmed |

**Full-text fetches (arxiv.org — accessible):** 2509.02432 (abs+meta), 2502.14624 (abs), 2504.18489 (abs), 2007.10545 (abs), 2007.10622 (abs), 2502.10516 (abs).
**Failed fetches:** SIAM SODA27 + SODA26 submission pages — HTTP 403 (see §4).

---

## 2. Special assignments (load-bearing checks)

### (i) A-T arXiv:2509.02432 — "A threshold for online balancing of sparse i.i.d. vectors"
- **Version history:** v1 2025-09-02, v2 2025-09-11, **v3 2025-10-20** (minor edits). No new multicolor result in any version.
- **Model confirmed:** i.i.d. uniform d-sparse n-dim **binary** vectors, `T = Θ(n)`, sparsity `2 ≤ d ≤ (loglog n)²/logloglog n`; **two-color** online balancing (±1 signs).
- **Main theorem confirmed (P1):** every online algorithm incurs `≥ Ω(loglog n)`; an efficient algorithm achieves matching `O(loglog n)` w.h.p.; **the optimal online discrepancy is order loglog n, independent of d and the norms**. Independence ceases at `d = ω((loglog n)²)`.
- **Multicolor (k>2):** **NOT mentioned, NOT posed, NOT solved.** No multicolor follow-up found (A-T author page, Q5).
- **Verdict on (i):** ✅ P1 confirmed against source; **no scoop**; the multicolor question is genuinely untouched by A-T. (Spread/population lower-bound machinery `s_q = n/(log n)^{3^q}` not re-derived from full text here — flagged for attack-loop-time re-verify; abstract-level claim is solid.)

### (ii) GKKS arXiv:2007.10545 — online carpooling / edge orientation
- **Model confirmed:** online **edge orientation** on randomly-arriving graph edges (`d=2`): orient `u→v` or `v→u`, minimize `max_v |indeg − outdeg|`. **Binary orientation, NOT k-coloring / NOT pairwise-color-imbalance.**
- **Bound:** `O(loglog n)` for complete graphs (prior result, as the guide flagged: `O(·)` not `Θ(·)`); their contribution = `polylog(n,T)` for general graphs via expander decomposition.
- **k>2 / multi-bin local load:** **NOT addressed.**
- **Verdict on (ii):** ✅ confirmed it is indegree-orientation, not color-load imbalance; **no k-color special case hiding here**; no partial scoop.

### (iii) Bansal 2007.10622 — "Online Discrepancy Minimization for Stochastic Arrivals"
- **Model:** stochastic arrivals from an arbitrary distribution in `R^n` (general, not sparse-specific).
- **Bounds:** Komlós `Õ(1)`; Tusnády `O(log^{d+4} T)`; Banaszczyk `Õ(1)` for sub-exponential — all **generic polylog**.
- **Multicolor:** ✅ **explicitly extends to online multi-color discrepancy** — BUT only generic polylog upper bounds; **NO sharp sparse threshold, NO matching lower bound.**
- **Verdict on (iii):** ✅ confirmed — the multicolor *reduction* exists generically; our novelty must be the **sharp sparse threshold + the lemma `(★)`**, NEVER "the multicolor reduction". No scoop.

### (iv) HPVX arXiv:2502.14624 — "Online Envy Minimization and Multicolor Discrepancy: Equivalences and Separations"
- **Model:** **general unit vectors** `‖v_i‖₂ ≤ 1`, online, assigned to one of n colors. NOT sparse binary i.i.d.
- **Bounds:** multicolor disc `Θ(√log T)` (oblivious adversary); `Θ(√T)` (adaptive); i.i.d. adversary gives a separation (online vector balancing `Ω(√(log T/loglog T))` vs envy min `O(1)`).
- **Mechanism:** **binary-tree reduction** — internal nodes run weighted online vector balancing (this is exactly the N4-style multicolor-binary-tree; gives only the generic bound).
- **Verdict on (iv):** ✅ dense/general, no sparse loglog threshold, no matching sparse bound; the metric matches (pairwise-L∞) but the regime is different. Distinguish (sparse vs dense). Confirms N4 caveat. No scoop.

### (v) Adjacent multicolor lower bounds (offline — the contrast, not a scoop)
- **2504.18489** ("Tight Lower Bound for Multicolor Discrepancy"): **offline** worst-case hypergraph, `k`-color disc `≥ Ω(√n)` for all `k ≥ 2` (improving `Ω(√(n/log k))`). Opposite k-direction (offline worst-case: more colors do NOT help past √n). Use for the online-vs-offline contrast.
- **2502.10516** ("A new lower bound for multi-color discrepancy, fair division"): **offline** set-system, `k`-color disc `≥ Ω(√(n/ln k))`. Decreasing in `k` as `1/√ln k` but at the `√n` worst-case scale — entirely different model/regime from our online average-case `loglog n`. No scoop.

### (vi) Scoop sweep — recent listings
- **2511.16100** (online graph coloring for k-colorable graphs, Nov-2025/Apr-2026): different problem (proper coloring, competitive ratio), not discrepancy/load imbalance. No threat.
- **2602.09948** (Feb-2026, "Non-Additive Discrepancy: Coverage Functions in Beck-Fiala"): coverage-function discrepancy, not online multicolor sparse threshold. No threat.
- Q8 (the exact target description) returned **no matching paper** → the specific line is open.

---

## 3. Concern table → kill-criteria evaluation

| Threat checked | Pre-frozen criterion | Finding | Status |
|---|---|---|---|
| A-T or follow-up already gives the matching multicolor sparse characterization | RED if yes | A-T (all versions) is k=2 only; no multicolor follow-up | **NOT triggered** |
| GKKS hides a k-color local-load special case | RED/partial-scoop if yes | binary indegree orientation only; no k-color | **NOT triggered** |
| Bansal/HPVX already give a sparse sharp threshold + matching lower | RED if yes | only generic polylog / general-unit-vector `√log T`; no sparse threshold | **NOT triggered** |
| `(★)` provably false + no fast compression (plateau) | RED if proven | not a literature question — defer to the `(★)` de-risk (Sim A/B) | pending de-risk |
| P1/P2/P3 substrate contradicted by sources | YELLOW if yes | P1 confirmed; P2/P3 are our own derivations consistent with the A-T model | **NOT triggered** |
| Live lookup failure on load-bearing A-T/GKKS facts | cannot be GREEN if yes | A-T/GKKS/Bansal/HPVX all fetched from arxiv.org OK | **NOT triggered** |

---

## 4. Failed / partial lookups (honesty rail — recorded, not faked)

- **SIAM SODA27 + SODA26 submission pages: HTTP 403** (WebFetch blocked). **Deadline 2026-07-09** is confirmed by TWO independent CFP aggregators (callforpaper.org, wikicfp) + the SIAM SODA27 listing title; Philadelphia, Jan 24-27 2027. **Double-blind format NOT text-confirmed** for SODA27 — guide already flags "lightweight double-blind (2024+, verify against live CFP)" as a **writing-time** item, not a Phase-0 blocker. ⚠️ Re-confirm anonymization + page policy at writing time via the live CFP / hotcrp.
- These failures are on the **venue logistics**, NOT on the load-bearing math facts — so per the honesty rail they do **not** force a non-GREEN verdict (the A-T/GKKS load-bearing lookups all succeeded).

---

## 5. SCAN VERDICT

**GREEN (literature dimension)** — proceed toward attacking `(★)`, conditional on the `(★)` de-risk (Sim A/B) not refuting the decreasing+collapse picture.

**Rationale:**
- **No scoop.** No paper gives the matching multicolor sparse-threshold characterization (cascade or fast) in the A-T regime. A-T is k=2 only (v3 current, no multicolor follow-up). Bansal/HPVX multicolor results are generic-polylog / dense-general-vector with no sharp sparse threshold and no matching lower. The offline multicolor LBs (2504.18489, 2502.10516) are the contrast, not competitors.
- **Substrate intact.** P1 (`ondisc_2 = Θ(loglog n)`, d-independent) confirmed against the source. GKKS confirmed as binary orientation (no k-color hiding place). The Bansal/HPVX multicolor reductions confirm the N4 caveat and that our novelty is the lemma, not the reduction.
- **One YELLOW flag (logistics, not science):** SODA double-blind/page policy not text-confirmed (SIAM 403); deadline confirmed. Re-confirm at writing time. Does not gate Phase 0.
- **Deferred to de-risk:** the only RED-eligible scientific question (`(★)` false + no fast fallback ⇒ plateau) is a math question for Sim A/B + the attack loop, not the literature.

> Caveat carried forward: A-T's spread/population lower-bound machinery (`s_q = n/(log n)^{3^q}`) was confirmed only at abstract level, not re-derived from full text. Re-verify when P2's `Ω(loglog n/k)` reduction is briefed to the attacker.
