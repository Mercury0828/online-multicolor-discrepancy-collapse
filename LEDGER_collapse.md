# LEDGER — `online-multicolor-discrepancy-collapse` (append-only research-line ledger)

> Per guide §5. **Re-read this + `PROJECT_STATE.md` + frozen artifacts before continuing — never from memory.**
> Append-only: never rewrite a dated entry; add new dated entries below.

---

## HEADLINE (status)

**VERIFICATION COMPLETE → 🟢 READY TO WRITE (2026-06-22).** Owner-mandated multi-agent adversarial verification of A/B/C:
**all VERIFIED, no FATAL/GAP** — V1 (T2: REPRODUCED the A-T category recursion, 90%), V2 (T1 offline construction re-derived +
numerically stress-tested, 88%), V3 (T1 lower Ω(Ψ) + fixed-k separation + P2, 88%) — on top of the per-round audits (T1 3 blind,
etc.). Residuals are prose-completeness, not logic holes. Owner standard: AI-multi-agent-verified = "verified"; the genuine human
check = post-submission referees. Cross-project dedup vs `dynamic-weighted-mis-fat-objects` + `emst-oracle-lower-bound` = CLEAN
(no overlap/contradiction). The paper: **T1 `offdisc_k=Θ(Ψ)` + T2 `ondisc_k=Θ(loglog n)` (fixed k) + the online-vs-offline
separation**; growing-k = the shelved open-problem section. See `paper/FROZEN_RESULTS.md`, `paper/VERIFICATION_CAMPAIGN.md`.

**ROUND 7 DONE (2026-06-22) → 📝 WRITING PHASE.** The one authorized PF round refuted the displayed PF (B5, phase conveyor)
but did NOT close RB (not a lower bound). Per the pre-committed plan ⇒ **PIVOT TO WRITING.** The paper: **(offline) `offdisc_k =
Θ(Ψ)`** (P11) + **(online fixed-k) `ondisc_k = Θ(loglog n)`** (P12) + the **online-vs-offline separation** + the growing-k
bracket `[max{Ψ, loglog n/k}, loglog n]` with the open problem sharply mapped (RB ⟸ `PF_tr` ⟸ fold-or-Fibonacci; symmetric
route B4 + naive-expectation route B5 both proven dead). 🔴 Binding risk for the venue = **human verification of P11/P12/P13**.
P(SODA-worthy paper) ≈ 0.55–0.65 (conditional on human verification). (R6: P13/BC + B4. R5: P12. R4: P11. R1–R3: lower bounds.)

**ROUND 6 DONE (2026-06-22) → RB OPEN; PIVOT-TO-WRITING decision at the owner.** Two complete results stand:
**(offline) `offdisc_k = Θ(Ψ)`** (P11) + **(online fixed-k) `ondisc_k = Θ(loglog n)`** (P12) — a multicolor online-vs-offline
separation. **Growing-k OPEN, bracketed `[max{Ψ, loglog n/k}, loglog n]`.** Round 6 (RB attack): banked **P13 (BC)** + **B4**
(symmetric route DEAD — gives `H/log k` not `H/k`); RB narrowed to the **Profile-Fibonacci lemma (PF)** via the asymmetric
**LeftGap** rule (UNPROVEN, GPT 60%). Pre-committed plan: RB didn't close ⇒ **pivot to writing** (RB→PF as open problem). MATCH
ruled out small-k only; L2→L∞ no-go. "AI-verified ≠ proved": P11/P12/P13 pending human check. P(SODA-worthy paper) ≈ 0.55–0.65.
(Round 5: P12 + fixed-k. Round 4: P11. R1–R3: lower bounds + refutations.)
(Round 2: clean forms refuted (N5), P7/P8/N6 banked. Round 1: literal `(★)` refuted; P6 banked.) Seed = the CORRECTED *decreasing/collapse* direction of
`ondisc_k(μ_{d,n})` (multicolor online prefix discrepancy in the Altschuler–Tikhomirov stochastic online
Beck–Fiala model). Target venue = **SODA** (deadline 2026-07-09 AoE, re-confirm at Phase 0). Contribution =
a **matching (tight) multicolor threshold characterization** of `ondisc_k` as a function of `k`.

**Nothing is frozen as a theorem beyond the re-verified substrate `P1–P4` + barriers `B1–B3` below.**
The load-bearing crux `(★)` (profile-entropy / no-compression lemma) is OPEN and controls both the matching
upper and the matching lower bound. The attack loop has **NOT** started (begins only after a human GREEN gate).

---

## Frozen model / notation (guide §Formal Framework)

- `R^n`; arrivals `v_1,…,v_T` i.i.d. uniform over exactly-`d`-ones 0/1 vectors, `d ∈ [2, (loglog n)²/logloglog n]`,
  `T = Θ(n)`. (`d=2` ⇒ random graph edges on `n` vertices.)
- Online k-coloring: each `v_t → χ(t) ∈ [k]`, irrevocable. Color-class load `S_c(t) = Σ_{s≤t, χ(s)=c} v_s ∈ Z_{≥0}^n`.
- Coordinate profile `x_i(t) = (S_{i,1},…,S_{i,k})`; **pairwise range** `R_i = max_c x_{i,c} − min_c x_{i,c}`.
- `ondisc_k(μ_{d,n})` = the **optimal online** value of `max_{t,i} R_i(t)` (w.h.p. / in expectation).
- `M = max_t #{s<t : supp(v_s) ∩ supp(v_t) ≠ ∅} = Θ(log n / loglog n)` w.h.p.
- `L = loglog n`. Forbidden set `F_D(i) = argmax_c x_{i,c}` when `R_i = D` (else `∅`).
- Forcing condition (P4): support `E` forces `D+1` ⟺ `∪_{i∈E} F_D(i) = [k]`.

---

## Proof substrate `P*` (P1–P4 PENDING Phase-0 re-verify, then "use freely"; P5 = SIM EVIDENCE ONLY)

- **P1** `ondisc_2 = Θ(loglog n)`, d-independent [A-T arXiv:2509.02432]. *Status: pending source re-verify.*
- **P2** `ondisc_k ≥ Ω(loglog n / k)` for ALL `k` (even & odd). Two-block projection: split `[k]` into equal
  groups A,B; any k-coloring induces a valid two-color signing with `|Σ_A S − Σ_B S| ≤ kD/2`, so A-T's
  `Ω(loglog n)` gives `D ≥ Ω(loglog n / k)`. Odd `k` fully proven (asymmetric `ξ(c)=1` on A, `−a/(a+1)` on B;
  actions `{+1,−ρ}`, `ρ∈[1/2,1]`; each stage gap grows `≥1/2`; A-T recurrence unchanged, constant loss ≤2).
  *A real partial result IN HAND.* *Status: pending re-derive + numeric check.*
- **P3** `ondisc_k ≤ 1 + ⌊M/k⌋ = O(1 + log n/(k loglog n))`; `k > M ⟹ ondisc_k = 1` (online cap-h fresh-color
  algorithm). `K_fresh = Θ(log n / loglog n)`. *Status: pending re-derive M's extremal scale + numeric.*
