# Brief for GPT-5.5 Pro — round 7, the PROFILE-FIBONACCI lemma (PF) via LeftGap — the last gap

> **Archive role:** round-7 BRIEF (`rounds/README.md`). Pairs with `round7_response.md` + `round7_audit.md`.
> Builds on round 6: RB is reduced to ONE precise probabilistic lemma — **PF** — for your own asymmetric **LeftGap** rule.
> Round 6 PROVED that the symmetric `(R,s)` route cannot work (it gives `H/log k`, not `H/k`); the LeftGap staggered-Fibonacci
> structure is the only live path. Owner: **one PF round; if it doesn't close, we write** (RB→PF as the open problem).
> **Freeze FACTS / free METHODS.** Everything in the code fence is the paste-to-Pro payload.

```
CONTEXT (all audited). Online multicolor discrepancy, A-T model. Everything is closed EXCEPT one regime (growing k), which
is reduced to ONE lemma (PF) for your LeftGap rule. Standing facts:
  P11 (OFFLINE, CLOSED) offdisc_k = Θ(Ψ(λ,log k)), Ψ(λ,L)=1+√(λL)+L/log(e+L/λ), λ=Td/(nk)=Θ(d/k), L=log(ek).
  P12 (ONLINE, ALL k) ondisc_k = O(loglog n) ⇒ fixed-k closed Θ(loglog n).  P2: ondisc_k ≥ Ω(loglog n/k).
  Bracket: max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n.  P13 (BC) E Σ_i (B_{i,r})_a ≤ nη(2τ_+ d²η)^a (broadening-cost, uniform
    over adaptive epochs). 
  B4 (PROVEN OBSTRUCTION — do NOT retry): the SYMMETRIC (R,s)/H_{r,a} moment route gives only a k-fold range recurrence
    η_{r+1} ≲ (Aη_r)^k ⇒ exp(−k^j) ⇒ union-over-n needs j ≳ loglog n/log k = H/log k, NOT the H/k RB needs. A deterministic
    skip obstruction (narrow-rainbow) kills all permutation-invariant (R,s) methods. ⇒ an ASYMMETRIC full-profile rule is
    REQUIRED. (Not a lower bound — an asymmetric rule can stagger phases.)

MODEL: R^n; v_1..v_T iid uniform EXACTLY-d-sparse 0/1, d∈[2,(loglog n)²/logloglog n], T=Θ(n). ONLINE k-coloring χ(t)∈[k]
  irrevocable; x_{i,c}(t) loads; R_i=max−min; H:=loglog n; L:=log(ek). Goal R ≤ 1+ρ/(k−1), ρ=(k−1)(R−1)+s.

THE RULE (LeftGap, LG): g_{i,c}=x_{i,c}−min_b x_{i,b}; for support S_t, h_c=max_{i∈S_t} g_{i,c}; choose the color minimizing
  lexicographically (h_c, c). Represent g_{i,c}≥ℓ by a live token (i,c,ℓ) with PHASE Q(i,c,ℓ)=k(ℓ−1)+c (pushed when a gap
  increases, popped when the row minimum rises).
  DETERMINISTIC NO-SKIP CERTIFICATE (proven): a principal token born of height h+1, color c (phase Q=kh+c) has prior witnesses
  at phases Q−1,…,Q−k (same cell at Q−k; each j<c gives Q−(c−j) via h_j≥h+1; each j>c gives Q−(k+c−j) via h_j≥h). So a phase-Q
  token has k prior witnesses at Q−1,…,Q−k ⇒ a leaf count obeying the STAGGERED FIBONACCI F_k(m)=Σ_{j=1}^k F_k(m−j)=Θ(φ_k^m),
  φ_k↑2 (the Always-Go-Left mechanism that yields loglog n/k, not loglog n/log k).

THE TARGET (PF — the Profile–Fibonacci lemma). Let B=CΨ(λ,L); Z_q = number of principal LeftGap-token births of phase ≥ q.
  Prove: there are absolute c,C>0 such that, uniformly for 0 ≤ m ≤ CH,
     E Z_{kB+m} ≤ C·n·d·exp[ −c·F_k(m) ].                                                                   (PF)
  PF ⇒ RB ⇒ growing-k closed: F_k(m) ≥ c0 φ_k^m, so m=C1·H ⇒ F_k(m) ≥ (log n)^{C2} ⇒ no phase above kB+C1H whp ⇒ max_{t,i} R_i
    = O(Ψ + H/k) ⇒ ondisc_k = Θ(max{Ψ(λ,L), loglog n/k}).
  WHERE PF BREAKS (the precise obstruction): a witness-tree count wants a PRODUCT estimate
     Pr( S_t ∩ A_j ≠ ∅  ∀ j∈J ) ≲ Π_{j∈J} d|A_j|/n,                                                          (overlap-false)
  which is FALSE when the A_j OVERLAP (A_1=…=A_a=A ⇒ LHS≈d|A|/n, RHS its a-th power). A single BROAD row carries many
  predecessor-color tokens, so the witness tree folds into a PROFILE DAG; sibling coalescence at one row need not create an
  ordinary graph cycle that multicycle counting would penalize. BC charges this overlap only as η_r^a (⇒ the dead k-fold range
  recurrence), NOT the staggered Fibonacci. PF needs a NEW MIXED-PROFILE TRANSPORT estimate controlling
     (1/n) Σ_i Π_{j∈J} 1{ g_{i,c_j} ≥ ℓ_j }                                                                  (mixed-moment)
  for DIFFERENT colors c_j and STAGGERED heights ℓ_j, uniformly over adaptive stopping times — either (i) dynamically FACTOR
  these mixed moments, or (ii) CHARGE every overlap to enough earlier token births that the folded DAG retains Ω(F_k(m))
  entropy-bearing leaves. P8 and P10 do neither.

BARRIERS / REFUTED (respect): B1 a broad row (D,…,D,0) blocks k−1 colors at once (the power-of-k independence analogy fails).
  B2 a fixed 1-D projection capped at Ω(L/k). B4 the symmetric (R,s) route is DEAD (above) — do NOT re-derive it. N2 naive
  k-ary witness tree collapses. L2/mean-square is dead at this scale.

WHAT WE NEED BACK:
  - A PROOF of PF (the mixed-profile transport estimate for the LeftGap token process) — via (i) dynamic factorization of the
    staggered mixed moments, or (ii) a DAG-folding charge that preserves Ω(F_k(m)) leaves — ⇒ RB ⇒ growing-k closed
    Θ(max{Ψ, loglog n/k}); OR
  - a PRECISE OBSTRUCTION to PF (overlap genuinely costs more), i.e. an ONLINE LOWER bound showing ondisc_k = ω(max{Ψ,
    loglog n/k}) in some growing-k regime (e.g. ≳ H/log k against EVERY online rule — a Yao-type argument, must hold vs all
    online algorithms and reduce to Θ(loglog n) at k=2); OR
  - the exact point where PF resists and what new probabilistic tool is missing.
  Full argument OR precise break-point; updated confidence (%); clear verdict (PF PROVEN ⇒ growing-k closed / PF FALSE + true
  online order / open + exact obstruction). Use any method. The no-skip certificate (8) + BC + P8/P11/P12 are available; the
  symmetric route is dead; flag any genuinely new lemma needed.
```
