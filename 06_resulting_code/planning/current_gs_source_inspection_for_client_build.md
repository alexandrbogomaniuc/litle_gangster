# Current GS Source Inspection For Client Build

Status: targeted planning inspection only. No source was modified.

## Roots Inspected

- `<STAGING>/platform-source/platform/Gamesv1`
- `<STAGING>/platform-source/platform/new-games-client`
- `<STAGING>/platform-source/platform/new-games-server`
- `<STAGING>/platform-source/platform/gs-server`

## Source Signals

|Question|Status|Evidence summary|
|---|---|---|
|Is `@gamesv1/core-protocol` available?|PROVEN|Found package at `Gamesv1/packages/core-protocol` with `IGameTransport`, schemas, and HTTP transport.|
|Is New Games server source available?|PROVEN|Found `new-games-server` with `/v1/contract` and `/slot/v1/*` endpoint handlers.|
|Is `slot-browser-v1` supported in source?|LIKELY|Gamesv1 docs/tools/tests and core protocol reference `slot-browser-v1`.|
|Is Vite/Pixi stack available?|PROVEN|Gamesv1 package and tool references show Vite, Pixi, `@gamesv1/pixi-engine`, and `@gamesv1/ui-kit`.|
|Can 7001 be used as direct template?|CANDIDATE_ONLY|7001 exists and uses Gamesv1 packages, but current server presentation code is 7001-specific and not v0.3 6x5.|
|Can premium-slot be used as direct template?|CANDIDATE_ONLY|Premium-slot exists as a package/reference, but direct Little Gangster suitability is unproven.|
|Does 8001 exist?|NOT_FOUND|Only unrelated numeric hit was found; no 8001 registration/runtime package was proven.|
|Can runtime API be proven for Little Gangster?|BLOCKED|No source proves a Little Gangster v0.3 result owner or adapter.|

## API Shape Signals

Gamesv1 core protocol defines bootstrap, opengame, playround, featureaction, resumegame, closegame, and gethistory flows. Runtime responses contain `wallet`, `round`, `feature`, `presentationPayload`, `restore`, `idempotency`, and `retry`.

`new-games-server` exposes matching `/slot/v1/*` endpoint names and has provisional result generation for existing reference games. It does not prove Little Gangster v0.3 result generation.

## Remaining Blockers

- Little Gangster 8001 package or runtime adapter not found.
- exact result owner not proven.
- exact v0.3 presentation payload shape not proven.
- history/VABS/Lasthands integration for v0.3 not proven.
- registration route/client path for 8001 not generated.
## RuntimeApiInspection Update

Additional targeted source inspection found:

- PROVEN generic `/slot/v1` endpoint names and server handlers in Gamesv1 core protocol and new-games-server.
- PROVEN generic `RuntimeEnvelopeResponse` in core protocol.
- PROVEN generic browser transport in `GsHttpRuntimeTransport`.
- PROVEN WebGS New Games internal bridge for session validation, wallet reserve/settle, request counters, idempotency, and history.
- LIKELY reusable presentation mapping pattern in premium-slot.
- CANDIDATE New Games backend result owner based on provisional sample outcome generation.
- NOT_FOUND Little Gangster/8001 runtime package, result owner, or v0.3 payload adapter.

The source inspection therefore supports planning against `/slot/v1`, but does not allow client implementation.
