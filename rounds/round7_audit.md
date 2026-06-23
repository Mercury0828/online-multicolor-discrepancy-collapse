# Round-7 audit — independent adversarial verifier(s) on `round7_response.md` (PENDING)

> **Status: NOT STARTED** (depends on `round7_response.md`). Convention (`rounds/README.md`): a claimed CLOSURE of PF (or a
> fully-matched online lower bound) → 3 blind audits. The mixed-profile transport estimate handling OVERLAP (the profile-DAG
> folding / preserving Ω(F_k(m)) leaves), all-prefixes/whp/adaptive-uniform, and any online lower (vs EVERY online algorithm)
> are the hardest points — audit them adversarially; check it does NOT covertly re-use the dead symmetric route (B4). Classify
> FATAL/GAP/MINOR; end with OUTCOME.

## Auditor verdict (one focused audit; verdict = refutation-of-PF, not a closure). **All 3 claims CORRECT (93%).**
- **CLAIM 1 (phase conveyor): CORRECT** — auditor SIMULATED LeftGap for `k=3,4,5,6`: the lex `(h_c,c)` rule selects colors
  `1,…,k` per cycle as claimed; the gap/min-tracking invariant holds with equality at every cycle boundary; the max principal
  phase advances by exactly `k` per cycle ⇒ phases `1..q` born with `O(kq)` rows (**linear in q**, defeating Fibonacci growth);
  exactly-`k`-sparse respected. (Row-count bound `k+1+(k−2)q` is a valid upper bound; conclusion unaffected.)
- **CLAIM 2 (refutes the displayed PF): CORRECT** — `E Z_u ≥ C(n,k)^{−⌈u⌉}`; in the regime `k=⌊H²/(2log H)⌋` (`k≫H, λ=Θ(1),
  Ψ=Θ(log H/loglog H)`): `log(1/EZ) ≤ qk log(en/k) = (log n)·H^{O(1)}`, while `F_k(m)=2^{m−2}=(log n)^{a ln2+o(1)}` at `m=aH`.
  **Decisive cross-check:** PF's own route to RB *requires* its window to reach `m=C_1H, C_1>1/ln2` — exactly where the conveyor
  bites ⇒ the untruncated PF is genuinely false for LeftGap.
- **CLAIM 3 (NOT a lower bound; RB still open; `PF_tr` is the corrected target): CORRECT** — conveyor prob
  `exp(−log n·H^{O(1)}) ≪ n^{−A}` ∀A; killing `E Z` (a first-moment tail) does not contradict a whp `Pr(Z>0)` bound (standard
  expectation-vs-whp gap). It legitimately refutes the quenched factorization (a flawed route to PF), but NOT RB. **RB neither
  proved nor refuted; growing-k order stays `max{Ψ, H/k} ≲ ondisc_k ≲ H`.** `PF_tr` (`+n^{−A}`) still ⇒ RB.
- −7%: definitions taken from the brief; `H` log-convention assumed standard (constants only).

## Classification — VERIFIED. RB OPEN; the displayed PF is DEAD.
- **Banked B5** (phase-conveyor refutation of PF + the quenched-factorization obstruction). RB neither proved nor refuted;
  the corrected open target = the truncated `PF_tr` via a fold-or-Fibonacci incidence-excess lemma. The two complete results
  (P11, P12) + the bracket are untouched.
- **No FATAL** (nothing proven dead; the project's results stand). The growing-k regime is open with a sharply-mapped frontier
  (symmetric route B4 dead; naive-expectation/quenched route B5 dead; `PF_tr`/fold-or-Fibonacci the remaining route).

## OUTCOME (what the orchestrator did)
1. Banked B5 (ledger). Growing-k stays open, open-problem section now precisely specified.
2. **PIVOT TO WRITING** — per the owner's pre-committed plan ("one PF round, then write") + the milestone health-check. The one
   authorized PF round did not close ⇒ NO further RB/PF rounds. The writable paper (P11 + P12 + separation + bracket + the mapped
   open problem) stands; the binding venue risk is **human verification of P11/P12/P13**, which now becomes the focus alongside writing.
3. Reported the transition to the owner + laid out the writing plan + the human-verification checklist.
