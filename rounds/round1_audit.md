# Round-1 audit — independent adversarial verifiers on `round1_response.md`

> Date 2026-06-22. TWO independent, blind, fresh-context adversarial auditors (proportionate for a substantive
> non-closure reply with load-bearing structural claims) + an orchestrator numeric triangulation
> (`code/verify_round1.py`). Convention: `rounds/README.md`. **Headline: the audits CONFIRM GPT's refutations and
> the new lemma, and IMPROVE on GPT by catching an over-claim in the FAST reduction.**

---

## Audit 1 — block-compression reduction (CLAIMs 1 & 2). Verdict (verbatim gist)

- **CLAIM 1 — block-compression lemma `ondisc_k ≤ q·ondisc_{kq}`: CORRECT (98%).**
  - Arithmetic sound: equal block sizes `q` ⇒ two block sums differ by ≤ `q(M_i−m_i) ≤ qR`; the equal-block-size
    cancellation is the load-bearing step.
  - Online-valid (fixed pre-chosen partition; real color = deterministic function of the virtual color at `t`).
  - Holds **pointwise at every prefix `t`**, per randomness-realization, sequence-coupled (no quantifier inversion;
    instantiating the virtual algorithm as the optimal `kq`-coloring is legitimate). No divisibility issue (`K=kq`).
  - **Strongest form:** for all integers `k,q≥1`, additive load over a fixed equal `k`-block partition of `[kq]`,
    `ondisc_k ≤ q·ondisc_{kq}`, pointwise in `t`, per realization. → **adopt as new tool P6.**
- **CLAIM 2 — FAST reduction: FLAWED AS WRITTEN (88%), repairable (~70%).**
  - The flaw: the **existential** hypothesis `K_1=O(loglog n)` ("disc-1 at SOME `K*=Θ(L)`") does NOT give
    `ondisc_{kq}=O(1)` for the **k-dependent** `kq=Θ(L)` you land on, unless **either** (a) `ondisc_K` is monotone
    non-increasing in `K` — **NOT proven, and P6/block-compression does NOT supply it** (P6 gives a downward factor-`q`
    relation, not upward monotonicity) — **or** (b) a genuinely **uniform-band** hypothesis.
  - **Minimal repair (H-uniform):** `ondisc_K ≤ C'` for EVERY integer `K∈[c1 L, c2 L]` with `c2 ≥ 2 c1`. Then for
    `k ≤ c1 L`, pick `q=⌈c1 L/k⌉` so `kq∈[c1 L, 2 c1 L]⊆[c1 L, c2 L]` ⇒ `ondisc_k ≤ q·C' = O(L/k)`. For `k∈[c1 L, c2 L]`
    the band gives `O(1)` directly.
  - **Residual gap:** the regime **`L ≲ k ≲ M`** (more precisely `c2 L < k < Ω(M)`) is NOT covered by the band nor by
    the fresh-color bound `1+⌊M/k⌋ = O(M/k)` (which **exceeds** the target `O(1)` since `M ≫ L`). Needs the band
    extended toward `M`, or a monotonicity proof, or a direct argument. **Real residual.**

## Audit 2 — refutations & obstructions (CLAIMs A, B, C). Verdict (verbatim gist): **A, B, C all CORRECT (93%).**

- **CLAIM A (refutation 2.2): CORRECT.** Recomputed exactly: `Q({c})=1/2`; `Q({c,c'})=(k−2)/(2k) > 1/4` for `k≥5`
  (equality at `k=4`); `Q(|A|=a)=(k−a)/(2k)`; binding constraint at `a=k−1` ⇒ `ρ ≥ (2k)^{−1/(k−1)} = 1−Θ(log k/k)`.
  Honestly weakened: shows range + S_k-symmetry + near-optimal-marginals do NOT force product domination; does NOT
  claim the law is algorithmically realized (so it refutes literal-`(★)`-under-symmetry, not a strawman).
- **CLAIM B (refutation 2.3): CORRECT.** Ratio `Q_1({c,c'})/Q_1({c})² = (t−1)/t · k/(k−1)`, exactly `>1 ⟺ t>k`,
  magnitude `1+O(1/k)`. **Stronger than A** — it fails on a GENUINE symmetrized optimal disc-1 (P3) process, killing
  the exact marginal `(★)` while leaving a constant-loss `(★')` alive (the `(1+O(1/k))^{|A|}` slack stays bounded for
  `|A|=O(k)`). Minor conceded modeling caveats (independent `d/n` coverage; conditioning on degrees `< k`) don't
  undermine the conclusion.