- **P4** forcing condition (FC) above. *Status: trivial; basis of forbidden-set analysis.*
- **P5** (SIM-confirmed, QUALITATIVE — never cite as proof) `ondisc_k` decreasing + collapse to 1 at `k≈M`;
  `k=2 ≈ loglog n`. Source `sim_online-multicolor-discrepancy.md` (prior session). *Use: anchors the curve only.*
- **P6** (NEW — Round-1, AUDIT-VERIFIED 98% + 0 numeric violations) **Block-compression lemma:**
  `ondisc_k ≤ q · ondisc_{kq}` for all integers `k,q≥1`. Merge `kq` virtual colors into `k` equal blocks of size
  `q`; output real color `c` when the virtual algorithm outputs a color in block `B_c`. Real load
  `x_{i,c}=Σ_{a∈B_c} y_{i,a}` ⇒ real range ≤ `q`·(virtual range), pointwise in `t`, per realization, online-valid.
  Source: GPT-Pro round 1 eq.(1), verified by `rounds/round1_audit.md` (Audit 1) + `code/verify_round1.py`. *Use freely.*
  ⚠️ **Does NOT imply monotonicity** of `ondisc_K` in `K` (it is a downward factor-`q` relation, not upward monotone).
- **P7** (NEW — Round-2, AUDIT-VERIFIED 93% + numeric-consistent) **Offline `√(d/k)` floor:** ∃ `c,C(α,β)` s.t. if
  `αn ≤ T ≤ βn`, `k ≥ C·log(dk)`, `d/k→∞` (and `d≤n/2`), then w.p. `1−exp(−Ω(nk))`:
  `ondisc_k ≥ offdisc_k ≥ c·√(d/k)`. (First-moment/small-ball: per-color row load `Y_c~Bin(m_c,d/n)`, `Var=Θ(d/k)`,
  max-atom `√(k/d)`; balanced classes; `k^T` union beaten when `k≥C log(dk)`.) Source: GPT-Pro round 2 §1, verified
  `rounds/round2_audit.md` (Audit A) + `code/verify_round2.py`. *Use freely.* 🔴 **This is the term the prior framing
  MISSED** — it breaks A-T's d-independence for `k>2`; it dominates the online term for `k ≳ L²/d` (= `Θ(log L)` at max
  `d`); `<1` only for `k>d`; consistent with P1 (k=2 excluded), P3, B3.
- **P8** (NEW — Round-2, AUDIT-VERIFIED 97%) **Aggregate cover lemma:** for a history `h`, `Pr(level-r cover | h) ≤
  (e·d·ρ)^k + O(d²/n)` whenever the AGGREGATE condition holds: `(AM)  (1/n)·Σ_{i:R_i=r} C(|F_r(i)|, a) ≤ C(k,a)·ρ_r^a`
  for all `a`. ⇒ **max-cylinder control is UNNECESSARY** for the cascade-upper cover recurrence; only the *aggregate*
  elementary-symmetric moments need control (then adaptive stability). Source: GPT-Pro round 2 §5, verified
  `rounds/round2_audit.md` (Audit B). Caveat: iid-coordinate coupling (`O(d²/n)`); hypothesis includes `a=k`.
  🔴 **SCOPE (Round-3, Audit B 80%):** P8 controls only **level-RAISING** covers, NOT **within-level broadening**
  (`(r,r−1,…)→(r,…,r,0)`, `|F_r|` growing without forcing `r+1`). The cascade upper additionally needs a
  **broadening-cost lemma** (drift `E[ΔH_{r,a}] ≤ −γH_{r,a} + C(k,a)η^a`) — OPEN. *Use P8 for covers only.*
- **P9** (Round-3, AUDIT-VERIFIED — but **CORRECTED in Round-4**; see P11) **Multicolor occupancy-entropy floor** (lower):
  `offdisc_k = Ω(Ψ(λ, log k))`, `λ:=Td/(nk)=Θ(d/k)`. 🔴 **Round-3's 2-regime form was WRONG in the intermediate band
  `1≪λ≪log k`** (it said `√(λ log k)`; the true scale is `log k/log((log k)/λ)`, bigger — counterexample at `λ=√(log k)`:
  claimed `(log k)^{3/4}` vs true `log k/loglog k`). **Use the corrected `Ψ` (P11), not the old 2-regime form.** Supersedes P7.
- **P11** (NEW — Round-4, AUDIT-VERIFIED by 3 blind audits 92/88/88% + numerics) 🎯 **OFFLINE OCCUPANCY-THRESHOLD
  CHARACTERIZATION — the project's FIRST matching (tight) result:**
  `offdisc_k = Θ_{τ}(Ψ(λ, log(ek)))` w.h.p., where `Ψ(λ,L) := 1 + √(λL) + L/log(e+L/λ)`, `λ=Td/(nk)=Θ(d/k)`,
  for `k→∞, k≤d, d,k=(log n)^{o(1)}, T=Θ(n)`. Three regimes: `√(λ log k)` (λ≳log k); `log k/log((log k)/λ)` (1≪λ≪log k);
  `log k/loglog k` (λ=Θ(1)). **Lower** = corrected Poisson tail inversion (P9/Audit A). **Upper** = an explicit randomized
  offline construction: a **uniform all-subsets negative-association structural lemma** (strongly-Rayleigh d-subsets +
  JDP P6/P7; the `e^{-cBsℓ_s}` union beats `C(T,s)≤e^{sℓ_s}`; Audit B) + a **density-sensitive exact-cardinality
  Lovett–Meka splitting lemma** (dense `√(μℓ)` / sparse `Ψ` thresholds + release; Audit C) + a **recursive color-tree**
  (error at a `q`-node attenuates `O(1/q)`; the two path-sums reassemble into `Ψ`; Audit C). **NO extra `log d / √log d /
  loglog n / recursive-log k` loss.** Source: GPT-Pro round 4 (fresh-context), verified `rounds/round4_audit.md`.
  🔴 **"AI-verified ≠ proved":** pending human verification of (i) the all-subsets NA union bound, (ii) the exact-cardinality
  limiting Lovett–Meka + the `m=O(1)` tail/cleanup. *Use freely; this is a complete OFFLINE theorem.* (This is the floor for
  the online value: `ondisc_k ≥ offdisc_k = Θ(Ψ)`; whether ONLINE matches `Ψ` or pays a penalty is the next crux.)
- **P13** (NEW — Round-6, AUDIT-VERIFIED 88%) **Adaptive broadening-cost lemma (BC):** for `r≥2`, `a≥1`, `η∈(0,1)`,
  `E Σ_i (B_{i,r})_a ≤ nη(2τ_+ d²η)^a` (uniform over adaptive stopping-time epochs), where `B_{i,r}` = # invisible
  broadenings (`R_i=r, s_i→s_i+1`) of row `i` before `T∧σ_{r,η}` and before reaching `r+1`. Proof: every range-`r` broadening
  certifies TWO range-≥`r` rows in the same support (cover certificate + rank arithmetic, needs `r≥2`); collision prob
  `≤2d²η/n`; falling-factorial moment bound. Source: GPT-Pro round 6 §1, verified `rounds/round6_audit.md`. *Use freely.*
  🔴 **But BC + P8 only give a `k`-fold RANGE-level recurrence ⇒ `H/log k`, NOT the `H/k` RB needs** (see B4).
