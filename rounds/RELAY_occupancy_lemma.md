# Relay to GPT-5.5-Pro — close the one cited-as-standard lemma (offline lower bound)

**Context for you (GPT-5.5-Pro).** We have a complete SODA submission proving, in the Altschuler–Tikhomirov
sparse-i.i.d. online Beck–Fiala model, three results on multicolor (k-color) prefix/final discrepancy. Everything is
self-contained and machine-verified **except one lemma**, which we currently invoke by citing the balls-into-bins
maximum-load literature. We want either (i) a clean, fully self-contained proof of the lemma below with an explicit
large-deviation rate, or (ii) a precise statement of which cited theorem (ABKU 1999 / BCSV 2006 / Raab–Steger 1998 /
Talwar–Wieder 2007) gives it as a black box, and the exact wording to cite. This lemma is the **offline lower bound**;
it is the only place the paper is not self-contained.

## Setup / notation
- `n` large; `T = Θ(n)` (constants `τ₋ ≤ T/n ≤ τ₊`); sparsity `2 ≤ d ≤ (loglog n)² / logloglog n`.
- A fixed coordinate `i ∈ [n]`. An offline `k`-coloring assigns each of the `T` arrivals a color in `[k]`; color `c`
  receives `m_c` arrivals, `Σ_c m_c = T`. In the Poissonized (independent-rows Bernoulli) model with `p = d/n`, the
  load of color `c` at coordinate `i` is `Y_c ~ Binomial(m_c, p)`, independent across `c`, with mean
  `μ_c = m_c p` and `Σ_c μ_c = T p = k λ`, where `λ := Td/(nk) = Θ(d/k)` is the per-color occupancy.
- Range at the coordinate: `R_i = max_c Y_c − min_c Y_c`.
- Threshold function: `Ψ(λ, L) := 1 + √(λL) + L / log(e + L/λ)`, with `L = log k`. Write `t* := Ψ(λ, log k)`. Its three
  regimes: `√(λ log k)` for `λ ≳ log k`; `log k / log((log k)/λ)` for `1 ≪ λ ≪ log k`; `log k / loglog k` for `λ = Θ(1)`.
- Poisson/Bennett tail (we use freely): for `X ~ Poisson(μ)`, `−log P(X ≥ μ+s) ≍ s²/μ` for `s ≲ μ` and `≍ s log(1+s/μ)`
  for `s ≳ μ`; inverting "rate = log k" gives deviation `Θ(Ψ(μ, log k))`.

## The lemma we need (verbatim target)
> **Lemma (occupancy spread, lower tail).** There is an absolute constant `δ > 0` such that, for every mean profile
> `(μ_c)_{c∈[k]}` with `μ_c ≥ 0` and `Σ_c μ_c = kλ` (with `λ = Θ(d/k)` in the stated range), the independent loads
> `Y_c ~ Binomial(m_c, p)` satisfy
> `P( max_c Y_c − min_c Y_c ≤ (1/4) Ψ(λ, log k) ) ≤ e^{−q}` with `q ≥ k^{δ}` (e.g. `δ = 1/5`).

Why we need exactly this: we then use independence of the `n` coordinates (independent rows of the Bernoulli matrix) to
get `P(max_{i≤n} R_i ≤ (1/4) t*) ≤ e^{−qn}`, and a union bound over the at most `k^T = e^{Θ(n log k)}` colorings (times the
`(C√d)^T` Poissonization cost `= e^{O(n log d)}`). The union is beaten iff `q n ≫ n log(dk)`, i.e. `q ≫ log(dk)`; with
`q ≥ k^{δ}` this holds under the hypothesis `k ≥ C₀ log^{1/δ}(dk)` (we currently state `k ≥ C₀ log⁵(dk)`, i.e. δ=1/5).
So **any `δ > 0` that is uniform over all mean profiles suffices** — we do not need the optimal rate, only `k^{Ω(1)}`.

