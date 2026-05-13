# Runtime Envelope Field Mapping

Status: GENERIC_CONTRACT_PROVEN; LITTLE_GANGSTER_MAPPING_REQUIRED.

| Envelope field | Generic meaning | Little Gangster v0.3 mapping | Evidence label |
|---|---|---|---|
| `ok` | Success flag. | Same generic meaning. | PROVEN_GENERIC |
| `requestId` | Operation correlation. | May mirror `clientOperationId` or server request ID. | PROVEN_GENERIC |
| `sessionId` | Runtime session identity. | Must be backend-provided and never invented by client. | PROVEN_GENERIC |
| `requestCounter` | Monotonic sequencing. | Must align with selected runtime rules. | PROVEN_GENERIC |
| `stateVersion` | Runtime state version. | Must align with v0.3 `state_persistence.stateVersion`. | PROVEN_GENERIC |
| `wallet` | Balance/currency/accounting summary. | Display only for client; accounting truth remains backend-owned. | PROVEN_GENERIC |
| `round` | Round ID, status, bet/win, outcome hash. | Must carry canonical round status and monetary values. | PROVEN_GENERIC |
| `feature` | Feature mode/action availability. | Must expose backend-approved feature actions and remaining actions. | PROVEN_GENERIC |
| `presentationPayload` | Browser-visible render payload. | Must carry reviewed Little Gangster v0.3 render state or extension. | PROVEN_GENERIC_EXTENSION_REQUIRED |
| `restore` | Unfinished-round restore metadata. | Must link unfinished v0.3 state and recovery payload. | PROVEN_GENERIC_BLOCKED_FOR_8001 |
| `idempotency` | Duplicate/replay safety state. | Backend owned; client only displays/handles retry policy. | PROVEN_GENERIC |
| `retry` | Client retry guidance. | Backend owned. | PROVEN_GENERIC |
| `history` | Optional history response block. | Must preserve enough v0.3 replay state for Lasthands/VABS equivalent. | PROVEN_GENERIC_BLOCKED_FOR_8001 |

## Non-Envelope v0.3 State

The v0.3 result schema is richer than the generic envelope. It should not be flattened into wallet/round/feature if that would blur boundaries. Render-only feature details belong in a reviewed presentation extension; accounting and
authoritative status stay in `wallet`, `round`, `feature`, `restore`, and `history`.

