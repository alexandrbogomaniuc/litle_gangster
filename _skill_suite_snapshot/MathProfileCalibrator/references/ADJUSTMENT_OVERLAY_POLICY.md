# Adjustment Overlay Policy

Use overlay files for calibration changes. Do not mutate base symbol weights,
paytables, feature probabilities, jackpot rules, or bonus-buy rules unless a
later sprint explicitly scopes that work.

## Allowed Overlay Fields

- `mathProfileId`
- `rtpLevel`
- `volatilityLevel`
- `targetRtpPercent`
- `observedRtpPercentBefore`
- `observedRtpPercentAfter`
- `rtpDeltaBefore`
- `rtpDeltaAfter`
- `clusterPaytableMultiplierAdjustment`
- `featureTriggerAdjustment`
- `freeSpinValueAdjustment`
- `featureModeValueAdjustment`
- `highSymbolWeightAdjustment`
- `lowSymbolWeightAdjustment`
- `volatilityPreservationNotes`
- `status`

## Rules

- Change only profiles that need adjustment.
- Prefer small profile-specific changes.
- Do not apply a single global multiplier to all profiles.
- Do not use post-spin payout scaling.
- Keep volatility ordering visible in reports.
- Record unchanged profiles explicitly when doing targeted adjustments.
