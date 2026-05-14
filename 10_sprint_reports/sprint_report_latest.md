# Sprint Report - MathProfileCalibrator RTP Range Update

Created: 2026-05-14

## Outcome

Reusable future-game RTP request range updated.

## Rule

- Allowed RTP range: 91.00% to 99.70%, inclusive
- RTP labels: LOW / MEDIUM / HIGH
- RTP ordering: LOW < MEDIUM < HIGH
- Decimal values allowed: true
- Operators choose approved pretested profiles only: true

## Validation

- Valid 91.00 / 96.00 / 99.70: passed
- Valid 93.24 / 96.32 / 99.30: passed
- Valid 92.50 / 95.75 / 98.90: passed
- Invalid 90.99 / 96.00 / 99.70: rejected with `below_minimum_allowed_rtp`
- Invalid 91.00 / 96.00 / 99.71: rejected with `above_maximum_allowed_rtp`
- Non-ascending 95.00 / 94.00 / 98.00: rejected with `rtp_levels_not_strictly_ascending`
- Duplicate 94.00 / 94.00 / 98.00: rejected with `duplicate_rtp_levels`

## Gates

- Little Gangster RTP values changed: false
- No simulations run: true
- Backend adapter implementation allowed: false
- GameClientBuilder implementation allowed: false
- GameServerRegistrar generation allowed: false
- Release approved: false

## Next Prompt

Use MathProfileCalibrator with the corrected 91.00%-99.70% range for the next future-game RTP/volatility calibration request, or run a raw-safe checkpoint after review.
