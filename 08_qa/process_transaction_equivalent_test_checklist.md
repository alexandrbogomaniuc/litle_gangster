# Process-Transaction Equivalent Test Checklist

Status: QA gate only; no tests executed.

## Current-Lane Translation

Do not assume Mantis `processTransactions` is the current API. For new-games lane, test the equivalent behavior across `/slot/v1/playround`, backend reserve/placebet, `/slot/v1/featureaction`, collect, wallet settle, history write, and restore state.

## Required Tests

- Base spin bet/win accounting.
- Feature spin accounting.
- Bonus-buy purchase accounting.
- Collect/finalize accounting.
- Failed reserve/bet behavior.
- Failed settle/win behavior.
- Refund/retry behavior where supported.
- Idempotency for duplicate request keys.
- Balance returned by authoritative transaction response is used.
- No extra `getBalance` dependency after a successful process-equivalent call unless current source requires it.

## Blockers

- `process_transaction_equivalent_unverified_for_current_gs`
- `wallet_launch_tests_missing`

