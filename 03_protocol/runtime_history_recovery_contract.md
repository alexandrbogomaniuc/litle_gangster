# Runtime History Recovery Contract

## Status

Generic history/recovery support is PROVEN. Little Gangster-specific history/replay payload remains BLOCKED.

## Generic Evidence

- `/slot/v1/resumegame` exists in core protocol and new-games-server.
- `/slot/v1/gethistory` exists in core protocol and new-games-server.
- WebGS `NewGamesInternalApiServlet` includes history write/read paths.
- GS source contains VABS/VBA/Lasthand/history concepts.

## Required Little Gangster State

Little Gangster history/recovery must preserve or reconstruct:

- `roundId`
- `spinId`
- `stateVersion`
- `clientOperationId` or equivalent idempotency marker
- current grid
- cascade progression
- golden-square persistence
- rainbow activation state
- coin/special reveal state
- feature mode state
- bonus-buy state
- max-win cap state
- round completion state
- final presentation payload for replay

## Open Questions

- Does Little Gangster replay use `/slot/v1/gethistory` only, VABS URLs, LastHand state, or a mixed path?
- Is `presentationPayload` stored in history as-is, reconstructed from servlet data, or rebuilt from backend state?
- What exact restore payload is returned for an unfinished Little Gangster round?

## Gate

WalletAndLaunchTester must not run Little Gangster history/recovery tests until the exact runtime and history payload contract is proven or fixture-approved.
