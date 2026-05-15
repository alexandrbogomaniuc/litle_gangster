# 8001 VABS Alias Compatibility Test Plan

Date: 2026-05-15

## Required Tests Before BO/CM Compatibility Claim

| Test | Expected Result |
| --- | --- |
| Legacy alias session render | Alias accepts `VIEWSESSID`, `GAMEID`, `LANG`, `TIMEZONE`, and `hideClose` and returns visual HTML or safe redirect. |
| Legacy alias round render | Alias accepts round id when supported and returns visual HTML or safe redirect. |
| Canonical new-games session render | `/slot/v1/8001/history/render/session/:gameSessionId` returns safe visual HTML. |
| Canonical new-games round render | `/slot/v1/8001/history/render/round/:roundId` returns safe visual HTML. |
| hideClose parameter | Boolean hide-close behavior is preserved or safely defaulted. |
| lang parameter | Language input is sanitized and propagated. |
| timeZone parameter | Timezone input is sanitized and propagated. |
| missing VIEWSESSID | Safe blocked/not-found response with no internal leakage. |
| wrong GAMEID | Safe blocked/not-found response; no cross-game replay. |
| no raw token leakage | Render and JSON outputs contain no raw tokens, signatures, private hosts, emails, passwords, or secrets. |
| BO/CM iframe or redirect compatibility | BO/CM can open the visual route in the expected frame/window or receives a safe blocked response. |
| In-game History button | Client opens bootstrap/backend-generated route, not a hardcoded private host. |
| Durable storage missing | Missing durable replay data returns safe blocked/not-found response. |

## Current Status

Not run. Alias implementation is not approved and does not exist yet.

## Release Gate

Release remains blocked until alias/canonical visual tests pass or BO/CM/product
explicitly accepts a documented blocker.
