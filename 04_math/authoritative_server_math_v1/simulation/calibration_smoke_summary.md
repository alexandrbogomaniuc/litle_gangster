# Calibration Smoke Summary

Status: completed as non-production smoke calibration.

This sprint ran the existing deterministic simulator once per RTP model with 75 rounds each.
The output is useful for harness health and blocker identification only; it is not certification-grade RTP evidence.

## Smoke Results

| Model | Seed | Rounds | Observed return multiplier | Target RTP | Status | Win tiers |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `rtp_96` | 800196 | 75 | 0.132 | 96.0 | smoke_not_calibrated | none:56, small:19 |
| `rtp_94` | 800194 | 75 | 0.349547 | 94.0 | smoke_not_calibrated | big:1, none:61, small:13 |
| `rtp_92` | 800192 | 75 | 0.1044 | 92.0 | smoke_not_calibrated | none:57, small:18 |

## Calibration Finding

- The simulator runs for `rtp_96`, `rtp_94`, and `rtp_92`.
- The outputs are structurally plausible smoke results: wins, tiers, contribution buckets, and cap states are emitted.
- The outputs are not RTP-plausible calibration results yet because tiny 75-round observed returns are not near target RTP.
- Exact values remain non-final and uncertified.

## Bonus Buy / Free Spins / Jackpot

- Bonus-buy EV remains blocked: the current simulator records the flag but does not model purchased feature EV.
- Free-spin and feature-mode configs exist, but exact trigger, retrigger, and mode probability values remain provisional.
- Jackpot remains disabled by default; hooks are present only for future product decision.

## Gate Impact

- Backend adapter implementation remains blocked.
- GameServerRegistrar generation remains blocked.
- Next required sprint: MathModelDesigner calibration continuation focused on implementable simulation rules for bonus-buy, free spins, and RTP tuning, or product/math decision sprint if final values must be supplied first.
