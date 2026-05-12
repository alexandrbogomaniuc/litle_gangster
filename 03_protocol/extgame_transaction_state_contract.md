# ExtGame Transaction State Advisory Contract

Generated: 2026-05-11
Corrected: 2026-05-11

## Scope

This file is an advisory state checklist. It does not prove that Little Gangster uses ExtGame or that `processTransactions` is the production API.

## Current-Lane Translation

If current GS later proves the new-games `slot-browser-v1` lane for Little Gangster, verify equivalent concepts through:

- `/slot/v1/playround`
- `/slot/v1/featureaction`
- `/slot/v1/resumegame`
- `/slot/v1/gethistory`
- new-games backend reserve/placebet/collect behavior
- GS internal wallet reserve/settle and history write/read bridge

## Checklist Concepts

- Backend-owned accounting values.
- Restore-safe game state.
- Round-complete marker.
- Idempotency and duplicate retry behavior.
- Pending collect / unfinished round state.
- Max-win cap state.
- VABS/history archive state.
- Browser presentation-only boundary.

## Blockers

- `process_transaction_equivalent_unverified_for_current_gs`
- `round_completion_contract_unverified_for_current_gs`
- `state_persistence_owner_unverified`
