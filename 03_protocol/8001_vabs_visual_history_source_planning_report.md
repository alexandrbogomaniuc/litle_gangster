# 8001 VABS/VBA/Lasthands Visual History Source Planning Report

Created: 2026-05-15

## Scope

This sprint planned Little Gangster 8001 visual history routes only. No Staging source,
backend adapter, lifecycle wrapper, client, registration, DB, wallet, donor, asset, or
release changes were made.

## Current Source Findings

- `new-games-server/src/index.ts` already has `/slot/v1/gethistory` and legacy
  `/v1/readhistory` JSON-style history endpoints.
- `new-games-server/src/index.ts` has an in-memory `historyBySession` cache, `rounds`
  cache, and `gsHistoryRead` / `gsHistoryWrite` bridge functions for local/internal
  history testing.
- Little Gangster now has lifecycle wrapper source under
  `new-games-server/src/games/little-gangster/lifecycle/`.
- Little Gangster has history payload placeholders through `historyMapper.ts`,
  `presentationPayload.ts`, and adapter/lifecycle output.
- `Gamesv1/packages/core-protocol` supports `gethistory` and requires a history payload
  for the canonical JSON runtime envelope.
- `Gamesv1/packages/ui-kit` exposes a History HUD button, but no 8001-specific visual
  history route integration exists.
- Existing legacy/current GS evidence shows VBA/VABS/Lasthands concepts exist as
  separate history/backoffice concerns. Stored JSON alone is not proven enough for
  release.

## Route Shape Decision

Recommended source shape:

- implement route helpers under `new-games-server/src/games/little-gangster/history/`;
- register guarded gameId 8001 routes in `new-games-server/src/index.ts`;
- keep existing `/slot/v1/gethistory` as the generic in-game list/read endpoint;
- add 8001-specific JSON replay and visual/render routes.

Recommended routes:

- `POST /slot/v1/8001/history/round/:roundId`
- `POST /slot/v1/8001/history/session/:gameSessionId`
- `POST /slot/v1/8001/history/session/:gameSessionId?wholeSession=true`
- `GET /slot/v1/8001/history/render/round/:roundId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId?wholeSession=true`

## Response Shape Decision

Both JSON replay and visual HTML/render responses are required unless current GS and
backoffice evidence later proves JSON-only replay is acceptable.

The JSON replay response should include deterministic replay fields, lifecycle state,
math profile identity, wallet/accounting references, round/session grouping, and
visual replay URL references. The visual response should render or wrap a visual replay
surface suitable for in-game History and Casino Manager/backoffice access.

## Data Source Decision

The route should read from:

- lifecycle wrapper state persistence and reconnect payloads;
- backend adapter `historyReplay` and `vabsFields`;
- `actionAccounting.walletAccountingRefs`;
- existing `gsHistoryRead` bridge when available;
- future durable history storage once selected.

Current in-memory `historyBySession` / `rounds` cache is acceptable for local smoke tests
only and is not a release storage source.

## Security And Privacy

History routes must not store or expose raw tokens, SIDs, signatures, private URLs,
wallet URLs, emails, or secrets. Public/render URLs should use opaque server-side
authorization and should carry only round/session references plus `lang`, `timeZone`,
`wholeSession`, and `hideClose` display controls where needed.

## Workflow Rule For Future Games

Future games must implement or explicitly block visual history/VBA/VABS/Lasthands routes
before release. Stored JSON alone is insufficient unless current GS/backoffice evidence
proves JSON-only replay is accepted.
