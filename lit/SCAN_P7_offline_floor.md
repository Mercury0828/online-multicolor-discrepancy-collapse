# Targeted scoop-scan — is the offline `√(d/k)` floor (P7) folklore/known? (gate-c pre-check)

> Date 2026-06-22. Triggered by the gate-(c) health-check ("the real danger is P7's novelty"). Decides whether the
> offline floor can be a headline (it cannot if known) vs a cited stepping-stone. Does NOT affect (a)/(b) novelty.

## Findings
- **Offline 2-color (k=2) random d-regular/d-sparse set-system discrepancy = `Θ(√d)` is KNOWN:**
  - **Bansal–Meka, "On the discrepancy of random low degree set systems" (arXiv:1810.03374):** tight `Θ(√t)` for
    random t-regular set systems across the whole `n,m` range (t = degree = our d).
  - **Ezra–Lovett:** `O(√(t log t))` for `n≤m`, `O(1)` for `n≫m^t`.
  - **Hoberg–Rothvoss:** disc `≤1` whp for `n ≥ Θ(m² log m)` (Fourier-analytic).
  ⇒ the `k=2` offline floor `√d` is **established prior work** (and the small-ball/anti-concentration mechanism P7
  uses is exactly this literature's standard toolkit).
- **Multicolor average-case `√(d/k)` (k>2):** no explicit published statement found, BUT it is a **routine small-ball
  extension** of the known k=2 `√d` (per-color load `Bin(m/k, d/n)`, `Var=Θ(d/k)`, union over `k^T`). The published
  multicolor LBs are **worst-case set systems** (`Ω(√n)` 2504.18489, `Ω(√(n/ln k))` 2502.10516) — a DIFFERENT model
  (worst-case, not random d-sparse average-case), so not a direct scoop of P7, but they confirm the `√` multicolor
  scaling is unsurprising.

## Verdict (for the gate)
**P7's offline `√(d/k)` floor is KNOWN/near-folklore (the k=2 core is published; the multicolor extension is routine).**
⇒ **Option (c) (offline-headlined paper) is NOT viable** — the offline floor is a *cited stepping-stone*, not a
contribution. **The project's TRUE novelty is the ONLINE-specific content:**
1. 🔴 **The matching ONLINE upper for the `√(d/k)` regime — i.e. that online CATCHES DOWN to the offline floor.**
   This is deep and uncertain precisely because A-T showed online is MUCH WORSE than offline at k=2 (`Θ(loglog n)` vs
   `√d=o(loglog n)`). Whether the online value drops to the offline `√(d/k)` as k grows (vs staying strictly above) is
   exactly the open crux and the real contribution.
2. The `F_online(k)` online-specific term at small `k` (fast `L/k` vs cascade `L/log k`).
3. The **d-independence-breaking** phenomenon (A-T d-independent at k=2 → d-dependent for k≥3) — a quotable framing.
4. The sharp matching characterization + the relocated collapse threshold `K_1≍d`.

**Net:** the folklore status of the offline floor does NOT kill (a)/(b) — it **sharpens** the contribution onto the
online side, which is where the difficulty and novelty genuinely live. It DOES kill (c).
