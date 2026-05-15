# 8001 VABS Visual History Security And Privacy

Created: 2026-05-15

## Banned From History URLs And Payloads

- raw tokens
- SIDs
- signatures
- passwords
- wallet secrets
- private URLs
- private hostnames
- raw donor URLs
- emails or unnecessary personal data

## Allowed Identifiers

- `gameId`
- `gameKey`
- `roundId`
- `gameSessionId`
- `playerSessionId` only if current GS/backoffice requires it
- `mathProfileId`
- wallet/accounting reference ids without secrets

## Display Parameters

- `lang` controls localization.
- `timeZone` controls date/time presentation.
- `hideClose` controls visual close-button visibility for embedded backoffice views.
- `wholeSession` controls session replay scope.

## Render Safety

Visual HTML/render routes must not leak stack traces or private storage paths. The render
wrapper should load only server-approved deterministic replay payloads and approved game
assets. Screenshot or binary storage is not required unless future GS/backoffice evidence
proves it.

## Error Safety

Error responses must be typed and must not echo unsafe request headers, tokens, private
URLs, wallet endpoint data, or raw signatures.
