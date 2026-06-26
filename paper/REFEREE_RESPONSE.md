# Referee response (Weak Reject, leaning Reject) — triage + status

Referee verdict: strong offline architecture, but multiple correctness/completeness gaps. Largely **right**.
Triage below; "FIXED" = done in this pass, "RELAY" = sent to GPT-5.5-Pro (`rounds/RELAY_referee_round2.md`),
"TODO" = next pass.

## Outright errors — FIXED this pass
- **2.1 separation `offdisc_k ≤ offdisc_2` via empty colors — FALSE** (an empty color sits at load 0 and inflates
  max−min). Replaced with the correct route: `lem:offline-upper` (the color-tree construction) holds for every `k≤d`
  with no lower-bound hypothesis and gives `O(Ψ(λ,Θ(1)))=O(√d)` for fixed `k`. (sec5)
- **2.5 "range was 0 and stays 0" in min-load repair — FALSE** ((3,3,3)→(4,3,3) is range 1). Repair acts only on
  exceptional coordinates (range `≥64H>0`), where `M−m≥1` so `m+1≤M`. Statement requalified everywhere
  ("never raises the range *of a positive-range/exceptional* coordinate"). (appC, sec4, overview)
- **2.6a `t*≥4√(λ log k)` — wrong constant** (def gives only `≥√(λ log k)`). Fixed. (appB)
- **2.6b splitting stage-sum "Ψ monotone, sup at start" — FALSE** (sparse Bennett term rises as μ↓,ℓ↑). Replaced with
  the correct bound: the sparse ratio `(ℓ₀+u)/(u+c)` is monotone in `u`, sup `= max{ℓ₀/c,1}=O(Ψ(μ₀,ℓ₀))` since `Ψ≥1`. (appB)

## Honesty / scoping — FIXED this pass
- **2.2 seed-tail "worst case k=2"** now shows the `k²`-absorption: exponent `Θ(H²k/d)` grows linearly in `k` while the
  prefactor is `k²`, so `k²exp(−Θ(H²k/d))` is decreasing on `[2,d]`; max at `k=2`. Scoped lem:online-upper + remark to
  `2≤k≤d`; softened "more colors do not help" → "do not change the order for fixed k / within the range". (appC, sec4)
- **2.8 optimal-value definition** made a threshold sequence with explicit quantifiers (lower bound = every algorithm whp;
  upper = some algorithm whp). (sec2)
- **Overclaims softened** (2.3/2.7): abstract/intro/overview "symmetric approach provably cannot reach it" →
  "a natural symmetric, permutation-invariant potential loses a `log k` factor"; "determine the multicolor value in two of
  three regimes" → "offline for growing k, online for every fixed k"; "identify exactly" → "pin down up to constants".

## Genuinely hard math — RELAY to GPT-5.5-Pro (`rounds/RELAY_referee_round2.md`)
- **2.3 odd-k online lower bound**: the asymmetric `{+1,−ρ}` (`ρ∈[1/2,1]`) two-action analogue of the AT two-color lower
  bound is currently asserted. Need the lemma + AT spread-induction re-run (or a constant-cost coupling to `±1`).
- **2.4 formal transfer lemma**: replace "AT category/level-set applies verbatim" with a self-contained abstract lemma
  (hypotheses (i)–(ii) + future-support independence + seed tail ⟹ `O(loglog n)`), AT's argument re-run in the range-`R_i`
  language (modified-incidence charging, exceptional-set sparsity, double-exp decay).

## TODO — next pass (my job, no new math)
- **2.6c** structural sparse Bennett inversion: fix a single cutoff, prove the uniform `μ h((KΨ−μ)/μ) ≥ Bℓ` (currently two
  narrative cases). **2.6d** expand the reverse-Cramér / comparable-mean calculus inequalities (B.5),(B.6) from
  GPT-5.5-Pro's earlier note (`RELAY_occupancy_lemma.md`) into appB instead of "one-variable calculus gives".
