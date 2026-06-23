# Second-Opinion Audit — Literature Kill-Scan (independent, fresh-context)

> Date: 2026-06-22. Auditor: independent fresh-context subagent (general-purpose), blind to the orchestrator's
> reasoning beyond the claimed-novelty statement + the list of already-checked papers. Adversarial brief:
> "try to BREAK the GREEN verdict by finding a scoop." Verbatim deliverable archived below.

---

## VERDICT: AGREE-GREEN (with one residual YELLOW footnote — not a downgrade). Confidence 82% no-scoop.

### (b) Most threatening item — and why it is NOT a scoop
The genuine threat is **not a discrepancy paper** but the **multiple-choice balls-into-bins / d-choice**
literature (Azar–Broder–Karlin–Upfal; Berenbrink–Czumaj–Steger–Vöcking heavily-loaded): online d-choice max
load `= m/n + loglog m / log d ± O(1)`. This is the ONE result whose functional form structurally matches the
conjectured **cascade** `Θ(loglog n / log k)` — same `loglog / log(branching)` skeleton. NOT a scoop because:
(i) different model (balls-into-bins picks among k *random* bins on a single coordinate; ours = fixed exactly-
d-sparse i.i.d. binary vectors irrevocably assigned to one of k colors, discrepancy = max-over-prefixes,
max-over-coordinates pairwise color-load **range**); (ii) no matching lower bound ties balls-and-bins to our
quantity; (iii) the "decreasing-in-k, collapse-to-1, anchored at A-T's Θ(loglog n) at k=2" packaging is absent.
**Resemblance = related-work to cite + a sanity check on the cascade form, NOT prior art proving the theorem.**

Closest actual discrepancy paper: HPVX 2502.14624 (general unit vectors, `Θ(√log T)`, `O(log k)` multicolor
factor via binary tree — NOT sparse, NOT the loglog-collapse regime). Bansal 2007.10622 (generic poly, no
k-collapse) and Manurangsi–Meka 2504.18489 (offline `Ω(√n)`, the contrast) confirmed non-scoops.

### (c) Search angle that worried the auditor — ACTIONABLE
🟡 The **balls-into-bins `loglog/log d` form**: a referee could claim the cascade UPPER bound is *folklore*.
**Mitigation (carry to writing):** (1) state the model separation explicitly; (2) check whether our cascade
upper is in fact a balls-and-bins-style argument — **if so, the novelty rests on the matching LOWER bound +
the k=2↔A-T anchoring, which must be foregrounded.** Second mild worry: 2026 preprints thinly indexed;
2602.09948 (offline non-additive coverage Beck–Fiala, has k & t) is the closest 2026 "k-in-a-Beck–Fiala-bound"
item — adjacent, not a scoop; worth a one-line cite.

### Foundational fact check (A-T anchor) — CONFIRMED, one self-consistency caveat
arXiv:2509.02432 v3: 2-color (±1), i.i.d. uniform exactly-d-sparse binary, `2 ≤ d ≤ (loglog n)²/logloglog n`,
optimal online discrepancy `Θ(loglog n)`, d-independent, matching Ω/O; independence ceases at `d=ω((loglog n)²)`.
🟡 CAVEAT: could not machine-confirm that A-T's quantity is **max-over-PREFIXES AND max-over-coordinates** exactly
as we restate it (abstract says "online discrepancy of partial sums" — consistent with prefix). Almost certainly
fine (online vector balancing disc is conventionally sup-over-prefixes ℓ∞), but **verify Thm 1.1 / the disc
definition in the PDF directly** since the k=2 reduction (P1/P2) depends on the quantifier matching.

### (d) Confidence: 82% NO scoop (cascade or fast) as of June 2026. Residual 18% = balls-and-bins novelty-framing
risk to the cascade upper + thin indexing of brand-new 2026 / non-arXiv SODA/FOCS-2026 submissions. STOC 2026
accepted list checked: no multicolor-threshold paper.

Key IDs: 2509.02432, 2502.14624, 2007.10622, 2504.18489, 2102.02765, 2602.09948; balls-into-bins (ABKU + BCSV,
classic STOC/SICOMP, no single arXiv).

---

## Orchestrator's disposition of the two YELLOW flags
1. **Balls-into-bins cascade-folklore risk** → recorded as a **writing-time positioning mandate** + an **attack-
   loop note**: if `HS-upper` turns out to be a balls-and-bins-style argument, novelty must be foregrounded on
   `HS-lower` (the matching lower) + the A-T anchoring. Added to `PROJECT_STATE.md` risk notes & the brief's
   "what we need back". Does NOT change the GREEN verdict (it is a framing risk, not a scoop).
2. **A-T prefix/coordinate quantifier self-check** → resolved by a direct full-text check (see `lit/SCAN_REPORT.md`
   addendum / below). Load-bearing for P1/P2.
