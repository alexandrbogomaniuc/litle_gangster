# Runtime State Persistence Mapping

Status: REQUIRED_MAPPING_NOT_PROVEN_FOR_8001.

## Generic Persistence Signals

Generic `/slot/v1` source proves `stateVersion`, `restore`, `idempotency`, `retry`, `requestCounter`, and history response concepts. It does not prove a Little Gangster-specific persistence payload.

## v0.3 State To Persist

| v0.3 field | Runtime persistence location | Evidence label |
|---|---|---|
| `roundId` | `round.roundId`, history record, v0.3 state | PROVEN_GENERIC |
| `spinId` | v0.3 state or game-specific extension | REQUIRED_REVIEW |
| `stateVersion` | envelope `stateVersion`, `state_persistence.stateVersion` | PROVEN_GENERIC |
| `clientOperationId` / `idempotencyKey` | request headers/body and idempotency state | PROVEN_GENERIC |
| current/final grid | v0.3 presentation extension and restore snapshot | REQUIRED_EXTENSION |
| pending cascades | restore snapshot and v0.3 `state_persistence.pending_cascades` | REQUIRED_EXTENSION |
| golden-square state | restore snapshot and v0.3 state | REQUIRED_EXTENSION |
| feature mode | envelope `feature` plus v0.3 feature state | PROVEN_GENERIC_PLUS_EXTENSION |
| free spins/feature rounds remaining | `feature.remainingActions` plus v0.3 details | PROVEN_GENERIC_PLUS_EXTENSION |
| bonus-buy purchase state | `feature` plus v0.3 bonus-buy state | REQUIRED_EXTENSION |
| cap state | v0.3 `max_win_cap` and restore snapshot | REQUIRED_EXTENSION |
| last action | v0.3 `lastAction_or_current_gs_equivalent` | REQUIRED_REVIEW |
| recovery state | envelope `restore` and history | PROVEN_GENERIC_BLOCKED_FOR_8001 |

## Restore Rule

Reconnect must not depend on browser memory. A refreshed client must be able to restore from backend state or a backend-provided fixture in planning mode.

