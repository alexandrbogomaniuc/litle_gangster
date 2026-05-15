# 8001 Lifecycle Wrapper Source Planning Report

Status: planning only. No Staging source was modified.

## Executive Summary

Little Gangster 8001 should continue to use the current Staging adapter as a guarded `presentationPayload.gamePayload` mapper only. It should not be
  treated as the full GS lifecycle owner.

Recommended wrapper option: Option 5, combined small wrapper first, then separate visual history route later.

- Wrapper source location: `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/lifecycle/`
- VABS/VBA/Lasthands route source location: `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/history/`
- Route integration host: `[STAGING_SOURCE_ROOT]/new-games-server/src/index.ts`
- Current adapter dependency: `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/adapter.ts`

Crazy Rooster / game 7001 is not authoritative. It is weak candidate reference only.

## Source Evidence

Current `new-games-server/src/index.ts` is the proven route host for `/slot/v1/bootstrap`, `/slot/v1/opengame`, `/slot/v1/playround`,
  `/slot/v1/featureaction`, `/slot/v1/resumegame`, `/slot/v1/gethistory`, and `/slot/v1/closegame`. It already includes wallet reserve/settle bridge
  helpers, local session/round/history maps, idempotency fields, and guarded 8001 adapter calls for base spin and 100x bonus-buy presentation
  payloads.

Current Little Gangster files under `new-games-server/src/games/little-gangster/` are payload mapper files. They create result, presentation,
  persistence, fixture, and history payload shapes, but they do not own launch/session, wallet settlement, pending transaction recovery, close
  session, restart/FRB transitions, or visual history routing.

Current `Gamesv1/packages/core-protocol/src/` already defines runtime envelope, request counter, idempotency, client operation, resume, close, get
  history, and `presentationPayload.gamePayload` support. This makes it a likely schema target only if future wrapper or visual-history routes need
  typed expansion.

UI-kit evidence shows history UI and `gamePayload` passthrough support, but no proven Little Gangster VABS/VBA/Lasthands visual replay route. Treat
  visual history route support as required and not yet implemented.

Legacy GS evidence shows independent launch/session, restart/FRB, close/reconnect, lasthand/VABS/VBA, wallet pending operation, game template/config,
  and max-win/FRB message paths. These are lifecycle requirements around the adapter, not behavior proven by the current 8001 mapper.

## Source Target Map Summary

Proven targets:

- `new-games-server/src/index.ts`: existing route host and guarded 8001 integration point.
- `new-games-server/src/games/little-gangster/adapter.ts`: existing payload mapper dependency, not the preferred wrapper implementation file.
- `Gamesv1/packages/core-protocol/src/schemas.ts`: existing runtime envelope and `presentationPayload.gamePayload` schema support.
- `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts`: existing transport lifecycle methods.

Likely targets to create in a future apply sprint:

- `new-games-server/src/games/little-gangster/lifecycle/types.ts`
- `new-games-server/src/games/little-gangster/lifecycle/lifecycleWrapper.ts`
- `new-games-server/src/games/little-gangster/lifecycle/stateMachine.ts`
- `new-games-server/src/games/little-gangster/lifecycle/actionAccounting.ts`
- `new-games-server/src/games/little-gangster/lifecycle/reconnectRecovery.ts`
- `new-games-server/src/games/little-gangster/lifecycle/roundCompletion.ts`
- `new-games-server/src/games/little-gangster/lifecycle/blockers.ts`
- `new-games-server/src/games/little-gangster/history/historyPayload.ts`
- `new-games-server/src/games/little-gangster/history/vabsVisualHistoryRoutes.ts`
- `new-games-server/src/games/little-gangster/history/historyRouteContracts.ts`

Blocked or candidate targets:

- Visual HTML/VABS/VBA backoffice compatibility target is not proven in `new-games-server`; legacy JSP routes exist under GS source, but should not be
  edited for this first wrapper patch.
- Wallet/accounting owner remains existing GS/new-games bridge; Little Gangster wrapper should carry references, idempotency, and state, not call
  wallet endpoints directly.
- Registration and config source remains blocked until settings generation/apply is explicitly approved.

## Wrapper Shape Decision

Use Option 5:

