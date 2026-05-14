# Calibration Report Requirements

Every MathProfileCalibrator report must preserve profile identity and gate
status.

## Required Summary Fields

- profiles calibrated yes/no
- train gate status
- validation gate status
- profiles within tolerance
- profiles outside tolerance
- scale mode
- train seeds used yes/no
- validation seeds used yes/no
- validation seeds used for tuning yes/no
- bonus-buy status
- tail/max-win status
- exact values final yes/no
- certification status yes/no
- backend adapter allowed yes/no
- registration generation allowed yes/no

## Required Per-Profile Fields

- `mathProfileId`
- `rtpLevel`
- `volatilityLevel`
- `targetRtpPercent`
- `observedRtpPercent`
- `deltaFromTarget`
- `passFailAgainstTolerance`
- `hitRate`
- `standardDeviation`
- `capFrequency`
- `winTierDistribution`
- `blockerNotes`

## Required Language

Use `outside_tolerance`, `outside_smoke_tolerance`, or
`inconclusive_due_variance` as appropriate. Do not call a profile truly failed
unless the sample size and confidence interval justify that statement.