- **P12** (NEW — Round-5, AUDIT-VERIFIED 85%) 🎯 **ONLINE upper bound — the project's FIRST online upper:**
  `ondisc_k = O(loglog n)` for ALL `k` (multicolor extension of A-T's two-color upper). Algorithm: seed colors
  `χ~_t~Unif[k]` + repair the uniquely-largest supported exceptional row by its min-load color (never raises its range) +
  A-T's category-sparsity (`|E_T| ≤ n d^{-5}`) + the double-exponential `M(T,r)` recurrence (`r=2H` ⇒ `max_{t,i} R_i < 80·loglog n`).
  The A-T machinery is `k`-free (uses only: future-support independence; sparse category-0; actual≠seed ⇒ a prior exceptional
  row in the column). 🔴 **Crux invariant:** an upcrossing of an exceptional row certifies another exceptional row in the same
  support. Source: GPT-Pro round 5 §1, verified `rounds/round5_audit.md` (Audit A; the flagged seed-tail holds with 9× margin).
  *Use freely.* 🔴 **"AI-verified ≠ proved":** pending human verification of the imported A-T category high-moment recursion
  (not reproduced line-by-line). **⇒ with P2: `ondisc_k = Θ(loglog n)` for every FIXED k (CLOSED).**
- **P10** (NEW — Round-3, AUDIT-VERIFIED 95%) **Online mean-square lemma:** greedy on `Φ(t)=Σ_{i,c} z_{i,c}²`
  (`z_{i,c}=x_{i,c}−deg_t(i)/k`, choose `c` minimizing `Σ_{i∈E} z_{i,c}`) gives `Φ(t) ≤ t·d` deterministically ⇒
  `(1/nk)Σ z² = O(d/k)`: online achieves the `√(d/k)` scale **in MEAN SQUARE (L2) per coordinate-color**. Source:
  GPT-Pro round 3 §5, verified `rounds/round3_audit.md` (Audit B), exact constant `1−1/k`. 🔴 **L2-ONLY** — says NOTHING
  about the `L∞`/max-range (the hard part); promotion L2→L∞ is exactly what costs the P9 occupancy entropy. *Use freely.*

## Barriers `B*` (proven; any attempt MUST evade — do NOT re-walk)

- **B1** naive k-ary witness **collapses**: profile `(D,…,D,0)` has `|F_D| = k−1`; two coordinates cover `[k]`.
  ⇒ "all k colors blocked" does NOT give k independent sub-certificates; the cascade lower's `k^r` is not mechanical.
- **B2** any single fixed 1-D zero-sum projection + A-T spread is **capped at `Ω(loglog n / k)`** (k-loss tight).
  ⇒ proving `loglog n / log k` REQUIRES nonlinear profile/subset-entropy, not a fancier balanced cut.
- **B3** `K_1 = Θ(M)` is **NOT proven**. Only `Ω(loglog n) ≤ K_1 ≤ O(log n / loglog n)`. 🔴 Do NOT headline
  `K_1 = Θ(M)` / `k* = Θ(log n/loglog n)` as a theorem. `K_fresh = Θ(M)` is only a *sufficient* collapse scale (P3).
- **B5** (NEW — Round-7, AUDIT-VERIFIED 93%) **The displayed PF is FALSE for LeftGap; the quenched / expectation route is dead.**
  An explicit deterministic **phase conveyor** recycles one broad row to birth consecutive LeftGap phases `1,2,…,q` with only
  `O(kq)` rows (LINEAR, not Fibonacci) ⇒ `E Z_{kB+m} ≥ C(n,k)^{-q} ≫ exp(−cF_k(m))` for `m > H/log2` (exactly the window PF
  needs) ⇒ **the untruncated PF is false**; and the **uniform-over-stopping-times mixed-profile factorization is false**
  (overlap `∩_j A_j={a}`, conditional collision `≥k/n ≫ Π(k|A_j|/n)`). 🔴 **NOT a lower bound** — the conveyor has prob
  `exp(−log n·H^{O(1)}) ≪ n^{−A}`, so it does NOT refute RB and gives no online penalty. **Corrected target: a TRUNCATED
  `PF_tr`** `Pr(Z_{kB+m}>0) ≤ Cnd e^{−cF_k(m)} + n^{−A}` (the `n^{−A}` absorbs folded histories) `⇒ RB`, via a **fold-or-Fibonacci
  incidence-excess lemma** (every canonical witness has `Ω(F_k(m))` disjoint base obligations OR a sub-DAG of incidence excess
  `≥A+2`, bounded `n^{−A}`). Source: GPT-Pro round 7, verified `rounds/round7_audit.md`. *Use as the precise open-problem statement.*
- **B4** (NEW — Round-6, AUDIT-VERIFIED) **The symmetric-rank route CANNOT prove RB.** Any permutation-invariant `(R,s)` /
  `H_{r,a}=(1/n)Σ_{i:R_i=r}C(|F_r(i)|,a)` moment method (BC + P8) gives only a `k`-fold range recurrence `η_{r+1} ≲ (Aη_r)^k`
  ⇒ `η ≤ exp(−c k^j)` ⇒ union-over-n needs `j ≳ loglog n/log k = H/log k`, **an extra `log k` factor vs the `H/k` RB needs.**
  Deterministic skip obstruction (narrow-rainbow: a visible raise skips all `k−2` intermediate phases ⇒ the `k^r` mechanism).
  🔴 **NOT a stochastic online lower bound** — an asymmetric (color-staggering) rule could evade it (cf. Always-Go-Left beats
  `k`-choice: `loglog n/k` not `loglog n/log k`). Beating `H/log k`→`H/k` needs an **asymmetric full-profile** rule + a
  **mixed-profile (Profile-Fibonacci) lemma**. At `k=2` both are `Θ(H)` (A-T anchor can't distinguish). Source: round 6 §2–3.

## Refuted routes `N*` ("do NOT attempt" + reason)

- **N1** increasing forms `Θ(loglog n + √log k)`, `Θ(√k · loglog n)` — DEAD (P3 gives discrepancy-1 for large k).
- **N2** naive k-ary witness tree (`|W_r| ≍ k^r` mechanically) — collapses (B1).
- **N3** a fancier balanced cut / single 1-D projection to beat `loglog n/k` — capped at `Ω(loglog n/k)` (B2).
- **N4** black-box A-T-into-a-multicolor-binary-tree — input adaptively thinned (the DEAD sibling's route);
  use a DIRECT k-color analysis.
- **N5** (NEW — Round-2) the **clean forms `Θ(max{1, L/k})` (fast) and `Θ(max{1, L/log k})` (cascade) as the FULL
  answer** — REFUTED by P7: they omit the `√(d/k)` floor, which dominates for `k ≳ L²/d` and `→∞` at `d=Θ(L²/log L),
  k=Θ(L)`. Do NOT state either clean form as the complete characterization; the answer carries a `√(d/k)` term.
- **N6** (NEW — Round-2) assuming **`ondisc_K` is monotone non-increasing in K** — REFUTED (exact `n=3,d=2,T=4`:
  `ondisc_2=11/9 < ondisc_3=13/9`, `ondisc_4=1`; + a `d=2` adversarial stream `D_m=1<D_{m+1}`). No monotonicity lemma
  is usable; "decreasing in k" is **rate-level only** (already a standing caveat; now hard-refuted at the value level).
- **N7** (Round-3) **online/offline `O(√(d/k))` as the matching upper (Targets A1/A2)** — REFUTED: the offline floor is
  `Ψ(λ,log k)` (P11), strictly above `√(d/k)`. The `√(d/k)` (P7) is valid but NON-TIGHT. (Also: the round-3 "`√(λ log k)`
  for all `λ≫1`" was itself non-tight in the intermediate band — see P9 correction / P11.)

---

## THE EXACT OPEN PROBLEM = `(★)` + its three forks

**(★) Profile-entropy / no-compression lemma:** for a near-optimal online k-coloring on `μ_{d,n}`, the forbidden
(high-color) set `F_r(I)` of a typical coordinate `I` at discrepancy level `r` satisfies
`Q_r(A) := Pr(A ⊆ F_r(I)) ≤ ρ_r^{|A|}` for all `A ⊆ [k]`, **stable under adaptive online evolution**.
(The static profile `(D,…,D,0)` shows this is NOT a plain Chernoff bound.)

- **HS-upper** (if `(★)` holds): elementary-symmetric potential `G_i(s)=∏_c(1+s·e^{λ z_{i,c}})`, `z=S−occ/k`;
  subset-tail union bound `(dρ_r)^k`, recurrence `ρ_{r+1} ≤ C_d(dρ_r)^k + ε_n` ⇒ `r = O(loglog n / log k)` (cascade upper).
- **HS-lower** (if `(★)` holds, Profile-Branching): each level raises pruned-witness entropy `≥ c·log(k+1)` ⇒
  `|W_r| ≥ (k+1)^{cr}`, random embedding works for `|W_r| ≤ c'·log n` ⇒ `ondisc_k ≥ Ω(loglog n / log k)` (cascade lower).
  ⇒ **cascade form** `ondisc_k = Θ(max{1, loglog n / log(k+1)})`.
- **HS-alt** (if `(★)` FAILS): construct a star/junta compression online strategy giving `O(loglog n / k)` (fast
  upper); pair with P2 lower ⇒ **fast form** `ondisc_k = Θ(max{1, loglog n / k})`. Still SODA.
- **HS-k\*** pin the exact discrepancy-1 threshold `K_1` (currently `Ω(loglog n) .. O(log n/loglog n)`, B3); a
  matching `K_1 = Θ(M)` needs the boundary witness for `D=1`.

**Three clean outcomes; two are SODA.** Prior GPT-Pro confidence: cascade 0.40 / fast 0.35 / plateau 0.10 / other 0.15.
The project命题 is **"prove or refute `(★)`"**, not "guess the form".

### 🔶 Round-1 update (2026-06-22) — `(★)` literal REFUTED; targets sharpened (audit-verified)
- **Literal/exact `(★)` is REFUTED** (under the natural `ρ_r = max_c Q_r({c})`; vacuous if `ρ_r` unrestricted).
  Both a color-symmetric feasible law and a **genuine symmetrized optimal disc-1 (P3) process** violate product
  domination (the latter by `(t−1)/t·k/(k−1) > 1` for `t>k`, a `1+O(1/k)` slack). ⇒ range+symmetry+near-optimality
  do NOT imply product domination; an extra **profile-shape** invariant is indispensable. (Audit 2, CLAIMs A,B.)
- **Repaired target `(★')` (cascade upper):** a **pathwise, history-conditional** empirical cylinder bound
  `q^h_{r,t}(A) := (1/n)|{i: R_i=r, A⊆F_r(i,t)}| ≤ ρ_{r,t}(h)^{|A|}`, uniform over stopping times. Under `(★')` the
  cover recurrence `(dρ)^k + O(d²/n)` is CORRECT (GPT eq.13). **Missing = max-cylinder control**: the elementary-
  symmetric potential bounds `Σ_{|A|=a}` but the cover needs `max_{|A|=a}`; an adaptive junta concentrates the mass,
  costing `C(k,a)≈2^k`. **OPEN.**
- **FAST target (sharpened, audit-corrected) — via the new P6:** FAST upper ⟸ **(CP-uniform)** `ondisc_K = O(1)`
  for ALL integer `K` in a band `[c₁ loglog n, c₂ loglog n]` (`c₂≥2c₁`), NOT merely the existential `K_1=O(loglog n)`
  (Audit 1 caught this). The critical `D=1` process is an **online rotating-palette problem**: keep
  `∩_{i∈E}([k]\U_i) ≠ ∅` with `k=O(loglog n)`, `U_i`=colors one above the coord min. Missing = a **dynamic palette-
  persistence/junta lemma** (the star center is consumed from every non-saturated palette; no invariant bounds the
  consume/renew/rotate rate). PLUS a **residual `L≲k≲M` regime** uncovered by the band or fresh-color (`O(M/k)≫O(1)`).
  Open **sub-question that would simplify everything: is `ondisc_K` monotone non-increasing in `K`?** (P6 does NOT decide it.)
- **CASCADE lower (HS-lower):** needs a **bounded-fiber witness-entropy lemma** — `(r,…,r,0)` gives `2^{k−1}`
  subset-certificates from ONE history; un-quotiented subset-counting over-counts ⇒ naive pigeonhole gives only the
  `L/k` (fast) scale. B2-consistent (no projection). **OPEN.**
- **Net:** no fork closed, no fork dead. The scalar `H^+` potential is only a forcing certificate, not amortized
  (broad min-plateaus absorb safe updates) ⇒ no multicolor analogue of the binary A-T one-step contraction.

### 🔶🔶 Round-2 update (2026-06-22) — the `√(d/k)` floor RESHAPES the contribution (audit-verified) → human gate (c)
- **The clean targets are REFUTED (N5).** The corrected characterization is
  **`ondisc_k = Θ( max{ 1, F_online(k), √(d/k) } )`**, where `F_online(k)` is the online-specific term (fast `L/k`
  via P2, or cascade `L/log k`) and `√(d/k)` is the **offline floor (P7)**. Lower bound in hand:
  `ondisc_k ≥ max{1, Ω(L/k) [P2], c√(d/k) [P7]}`.
- **Regime map (at max `d=Θ(L²/log L)`, `L=loglog n`):**
  - `k ≲ log L`: online term governs (`F_online(k) ≥ √(d/k)`) — the fast/cascade question lives HERE.
  - `log L ≲ k ≲ d`: the **offline `√(d/k)` floor governs**, decreasing from `~L/log L` down to `1`.
  - `k ≳ d`: `ondisc_k = O(1)` (floor `<1`; collapse) — so the **disc-1 threshold `K_1 ≍ d`** at max `d` (within B3).
  For smaller `d` the floor is dominated/irrelevant and the original online picture survives throughout.
- **The binding OPEN question is now the matching ONLINE UPPER bound for the `√(d/k)`-dominated middle regime**
  (`log L ≲ k ≲ d`): is the offline `O(√(d/k))` upper achievable ONLINE? (Plus: the offline `O(√(d/k))` upper itself
  must be confirmed; and the fast-vs-cascade `F_online` form for small `k`; and HS-lower `Ω(L/log k)`.)
- **P8 simplifies the cascade upper:** the cover recurrence needs only the AGGREGATE moment condition `(AM)`, NOT
  max-cylinder; the cascade upper now hinges on **adaptive stability of `(AM)`** under the online update (still open, §6).
- **NOT a kill:** the corrected form is still a tight, matching-able characterization — arguably MORE novel (breaks
  A-T d-independence for `k>2`). But the contribution SHAPE + the constant-disc target (`k≍L → k≍d∨L`) changed ⇒ gate (c).

### 🔶🔶🔶 Round-3 update (2026-06-22) — the offline floor is an OCCUPANCY-ENTROPY THRESHOLD (audit-verified); A1/A2 refuted
- **The offline floor is bigger than `√(d/k)` (P9, audit-verified).** Keeping `k` Poisson(λ) occupancies in a width-D
  window forces the **extreme-value spread of k Poissons** (balls-into-bins max-load): `√(λ log k)` (or `log k/loglog k`
  at `λ=Θ(1)`). ⇒ **Targets A1 (online `O(√(d/k))`) and A2 (offline `O(√(d/k))`) are REFUTED (N7).** The √(d/k)
  catch-down cannot happen. The true offline benchmark is the **entropy threshold `D_ent`**.
- 🔴 **CORRECTION to the round-2 record:** the round-2 scoop-scan called the offline `√(d/k)` "folklore". That holds for
  the **2-color `√d`** (Bansal–Meka etc.) ONLY; the **multicolor (k-color) offline matching UPPER is OPEN/novel** (not on
  the shelf), per Audit B (70%) — though possibly a routine partial-coloring extension (do not over-claim deep novelty).
  ⇒ the offline multicolor occupancy-threshold characterization (`D_ent` lower + a saturation upper) is itself an open,
  potentially-SODA-worthy problem.
- **Positive online tool banked: P10** (mean-square `Φ≤td` ⇒ online hits `√(d/k)` in **L2**; the hard part is L2→L∞).
- **The new open lemmas (all unproven after 3 rounds):** (1) **offline entropy-saturation** (the matching upper for
  `D_ent` — a random-CSP existence theorem; the most reachable novel result?); (2) **online localization** (does online
  match the offline `D_ent`, or pay a penalty?); (3) **bounded-d FAST** (renewal-stable palette compression ∀`k≥CL`);
  (4) **bounded-d CASCADE upper** (the within-level **broadening-cost** lemma — P8 covers only level-raising);
  (5) **bounded-d CASCADE lower** (the bounded-probability **ancestry-fiber** lemma; B2-consistent).
- 🔴🔴 **STRATEGIC INFLECTION (orchestrator, honesty rail):** after **3 strong rounds** we have a rich, growing pile of
  VERIFIED LOWER bounds + structural results (P2,P6,P7,P8,P9,P10; B1–B3; N1–N7) but **ZERO matching UPPER bound in ANY
  regime**, and the target has reshaped **three times** — the original online-vs-offline *contrast* headline has dissolved
  (in the middle regime the online answer just inherits the offline floor). This is a **sustained drop in closure-prospect**
  (a first-class escalation signal), though **NOT proof-of-death** (the uppers are OPEN, not refuted). → triggers a STRATEGY
  health-check + an owner touch (gate-(a)/(c)-adjacent): escalate a fresh attacker on the most reachable UPPER (the offline
  saturation lemma?) / re-aim the headline at the offline occupancy-threshold characterization / reassess scope-venue.
  **NO silent downgrade; NO kill (no proof-of-death). Escalate, don't weaken.**

### 🟢🟢 Round-4 update (2026-06-22) — the OFFLINE characterization CLOSED (P11, 3 audits) — the FIRST matching result
- **`offdisc_k = Θ(Ψ(λ, log k))`** is **CLOSED** (audit-verified 92/88/88% + numerics), `Ψ(λ,L)=1+√(λL)+L/log(e+L/λ)`.
  The project's first matching (tight) characterization — a complete OFFLINE theorem with a NON-trivial construction
  (all-subsets-NA structural lemma + density-sensitive exact-cardinality Lovett–Meka + recursive color-tree). Corrected P9.
- 🔴 **The strategy health-check's binary test came back POSITIVE within the clock:** "#1 closes ⇒ complete offline
  characterization, write with confidence." The "3 rounds, ZERO upper anywhere" inflection is **partly resolved** — ONE
  matching upper now exists (offline). The upper is NOT a routine partial-coloring corollary (corrected threshold +
  adaptive-NA union + color-tree), softening the "ESA-grade/thin" worry (though offline + average-case still pulls toward
  ESA/RANDOM unless the ONLINE side closes).
- **Remaining crux for SODA-grade = the ONLINE side:** does `ondisc_k` match the offline `Ψ`, or pay an online penalty
  (A-T: online `Θ(loglog n)` ≫ offline `√d` at k=2)? P10 gives only L2; L2→L∞ is the cost. Plus the small-k `F_online`
  form + the bounded-d sub-problems. Updated picture: `ondisc_k = Θ(max{1, F_online(k), Ψ_online(λ,k)})`, `Ψ_online ≥ Ψ`;
  open whether `Ψ_online = Ψ`. "AI-verified ≠ proved": P11 pending human verification of the NA-union + exact-LM steps.

### 🟢🟢 Round-5 update (2026-06-22) — the ONLINE side: FIRST online upper (P12) + fixed-k CLOSED; growing-k open at RB
- **`ondisc_k = O(loglog n)` for ALL k (P12, audit-verified 85%)** — the project's first ONLINE upper bound (A-T extension).
  **⇒ fixed-k CLOSED: `ondisc_k = Θ(loglog n)`** (P12 upper + P2 lower). A complete online result; d-independent.
- **The bracket (verified):** `c·max{Ψ(λ,log(ek)), loglog n/k} ≤ ondisc_k ≤ C·loglog n`. (lower = P11 `online≥offline=Ω(Ψ)`
  + P2 `Ω(loglog n/k)`; upper = P12.)
- 🔴 **MATCH ruled out ONLY for SMALL k** (Audit B correction — NOT global): where `loglog n/k ≫ Ψ` (small/fixed k; k=2 via P1)
  the online value strictly exceeds the offline floor `Ψ` — a genuine **online penalty**. For **growing k** with `loglog n/k ≲ Ψ`,
  whether `ondisc_k = Θ(Ψ)` (MATCH) is **still OPEN**. Do NOT state "MATCH ruled out" globally.
- **L2→L∞ no-go (verified):** `R_i≥D ⇒ Σ_c z² ≥ D²/2` ⇒ P10 gives only `#{R_i≥D} ≤ O(nd/D²) ≥ n` at `D≍Ψ` — the mean-square
  tool provably gives NO L∞ control at the entropy scale.
- **The EXACT open piece for growing-k = the RANKED-BROADENING LEMMA (RB)** (verified as the exact sufficient reduction):
  with rank `ρ(x)=(k−1)(R−1)+s(x)` (`s=|argmax|`), `R ≤ 1+ρ/(k−1)`; RB = "∃ online rule with `max_{t,i} ρ_i(t) ≤ C(kΨ+H)`
  whp" ⇒ `ondisc_k = Θ(max{Ψ, loglog n/k})` (the conjectured closure, GPT 60%). RB charges the within-level **broadening**
  (`Δρ=+1`, `(D,D−1,…)→(D,…,D,0)`) that P8 misses; the balls-into-bins power-of-k analogy fails (one broad row blocks `k−1`
  colors — B1/N2). **UNPROVEN — the new attack target.**
- **🟢 Net picture (two complete results + a bracket, pending human verification):**
  `offdisc_k = Θ(Ψ)` (offline, P11) | `ondisc_k = Θ(loglog n)` (online, fixed k) | `ondisc_k ∈ [max{Ψ, loglog n/k}, loglog n]`
  (online, growing k, open at RB). **A genuine MULTICOLOR online-vs-offline separation** (online stays `loglog n` for fixed k;
  offline drops to `Ψ < loglog n`) — extends A-T's k=2 phenomenon. The round-3 "no upper anywhere" inflection is RESOLVED.

### 🔶 Round-6 update (2026-06-22) — RB OPEN (not closed); BC proven (P13); symmetric route DEAD (B4); narrowed to PF/LeftGap
- **RB neither proved nor refuted.** Banked **P13 (BC)** — invisible broadening is not free — and **B4** — the symmetric
  `(R,s)`/`H_{r,a}` route provably gives only `H/log k`, NOT the `H/k` RB needs (a `log k` exponent mismatch + a deterministic
  skip obstruction). So the natural (permutation-invariant) approach is **excluded** — not a lower bound, a proof obstruction.
- **The remaining path = an ASYMMETRIC full-profile rule (LeftGap) + the Profile-Fibonacci lemma (PF):** `E Z_{kB+m} ≤
  Cnd·exp[−c F_k(m)]`, `F_k(m)=Σ_{j=1}^k F_k(m−j)=Θ(φ_k^m)` (`φ_k↑2`, the Always-Go-Left staggered-Fibonacci that gets
  `loglog n/k`). **PF ⇒ RB ⇒ growing-k closed `Θ(max{Ψ, loglog n/k})`.** PF is **UNPROVEN** — needs a new mixed-profile
  transport estimate on `(1/n)Σ_i Π_{j} 1{g_{i,c_j}≥ℓ_j}` (overlap makes the naive product bound false; P8/P10 don't supply it).
  GPT confidence RB-true-via-LeftGap: 60%.
- **Unconditional bracket UNCHANGED:** `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n`. The two complete results (P11, P12 fixed-k)
  are untouched.

### 🔶 Round-7 update (2026-06-22) — the displayed PF REFUTED (B5); RB still OPEN; → PIVOT TO WRITING
- **PF (as displayed) is FALSE for LeftGap** (phase conveyor, B5) — but **NOT a lower bound** (`≪ n^{−A}`), so **RB is still
  neither proved nor refuted**; growing-k order remains `max{Ψ, loglog n/k} ≤ ondisc_k ≤ loglog n`. The corrected open target is
  the **truncated `PF_tr`** (`+n^{−A}` slack) via a **fold-or-Fibonacci incidence-excess lemma** (a cycle-aware causal-DAG count).
- 🔴 **This was the ONE owner-authorized PF round; it did NOT close ⇒ per the pre-committed plan: PIVOT TO WRITING.** No further
  RB/PF rounds. The open-problem section is now sharply specified: RB ⟸ `PF_tr` ⟸ fold-or-Fibonacci; the symmetric route (B4) and
  the naive expectation/quenched route (B5) are both proven dead — a strong, well-mapped frontier.
- **WRITABLE PAPER STANDS:** the two complete results (P11 offline `Θ(Ψ)`, P12 online fixed-k `Θ(loglog n)`) + the separation +
  the growing-k bracket + the mapped open problem. 🔴 Binding risk = **human verification of P11/P12/P13** (the venue floor), NOT
  the open problem.

---

## Confidence trend (dated, % — first-class escalation signal)

| Date | cascade | fast | plateau | other | Source / trigger |
|---|---|---|---|---|---|
| 2026-06-22 | 0.40 | 0.35 | 0.10 | 0.15 | Inherited from GPT-Pro round-2 verdict (pre-Phase-0). Baseline. |
| 2026-06-22 | 0.42 | 0.33 | 0.07 | 0.18 | Post Phase-0 de-risk: Sim B shows clear collapse-to-1 (NOT plateau) ⇒ plateau down; Sim A binding-level forbidden sets small (single leader, |F|≈1), Γ increasing ⇒ `(★)`-consistent / mildly cascade-favorable ⇒ cascade up slightly; `other` up to absorb the balls-into-bins "cascade-upper-is-folklore" framing risk (auditor). Small, evidence-based update only (coarse sim). |
| 2026-06-22 | 0.45 | 0.33 | 0.04 | 0.18 | Post Round-1 (audit-verified): literal `(★)` refuted (expected); new tool P6; cascade up (GPT 60% lean + single-leader evidence; `(★')` cover recurrence correct under the lemma); fast held (Audit 1 showed the FAST floor is HARDER than framed — needs uniform-band + `L≲k≲M` residual + the monotonicity sub-question); plateau down (collapse + P6). GPT's own: cascade-is-truth 60% / fast-is-truth 40%. |
| 2026-06-22 | — | — | 0.03 | — | **Forks REFRAMED (Round-2, P7).** The cascade/fast/plateau labels were about the FULL online form; that framing is REFUTED (N5) — the answer is now `Θ(max{1, F_online(k), √(d/k)})`. New decomposition: P(corrected d-dependent characterization is tight & SODA-worthy & reachable) ≈ **0.55**, of which the `F_online` small-k form is cascade≈0.55 / fast≈0.45 (sub-prob); plateau≈0.03 (dead). Dominant NEW risk = the **matching online upper for the `√(d/k)` regime** (unproven) ⇒ ~0.42 "open/partial". This is a gate-(c) re-quantification — the simple 4-way table no longer fits; see the Round-2 update block above. |
| 2026-06-22 | — | — | — | — | **Round-5: TWO COMPLETE RESULTS — offline `Θ(Ψ)` (P11) + online fixed-k `Θ(loglog n)` (P12).** P(a SODA-worthy paper by 07-09) UP to ≈ **0.55–0.65**: two complete tight results + a genuine multicolor online-vs-offline separation + the growing-k gap reduced to ONE clean lemma (RB). A coherent paper EXISTS now even if RB stays open. P(full growing-k tight via RB) ≈ 0.30–0.40. The round-3 "no upper" inflection is resolved. |
| 2026-06-22 | — | — | — | — | **Round-4: FIRST MATCHING RESULT — the OFFLINE characterization CLOSED (P11, `offdisc_k=Θ(Ψ)`).** P(a SODA-worthy paper by 2026-07-09) UP to ≈ **0.40–0.50**: a complete tight offline theorem with a non-trivial construction is in hand (pending human verification). The SODA-grade upgrade still needs the **ONLINE** side (does `ondisc_k` match `Ψ`?). If the offline theorem alone → likely ESA/RANDOM-grade-but-now-substantial; offline + online match → SODA. Decomposition: P(online matches/closes too) ≈ 0.25–0.35; P(offline-only paper) ≈ high (bankable now). |
| 2026-06-22 | — | — | — | — | **Round-3: P(a matching SODA-worthy characterization closes by 2026-07-09) DROPPED to ≈ 0.35–0.40.** Reason: the `√(d/k)` benchmark itself refuted (P9 floor is bigger); the offline benchmark's UPPER is now also open; **3 rounds, no matching upper in ANY regime.** Decomposition: most-reachable = the **OFFLINE occupancy-threshold characterization** (saturation upper) ≈ 0.45 reachable & novel(ish); bounded-d FAST/CASCADE ≈ 0.30; online middle-regime localization ≈ 0.20. Sustained closure-prospect drop ⇒ escalate fresh attacker / owner touch (NOT a downgrade, NOT a kill). |

> (cascade + fast = 0.75 ⇒ "two of three outcomes are SODA". Plateau weakly down-weighted by the de-risk.)

---

## Log

- **2026-06-22** — Ledger created (day-0). Phase 0 started: scaffold complete; kill-scan + `(★)` de-risk pending.
- **2026-06-22** — **Kill-scan = GREEN** (`lit/SCAN_REPORT.md` + independent second opinion `lit/SCAN_SECOND_OPINION.md`,
  82% no-scoop). No paper gives the matching multicolor sparse-i.i.d. online threshold (cascade/fast). A-T 2509.02432
  v3 = k=2 only (Def 1.4 confirmed: disc = max over prefixes of ℓ∞ partial sum; Thm 1.1 lower `max(⅛ loglog n, Ω(√d))`,
  upper `35 loglog n` for `d≤(loglog n)²/logloglog n`) ⇒ **P1 quantifier + d-independence verified against source.**
  GKKS 2007.10545 = binary orientation (no k-color). Bansal 2007.10622 / HPVX 2502.14624 = generic-polylog / dense
  `Θ(√log T)`, no sparse threshold (our novelty = the lemma, NOT the multicolor reduction). Offline LBs (2504.18489
  `Ω(√n)`, 2502.10516 `Ω(√(n/ln k))`) = the contrast. 🟡 carried: SODA double-blind/page policy not text-confirmed
  (SIAM 403; deadline 2026-07-09 confirmed via 2 CFP aggregators) — re-confirm at writing time. 🟡 carried: A-T spread
  machinery `s_q=n/(log n)^{3^q}` only abstract-level — re-derive when P2 is briefed.
- **2026-06-22** — **`(★)` de-risk (Sim A/B, `code/DERISK_REPORT.md`, `code/phase0_results.json`) = NOT REFUTED.**
  Sim B (lookahead player, d=2,3, n up to 2e5): `ondisc_k` monotone decreasing + collapses to 1 (~k≈2–3·M) — P5
  confirmed directionally, **NOT a plateau**. Sim A (Γ-statistic, n up to 1e6): at **binding stressed levels r=D**
  forbidden sets are SMALL (mean |F|≈1.0–1.08, single-leader dominated — B1's `(D,…,D,0)` compression does NOT
  dominate), Γ(q) **increasing** ⇒ `Q_r(A)` decays ≥ geometrically ⇒ **consistent with `(★)`**, mildly cascade-favorable.
  Γ only flattens at the trivial level r=1 in the already-collapsed regime. Cascade-vs-fast indistinguishable
  (loglog n≈2.5, coarse — as pre-registered). 🔴 Honesty: heuristic player, NOT optimal; `(★)`'s adaptive-evolution
  stability is unsimulatable theory (`HS-core`).
- **2026-06-22** — 🔴 **CASCADE-FORK LOWER-BOUND GAP (record explicitly):** P2 gives `Ω(loglog n/k)`, which is the
  MATCHING lower for the **fast** fork only. For the **cascade** fork the target is `Θ(loglog n/log k)` and
  `loglog n/log k ≫ loglog n/k`, so **P2 is NOT the matching cascade lower** — the cascade fork needs BOTH a new
  upper (`HS-upper`) AND a new stronger lower (`HS-lower`, Profile-Branching, `Ω(loglog n/log k)`), and B2 says the
  lower CANNOT come from a single linear projection (needs nonlinear subset-entropy). Do not present P2 as "the
  matching lower" without naming which fork.
- **2026-06-22** — 🟡 **Novelty-framing risk (auditor):** cascade `loglog n/log k` resembles balls-into-bins d-choice
  max-load `loglog m/log d`; a referee may call the cascade UPPER folklore. If `HS-upper` is a balls-and-bins-style
  argument, foreground novelty on `HS-lower` (the matching lower) + the A-T anchoring. Carried to writing + the brief.
- **2026-06-22** — **HEALTH-CHECK** (`docs/HEALTH_CHECK_phase0.md`): on-track for SODA; no drift; named the cascade-
  lower gap; recommended **fast-first sequencing** (bank `HS-alt` `O(loglog n/k)` upper → complete tight theorem with
  P2, no adaptivity-stability needed → guaranteed SODA floor; THEN gamble `(★)`/cascade). Over-claim rails: K_1 bracket,
  rate-level monotonicity, "P2+algorithm ≠ SODA".
- **2026-06-22** — **PHASE-0 VERDICT = GREEN.** ▶ **Human GREEN gate PASSED (owner).** Attack loop authorized.
  Owner overrides codex-xhigh default → dispatch **directly to web GPT-5.5-Pro**, owner relays manually. Sequencing =
  **fast-first**. Round-1 brief = `rounds/round1_brief.md` (ready to paste). **Round 1 = OPEN (awaiting GPT-Pro
  response to adversarially audit).** Confidence unchanged (cascade 0.42 / fast 0.33 / plateau 0.07 / other 0.18).
- **2026-06-22** — **ROUND 1 (GPT-5.5-Pro) — non-closure, real progress.** Reply `rounds/round1_response.md`; two blind
  adversarial audits + numeric triangulation `rounds/round1_audit.md` (`code/verify_round1.py`). Results: **(i) NEW
  verified tool P6** (block-compression `ondisc_k ≤ q·ondisc_{kq}`, audit 98% + 0 numeric violations). **(ii) Literal
  `(★)` REFUTED** (CLAIMs A,B audit-CORRECT 93%) — repaired pathwise `(★')` open at max-cylinder control. **(iii) FAST
  reduction over-claimed by GPT** (Audit 1, 88%): needs the **uniform-band** `(CP-uniform)` not the existential
  `K_1=O(loglog n)`, + a residual `L≲k≲M` gap; opened the **`ondisc_K` monotonicity** sub-question. **(iv) HS-lower**
  needs a bounded-fiber witness-entropy lemma. Classification **GAP/PROGRESS, NOT FATAL**; no kill, no stall, no human
  gate. Next = `rounds/round2_brief.md` (fast-first: prove `(CP-uniform)` + the palette-persistence lemma; the
  monotonicity question; then `(★')` max-cylinder + bounded-fiber). Confidence → 0.45/0.33/0.04/0.18.
- **2026-06-22** — **GATE (a/c) RESOLVED (owner): KEEP SODA full-force** (no venue downgrade despite ~10–15% odds — NO-RETREAT
  exercised). **Round 4 = a FRESH-context attacker on the offline entropy-saturation UPPER (#1) ONLY** (`rounds/round4_brief.md`,
  ~5-day binary clock). Goal: prove `offdisc_k = O(D_ent)` matching the P9 lower ⇒ bank the complete OFFLINE occupancy-threshold
  characterization `Θ(D_ent)`; online-localization remains the SODA-grade prize. No ESA/RANDOM writing pivot.
- **2026-06-22** — **VERIFICATION CAMPAIGN (owner-mandated multi-agent) → READY TO WRITE.** 3 independent fresh-context
  adversarial verifiers: V1 T2/A-T-category-recursion REPRODUCED (90%); V2 T1 offline construction re-derived + numeric (88%);
  V3 T1 lower + separation + P2 (88%). All VERIFIED, no FATAL/GAP. Plus cross-project dedup CLEAN (`lit/DEDUP_sibling_projects.md`).
  Artifacts `paper/FROZEN_RESULTS.md` + `paper/VERIFICATION_CAMPAIGN.md`. Growing-k open problem SHELVED (owner). → writing.
- **2026-06-22** — **ROUND 7 (GPT-5.5-Pro) — PF attack: the displayed PF REFUTED (B5), RB still OPEN.** Reply
  `rounds/round7_response.md`; audit `rounds/round7_audit.md` (93%; auditor simulated LeftGap k=3–6). An explicit phase conveyor
  refutes the untruncated PF + the quenched factorization, but is `≪ n^{−A}` ⇒ NOT a lower bound ⇒ RB neither proved nor refuted.
  Corrected target = truncated `PF_tr` via a fold-or-Fibonacci incidence-excess lemma. **This was the one authorized PF round ⇒
  PIVOT TO WRITING** (owner's pre-committed plan). Banked B5. Growing-k bracket unchanged.
- **2026-06-22** — **ROUND 6 (GPT-5.5-Pro) — RB attack: OPEN (not closed), but productive.** Reply `rounds/round6_response.md`;
  audit `rounds/round6_audit.md` (88%). Banked **P13 (BC** adaptive broadening-cost) + **B4** (symmetric `(R,s)`/`H_{r,a}` route
  provably gives `H/log k` not `H/k` — a `log k` exponent mismatch + deterministic skip obstruction; NOT a stochastic lower
  bound). RB narrowed to the **Profile-Fibonacci lemma (PF)** via the asymmetric **LeftGap** rule (staggered Fibonacci
  `F_k(m)=Σ_{j=1}^k F_k(m−j)`); PF UNPROVEN (GPT 60%). Unconditional bracket unchanged. **Pre-committed plan: RB didn't close ⇒
  PIVOT TO WRITING** (RB→PF as the open-problem section); owner to confirm write-now vs one PF round.
- **2026-06-22** — **ROUND 5 (GPT-5.5-Pro) — TWO COMPLETE RESULTS + growing-k bracket.** Reply `rounds/round5_response.md`;
  2 blind audits `rounds/round5_audit.md` (Audit A 85% the `O(loglog n)` online upper; Audit B 88% bracket/fixed-k/no-go/RB).
  Banked **P12** (`ondisc_k=O(loglog n)` ∀k) ⇒ **fixed-k CLOSED `Θ(loglog n)`**. With P11 (offline `Θ(Ψ)`): TWO complete tight
  results + a multicolor online-vs-offline separation. MATCH ruled out for SMALL k only; L2→L∞ no-go; growing-k OPEN at the
  ranked-broadening lemma **RB** (the exact sufficient reduction ⇒ conjectured `Θ(max{Ψ, loglog n/k})`). Round-3 "no upper"
  inflection RESOLVED. P(SODA-worthy paper) ↑ ≈ 0.55–0.65. Milestone health-check `docs/HEALTH_CHECK_milestone_r5.md`.
- **2026-06-22** — **ROUND 3 (GPT-5.5-Pro) — stronger lower bound, but closure-prospect drop.** Reply
  `rounds/round3_response.md`; 2 blind audits + numerics `rounds/round3_audit.md` (`code/verify_round3.py`). Banked:
  **P9** (occupancy-entropy floor `√(λ log k)` / `log k/loglog k`, Audit A 88% — supersedes P7), **P10** (mean-square,
  L2-only, Audit B 95%), **N7** (A1/A2 `√(d/k)` matching upper refuted). **Folklore record CORRECTED**: multicolor offline
  UPPER is open (only 2-color `√d` is folklore). P8 scope sharpened (level-raising covers only). Classification
  **VERIFIED PROGRESS + STRATEGIC INFLECTION** (3 rounds, no upper anywhere) → STRATEGY health-check
  `docs/HEALTH_CHECK_strategy_r3.md` + owner touch. NOT a kill.
- **2026-06-22** — **P7 folklore scoop-scan** (`lit/SCAN_P7_offline_floor.md`, gate-c pre-check): the offline `√(d/k)`
  floor is **KNOWN/near-folklore** — k=2 `√d` is published (Bansal–Meka 1810.03374; Ezra–Lovett; Hoberg–Rothvoss), the
  multicolor `√(d/k)` is a routine small-ball extension. ⇒ option (c) (offline-headlined) NOT viable; the offline floor
  is a cited stepping-stone. **TRUE novelty = the ONLINE side:** the matching ONLINE upper for the `√(d/k)` regime
  (online catching DOWN to offline — deep, since A-T showed online ≫ offline at k=2), the `F_online` small-k term, the
  d-independence-breaking framing. Folklore status SHARPENS (not kills) (a)/(b).
- **2026-06-22** — **ROUND 2 (GPT-5.5-Pro) — contribution-altering, audit-verified.** Reply `rounds/round2_response.md`;
  THREE blind audits + numerics `rounds/round2_audit.md` (`code/verify_round2.py`). Banked: **P7** (offline `√(d/k)`
  floor, Audit A 93%), **P8** (aggregate cover lemma, Audit B 97%), **N5** (clean forms refuted), **N6** (monotonicity
  refuted; exact `11/9,13/9,1`). The clean FAST/CASCADE forms are REFUTED; corrected = `Θ(max{1,F_online(k),√(d/k)})`.
  Max-cylinder shown UNNECESSARY (P8). Classification **MAJOR PROGRESS + scope change, NOT a kill** → **HUMAN GATE (c)**
  fired. Binding open = matching ONLINE upper for the `√(d/k)` regime. Health-check `docs/HEALTH_CHECK_gate_c.md`.
- **2026-06-22** — **Solver-exchange archive established** at `rounds/` (index `rounds/README.md`), mirroring the
  `dynamic-weighted-mis-fat-objects` mode (owner request). Convention: per round `n`, `round{n}_brief.md` (sent) /
  `round{n}_response.md` (verbatim reply §1 + faithful restatement §2 + audit points + disposition §3) /
  `round{n}_audit.md` (fresh-context adversarial verdict + FATAL/GAP/MINOR + OUTCOME; claimed-closure ⇒ 3 blind
  audits). Round-1 slots seeded (brief ready; response/audit pending). All briefs/replies/audits filed here verbatim
  — re-read from here + this ledger, never from memory.
