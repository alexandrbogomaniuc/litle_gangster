# MathModelDesigner Calibration Fast Lane

Use this sequence before tuning math for any future game.

## 1. Denominator And Unit Sanity

- Confirm target RTP unit, for example `96.0` percent versus `0.96` return multiplier.
- Confirm observed return formula.
- Confirm total bet denominator and game-specific bet model.
- For cluster games, do not silently apply a fixed-line formula.
- Fail loudly if denominator fields are missing.

## 2. Base-Game Contribution Sanity

- Run deterministic base-game smoke tests first.
- Report base bet total, base win total, cluster-hit frequency, no-win frequency, and observed base return.
- Do not tune features until the base contribution is visible.

## 3. Cascade Contribution Sanity

- Report cascade count, refill count, cluster count after cascades, and cascade win contribution.
- Confirm cap handling does not hide runaway cascade wins.

## 4. Feature And Free-Spin Contribution Sanity

- Use configured trigger probabilities, mode weights, and spin counts.
- Report trigger count, feature spin count, feature wins, and feature contribution separately.
- Keep feature values provisional until multi-seed validation.

## 5. Bonus-Buy EV Sanity

- Report bonus-buy cost total and bonus-buy win total separately.
- Report bonus-buy observed return separately from base RTP.
- Do not invent final bonus-buy cost or EV. Mark unresolved cost/EV as a blocker.

## 6. Cap And Win-Tier Sanity

- Report max-win cap multiplier, cap hits, cap frequency, pre-cap win total, capped win total, and win-tier distribution.
- Do not claim max-win behavior until large simulations exercise the cap.

## 7. Limited Tuning

- Pick at most three tuning levers per fast-lane sprint.
- Apply at most one provisional tuning set before re-running diagnostics.
- Prefer real model levers such as paytable ranges, weights, trigger odds, spin counts, and feature EV.
- Do not use post-spin payout scaling as release math.

## 8. Multi-Seed Validation

- Run every RTP model with multiple deterministic seeds.
- Compare target RTP percent, target return multiplier, observed return multiplier, and observed RTP percent.
- Report RTP with and without bonus-buy separately.

## 9. Certification-Scale Validation

- Only after fast-lane smoke results are plausible, run larger simulations.
- Keep exact values non-final until certification-scale validation, volatility, cap, feature, and bonus-buy reports pass.
- Preserve GL/registration mapping and backend result-state ownership boundaries.
