# Brief for GPT-5.5 Pro — round 1, `HS-core` (prove or refute `(★)`)

> **Archive role:** round-1 BRIEF (solver-exchange archive; see `rounds/README.md`). Pairs with
> `rounds/round1_response.md` (GPT Pro's reply: verbatim + restatement) and `rounds/round1_audit.md` (adversarial audit).
>
> ✅ **GREEN gate passed (2026-06-22).** Owner elected to dispatch **directly to web GPT-5.5-Pro** (overriding the
> codex-xhigh default) and to **relay manually** (write-file → owner copy-pastes → owner pastes the reply back for
> adversarial audit). Sequencing = **fast-first** (owner-unopposed; recommended by the Phase-0 health-check).
> **Everything inside the code fence below is the message to paste to GPT-5.5-Pro.**
> **Freeze FACTS / free METHODS. Do NOT edit the FROZEN/REFUTED/BARRIER blocks to assert more than is proven.**
> (Derived from `guide.md` Appendix, refined with the Phase-0 health-check sequencing + the verified P1 quantifier.)

```
TARGET (exact claim to settle):
  PROVE or REFUTE (★): for a near-optimal online k-coloring on μ_{d,n}, the forbidden (high-color) set
  F_r(I) of a typical coordinate I at discrepancy level r satisfies Q_r(A):=Pr(A ⊆ F_r(I)) ≤ ρ_r^{|A|}
  for all A ⊆ [k], STABLE under adaptive online evolution (the static profile (D,…,D,0) shows this is
  NOT a plain Chernoff bound). (★) controls BOTH matching bounds:
   - if (★) holds: HS-upper (elementary-symmetric potential G_i(s)=∏_c(1+s·e^{λ z_{i,c}}), z=S−occ/k,
     recurrence ρ_{r+1}≤C_d(dρ_r)^k+ε_n ⇒ r=O(loglog n/log k)) AND HS-lower (Profile-Branching: each
     level raises pruned-witness entropy ≥ c·log(k+1) ⇒ |W_r|≥(k+1)^{cr}) ⇒ ondisc_k=Θ(max{1,loglog n/log(k+1)});
   - if (★) fails: HS-alt — can a star/junta compression online strategy give O(loglog n/k)? (paired with
     P2 ⇒ ondisc_k=Θ(max{1,loglog n/k})). Either fork closes the project.

FROZEN SUBSTRATE — use freely, do NOT re-derive (P1–P4 Phase-0-verified; P5 is sim-only, do NOT cite as proof):
  P1: ondisc_2 = Θ(loglog n), d-independent [A-T 2509.02432 v3, Def 1.4: disc = max_{t≤T} ‖Σ σ_i X_i‖_∞;
      Thm 1.1: lower max(⅛ loglog n, Ω(√d)), upper 35 loglog n for d ≤ (loglog n)²/logloglog n].
  P2: ondisc_k ≥ Ω(loglog n/k) for ALL k (even & odd) — two-block projection + the proven asymmetric odd-k version.
  P3: ondisc_k ≤ 1+⌊M/k⌋ = O(1+log n/(k·loglog n)); k>M ⇒ ondisc_k=1; M=Θ(log n/loglog n). [K_fresh = SUFFICIENT scale]
  P4: forcing condition — support E forces D+1 ⟺ ∪_{i∈E} F_D(i) = [k], F_D(i)=argmax_c x_{i,c}.

REFUTED ROUTES — do NOT attempt:
  N1: increasing forms Θ(loglog n+√log k), Θ(√k·loglog n) — DEAD (P3 gives discrepancy-1 for large k).
  N2: naive k-ary witness tree (|W_r|≍k^r mechanically) — collapses (B1: forbidden sets share).
  N3: a fancier balanced cut / single 1-D projection to beat loglog n/k — capped at Ω(loglog n/k) (B2).
  N4: black-box A-T-into-a-multicolor-binary-tree — input adaptively thinned; use a DIRECT k-color analysis.

BARRIERS to respect:
  B1: profile (D,…,D,0) has |F_D|=k−1; two coordinates cover [k] ⇒ no k independent sub-certificates.
  B2: any single fixed 1-D zero-sum projection + A-T spread is capped at Ω(loglog n/k) ⇒ loglog n/log k
      REQUIRES nonlinear profile/subset-entropy. ⇒ The CASCADE LOWER bound is NOT P2 and NOT any projection.
  B3: K_1=Θ(M) is NOT proven (only Ω(loglog n) ≤ K_1 ≤ O(log n/loglog n)); do NOT assume it.

KEY STATUS NOTE (do not mis-state which bounds are open):
  - FAST fork Θ(max{1,loglog n/k}): P2 IS the matching lower; only the O(loglog n/k) UPPER (HS-alt) is missing.
  - CASCADE fork Θ(max{1,loglog n/log k}): BOTH bounds open — the upper (HS-upper) AND a STRONGER lower
    (HS-lower, Ω(loglog n/log k)) that P2 does NOT give and B2 forbids from any fixed projection.

OPEN QUESTION (method-agnostic): prove or refute (★); if it holds, supply HS-upper AND HS-lower; if it
  fails, supply HS-alt (the star/junta compression + O(loglog n/k)); if neither, say so plainly and state
  the precise obstruction. Use any method — do NOT treat the elementary-symmetric potential as mandated.

WHAT WE NEED BACK (priority-ordered — bank the floor first):
  (FLOOR, do this first) Can you prove the FAST O(loglog n/k) UPPER bound (HS-alt: a star/junta / compression
     online strategy)? It pairs with P2 to give a COMPLETE tight theorem Θ(max{1,loglog n/k}) — a guaranteed
     SODA result, and it does NOT need (★)'s adaptive-stability. Settle this first if you can.
  (STRETCH) Then prove or refute (★); if it holds, deliver HS-upper + HS-lower for the cascade upgrade.
     NB: the cascade LOWER (HS-lower) is the entire novelty defense — the cascade UPPER loglog n/log k resembles
     the balls-into-bins d-choice max-load loglog m/log d, so a referee may call it folklore. Make HS-lower
     load-bearing-proven, not bracketed.
  In all cases: the full argument OR a precise break-point; an updated confidence (%); a clear verdict
  (★ proven / ★ refuted+fast-fallback / ★ refuted+no-fallback ⇒ plateau / open+where).
  Empirical context (NOT a proof, do not lean on it): a heuristic-player de-risk found binding-level forbidden
  sets are small (single leader, |F|≈1) with Γ(q) increasing — consistent with (★) — but could not probe the
  OPTIMAL player or adaptive-evolution stability; treat (★)'s adaptivity clause as fully open.
```
