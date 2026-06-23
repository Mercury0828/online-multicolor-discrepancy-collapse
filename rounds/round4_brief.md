# Brief for GPT-5.5 Pro — round 4 (FRESH-CONTEXT attacker): the offline entropy-saturation UPPER

> **Archive role:** round-4 BRIEF (`rounds/README.md`). Pairs with `round4_response.md` + `round4_audit.md`.
> **Escalation = a FRESH-CONTEXT attacker** (escalation ladder, first-class lever) on the SINGLE most reachable upper.
> Owner decision: **keep SODA full-force; attack the offline saturation upper #1 only** (bank the complete OFFLINE
> occupancy-threshold characterization first; online localization stays the SODA-grade prize). Suggested **hard ~5-day
> clock, binary outcome**. Deliberately minimal/fresh framing (no online baggage). **Freeze FACTS / free METHODS.**
> Everything in the code fence is the paste-to-Pro payload.

```
A clean OFFLINE random-discrepancy existence question. Please solve it your way — any method (partial coloring /
Lovett–Meka / Beck–Fiala adaptation / second moment / entropy). We have a matching LOWER bound (below); we need the
matching UPPER, or a proof that none exists at that scale.

SETUP. n coordinates. T arrivals, τ-n ≤ T ≤ τ+n (constants), each an EXACTLY-d-sparse 0/1 vector in {0,1}^n, drawn
i.i.d. uniform over the C(n,d) supports. An OFFLINE k-coloring assigns each arrival a color χ(t)∈[k] (full knowledge
of all arrivals). For coordinate i and color c, x_{i,c} = #{arrivals colored c that cover i}. Coordinate pairwise
range R_i = max_c x_{i,c} − min_c x_{i,c}. offdisc_k = min over colorings χ of max_i R_i.
Parameter regime: k → ∞, k ≤ d, with d, k = (log n)^{o(1)} (so d,k grow but slowly). Occupancy λ := Td/(nk) = Θ(d/k).

WHAT IS PROVEN (a matching LOWER bound — use freely, do NOT re-derive):
  offdisc_k ≳ D_ent(λ,k) := { √(λ log k),         if λ ≫ 1
                              log k / loglog k,    if λ = Θ(1) }   (whp).
  [First-moment + Poissonization: each coordinate's k color-occupancies are ≈ independent Poisson(λ); keeping all k in
   a width-D window forces D to be the EXTREME-VALUE spread of k Poisson(λ) — the balls-into-bins maximum-occupancy
   floor. This is verified/audited.] Note this EXCEEDS the naive one-std-dev bound √(d/k)=√λ by a factor √(log k)
   (resp. log k/loglog k).

THE TARGET (the matching UPPER — the whole ask):
  Prove there EXISTS an offline k-coloring achieving  max_i R_i = O(D_ent(λ,k))  w.h.p.,
  i.e. offdisc_k = Θ(D_ent(λ,k)). Equivalently: balance the k color-occupancies at EVERY coordinate simultaneously down
  to the extreme-value scale. Concretely for λ ≫ 1: a coloring with all coordinate ranges O(√(λ log k)) = O(√((d/k)log k)).
  If the true upper is a different (larger) function, identify it and prove it — pin offdisc_k exactly.

WHAT WE KNOW FROM THE LITERATURE (context, not constraints):
  - TWO-color (k=2, ±1) random d-sparse/d-regular set-system discrepancy is Θ(√d) [Bansal–Meka arXiv:1810.03374;
    Ezra–Lovett; Hoberg–Rothvoss]. These are k=2 only.
  - Classical multicolor reductions (Doerr–Srivastav recursive/floating colors) do NOT automatically give the 1/√k
    (or the √(log k) extreme-value) behavior for this random sparse multicolor model.
  So the k-color matching upper at the occupancy-entropy threshold is, as far as we know, NOT on the shelf.

WHAT WE NEED BACK:
  - The matching offline upper bound O(D_ent) with a full construction/analysis (an explicit coloring or an existence
    proof), OR the true offline order if it differs (with proof), OR a precise obstruction if the upper genuinely cannot
    reach the lower at this scale.
  - State the method, the exact constant/log-power you achieve, and an updated confidence (%).
  - A clear verdict: offline occupancy-threshold characterization CLOSED (Θ(D_ent)) / closed at a different order /
    open + the exact obstruction.
  (Adaptivity is NOT required — this is fully offline. Use any method; nothing is mandated.)
```
