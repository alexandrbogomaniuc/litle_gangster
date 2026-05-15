# 8001 VABS Visual History Route Test Plan

Created: 2026-05-15

## Route Tests

- JSON round replay returns one round by `roundId`.
- JSON session replay returns paginated session records by `gameSessionId`.
- JSON whole-session replay returns or pages the whole session.
- Visual round render returns HTML/render wrapper or an explicit blocked response.
- Visual session render returns HTML/render wrapper or an explicit blocked response.
- Visual whole-session render returns HTML/render wrapper or an explicit blocked response.

## In-Game History Button Tests

- History button can request history list.
- Selecting a round opens JSON replay or visual render according to the client contract.
- Missing round shows a safe not-found message.
- Incomplete history shows a blocked/missing-history message.

## Casino Manager / Backoffice Tests

- Backoffice can open round replay.
- Backoffice can open session replay.
- Backoffice can open whole-session replay.
- `hideClose`, `lang`, and `timeZone` parameters are honored.
- Backoffice route does not require or expose raw tokens.

## Replay Data Tests

- `mathProfileId` is present.
- RTP level and volatility level are present.
- `declaredBfRtpTarget` is present.
- `bonusBuyCostMultiplier` is present for bonus-buy rounds.
- `actionSequence` is present.
- `cascadeSequence` is present.
- lifecycle state persistence is present.
- wallet/accounting references are present.
- deterministic replay refs are present.

## Security Tests

- raw tokens are not persisted.
- raw signatures are not persisted.
- private URLs are not exposed.
- wallet secrets are not exposed.
- not-found and blocked responses do not leak stack traces.

## Evidence Media Policy Tests

- default `historyEvidenceMode` is `deterministic_replay_only`.
- visual route remains required when media capture is disabled.
- screenshot refs are empty or absent when screenshot mode is disabled.
- video refs are empty or absent when video mode is disabled.
- media manifest includes checksums and retention expiry when media is enabled.
- full-video mode is blocked without explicit product/operator/release setting.
- durable media storage unavailable returns a blocked response rather than fake refs.
