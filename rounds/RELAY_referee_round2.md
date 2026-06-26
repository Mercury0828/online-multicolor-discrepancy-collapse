# Relay to GPT-5.5-Pro — two proof gaps flagged by a (Weak-Reject) referee

**Context.** A referee read our SODA submission on multicolor discrepancy of sparse random 0/1 vectors (the
Altschuler–Tikhomirov i.i.d. online Beck–Fiala model, extended from 2 colors to `k`). The referee judged the offline
upper-bound architecture strong, but flagged several issues. We have already fixed the outright errors ourselves (a false
"ignore `k-2` colors" monotonicity in the separation; a "range 0 stays 0" slip in the min-load repair; a spurious `t*≥4√`;
the seed-tail `k²`-absorption; a false `Ψ` monotonicity in the splitting stage-sum). **Two gaps need real proof work and we
are relaying them to you.** Please return self-contained statements + proofs we can typeset; terse is fine.

---

## GAP 1 — Online lower bound for odd `k`: the asymmetric two-action `{+1,−ρ}` bound

**What we have.** For an online `k`-coloring on the random sparse i.i.d. stream, we project the `k` colors onto two via a
zero-sum signing `ξ:[k]→ℝ`, `Σ_c ξ(c)=0`. For **even** `k` this is the clean `±1` split (`k/2` colors `+1`, `k/2` colors
`−1`): the signed sum `Σ_c ξ(c) x_{i,c}` is a valid online `±1`-balancing of the same arrivals, and `|Σ_c ξ(c) x_{i,c}| ≤
(k/2) R_i` where `R_i = max_c x_{i,c} − min_c x_{i,c}`. The two-color online lower bound `Ω(loglog n)` of
Altschuler–Tikhomirov [AT, arXiv:2509.02432] then forces `R_i = Ω(loglog n / k)`, hence `Ω(loglog n)` for fixed `k`.

For **odd** `k = 2a+1`, no exact `±1` split exists. We use `ξ ≡ +1` on a part of size `a+1` and `ξ ≡ −(a+1)/a` on a part of
size `a` (zero-sum). After rescaling, the induced online process takes **steps in `{+1, −ρ}` with `ρ = a/(a+1) ∈ [1/2, 1]`**.

**The gap (referee).** We currently *assert* that the AT two-color lower-bound recurrence "loses only a constant factor for
`ρ ∈ [1/2,1]`." But AT formally prove the `±1` (`ρ=1`) case; their spread induction uses, at each of the `Θ(loglog n)` stages,
that for a fresh column joining a low and a high group, choosing `+1` or `−1` must increase the spread by 1. The asymmetric
`{+1,−ρ}` version is not in AT and we do not prove it.

**What we need from you.** A self-contained lemma:

> **Lemma (asymmetric online lower bound).** Fix `ρ ∈ [1/2, 1]`. In the sparse i.i.d. model `μ_{d,n}` (`T=Θ(n)`,
> `2 ≤ d ≤ (loglog n)²/logloglog n`), every online rule that assigns each arrival a step in `{+1, −ρ}` (irrevocably, knowing
> only the past) produces a coordinate whose prefix imbalance `|Σ_{s≤t, i∈supp} step_s|` reaches `Ω(loglog n)` w.h.p., with
> the constant uniform over `ρ ∈ [1/2,1]`.

Ideally: re-run the AT spread induction for the two-action `{+1,−ρ}` case, handling the non-integer levels `ρ` introduces,
and confirm the per-stage gap grows by `≥ min{1,ρ} ≥ 1/2`. State precisely which AT probabilistic events/estimates are
unchanged and which need the `ρ`-adjustment. If instead there is a slicker reduction (e.g. coupling the `{+1,−ρ}` process to
a `±1` process at a constant cost), that is equally welcome.

---

## GAP 2 — A formal "transfer lemma" for the online upper bound (replace "verbatim")

