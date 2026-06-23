# Brief for GPT-5.5 Pro — round 6, the RANKED-BROADENING LEMMA (RB) — close growing-k

> **Archive role:** round-6 BRIEF (`rounds/README.md`). Pairs with `round6_response.md` + `round6_audit.md`.
> Builds on round 5: the bracket `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n` is verified, and the entire growing-k gap is
> reduced to ONE precisely-stated lemma — **RB** (your own reduction, audit-confirmed as the exact sufficient piece). Owner:
> attack RB to close growing-k. Suggested hard ~5-day clock; **if it does not close, we write the two complete results with RB
> as a stated conjecture.** **Freeze FACTS / free METHODS.** Everything in the code fence is the paste-to-Pro payload.

```
CONTEXT (all audited). Online multicolor discrepancy, A-T model. The bracket is closed except for ONE lemma. We have:
  P11 (OFFLINE, CLOSED) offdisc_k = Θ(Ψ(λ,log k)), Ψ(λ,L)=1+√(λL)+L/log(e+L/λ), λ=Td/(nk)=Θ(d/k), L=log(ek).
  P12 (ONLINE upper, ALL k) ondisc_k = O(loglog n) ⇒ fixed-k: ondisc_k=Θ(loglog n).
  Bracket (verified): max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n.  P2: ondisc_k ≥ Ω(loglog n/k).
  L2→L∞ NO-GO (verified): the mean-square greedy (P10) gives #{R_i≥D} ≤ O(nd/D²) ≥ n at D≍Ψ — useless at the entropy scale.
  Your RB reduction is audit-confirmed as the EXACT sufficient missing piece.

MODEL: R^n; v_1..v_T iid uniform EXACTLY-d-sparse 0/1, d∈[2,(loglog n)²/logloglog n], T=Θ(n). ONLINE k-coloring χ(t)∈[k]
  irrevocable; row-i color loads x_{i,c}(t); R_i=max_c x_{i,c}−min_c x_{i,c}; s_i=|argmax_c x_{i,c}|. H:=loglog n. L:=log(ek).
  RANK: ρ(x)=0 if R(x)=0; ρ(x)=(k−1)(R(x)−1)+s(x) if R(x)≥1.  ⇒ R(x) ≤ 1 + ρ(x)/(k−1).
  Transitions: update a MAX color ⇒ range+1, s→1, Δρ=k−s (a "visible raise"); update a (MAX−1) color ⇒ s→s+1, range fixed,
    Δρ=+1 (an "invisible BROADENING", e.g. (D,D−1,…,D−1,0)→(D,…,D,0)); other updates leave ρ unchanged/decrease.
  COVER CERTIFICATE (9): for the rank-greedy rule (choose color a minimizing the ↓-sorted vector sort_↓(ρ_i^a : i∈S_t)),
    if the chosen color makes some row reach rank q, then ∪_{i∈S_t} F_{i,q} = [k], where F_{i,q}={a: ρ_i^a ≥ q}. (Lex-minimality:
    if some alternative color kept every supported row's post-rank below q, it would have a strictly better sorted vector.)

THE TARGET (RB): prove there is an ONLINE color rule such that
   max_{t≤T, i≤n} ρ_i(t) ≤ C·(k·Ψ(λ,L) + H)   whp.                                                         (RB)
By R ≤ 1+ρ/(k−1), RB ⇒ max_{t,i} R_i = O(Ψ + H/k) ⇒ (with P2, P11) ondisc_k = Θ(max{Ψ(λ,L), loglog n/k}) — closing growing-k.
Equivalently, a one-row double-exponential tail suffices: Pr[ R_i* > CΨ + r ] ≤ exp(−exp(c·k·r))  (11); union over n rows ⇒
  r = O(H/k).
  THE CRUX: P8 (the aggregate cover lemma) controls only VISIBLE RAISES (range r→r+1). RB additionally needs control of the
  INVISIBLE BROADENING transitions (Δρ=+1) — the within-level growth of the forbidden/max set from size 1 toward k−1 that
  prepares a later raise and that a level-raising-cover lemma never charges. Needed (your §4 schematic): a BROADENING-COST /
  drift control, e.g. E[ΔH_{r,a} | F_t] ≤ −γ H_{r,a} + C(k,a)η_r^a (epochwise, uniform over stopping times), where
  H_{r,a}=(1/n)Σ_{i:R_i=r} C(|F_r(i)|,a), feeding the per-level cover bound (edρ_r)^k as a source term — OR a genuinely
  different argument.

BARRIERS / REFUTED (respect): B1 a broad row (D,…,D,0) has |F_D|=k−1 and BLOCKS k−1 colors at once ⇒ the power-of-k
  balanced-allocation analogy FAILS (choices are NOT independent); N2 the naive k-ary witness tree collapses. B2 a fixed 1-D
  projection is capped at Ω(L/k). The L2/mean-square route is dead at this scale (the no-go above).

WHAT WE NEED BACK:
  - A proof of RB (or the one-row tail (11)) via an online rule + the broadening-cost control — OR a precise obstruction /
    an ONLINE LOWER bound showing ondisc_k = ω(max{Ψ, loglog n/k}) in some growing-k regime (i.e. RB is false, there is a
    further online penalty — then identify the true order).
  - If RB needs a new lemma, state it precisely and prove it, or pinpoint exactly where it breaks.
  - Full argument OR precise break-point; updated confidence (%); a clear verdict (RB PROVEN ⇒ growing-k closed at
    Θ(max{Ψ, loglog n/k}) / RB FALSE + true order / open + exact obstruction).
  Use any method. The cover certificate (9) + P8 + P11/P12 are available; the L2 route is dead. Flag any new online lemma needed.
```
