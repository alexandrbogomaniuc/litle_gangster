# VABS / History Math Profile Fields

Created: 2026-05-13T08:55:01Z

Every replay/history record must include profile identity so VABS/Lasthands can replay the correct math model.

## Required Fields

- `mathProfileId`
- `rtpLevel`
- `targetRtpPercent`
- `targetReturnMultiplier`
- `volatilityLevel`
- `volatilityIndexTarget`
- `modelVersion`
- `mathVersion`
- `ruleSetVersion`
- operator/casino selected profile reference, if available
- profile effective timestamp, if available
- round id, session id, spin id
- deterministic replay payload

Do not store raw RNG secrets, wallet secrets, or executable math in history. Store audit references and deterministic replay payloads.
