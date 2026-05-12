# Backend Adapter History / Lasthands Plan

Status: PLAN_ONLY_NOT_IMPLEMENTED.

## Required History Output

The adapter must preserve enough state for history, Lasthand, and VABS/VBA-equivalent review flows to replay the
visible v0.3 outcome without browser authority.

| Data | Required handling | Evidence label |
|---|---|---|
| Final round summary | Store bet, win, round status, cap state, and outcome reference. | PROVEN_GENERIC_PLUS_REQUIRED_V0_3 |
| Presentation replay payload | Store or reconstruct `presentationPayload.gamePayload.payload`. | REQUIRED_V0_3 |
| Cascade/reveal sequence | Preserve removed cells, dropped cells, new symbols, coin/special reveals, and animation order. | REQUIRED_V0_3 |
| Feature/bonus buy state | Preserve selected mode, remaining actions, and feature completion state. | REQUIRED_V0_3 |
| Restore correlation | Preserve state version and unfinished round pointer for reconnect. | PROVEN_GENERIC |
| VABS/Lasthands archive | Map to existing archive fields only after selected runtime history format is approved. | BLOCKED_FORMAT_UNPROVEN |

## `gethistory` Mapping

Future `gethistory` output should include history records whose replay payload can reconstruct the strict fixture
shape for final or recoverable rounds. The strict fixture `24_error_or_recovery_pending_state.json` proves that
`history` can coexist with `presentationPayload.gamePayload` in the patched schema, but it does not prove production
history storage.

## Blockers

- No 8001 history persistence component exists.
- Current new-games history records are generic and 7001/provisional oriented.
- Exact VABS/Lasthands serialization for Little Gangster is not proven.