- **2.7 demote §6/appD**: rename to "Discussion and open problems", make the phase conveyor a clearly-labelled heuristic
  counterexample (not a numbered Proposition) OR define rank-greedy / forbidden-set / cover-certificate / principal-token
  precisely; state the symmetric obstruction's excluded potential class formally.
- **Writing**: cut ~25% repetition (the "offline help / online don't" refrain appears 5–6×); invert length allocation
  (defer standard Bennett/NA to appendix, expand the hard steps); trim related-work classical-textbook background.

## Status
40pp, compiles clean (0 undefined), 0 style violations. The outright errors are fixed; the two load-bearing missing proofs
(odd-k lower bound, formal transfer lemma) are with GPT-5.5-Pro. After those return and the TODO writeup pass, this addresses
the referee's blocking items.

---

# Round-2 referee (Weak Reject near Borderline, 4.5–5/10) — triage

Referee confirmed the round-1 fixes and found that some were still imperfect, plus one important new gap. All fixed this
pass except the two relayed proofs.

## Fixed this pass
- **Thm 2 vs Lemma 7 parameter-range gap (theorem-level)**: lem:online-upper restated for "every `k≤d` and every fixed `k`"
  (covers fixed `k=5,d=2`). (sec4)
- **Seed-tail "worst case k=2" still wrong** (exponent saturates at `Θ(H)` when `V≲H`, not `Θ(H²k/d)`): rewritten as a
  correct two-regime argument (`d/k≥H`: decreasing in `k`, max at `k=2`; `d/k<H`: saturated `Θ(H)`, `k²e^{-Θ(H)}≤d^{-28}`).
  Covers `k≤d` and all fixed `k`. (appC)
- **Transfer-lemma interface (i),(ii) INSUFFICIENT** (pure-seed coloring satisfies them but fails the conclusion): added the
  third condition (iii) "an exceptional coordinate's range rises only with a co-present helper of ≥ range", and verified our
  min-load algorithm satisfies it. Updated overview/intro/sec4 sketches. (appC, sec4, sec1)
- **Splitting sparse-stage seam `μ₀≈ℓ₀` (c=0 division)**: fixed with `log(e+ℓ/μ)≥½(1+u+c)`, sup `=max{ℓ₀/(1+c),1}`, no
  blow-up at the seam. (appB)
- **Corollary 2 monotonicity unprovable**: replaced with the endpoint statement (`offdisc_k=O(√d)`, `=Θ(log d/loglog d)` at
  `k=Θ(d)`); no monotonicity-requiring calculus. (sec7)
- **Internal inconsistencies**: the "Thm 1 excludes k=2 because two-color is √d not Ψ" sentence is FALSE (Ψ at k=2 IS Θ(√d));
  reworded to "the hypothesis is what the first-moment lower bound needs, not where the formula fails". Removed the leftover
  Thm 3 "offline value quoted from classical bounds" paragraph (now correctly attributes to lem:offline-upper). Replaced the
  load-bearing "verbatim" uses with the interface language. Softened "reduce the exact order to one lemma" → "identify a
  sufficient high-probability lemma". (sec3, sec5, sec1, sec4, abstract)
- **odd-k**: now a stated `lem:asym-online` with the explicit per-stage increment `≥ρ≥1/2` (referee's argument); full
  AT-induction re-run still RELAYED.

## Still RELAYED to GPT-5.5-Pro (the two things the referee says would flip to Weak Accept)
- GAP 1: full induction for `lem:asym-online` (AT spread recurrence for the `{+1,−ρ}` process).
- GAP 2: formal transfer lemma under (i)–(iii), AT category/level-set re-run in the range language.

## Still TODO (writeup, my job)
- 2.6c structural sparse Bennett uniform inversion (single cutoff, uniform constant).
- §7/appD demotion to "Discussion and open problems"; define rank-greedy/forbidden-set/cover-certificate/principal-token or
  mark the conveyor a heuristic; formalize the excluded symmetric potential class.
- Writing: cut ~25% repetition; invert length allocation; trim classical related-work.

41pp, compiles clean (0 undefined), 0 style violations. Referee's verdict: fix GAP 1 + GAP 2 + the param-range/tail/calculus
(latter three now done) ⟹ Weak Accept.
