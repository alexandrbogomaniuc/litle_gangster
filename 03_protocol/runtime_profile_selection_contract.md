# Runtime Profile Selection Contract

Created: 2026-05-13T08:55:01Z

The runtime result must carry the selected profile identity. The backend receives or resolves `mathProfileId`; the client/browser must not choose or mutate it.

## Runtime Fields

- `mathProfileId`
- `rtpLevel`
- `targetRtpPercent`
- `targetReturnMultiplier`
- `volatilityLevel`
- `volatilityIndexTarget`
- `modelVersion`
- `mathVersion`
- `ruleSetVersion`
- `runtimeProfileCode`

## Presentation Payload

`presentationPayload.gamePayload.payload` may include profile identity for rendering, history, and debug display only. It is not browser authority. `browser_result_authority_allowed` remains false.
