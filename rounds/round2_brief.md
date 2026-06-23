# Brief for GPT-5.5 Pro — round 2, FAST floor + CASCADE stretch (post-audit)

> **Archive role:** round-2 BRIEF (`rounds/README.md`). Pairs with `round2_response.md` + `round2_audit.md`.
> Builds on round 1 (`round1_response.md`): your block-compression lemma is **verified and banked as P6**; literal
> `(★)` is **accepted as refuted**; we adopt your pathwise `(★')` reframing. Independent audit **caught one over-claim
> in your FAST reduction** (existential vs uniform) — folded in below. **Freeze FACTS / free METHODS.**
> **Everything inside the code fence is the message to paste to GPT-5.5-Pro.**

```
CONTEXT: This continues our online multicolor discrepancy thread. Round 1 outcome (all independently audited):
  - VERIFIED & BANKED — P6 (block-compression): ondisc_k ≤ q·ondisc_{kq} for all integers k,q≥1 (equal k-block
    merge of kq virtual colors; pointwise in t; online-valid). Use freely.
  - ACCEPTED — literal/exact (★) is REFUTED (natural ρ_r=max_c Q_r({c})): a color-symmetric feasible law AND a
    symmetrized optimal disc-1 process both violate product domination (the latter by (t−1)/t·k/(k−1)>1 for t>k).
    So range+symmetry+near-optimality do NOT imply product domination; a profile-shape invariant is needed.
  - CAUGHT (audit correction to your FAST reduction): "K_1=O(loglog n)" (disc-1 at SOME K*=Θ(L)) does NOT by
    itself give ondisc_k=O(max{1,L/k}). It needs EITHER monotonicity of ondisc_K in K (UNPROVEN; P6 does not give
    it), OR a UNIFORM-band hypothesis. And there is a residual regime L≲k≲M not covered by either the band or the
    fresh-color bound (which only gives O(M/k)≫O(1) there, since M=Θ(log n/loglog n) ≫ L=loglog n).

MODEL (unchanged): R^n; arrivals v_1..v_T i.i.d. uniform over EXACTLY-d-ones 0/1 vectors, d∈[2,(loglog n)²/logloglog n],
  T=Θ(n). Online k-coloring χ(t)∈[k]; color load S_c(t)=Σ_{s≤t,χ(s)=c} v_s. Pairwise range R_i=max_c x_{i,c}−min_c x_{i,c};
  ondisc_k = optimal-online value of max_{t,i} R_i. M=Θ(log n/loglog n). L:=loglog n. F_r(i)=argmax_c x_{i,c} when R_i=r.

FROZEN SUBSTRATE — use freely, do NOT re-derive:
  P1: ondisc_2 = Θ(loglog n), d-independent [A-T 2509.02432 v3, Def 1.4 / Thm 1.1].
  P2: ondisc_k ≥ Ω(loglog n/k) for ALL k (even & odd). [This IS the matching lower for the FAST form.]
  P3: ondisc_k ≤ 1+⌊M/k⌋; k>M ⇒ ondisc_k=1; M=Θ(log n/loglog n).
  P4: forcing condition — support E forces D+1 ⟺ ∪_{i∈E} F_D(i)=[k].
  P6: ondisc_k ≤ q·ondisc_{kq} (block-compression). [NEW, verified round 1.]

BARRIERS (respect): B1 (D,…,D,0) has |F_D|=k−1 ⇒ no k independent sub-certificates. B2 any single fixed 1-D
  projection capped at Ω(loglog n/k) ⇒ a loglog n/log k LOWER needs nonlinear subset-entropy, NOT a projection.
  B3 K_1=Θ(M) NOT proven (only Ω(loglog n) ≤ K_1 ≤ O(log n/loglog n)).
REFUTED (do NOT attempt): N1 increasing forms; N2 k^r witness tree; N3 a fancier projection to beat loglog n/k;
  N4 black-box A-T-into-binary-tree (gives only generic log-k, NOT 1/k). literal exact (★) (refuted, round 1).

============================================================================================================
TARGET 1 — THE FAST FLOOR (priority; banks a complete tight SODA theorem with P2). Method-agnostic.
  Prove (CP-uniform):  ondisc_K = O(1) for EVERY integer K in a band [c1·loglog n, c2·loglog n] with c2 ≥ 2c1.
  Via P6 this yields ondisc_k = O(max{1, L/k}) for k ≤ c1·L; with P2 lower ⇒ ondisc_k = Θ(max{1, L/k}) there — a
  full tight FAST theorem on that range. Concretely the critical case is D=1: a disc-1 online k-coloring needs, on
  each arriving support E, a color c ∉ ∪_{i∈E} U_i, where U_i = {colors one above the coordinate min} (|U_i| =
  deg_t(i) mod k), with U_i resetting at [k]. I.e. an ONLINE ROTATING-PALETTE problem: keep ∩_{i∈E}([k]\U_i) ≠ ∅
  for all t, with k = Θ(loglog n). The open piece you identified is a DYNAMIC palette-persistence/junta lemma
  (snapshot "available sets ≈ a star" does not survive: choosing the star center consumes it from every
  non-saturated palette in the support; no current invariant bounds the center consume/renew/rotate rate).
  Also please settle the two pieces the audit isolated:
   (1a) THE MONOTONICITY SUB-QUESTION: is ondisc_K monotone non-increasing in K? (Prove it, or give a
        counterexample.) If YES, the existential K_1=O(loglog n) suffices and TARGET 1 simplifies enormously.
   (1b) THE RESIDUAL REGIME L ≲ k ≲ M: give ondisc_k = O(1) there (target is O(1) since L/k<1), OR show it needs
        the band extended toward M, OR a direct argument. Fresh-color only gives O(M/k)≫O(1).

TARGET 2 — THE CASCADE STRETCH (higher value; needs both a stronger upper AND a stronger lower).
  (2a) UPPER: prove the pathwise (★'):  q^h_{r,t}(A) := (1/n)|{i: R_i(t)=r, A⊆F_r(i,t)}| ≤ ρ_{r,t}(h)^{|A|}, a
       history-conditional empirical inequality uniform over stopping times, with ρ_{r,t}(h) measurable before the
       next arrival. Under (★') the cover recurrence Pr(∪_j F_r(I_j)=[k]|h) ≤ (dρ)^k+O(d²/n) is already correct.
       The crux is MAX-CYLINDER control: the elementary-symmetric potential bounds Σ_{|A|=a} q(A) but the cover
       needs max_{|A|=a} q(A); an adaptive junta can concentrate the mass on one A, costing C(k,a)≈2^k. Find the
       extra profile-shape invariant (or a different potential) that controls the max pathwise — or show it fails.
  (2b) LOWER (Ω(loglog n/log k), Profile-Branching): the obstruction is witness-sharing — (r,…,r,0) yields 2^{k−1}
       subset-certificates from ONE coordinate history, so subset-counting over-counts. Supply a canonical pruning
       map with a BOUNDED-FIBER theorem (each branching level contributes Ω(log k) NEW independent arrival
       information after shared history is quotiented out), or show no such bound exists. Recall B2: this LOWER
       cannot come from any fixed projection.

WHAT WE NEED BACK (priority-ordered):
  FIRST, TARGET 1 — the FAST floor: the dynamic palette-persistence lemma proving (CP-uniform), plus answers to
   (1a) monotonicity and (1b) the L≲k≲M regime. This alone (with P2) is a complete tight SODA theorem on its range.
  THEN, TARGET 2 — the cascade: (2a) pathwise max-cylinder (★') and (2b) the bounded-fiber witness-entropy lower.
  For each: the full argument OR a precise break-point; updated confidence (%); a clear verdict per target
  (proved / refuted+why / open+exact obstruction). Use any method. Do NOT treat any of our potentials as mandated.
```
