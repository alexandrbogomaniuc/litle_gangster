# 8001 Accounting Boundary Patch Blueprint

Status: blueprint only. No implementation applied. No Staging source modified. No wallet/API calls occurred.

Current Little Gangster adapter must not call wallet endpoints. Lifecycle wrapper should carry accounting references and use existing route-level
wallet/accounting bridge results.

## Future Source Location

- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/src/games/little-gangster/lifecycle/actionAccounting.ts`

## Required Accounting Representation

- Paid base spin action and debit/reference.
- Cascade action/result continuation.
- Free-spin action/result representation.
- 100x bonus-buy purchase debit/reference.
- 100x bonus-buy feature result representation.
- Cap enforcement state.
- Settlement pending/complete state.
- Wallet/accounting reference fields.
- Request counter, idempotency key, client operation ID.
- Pending/stuck action recovery state.

## Boundary Rules

- Balance must come from settle/process response, not repeated `getBalance`.
- The wrapper must not call wallet endpoints directly.
- Wallet truth remains outside `presentationPayload.gamePayload`.
- `gamePayload` may carry render/history/accounting references only.
- 125x and 150x bonus-buy tiers remain blocked.
- 100x bonus buy remains implementation-planning-only, not release-approved and not certified.

## Required Tests

- Base spin debit/reference represented.
- Free-spin result represented without extra debit.
- Bonus-buy purchase debit represented separately from feature result.
- Settlement response balance propagated.
- Duplicate idempotency does not duplicate debit.
- Pending/stuck transaction is recoverable.
- Cap reached state blocks further paid progression until handled.
