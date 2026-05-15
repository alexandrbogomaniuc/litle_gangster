# 8001 VABS Alias Registration Config Audit

Date: 2026-05-15

## Summary

Registration/configuration is required or must be proven unnecessary for BO/CM visual
history route discovery. The exact 8001 registration field remains blocked.

Current status: `blocked_exact_field_shape_unproven`.

## Config Evidence

- PROVEN_SOURCE: `BankInfo` defines `ENABLE_IN_GAME_HISTORY`.
- PROVEN_SOURCE: `BankInfo` defines `GAME_HISTORY_URL`.
- PROVEN_SOURCE: `BankInfo` defines `OPEN_GAME_HISTORY_IN_SAME_WINDOW`.
- PROVEN_SOURCE: start-game flow passes the resolved game history URL into launch.
- PROVEN_SOURCE: Gamesv1 bootstrap contract exposes `historyPolicy.gameHistoryUrl`.
- LIKELY_SOURCE: the configured game history URL can point to either a legacy alias or
  a canonical 8001 history route, depending on BO/CM acceptance.

## Required Or Unproven Fields

| Field Concept | Status |
| --- | --- |
| VABS base URL | BLOCKED, exact field name not proven |
| VBA base URL | BLOCKED, exact field name not proven |
| history URL | REQUIRED as concept; `GAME_HISTORY_URL` / `historyPolicy.gameHistoryUrl` are proven, registration field shape is blocked |
| client history route | REQUIRED as bootstrap/backend-generated URL, not hardcoded |
| BO/CM route field | BLOCKED, exact field name not proven |

## Generation Impact

GameServerRegistrar generation remains blocked. Do not generate registration artifacts
until one of these is proven:

1. `GAME_HISTORY_URL` or equivalent registration/config can safely carry the 8001 visual
   alias/canonical URL;
2. GS/CM automatically generates the visual URL without per-game route config;
3. BO/CM tests prove canonical 8001 routes are accepted without a legacy alias.

## No-Generation Assertion

No registration artifact was generated in this sprint.
