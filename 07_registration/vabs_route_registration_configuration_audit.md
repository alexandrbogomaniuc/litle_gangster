# VABS Route Registration Configuration Audit

Generated: 2026-05-15

## Summary

Registration/configuration is required for visual history route discovery, but the exact
GameServerRegistrar field path is blocked.

The current registration field shape is unproven.

## Proven Configuration Evidence

- PROVEN_SOURCE: bootstrap contract exposes `historyPolicy.gameHistoryUrl`.
- PROVEN_SOURCE: bootstrap source keys include `ENABLE_IN_GAME_HISTORY`,
  `GAME_HISTORY_URL`, and `OPEN_GAME_HISTORY_IN_SAME_WINDOW`.
- PROVEN_SOURCE: legacy start-game passes `GAME_HISTORY_URL` when in-game history is
  enabled.
- LIKELY_SOURCE: legacy bank/game settings can provide a history action URL or history
  route that is passed to the client.

## Not Proven

- NOT_FOUND: release-registration schema evidence for `vabsUrl`.
- NOT_FOUND: release-registration schema evidence for `vbaUrl`.
- NOT_FOUND: release-registration schema evidence for `historyBaseUrl`.
- NOT_FOUND: release-registration schema evidence for `gameHistoryUrl`.
- NOT_FOUND: a proven 8001 registration field mapping for visual render route, CM access,
  or legacy `/vabs/show.jsp` compatibility.

## Required Before Generation

GameServerRegistrar generation remains blocked until one of these is proven:

1. a registration field or template field that carries the 8001 visual history URL;
2. a documented mapping from registration output to bootstrap `historyPolicy.gameHistoryUrl`;
3. a legacy-compatible GS route resolver that does not require per-game registration
   fields, plus tests proving CM/backoffice and in-game History behavior.

## Current Decision

`registration_config_required = true`

The field shape is blocked. Do not generate registration artifacts for 8001 visual
history until this is resolved.
