# Calibration Loop Policy

The calibration loop is train-only until the train gate passes.

## Default Loop Rules

- Default max iterations: 3.
- Use train seeds only.
- Never tune with validation seeds.
- Use profile-specific adjustment overlays.
- Do not use global post-spin payout scaling.
- Do not use runtime forced payout scaling.
- Stop if simulator or model reliability becomes questionable.
- Preserve volatility identity and ordering.

## Iteration Steps

1. Run train jobs or import train results.
2. Compare observed RTP against target RTP.
3. Classify every profile:
   - `within_tolerance`
   - `needs_upward_adjustment`
   - `needs_downward_adjustment`
   - `inconclusive_due_variance`
4. Update overlay entries only for profiles needing adjustment.
5. Write an iteration report.
6. Rerun train or stop at max iterations.

## Tolerances

- Fast gate: +/-2.0 percentage points.
- Stronger train gate: +/-1.0 percentage point.
- Tighter targets require larger train/validation or lab-scale evidence.

## Bonus Buy And Jackpot

Do not tune bonus-buy EV unless the bonus-buy model is complete, cost is
approved, purchase state is authoritative, and EV denominator is proven.

Do not tune jackpot contribution unless jackpot is enabled, modeled, and
approved for the current game.

