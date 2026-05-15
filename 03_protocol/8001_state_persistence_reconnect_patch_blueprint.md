# 8001 State Persistence And Reconnect Patch Blueprint

Status: blueprint only. No implementation applied. No Staging source modified.

Current adapter is payload mapper only. Lifecycle wrapper is required to own 8001 reconnect and recovery semantics.

## Future Source Location

- `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/lifecycle/reconnectRecovery.ts`
- `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/lifecycle/stateMachine.ts`
- `[STAGING_SOURCE_ROOT]/new-games-server/src/games/little-gangster/lifecycle/roundCompletion.ts`

## Required Persisted State

- `stateVersion`
- `sessionId`
- `roundId`
- `gameSessionId`
- `playerSessionId`
- `requestCounter`
- `clientOperationId`
- `idempotencyKey`
- `lastSuccessfulAction`
- `pendingAction`
- `currentCascadeIndex`
- `featureMode`
- `freeSpinState`
- `bonusBuyState`
- `capState`
- `settlementState`
- `roundCompletion`
- `reconnectHints`
- `restartRequired`

## Recovery Rules

- Reconnect must not replay a paid action without idempotency proof.
- Reconnect must restore the last successful action and pending action separately.
- Cascade recovery must know the current cascade index and whether cascades are complete.
- Free-spin recovery must know remaining count and whether settlement is pending.
- Bonus-buy recovery must preserve purchase debit reference and feature result state separately.
- Round completion requires cascades/free spins/bonus-buy feature/cap/settlement/restart checks.

## Required Tests

- Resume from base idle.
- Resume during cascade active.
- Resume during free spins.
- Resume after 100x bonus-buy purchase before feature result.
- Resume during bonus-buy feature.
- Resume after settlement pending.
- Retry duplicate idempotency key.
- Pending/stuck action recovery.
