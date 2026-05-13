# Transaction State And Round Completion Checklist

Status: advisory checklist for current-GS validation.

## Current Source Signals

| Topic | Evidence | Current interpretation |
|---|---|---|
| New-games transaction flow | `new-games-server/src/index.ts:1165-1338` reserves wallet funds, creates an outcome, stores a round, writes history, and returns math details from `/v1/placebet`. | Current lane has a reserve/placebet flow,
not proof of Mantis `processTransactions`. |
| Browser playround | `new-games-server/src/index.ts:1700-1766` wraps `/v1/placebet` under `/slot/v1/playround`. | Browser calls `playround`; backend handles wallet/math/history details. |
| Feature collect | `new-games-server/src/index.ts:1767-1808` supports `featureaction` with `COLLECT`. | Current flow has feature/collect behavior; exact Little Gangster feature modes need mapping. |
| Idempotency | Current source stores idempotent responses for operation keys and Gamesv1 core protocol requires request counters/idempotency headers. | Duplicate/retry validation is required. |
| Round helper | `RoundFinishedHelper.java:1-53` and `BaseGameInfoTemplate.java:39-45` show configurable round-finished concepts. | Little Gangster needs an explicit round-complete field, but current config usage is unverified. |

## Checklist Requirements

- Translate Mantis `processTransactions` into the current lane's reserve/settle/process-equivalent calls.
- Verify whether every paid spin, free spin, feature spin, bonus buy, and collect produces correct wallet/accounting state.
- Do not accumulate all feature wins and settle only once unless current GS explicitly requires that pattern.
- Use the balance returned by the authoritative transaction response.
- Define `gameState` or restore state for cascades, golden squares, feature modes, cap reached, and pending collect.
- Define a round-complete marker compatible with `/slot/v1/*` and any GS `roundFinishedHelper` requirement.
- Validate duplicate request behavior and state-version mismatch behavior.

## Blockers

- `process_transaction_equivalent_unverified_for_current_gs`
- `round_completion_contract_unverified_for_current_gs`
- `state_persistence_owner_unverified`