**What we have.** Our `k`-color online upper bound is a seed-and-repair algorithm: pre-sample i.i.d. uniform seed colors
`χ̃_t ∈ [k]`; on arrival `t` with support `S_t`, if there is a unique coordinate `i*∈S_t∩E_{t-1}` that is the strict
range-maximum of `S_t` (where `E_{t-1}` = coordinates of range `≥ 64 H`, `H=loglog n`), assign `i*` a **minimum-load** color;
else follow the seed. We then invoke AT's exceptional-set sparsity lemma (`|E_T| ≤ n d^{-5}` w.h.p.) and level-set
double-exponential decay lemma (`max_{t,i} R_i < 80H`) **as black boxes**, claiming they apply because the analysis "uses
only" two interface properties:
 (i) the repair never increases the range of the (exceptional, hence positive-range) coordinate it repairs;
 (ii) the assigned color differs from the seed only on arrivals whose support contains a coordinate already at range `≥ 64H`.
We also bound the seed tail directly (a Freedman/Bernstein martingale bound giving `Pr(seed range ≥ 32H) ≤ d^{-28}`).

**The gap (referee).** "None of these mentions `k`" is not a proof. AT's category definition and level-set recurrence are
written for two-color *signed partial sums* `⟨A_i, σ⟩` and their absolute values; we need a formal statement that the same
argument runs **row-by-row with the range `R_i` in place of `|⟨A_i,σ⟩|`**, given (i)–(ii), future-support independence, and
the seed tail.

**What we need from you.** A self-contained **abstract transfer lemma**, stated for any online algorithm of the
"seed + deterministic range-repair" form satisfying (i)–(ii), with hypotheses listed explicitly, whose conclusion is
`max_{t,i} R_i(t) = O(loglog n)` w.h.p., and a proof that re-runs AT's category/level-set argument in the `R_i` language.
Concretely we need verified:
 - each arrival raises any one coordinate's range by at most 1, and a coordinate's range crosses a level only when it is not
   the unique strict max of its support (so a co-present coordinate of `≥` range is charged) — the multicolor analogue of
   AT's "modified incidence" charging;
 - the category recursion (exceptional set sparsity) and the level-set double-exponential decay hold verbatim with `R_i`
   replacing `|⟨A_i,σ⟩|`, using only future-support independence + the seed tail + (i)–(ii);
 - the number of colors `k` enters nowhere (and the regime is `2 ≤ k ≤ d`).

If the cleanest route is to restate the two AT lemmas with explicit hypotheses (an "interface" they expose) and cite AT for
their proofs, that is acceptable — but we need the interface and the verification that our algorithm meets it, not "verbatim."

---

## Deliverable
Two short notes: (1) the asymmetric `{+1,−ρ}` online lower-bound lemma with proof (or a constant-cost reduction to `±1`);
(2) the abstract seed-and-repair transfer lemma with the AT category/level-set argument re-run in the range language. We will
typeset them into the online section (replacing the current "verbatim" assertions and the odd-`k` hand-wave).

---

## ADDENDUM (round-2 referee) — refinements to the two gaps

**GAP 1 is now stated as `lem:asym-online`** in appC: "Fix ρ∈[1/2,1]; every online {+1,−ρ}-rule on μ_{d,n} produces a
coordinate with prefix imbalance Ω(loglog n) whp, uniform in ρ." We typeset the NEW part (per-stage spread increment
≥ min{1,ρ}=ρ≥1/2 with real-valued endpoints). **We still need you to supply the full induction**: re-run AT's spread
recurrence (support-set counts, second-moment, surviving-rows) for the two-action {+1,−ρ} process and confirm the
probabilistic estimates are AT's unchanged.

**GAP 2 interface now has THREE conditions** (the referee showed (i),(ii) are insufficient — the pure-seed coloring
satisfies them but does not get the level-set bound). The transfer lemma's hypotheses are now:
 (i) repair never raises the range of the coordinate it repairs;
 (ii) the color differs from the seed only when the support holds a coordinate already at range ≥ 64H;
 (iii) whenever an already-exceptional coordinate's range increases on an arrival, the support holds another coordinate of
       at least its range (the "co-present helper" the level-set recurrence needs).
We verify our minimum-load algorithm satisfies (iii) (an exceptional non-repaired coordinate is not the unique strict
range-max of its support, so a co-present helper of ≥ range exists). **We still need you to formalize the transfer lemma**:
state it for any seed+range-repair rule satisfying (i)–(iii) + future-support independence + seed tail, and re-run AT's
category (exceptional-set sparsity) and level-set (double-exp decay) arguments in the range-`R_i` language, confirming
(iii) is exactly what the level-set step uses.
