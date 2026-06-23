# Brief for GPT-5.5 Pro — round 5, ONLINE LOCALIZATION (the SODA-deciding crux)

> **Archive role:** round-5 BRIEF (`rounds/README.md`). Pairs with `round5_response.md` + `round5_audit.md`.
> Builds on round 4: the OFFLINE characterization is CLOSED & verified — `offdisc_k = Θ(Ψ(λ, log k))` (P11). The whole
> SODA-vs-ESA question now reduces to ONE thing: **does the ONLINE value match the offline floor `Ψ`, or pay a penalty?**
> Owner: full force on this, full regime. **Freeze FACTS / free METHODS.** Everything in the code fence is the paste-to-Pro payload.

```
CONTEXT (all independently audited). Online multicolor discrepancy, A-T stochastic model. We have just CLOSED the OFFLINE
problem and now ask the ONLINE matching question — this single question decides the venue.

MODEL: R^n; arrivals v_1..v_T iid uniform EXACTLY-d-sparse 0/1 vectors, d∈[2,(loglog n)²/logloglog n], T=Θ(n). ONLINE
  k-coloring χ(t)∈[k] IRREVOCABLE (no knowledge of future arrivals). Color load S_c(t); coordinate range
  R_i=max_c x_{i,c}−min_c x_{i,c}; ondisc_k = optimal-online value of max_{t,i} R_i (whp / in expectation).
  λ := Td/(nk) = Θ(d/k). L := log(ek) ≍ log k. Regime of interest: 2 ≤ k ≤ d, and especially k→∞, k≤d.

FROZEN SUBSTRATE — use freely, do NOT re-derive:
  P1  ondisc_2 = Θ(loglog n), d-INDEPENDENT [A-T 2509.02432]. (NB: at k=2, online Θ(loglog n) ≫ offline √d — an ONLINE
      PENALTY exists at k=2.)
  P11 (OFFLINE, CLOSED & verified) offdisc_k = Θ(Ψ(λ, log k)),  Ψ(λ,L) := 1 + √(λL) + L/log(e+L/λ).
      [√(λ log k) for λ≳log k; log k/log((log k)/λ) for 1≪λ≪log k; log k/loglog k for λ=Θ(1).]
      Construction (offline): all-subsets-NA structural lemma + density-sensitive EXACT-CARDINALITY Lovett–Meka partial
      coloring + a recursive balanced color-tree (split each node into 2 children, error attenuates O(1/q)).
  P10 (ONLINE, L2 only) greedy on Φ=Σ_{i,c} z_{i,c}² (z_{i,c}=x_{i,c}−deg_t(i)/k) gives Φ(t) ≤ td ⇒ (1/nk)Σ z² = O(d/k):
      online reaches the √(d/k) scale IN MEAN SQUARE per coordinate-color. The L2→L∞ promotion is the open cost.
  P2  ondisc_k ≥ Ω(loglog n / k).   P6  ondisc_k ≤ q·ondisc_{kq} (block-compression).   P8  aggregate cover lemma + (AM)
      [controls level-RAISING covers only; within-level broadening needs a separate lemma].
  Trivially ondisc_k ≥ offdisc_k = Ω(Ψ).
BARRIERS: B1 (D,…,D,0) has |F_D|=k−1. B2 fixed 1-D projection capped at Ω(L/k). B3 K_1∈[Ω(L),O(M)], M=Θ(log n/loglog n).
REFUTED (do NOT attempt): N1 increasing forms; N2 k^r witness tree; N3 projection beating L/k; N4 A-T-into-binary-tree;
  N5 clean forms as full answer; N6 monotonicity of ondisc_K; N7 √(d/k) as the matching scale; literal exact (★).

THE QUESTION (full regime): determine the true order of ondisc_k (online). Two possibilities:
  (MATCH) ondisc_k = Θ(Ψ(λ, log k)) — the online value CATCHES DOWN to the offline floor. This needs an ONLINE algorithm
    achieving max_{t,i} R_i = O(Ψ) whp (an L2→L∞ promotion of P10, WITHOUT the offline partial-coloring/color-tree, which
    needs the future). ⇒ ondisc_k = Θ(Ψ) and the whole characterization closes.
  (PENALTY) ondisc_k = ω(Ψ) in some regime — an ONLINE-SPECIFIC penalty above the offline floor (as at k=2, where online
    Θ(loglog n) ≫ offline √d). Then identify the true online order ondisc_k = Θ(?) with a matching online algorithm AND an
    online lower bound, across the regime 2 ≤ k ≤ d. (The penalty may be a function of loglog n and k together.)
  Resolve which holds, in EACH regime of λ (λ=Θ(1) / 1≪λ≪log k / λ≳log k) and small k (where the online loglog-n term
    may dominate). The k=2 anchor (P1) is the boundary datum: any correct answer must reduce to Θ(loglog n) at k=2.

WHAT WE NEED BACK:
  - The true order of ondisc_k(online) across the full regime: either Θ(Ψ) (match, with the online algorithm + analysis),
    or Θ(g(λ,k,loglog n)) with g ≥ Ψ (penalty, with BOTH a matching online upper and an online lower bound).
  - In particular: can the P10 mean-square (L2) bound be promoted to L∞ ONLINE at scale Ψ? If not, what is the online
    obstruction and the resulting true scale?
  - The interaction with the online loglog-n phenomenon (P1) for small k: where does the online term dominate Ψ, and what
    is the combined form? (We expect something like ondisc_k = Θ(max{ online-term(k, loglog n), Ψ(λ,log k) }) — pin it.)
  - Full argument OR precise break-point; updated confidence (%); a clear verdict (MATCH / PENALTY+true order / open+where).
  Use any method. P6/P8/P10 + the offline P11 construction are available as context, but the online algorithm cannot use
  future arrivals — flag any place you need a genuinely new online lemma.
```