## What we have (our current argument, which a reviewer flagged as "correct only modulo the cited comparable-mean law")
We split on the mean profile:
- **Heavy bin.** If `max_c μ_c ≥ k^{1/4} λ`, that bin's load is `≥ μ/2 ≥ (1/2)k^{1/4}λ` by Chernoff (failure
  `e^{−Ω(k^{1/4}λ)}`); the average constraint forces `Ω(k^{1/4})` bins of mean `≤ λ`, whose minimum is `≤ 2λ` w.h.p.
  (each `≤ 2λ` w.p. `≥ 1/2` by Markov, independence over `Ω(k^{1/4})` bins → failure `2^{−Ω(k^{1/4})}`). Since
  `k^{1/4}λ ≥ 8(λ + t*)`, `R_i ≥ (1/4) k^{1/4} λ ≥ t*`. Rate `q = Ω(k^{1/4})`.
- **No heavy bin** (all `μ_c < k^{1/4}λ`). Discard bins with `μ_c < λ/2`; the rest `H` carry `Σ μ_c > kλ/2`, so
  `|H| ≥ (kλ/2)/(k^{1/4}λ) = k^{3/4}/2`. Partition `[λ/2, k^{1/4}λ)` into `O(log k)` dyadic bands `[M, 2M]`; the densest
  band `B` has `k'' := |B| ≥ k^{3/4−o(1)}` bins of comparable mean `M ∈ [λ/2, k^{1/4}λ)`. We then **invoke the
  comparable-mean extreme-value law**: for `m` independent loads of comparable mean `Θ(M)`, `max − min ≥ Θ(Ψ(M, log m))`
  off probability `e^{−Θ(√m)}`. Since `Ψ` is nondecreasing in the first argument and `M ≥ λ/2`,
  `Ψ(M, log k'') ≥ Ψ(λ/2, Θ(log k)) ≥ (1/4) t*`. Hence failure `e^{−Θ(√{k''})} = e^{−k^{3/8−o(1)}}`, so `q ≥ k^{1/5}`.

## The two precise things we want from you
1. **The comparable-mean extreme-value law, stated and proved (or cleanly cited).** Concretely: let `Z_1,…,Z_m` be
   independent with `Z_j ~ Binomial(n_j, p)`, means `μ_j ∈ [M, 2M]`, `M ≥ 1/2`. Show
   `P( max_j Z_j − min_j Z_j ≤ c·Ψ(M, log m) ) ≤ e^{−Ω(√m)}` for an absolute `c > 0`, uniformly across the regimes
   `M = Θ(1)` (occupancy/Poisson max-load), `1 ≪ M ≪ log m` (Bennett), and `M ≳ log m` (Gaussian). We believe this is
   exactly ABKU/RaabSteger (M=Θ(1)) generalized to weighted/Bennett means (Talwar–Wieder, BCSV), but we want either a
   short self-contained proof or the exact theorem+statement to cite. The subtle point a reviewer raised: in a dyadic
   band the means may all be equal (no mean-spread) — so the spread must come from the **two-sided random fluctuation**
   `Ψ(M, log m)` itself, which is fine for `M = Θ(1)` (min hits 0, max hits `log m / loglog m`) and for large `M`
   (Gaussian `±√(M log m)`), but please confirm the intermediate Bennett band and that the **minimum** side also
   deviates by `Ω(Ψ)` (note: when `Ψ(M, log m) > M`, the min is simply `0` w.h.p., it cannot go negative — handle this).
2. **Confirm or correct the global reduction**: that the heavy/no-heavy split above yields a uniform `q ≥ k^{Ω(1)}` over
   ALL mean profiles with `Σμ_c = kλ`, and that no profile (e.g. a few medium bins `μ ≈ √k λ` with the rest tiny, or
   all-equal `μ_c = λ` with `λ ≫ log k`) escapes both cases. If our `k^{1/4}λ` threshold or band count is off, give the
   corrected threshold and the resulting `δ` (hence the resulting hypothesis `k ≥ C₀ log^{1/δ}(dk)`).

## Deliverable
A short note containing: (1) the comparable-mean spread lower-tail lemma with proof or exact citation; (2) the verified
global reduction giving `q ≥ k^{δ}` with the explicit `δ` and the matching hypothesis on `k`; (3) any correction to our
constants. Terse is fine; we will typeset it into Appendix B (replacing the current `lem:occ-spread` sketch).
