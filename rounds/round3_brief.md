# Brief for GPT-5.5 Pro — round 3, the matching ONLINE upper (two parallel targets)

> **Archive role:** round-3 BRIEF (`rounds/README.md`). Pairs with `round3_response.md` + `round3_audit.md`.
> Builds on round 2: your offline `√(d/k)` floor (P7) and aggregate cover lemma (P8) are **verified & banked**; the
> clean forms are refuted (N5); monotonicity refuted (N6). A scoop-scan found the offline floor is **known/folklore**
> (Bansal–Meka; Ezra–Lovett; Hoberg–Rothvoss) ⇒ the contribution must rest on the **ONLINE** side. Owner scope =
> **(a) full-d-range richer theorem + (b) the `d=O(1)` clean theorem as the bankable floor.** Attack BOTH in parallel.
> **Freeze FACTS / free METHODS.** Everything in the code fence is the paste-to-Pro payload.

```
CONTEXT (all independently audited): Online multicolor discrepancy, A-T model. Round-2 outcome:
  - P7 (offline floor, VERIFIED & BANKED): ondisc_k ≥ offdisc_k ≥ c√(d/k) whp, for k ≥ C log(dk), d/k→∞. At
    d=Θ(L²/log L), k=Θ(L) this is √(L/log L)→∞, refuting the clean forms Θ(max{1,L/k}) and Θ(max{1,L/log k}).
  - P8 (aggregate cover, VERIFIED & BANKED): Pr(level-r cover|h) ≤ (edρ)^k + O(d²/n) under the AGGREGATE condition
    (AM): (1/n)Σ_{i:R_i=r} C(|F_r(i)|,a) ≤ C(k,a)ρ_r^a ∀a. ⇒ max-cylinder control is UNNECESSARY for the cover.
  - Monotonicity of ondisc_K in K is REFUTED; literal/exact (★) is REFUTED.
  - The offline √(d/k) floor is KNOWN/folklore (Bansal–Meka 1810.03374; Ezra–Lovett; Hoberg–Rothvoss for k=2 √d; the
    multicolor √(d/k) is a routine small-ball extension). So the floor is a CITED stepping-stone, NOT our novelty.
  The CORRECTED characterization (target): ondisc_k = Θ(max{1, F_online(k), √(d/k)}), F_online = L/k (fast) or L/log k
    (cascade). Lower bound in hand: ondisc_k ≥ max{1, Ω(L/k) [P2], c√(d/k) [P7]}. The whole question is the matching
    ONLINE UPPER.

MODEL: R^n; v_1..v_T iid uniform EXACTLY-d-sparse 0/1, d∈[2,(loglog n)²/logloglog n], T=Θ(n). Online k-coloring
  χ(t)∈[k]; color load S_c(t); pairwise range R_i=max_c x_{i,c}−min_c x_{i,c}; ondisc_k = optimal-online max_{t,i} R_i.
  L:=loglog n; M:=Θ(log n/loglog n). F_r(i)=argmax_c x_{i,c} when R_i=r.

FROZEN SUBSTRATE — use freely, do NOT re-derive:
  P1 ondisc_2=Θ(loglog n), d-INDEPENDENT [A-T 2509.02432].  P2 ondisc_k ≥ Ω(L/k) ∀k (matching lower for the FAST term).
  P3 ondisc_k ≤ 1+⌊M/k⌋; k>M⇒1.  P4 forcing condition.  P6 ondisc_k ≤ q·ondisc_{kq} (block-compression).
  P7 ondisc_k ≥ c√(d/k) (offline floor, k≥C log(dk)).  P8 aggregate-cover lemma + (AM) [max-cylinder unnecessary].
BARRIERS: B1 (D,…,D,0) has |F_D|=k−1.  B2 fixed 1-D projection capped at Ω(L/k) ⇒ a L/log k LOWER needs nonlinear
  subset-entropy.  B3 K_1∈[Ω(L),O(M)].
REFUTED (do NOT attempt): N1 increasing forms; N2 k^r witness tree; N3 projection beating L/k; N4 A-T-into-binary-tree;
  N5 the clean forms as the FULL answer (omit √(d/k)); N6 assuming ondisc_K monotone in K; literal exact (★).

KEY OPEN FACT TO SETTLE FIRST (informs everything): at k=2, A-T give online Θ(loglog n) ≫ offline √d. So online is
  MUCH WORSE than offline at k=2. The corrected characterization NEEDS the online value to CATCH DOWN to the offline
  floor √(d/k) as k grows. Whether it does is unknown — maybe an online-specific term persists ABOVE √(d/k) in the
  middle regime. Determine the TRUTH, do not assume the floor is matched.

============================================================================================================
TARGET A (the (a) upgrade — the binding crux). Determine the matching ONLINE upper in the √(d/k)-DOMINATED regime
  log L ≲ k ≲ d (at max d; generally where √(d/k) ≥ F_online(k)). Specifically:
   (A1) Does the OPTIMAL online k-coloring achieve ondisc_k = O(√(d/k)) there — i.e. does online CATCH DOWN to the
        offline floor? Prove it (an online algorithm + analysis), OR show the online value is strictly larger
        (an online-specific lower bound above √(d/k)), and identify the true order.
   (A2) Confirm the OFFLINE O(√(d/k)) UPPER bound exists (partial coloring / known random-set-system results), so the
        offline value is Θ(√(d/k)) — the floor we must match online.
   Note: P6 (block-compression) + P8 (aggregate cover, (AM)) are available. The online achievability of a known
   offline floor, despite the large online-vs-offline gap at k=2, is the heart of the novelty.

TARGET B (the (b) bankable floor — guarantee this). Restrict to d=O(1) (bounded sparsity), where √(d/k)=O(1) for all
  k≥1 so the floor is dominated and ondisc_k = Θ(max{1, F_online(k)}) (the clean form). Prove the matching:
   (B1) FAST: a star/junta / compression online strategy giving ondisc_k = O(L/k) ⇒ with P2 ⇒ Θ(max{1,L/k}); OR
   (B2) CASCADE: ondisc_k = O(L/log k) via the elementary-symmetric potential, using P8 — the cover recurrence now
        needs only ADAPTIVE STABILITY of the aggregate condition (AM) (max-cylinder is NOT needed), PLUS the matching
        HS-lower Ω(L/log k) (a bounded-fiber / ancestry-entropy argument; recall B2: not from any fixed projection).
   State which fork (fast/cascade) is the truth for bounded d, with the matching upper AND lower.

WHAT WE NEED BACK (both targets, in parallel):
  For TARGET A: the true online order in the √(d/k) regime (matched to the floor, or strictly above + the true order),
    with algorithm+analysis or a lower bound; and confirmation of the offline O(√(d/k)) upper.
  For TARGET B: the proven fork for bounded d (fast or cascade), with BOTH matching bounds; if cascade, the (AM)
    adaptive-stability proof (HS-upper) + the HS-lower.
  For each: full argument OR precise break-point; updated confidence (%); a clear verdict. Use any method; do NOT treat
  any of our potentials (elementary-symmetric, block-compression) as mandated. Flag any place you need a new lemma.
```
