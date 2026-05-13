# Sprint Report - RTP Confidence Scale Correction

Created: 2026-05-13

## Outcome

Confidence-scale sprint completed. No simulations were run and no math values were tuned.

## Correction

The prior 10,000-round-per-seed 3x3 profile results are reclassified as `small_sample_profile_stability_inconclusive`. The correct wording is `profiles outside small-sample smoke tolerance`, not true RTP failures.

## Simulation Tiers

Defined tiers from wiring smoke through diagnostic smoke, calibration trend, calibration confidence, pre-certification, certification/lab scale, and tail/max-win discovery.

## Confidence Estimate Summary

- Worst-profile estimated rounds for +/-2.0 percentage points: 91,000 range.
- Worst-profile estimated rounds for +/-1.0 percentage point: 363,000 range.
- Worst-profile estimated rounds for +/-0.5 percentage point: 1.45M range.
- Worst-profile estimated rounds for +/-0.25 percentage point: 5.8M range.

These are normal-approximation estimates from smoke variance only. Tail, cap, bonus-buy, and jackpot behavior may require tens or hundreds of millions of rounds, or up to one billion rounds.

## Gates

- Small samples can approve RTP: false.
- Backend adapter remains blocked: true.
- Registration generation remains blocked: true.
- Release remains blocked: true.

## Next Prompt

Run a compact MathModelDesigner sprint to design larger train/validation simulation runs and confidence reporting before any tuning, backend adapter, or registration work.

