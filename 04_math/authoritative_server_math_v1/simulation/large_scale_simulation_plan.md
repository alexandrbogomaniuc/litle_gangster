# Large-Scale Simulation Plan

Created: 2026-05-13T11:16:56+00:00

## Goal

Move from smoke evidence to confidence evidence without confusing sample variance for math truth.

## Sequence

1. Wiring smoke: 2k to 10k rounds per profile after any simulator or config change.
2. Diagnostic smoke: 10k to 50k rounds per profile for contribution direction only.
3. Calibration trend: 100k to 500k rounds per profile with train/validation seeds before tuning.
4. Calibration confidence: 1M to 5M rounds per profile after a candidate tuning set.
5. Pre-certification: 10M to 50M rounds per approved candidate profile.
6. Tail/max-win discovery: 100M to 1B rounds or a validated tail-focused method that does not fake RTP evidence.

## Little Gangster Next Step

Do not tune immediately from the 10k smoke variance. Next, plan a train/validation calibration run at the calibration-trend tier, then decide whether the overlay needs adjustment. Bonus-buy EV and max-win tail remain separate blockers.

## Required Outputs

- RTP with confidence intervals.
- Seed spread and train/validation comparison.
- Feature contribution report.
- Volatility hit-rate and standard-deviation bands.
- Cap/tail evidence or explicit tail blocker.
- Clear statement that exact values remain non-final until certification-scale validation.
