# 8001 VABS Visual History Source Target Map

Created: 2026-05-15

## Recommended Source Location

`new-games-server/src/games/little-gangster/history/`

This should be a Little Gangster-specific route/helper module, not a generic runtime
rewrite.

## Recommended Route Host

`new-games-server/src/index.ts`

Reason: current Staging source already hosts `/slot/v1` routes, the existing
`/slot/v1/gethistory` endpoint, `gsHistoryRead`, `gsHistoryWrite`, local history cache,
and guarded gameId 8001 integration.

## Proven Targets

- `new-games-server/src/index.ts`: route registration and history bridge host.
- `new-games-server/src/games/little-gangster/lifecycle/`: lifecycle state,
  persistence, reconnect, accounting, and blocker source.
- `new-games-server/src/games/little-gangster/historyMapper.ts`: 8001 history replay
  and VABS field payload source.
- `Gamesv1/packages/core-protocol/src/IGameTransport.ts`: generic JSON `gethistory`
  transport contract.
- `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts`: existing
  read-only JSON history transport behavior.

## Likely New Files

- `historyTypes.ts`
- `historyStorage.ts`
- `historyResponseBuilder.ts`
- `historyRenderer.ts`
- `historyRoutes.ts`
- `index.ts`

## Candidate Client Targets

- `Gamesv1/packages/ui-kit/src/hud/PremiumTemplateHud.ts`
- `Gamesv1/packages/ui-kit/src/shell/hud/PremiumHudPolicy.ts`
- future GameClientBuilder-generated 8001 client code

These are blocked until GameClientBuilder is allowed.

## Blocked / Not Fully Proven

- Exact Casino Manager/backoffice route shape for 8001.
- Durable release storage source for 8001 visual history.
- Whether current GS accepts JSON-only visual replay. Until proven, visual HTML/render
  route remains required.
