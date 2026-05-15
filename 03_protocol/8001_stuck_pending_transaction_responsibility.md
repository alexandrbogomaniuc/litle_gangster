# 8001 Stuck/Pending Transaction Responsibility

Date: 2026-05-15
Status: read-only ownership audit

## Source Findings

- PROVEN_SOURCE: GS common-wallet code detects incomplete previous wallet operations
  and rejects a new debit when an earlier operation remains open.
- PROVEN_SOURCE: GS common-wallet code marks unresolved credit operations as
  `PENDING` and queues a high-priority wallet tracker task.
- PROVEN_SOURCE: `PendDataArchCF` stores pending wallet and FRB win operations.
- PROVEN_SOURCE: `WopCF` stores wallet operation information by operation id with
  game-session and round references.
- PROVEN_SOURCE: MQ/session code reports transaction states as approved, started,
  pending, or failed based on wallet operation status.
- PROVEN_SOURCE: failed/pending operation enter-game processing can run wallet tracker
  recovery before gameplay resumes.

## Assigned Owner

Pending/stuck transaction owner: current GS wallet-operation tracking and persistence,
plus wallet/provider response state.

Little Gangster runtime/lifecycle owner: pending marker, idempotency key, last action,
round id, recoverable payload, and blocker propagation.

Browser/client owner: no. The client may show a blocked/retry state from the runtime
envelope, but it must not decide transaction recovery, mutate balances, or silently
advance game state after an unresolved wallet operation.

## 8001 Contract

For 8001, any pending or stuck action must preserve:

- `actionId`;
- `clientOperationId`;
- `idempotencyKey`;
- `roundId`;
- `gameSessionId` or current candidate session id;
- last accepted lifecycle state;
- last wallet/accounting reference;
- recoverable payload;
- history/VABS reference;
- current blocker list.

If GS returns pending/rejected/unavailable accounting state, the wrapper must represent
`stuck_transaction_review` or equivalent blocked state rather than hiding the issue with
a fresh balance refresh.

## Remaining Blockers

- BLOCKED: exact 8001 production persistence for pending/stuck new-games operations is
  not proven until approved integration tests run against current GS.
- BLOCKED: rollback/refund route shape for 8001 is not proven.
- BLOCKED: BO/CM and wallet/history test acceptance remains missing.
