# State Persistence Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Backend/Runtime Must Persist

- `roundId`
- `spinId` or current-GS equivalent
- `stateVersion` or current-GS equivalent
- `clientOperationId` / idempotency key if selected lane requires it
- current grid
- pending cascades
- golden-square state
- feature mode
- free spins or feature rounds remaining
- bonus-buy purchase state
- max-win cap state
- lastAction or current-GS equivalent
- recovery/reconnect state

## Browser Boundary

Browser/client may render state and send commands but must not be authoritative owner of production outcome state.