1. Create a small 8001 lifecycle wrapper module under `new-games-server/src/games/little-gangster/lifecycle/`.
2. Keep existing `adapter.ts` as payload mapper only.
3. Integrate route-level calls in `new-games-server/src/index.ts` with minimal guarded gameId 8001 branches.
4. Create a separate history module under `new-games-server/src/games/little-gangster/history/`.
5. Defer any UI-kit, Gamesv1 game package, legacy JSP, or registration changes until separately approved.

This is safer than putting lifecycle logic into `adapter.ts`, and smaller than refactoring the global route host before Little Gangster-specific tests
  exist.

## VABS/VBA Route Shape

Future source plan:

- Route host: `new-games-server/src/index.ts`
- Route module: `new-games-server/src/games/little-gangster/history/vabsVisualHistoryRoutes.ts`
- Data/payload module: `new-games-server/src/games/little-gangster/history/historyPayload.ts`

Candidate JSON routes:

- `POST /slot/v1/games/8001/history/round`
- `POST /slot/v1/games/8001/history/session`
- `POST /slot/v1/games/8001/history/whole-session`

Candidate compatibility outputs:

- JSON deterministic replay payload for runtime/UI shell.
- HTML or URL handoff remains blocked until backoffice/Casino Manager compatibility is proven.

Required input fields:

- `gameId`, `gameKey`, `gameSessionId`, `playerSessionId`, `roundId`, `lang`, `timeZone`, `wholeSession`, `hideClose`.

Required output fields:

- history payload schema fields from `8001_history_payload_schema.json`, including `mathProfileId`, RTP/volatility profile, `bonusBuyCostMultiplier`,
  action/cascade/feature state, wallet accounting refs, replay determinism refs, VABS display, Lasthands display, and route metadata.

## State Persistence And Reconnect

Future wrapper must persist or reconstruct:

- `stateVersion`
- `sessionId`
- `roundId`
- `requestCounter`
- `clientOperationId`
- `idempotencyKey`
- `lastSuccessfulAction`
- `pendingAction`
- `currentCascadeIndex`
- `freeSpinState`
- `bonusBuyState`
- `capState`
- `roundCompletion`
- `settlementState`
- `reconnectHints`
- `restartRequired`

The current adapter has render payload persistence fields, but it is not the lifecycle persistence owner.

## Accounting Boundary

The wrapper must not call wallet endpoints directly. It should call existing route-level wallet/accounting bridge helpers or receive their results
  from the route host.

Required accounting representation:

- Paid base spin debit/result settlement.
- Cascade action/result continuation.
- Free spin or feature action/result.
- 100x bonus-buy purchase debit.
- 100x bonus-buy feature result.
- Cap enforcement state.
- Wallet/accounting reference IDs.
- Idempotency and pending/stuck action recovery.
- Balance from settle/process response, not repeated getBalance.

## Registration Impact

Meaningful wrapper tests remain blocked until 8001 settings dependencies are resolved enough to launch:

- `POSSIBLE_MODELS`
- `RTP_WITHOUT_BF`
- `BF_RTP`
- `BF_RTP_MIN`
- `SD_KEYS`
- FeatureKPI mapping
- `CAP_WIN_MULTIPLIER`
- `MAX_WIN`
- `POSSIBLE_MAX_WINS`
- GL bet fields
- `BF_BETS`
- VABS/VBA route fields if required

Registration generation remains blocked.

## Test Plan Summary

Future tests should live under:

- `new-games-server/test/little-gangster/lifecycle-wrapper.test.ts`
- `new-games-server/test/little-gangster/state-reconnect.test.ts`
- `new-games-server/test/little-gangster/accounting-boundary.test.ts`
- `new-games-server/test/little-gangster/vabs-visual-history-route.test.ts`
- `new-games-server/test/little-gangster/pending-stuck-recovery.test.ts`

Tests must cover route orchestration, state/reconnect, accounting boundaries, VABS route payloads, last hand, whole-session replay, and pending/stuck
  transactions.

## Recommendation

Proceed next only with an explicitly approved lifecycle wrapper implementation apply sprint. Keep VABS visual history route implementation,
  GameClientBuilder, GameServerRegistrar generation, wallet endpoints, DB/Cassandra, and release blocked unless separately approved.
