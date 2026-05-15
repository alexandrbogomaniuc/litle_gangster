# 8001 Lifecycle Wrapper Patch Blueprint

Status: blueprint only. No implementation applied. No Staging source modified.

Crazy Rooster / 7001 is not authoritative. Current Little Gangster adapter is payload mapper only. Lifecycle wrapper is required.

## Selected Option

Option 5: combined small wrapper first, then separate route later.

## Future Files To Create

Under `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/lifecycle/`:

- `types.ts`
- `stateMachine.ts`
- `lifecycleWrapper.ts`
- `actionAccounting.ts`
- `reconnectRecovery.ts`
- `roundCompletion.ts`
- `blockers.ts`

## Future Existing Files To Modify

- `[STAGING_SOURCE_ROOT]/new-games-server/src/index.ts`

Modification should be minimal and guarded by `gameId === 8001`.

## Files To Avoid In First Apply

- Existing `new-games-server/src/games/little-gangster/adapter.ts` unless a compile-time import shape requires a tiny export addition.
- Any legacy GS Java/JSP source.
- Any Gamesv1 game package.
- Any registration config/artifact.
- Any wallet service source.

## Wrapper Responsibilities

- Own 8001 lifecycle state transitions.
- Call current adapter only for `presentationPayload.gamePayload` construction.
- Preserve route-level wallet/accounting truth outside `gamePayload`.
- Propagate 100x bonus-buy planning-only blockers.
- Enforce 125x/150x blocked tier flags.
- Preserve request counter, idempotency, and client operation boundaries.
- Build recoverable state for reconnect/resume.
- Carry round completion, cap state, and restart advisory status.

## Route Touch Points

- `/slot/v1/opengame`: initialize 8001 lifecycle state when session gameId is 8001.
- `/slot/v1/playround`: route paid base spin through 8001 wrapper after generic validation/accounting.
- `/slot/v1/featureaction`: route cascade/free-spin/bonus-buy actions through 8001 wrapper; 100x only for standard bonus-buy.
- `/slot/v1/resumegame`: rebuild 8001 recovery payload from wrapper state.
- `/slot/v1/closegame`: include 8001 close/round completion readiness state.
- `/slot/v1/gethistory`: delegate 8001 history payload assembly to history module after it exists.

## Explicit Non-Goals

- Do not implement VABS/VBA HTML rendering in the lifecycle wrapper.
- Do not call wallet endpoints from Little Gangster modules.
- Do not generate RNG or determine results in browser.
- Do not generate registration artifacts.
- Do not mark bonus buy release-ready or certified.
