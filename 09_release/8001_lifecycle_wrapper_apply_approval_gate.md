# 8001 Lifecycle Wrapper Apply Approval Gate

Status: implementation blocked until explicit approval. No implementation applied. No Staging source modified.

## Current Decision

Lifecycle wrapper source planning is complete. The current 8001 adapter remains payload mapper only. Lifecycle wrapper is required. VABS visual
  history route is required.

## Apply Gate

Implementation is not allowed until a future prompt explicitly approves lifecycle wrapper implementation apply and names the allowed Staging source
  files or directories.

## Allowed Only After Explicit Future Approval

- Create `new-games-server/src/games/little-gangster/lifecycle/`.
- Create `new-games-server/src/games/little-gangster/history/`.
- Modify guarded gameId 8001 branches in `new-games-server/src/index.ts`.
- Add targeted tests under `new-games-server/test/little-gangster/`.

## Still Blocked

- VABS/VBA route implementation unless separately approved.
- Backend adapter refactor beyond wrapper integration.
- GameClientBuilder implementation.
- GameServerRegistrar generation.
- Registration artifact generation.
- DB/Cassandra changes.
- Wallet/API calls.
- WalletAndLaunchTester execution.
- RTPAndReleaseAuditor.
- Donor browsing or asset capture.
- Release approval.

## Required Before Apply

- Confirm wrapper option 5 remains accepted.
- Confirm exact source write scope.
- Confirm whether VABS route code is in or out of the same implementation sprint.
- Confirm targeted tests to run.
- Preserve rollback instructions for every Staging source change.
