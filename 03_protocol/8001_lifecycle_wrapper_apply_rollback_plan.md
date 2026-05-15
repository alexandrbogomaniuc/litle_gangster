# Little Gangster 8001 Lifecycle Wrapper Apply Rollback Plan

Created: 2026-05-15

## Scope

This rollback plan covers the Staging-only lifecycle wrapper implementation applied for
Little Gangster gameId 8001. No DB, Cassandra, wallet, registration, GameClientBuilder,
or release actions were performed.

## Staging Source Files Created

- `new-games-server/src/games/little-gangster/lifecycle/lifecycleTypes.ts`
- `new-games-server/src/games/little-gangster/lifecycle/lifecycleStateMachine.ts`
- `new-games-server/src/games/little-gangster/lifecycle/actionAccounting.ts`
- `new-games-server/src/games/little-gangster/lifecycle/roundCompletion.ts`
- `new-games-server/src/games/little-gangster/lifecycle/statePersistence.ts`
- `new-games-server/src/games/little-gangster/lifecycle/reconnectRecovery.ts`
- `new-games-server/src/games/little-gangster/lifecycle/blockerPropagation.ts`
- `new-games-server/src/games/little-gangster/lifecycle/lifecycleWrapper.ts`
- `new-games-server/src/games/little-gangster/lifecycle/index.ts`
- `new-games-server/test/little-gangster/lifecycle-wrapper.test.ts`
- `new-games-server/test/little-gangster/lifecycle-state-machine.test.ts`
- `new-games-server/test/little-gangster/action-accounting.test.ts`
- `new-games-server/test/little-gangster/round-completion-reconnect.test.ts`
- `new-games-server/test/little-gangster/blocker-propagation.test.ts`

## Staging Source Files Modified

- `new-games-server/src/index.ts`

The existing Little Gangster adapter files were not modified in this sprint.

## Remove Lifecycle Wrapper Files

Delete the lifecycle directory:

```sh
rm -rf new-games-server/src/games/little-gangster/lifecycle
```

Delete the lifecycle wrapper tests:

```sh
rm -f new-games-server/test/little-gangster/lifecycle-wrapper.test.ts
rm -f new-games-server/test/little-gangster/lifecycle-state-machine.test.ts
rm -f new-games-server/test/little-gangster/action-accounting.test.ts
rm -f new-games-server/test/little-gangster/round-completion-reconnect.test.ts
rm -f new-games-server/test/little-gangster/blocker-propagation.test.ts
```

## Restore Index/Adapter Call Path

Restore `new-games-server/src/index.ts` to import the existing payload mapper functions:

- `createLittleGangsterBaseSpinAdapterEnvelope`
- `createLittleGangsterBonusBuy100xAdapterEnvelope`

Then replace the guarded gameId 8001 route calls so they use the payload mapper envelope
directly rather than the lifecycle wrapper envelope.

## Remove Tests

Remove only the lifecycle-specific tests listed above. Keep the existing adapter, schema,
and history-recovery tests.

## DB Rollback

No DB rollback is needed. This sprint did not execute DB/Cassandra changes.

## Wallet Rollback

No wallet rollback is needed. This sprint did not call wallet endpoints or alter wallet
accounting.
