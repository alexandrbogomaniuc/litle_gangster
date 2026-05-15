# RTP / Volatility Profile Matrix

Every future game must define exactly three RTP levels:

- LOW
- MEDIUM
- HIGH

Every future game must define exactly three volatility levels:

- LOW
- MEDIUM
- HIGH

The required matrix is 3x3, for nine pretested profiles. Operators select from approved profiles only; arbitrary RTP percentages or volatility values
  are blocked.

## RTP Range

- Minimum allowed RTP: 92.00%.
- Maximum allowed RTP: 99.00%.
- Values outside this range require explicit product and regulatory approval.
- Store RTP as both percent and return multiplier.

## Required Profile Fields

- `mathProfileId`
- `rtpLevel`
- `targetRtpPercent`
- `targetReturnMultiplier`
- `volatilityLevel`
- `volatilityIndexTarget`
- `modelVersion`
- `mathVersion`
- `ruleSetVersion`
- `registrationModelCode`
- `runtimeProfileCode`
- `historyProfileCode`

## Workflow Rules

- Do not hardcode reusable models as `rtp_92`, `rtp_94`, or `rtp_96`; those are game-specific legacy IDs.
- Pretest all nine profiles before release.
- Report RTP with and without bonus-buy separately.
- Store profile identity in runtime result and VABS/history replay payloads.
- Registration records metadata only and must not import executable math.
