# Paper-Orientation Health-Check — Human Gate (c), post-Round-2 (independent subagent)

> Date 2026-06-22. Independent fresh-context reviewer, blind to the orchestrator. Verbatim conclusions +
> orchestrator disposition. (Guide §Workflow: every gate runs one.) Triggered by the Round-2 contribution reshaping.

## Bottom line
**Net GOOD news, but it changes WHICH paper you write.** The clean phase-transition headline is dead; a richer
**d-dependent** characterization replaces it, SODA-worthy **only if the matching online upper closes** — that one
bound is now the whole paper's risk. **The biggest latent threat is novelty of the offline floor (P7):** if `√(d/k)`
is folklore random-matrix discrepancy, the offline "richness" is borrowed and the paper's true delta shrinks to the
ONLINE-specific content (the matching online upper + the `F_online` term) — which is the right place for it anyway.

## ① On track? GOOD for correctness/novelty, BAD for the marketing arc.
- GOOD: `Θ(max{1, F_online(k), √(d/k)})` is a legitimate richer object; **breaking A-T's d-independence for k>2 is a
  genuinely novel, quotable phenomenon** (A-T: "d-independent at k=2" → "but d-DEPENDENT for k≥3, here's exactly how").
  N6 (non-monotonicity, exact `11/9<13/9`) strengthens the "subtle" framing.
- BAD: the "online average-case is DIFFERENT / more colors HELP" headline is **materially weakened** — across the
  middle regime `log L ≲ k ≲ d` the online answer **IS the offline floor** (you inherit it, not beat it). The
  online-specific phenomenon survives only in the small-k corner `k≲log L` and at the collapse boundary. The single
  sharp threshold becomes a two-regime, d-parametrized story (more correct, less marketable).
- Whether this is "offline floor + small correction" or a real online result **hinges on whether the middle-regime
  online upper is nontrivial to achieve online** — UNKNOWN yet; that is now the project's center of gravity.

## ② Strongest submittable theorem + the d-restriction arithmetic.
- **d=O(1) (bounded): floor DEAD, clean `Θ(max{1,F_online(k)})` fully recovered** (the safe haven). **d=L^{2−ε} does
  NOT kill the floor** (`√(d/k)` at `k=log L` is `L^{1−ε/2}/√(log L)→∞`). So the clean form is only recovered for
  `d` essentially bounded.
- Three papers: **(a)** full `Θ(max{1,F_online,√(d/k)})` with matching online upper — richest, best if it closes, but
  3 open pieces (offline O(√(d/k)) upper; its online achievability in `log L≲k≲d`; the `F_online` form + HS-lower);
  the online middle-regime upper is the binding un-derisked piece. **(b)** restricted `d=O(1)` clean theorem — cleanest,
  lowest-risk, fully matching (just `F_online`: fast HS-alt+P2, or cascade+HS-lower); a deliberate sub-case of (a).
  **(c)** offline `√(d/k)` + small-k online — WEAKEST (foregrounds the folklore-risk offline part); = the ESA downgrade.
- **Recommended: target (a) as ambition, guarantee (b) as committed floor. Prove (b) first (fast-first), bank it,
  then attack the middle-regime online upper to upgrade to (a).** Do NOT let (a)'s open upper hostage the submission.

## ③ Drift / scope.
- **Restricting d is NOT a retreat IF framed as isolating the online mechanism** (keep the full regime map in the
  paper; prove (b) cleanly; name the middle-regime online upper as the open problem). A bare "assume d=O(1)" with no
  acknowledgment of the floor WOULD be a retreat.
- **d-dependence is surprisingly MORE in A-T's spirit** (their signature = d-independence at k=2; showing it breaks at
  k≥3 via a concrete mechanism is a direct in-conversation extension) — a framing asset.
- 🔴 **FOLKLORE RISK on P7 is the real danger.** A `√(d/k)` small-ball/first-moment multicolor offline disc LB is
  "exactly the kind of result plausibly known/near-folklore" (random-matrix discrepancy; Ezra–Lovett / Hoberg–Rothvoss
  sparse; the offline multicolor LBs already in our scan 2502.10516, 2504.18489). **Run a targeted P7-scoop-scan NOW.**
  If folklore: paper (c) collapses and (a)'s richness is partly borrowed — BUT **(a)/(b) novelty SURVIVES** (the delta
  was never the floor; it's the ONLINE achievability + `F_online`). Folklore actually sharpens the contribution.

## ④ Recommendation for the gate.
- **Scope: (a) ambition + (b) committed floor.** Sequence (b)→(a). SODA still correct **conditionally**: a matching
  upper (even just regime (b)) = SODA; **lower-bounds-only (P7+P2+fresh-color) = downgrade venue** (the ESA/RANDOM rail).
- **Two cheap, decisive pre-checks before committing solver rounds:** (P7-scoop) is `√(d/k)` offline folklore?
  (offline-upper sanity) does the offline `O(√(d/k))` UPPER even exist? If even the offline upper is hard/false, fall
  back to (b) immediately.
- **Headline rewrite:** drop "more colors help, collapse to 1." Adopt **"A-T's d-independence is special to k=2: for
  k≥3 the online multicolor prefix discrepancy carries a d-dependent `√(d/k)` floor; we give a matching
  `Θ(max{1, F_online(k), √(d/k)})` [over d=O(1) / the full range]."**
- Deadline 2026-07-09 vs three open pieces for (a) is tight; (b) alone is a legitimate SODA submission.

## Orchestrator disposition
1. **Run the P7-folklore scoop-scan immediately** (orchestrator remit; results in `lit/SCAN_P7_offline_floor.md`) — fold
   into the gate so the owner decides with the novelty question resolved.
2. **Fire human gate (c)** with the three scope options + the (a)-ambition/(b)-floor recommendation + the conditional-
   SODA rule (matching upper = SODA; lower-only = downgrade). Agent does NOT pick scope.
3. Adopt the headline rewrite + the fast-first sequencing re-pointed at the new regime map (pending owner scope choice).
