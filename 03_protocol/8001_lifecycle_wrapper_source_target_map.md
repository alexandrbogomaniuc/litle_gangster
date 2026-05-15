# 8001 Lifecycle Wrapper Source Target Map

Status: planning only. No implementation applied. No Staging source modified.

Crazy Rooster / 7001 is not authoritative. Current 8001 adapter is payload mapper only. Lifecycle wrapper is required.

## Recommended Locations

- Wrapper: `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/lifecycle/`
- VABS/history: `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/history/`
- Route integration: `[STAGING_SOURCE_ROOT]/new-games-server/src/index.ts`

## Target Classes

| Target | Label | Next action |
| --- | --- | --- |
| `new-games-server/src/index.ts` | proven target | Add minimal guarded 8001 wrapper/route calls only after explicit approval. |
| `new-games-server/src/games/little-gangster/adapter.ts` | proven dependency | Keep as payload mapper; do not move lifecycle ownership into it. |
| `new-games-server/src/games/little-gangster/lifecycle/lifecycleWrapper.ts` | likely target | Create future wrapper orchestration. |
| `new-games-server/src/games/little-gangster/lifecycle/stateMachine.ts` | likely target | Create future state transition rules. |
| `new-games-server/src/games/little-gangster/lifecycle/actionAccounting.ts` | likely target | Create future accounting reference boundary. |
| `new-games-server/src/games/little-gangster/lifecycle/reconnectRecovery.ts` | likely target | Create future reconnect/recovery owner. |
| `new-games-server/src/games/little-gangster/lifecycle/roundCompletion.ts` | likely target | Create future completion/restart/cap owner. |
| `new-games-server/src/games/little-gangster/history/historyPayload.ts` | likely target | Create future deterministic history payload builder. |
| `new-games-server/src/games/little-gangster/history/vabsVisualHistoryRoutes.ts` | likely target | Create future round/session/whole-session route
  handlers. |
| `Gamesv1/packages/core-protocol/src/schemas.ts` | proven target if needed | Extend only if new route schemas must be shared. |
| `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | candidate later | Touch only with approved client/transport scope. |
| `Gamesv1/packages/ui-kit/` | candidate later blocked | Client route/view integration remains blocked. |
| legacy GS restart/VABS/wallet/config files | evidence only | Use for behavior parity; do not patch in first wrapper apply. |

## Blocked-Not-Found Or Blocked-Not-Ready

- New-games Little Gangster VABS/VBA HTML route: blocked, not found.
- Backoffice/Casino Manager visual history compatibility: blocked until route/API expectation is proven.
- Registration source target for 8001 settings: blocked until GameServerRegistrar generation/apply is explicitly approved.
- Wallet/accounting implementation changes: blocked; wrapper must use existing bridge/result references.

## Future Tests

- `new-games-server/test/little-gangster/lifecycle-wrapper.test.ts`
- `new-games-server/test/little-gangster/state-reconnect.test.ts`
- `new-games-server/test/little-gangster/accounting-boundary.test.ts`
- `new-games-server/test/little-gangster/vabs-visual-history-route.test.ts`
- `new-games-server/test/little-gangster/pending-stuck-recovery.test.ts`
