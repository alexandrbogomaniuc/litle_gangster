# VabsVisualHistorySourcePlanning Skill Report

Created: 2026-05-15

## Sprint

ProtocolAndSchemaMapper VABS/VBA/Lasthands visual history route source planning for
Little Gangster 8001, plus reusable workflow guidance patching for future games.

## Result

Completed planning only. No Staging source was modified and no VABS route code was
created.

## Key Decisions

- Recommended route source location:
  `new-games-server/src/games/little-gangster/history/`.
- Recommended route host: guarded 8001 route registration in
  `new-games-server/src/index.ts`.
- JSON replay and visual HTML/render responses are both planned.
- In-game History button and Casino Manager/backoffice access are both planned.
- Stored JSON alone remains insufficient unless current GS/backoffice evidence proves
  JSON-only replay is acceptable.

## Reusable Workflow Patch

Patched reusable skill guidance:

- ProtocolAndSchemaMapper
- WalletAndLaunchTester
- GameClientBuilder
- RTPAndReleaseAuditor

## Safety Boundaries

- No Staging source modification.
- No VABS route implementation.
- No lifecycle wrapper changes.
- No backend adapter changes.
- No client code generation.
- No registration artifacts.
- No DB/Cassandra action.
- No wallet/API call.
- No donor browsing or asset capture.
- No release approval.