- **CLAIM C (obstructions): CORRECT, properly scoped.** (i) max-vs-sum: the elementary-symmetric potential controls
  `Σ_{|A|=a} q(A)` but the cover needs `max_{|A|=a} q(A)`; an adaptive junta concentrates the mass, losing up to
  `C(k,a) ≈ 2^k` near `a=k/2` — enough to kill a `k`-fold recurrence (blocks THIS potential, not a general
  impossibility). (ii) bounded-fiber: `(r,…,r,0)` yields `2^{k−1}` subset-certificates from ONE history ⇒ un-quotiented
  subset-counting over-counts; a real Profile-Branching `Ω(loglog n/log k)` lower needs a bounded-fiber encoding
  (`Ω(log k)` NEW bits/level after quotienting shared history) — absent. Blocks the whole class of un-quotiented
  subset-certificate encodings, not just one.

## Orchestrator numeric triangulation (`code/verify_round1.py`)
- **Block-compression: 0 violations** of `real_range ≤ q·virtual_range` across `(k,q)∈{(2,3),(3,4),(4,3),(5,2),(3,8)}`,
  max ratio reaching exactly `q` — empirically confirms P6.
- **Mixture law: exact match** — `Q({c})=0.5`, `Q({c,c'})>0.25` for `k≥5`, `Q(a=k−1)=1/(2k)`, `ρ_needed=(2k)^{−1/(k−1)}`
  (k=5→0.562, k=8→0.673, k=12→0.749).
- **Eq.(11) ratio:** my Monte-Carlo was **underpowered** (sparse regime `μ=td/n≪1` ⇒ pairs almost never sampled, so the
  empirical ratio is unreliable) — noted honestly; the closed-form ratio is **analytically verified by Audit 2**, not
  by this MC. Not a discrepancy with GPT.

---

## Classification
- **GAP / PROGRESS — NOT FATAL.** Round 1 produced: one **verified new lemma** (P6 block-compression), a **verified
  refutation** of literal/exact `(★)` (CLAIMs A,B), **verified obstructions** (C), and — via the audit — a **caught
  over-claim** (CLAIM 2 FAST reduction needs the uniform-band hypothesis + has a residual `L≲k≲M` gap).
- **No proof-of-death** (literal `(★)` refuted but `(★')` open AND FAST not dead) ⇒ **no kill, no human gate.**
- **No stall** (`K_stall` not triggered — real new verified content). **No N-route / barrier violation** (GPT respects
  B1/B2/B3, N4; agrees with B1).

## Single biggest risk going forward
The **FAST floor is harder than first framed**: it needs `ondisc_K=O(1)` uniformly across a `Θ(loglog n)` band (or a
monotonicity-in-`K` theorem), AND a separate handle on `L≲k≲M`. The clean sub-question to settle early: **is `ondisc_K`
monotone non-increasing in `K`?** (If yes, the existential `K_1=O(loglog n)` suffices and FAST simplifies dramatically;
P6 does NOT decide it.)

## OUTCOME (what the orchestrator did)
1. **Absorb P6** (block-compression `ondisc_k ≤ q·ondisc_{kq}`, audit-verified + numerically 0-violation) into the
   substrate (ledger). It is a genuine new tool — the first verified gain of the attack loop.
2. **Re-state the FAST target** with the audit's correction: prove **(CP-uniform)** `ondisc_K=O(1)` for all `K` in a
   `Θ(loglog n)` band via a dynamic palette-persistence lemma, + resolve `L≲k≲M`, + the monotonicity sub-question.
3. **Re-state the CASCADE target:** pathwise `(★')` with **max-cylinder** control + the **bounded-fiber** witness-entropy
   lemma (B2: not from any projection).
4. **Confidence-trend update** (post-audit): cascade 0.45 / fast 0.33 / plateau 0.04 / other 0.18 (fast nudged down vs
   the provisional 0.35: the uniform-band + `L≲k≲M` residual make the fast floor harder than GPT's framing; cascade up
   per single-leader evidence + GPT lean; plateau down per the collapse + P6).
5. **Dispatch `round2_brief.md`** (fast-first) — the two sharpened lemmas + the monotonicity sub-question. No human
   gate (no closure, no kill, no scope change). Owner relays.
