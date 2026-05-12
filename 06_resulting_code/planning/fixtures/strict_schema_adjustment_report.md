# Strict Schema Adjustment Report

Status: COMPLETED_WITH_NON_PRODUCTION_BOUNDARY.

The original fixture examples were renderer-planning objects with top-level fixture metadata and candidate runtime-envelope fields.

The strict variants are pure candidate `/slot/v1` response envelopes. This was necessary because the patched canonical response schemas keep `additionalProperties: false` at the response and `presentationPayload` levels.

## Adjustments Applied

| Area | Original fixture pattern | Strict fixture pattern | Reason |
|---|---|---|---|
| Top-level shape | Fixture metadata wrapper | Canonical response envelope | Required by patched response schemas. |
| `stateVersion` | String fixture marker | Integer `1` | Canonical runtime schema expects non-negative integer. |
| `round.status` | Lowercase/custom states | `NONE`, `IN_PROGRESS`, or `FINAL` | Canonical round status values. |
| `wallet` | Display-only marker object | Required fake `FUN` wallet fields with zero values | Canonical schema requires wallet fields; no real balance is used. |
| `restore` | `hasOpenRound`, `roundId` | `hasUnfinishedRound`, `unfinishedRoundId`, `resumeStateVersion`, `opaqueRestorePayload` | Canonical restore shape. |
| `idempotency` | `duplicate` and client marker | `isDuplicate`, `duplicateOfRequestId`, `replaySafe` | Canonical idempotency shape. |
| `retry` | `retryable`, `reason` | `clientMayRetrySameKey`, `clientMustIncrementCounterOnNewAction` | Canonical retry shape. |
| `symbolGrid` | Symbol labels | Numeric 5x6 grid for generic presentation field | Keeps strict envelope generic while preserving symbolic v0.3 state in `gamePayload`. |
| Non-production markers | Top-level fixture fields | `gamePayload.payload.state_persistence.fixture_metadata` | Preserves safety markers while keeping response schema strict. |

## Validation Result

All 24 strict variants validate against the patched response schema selected for that fixture and against the v0.3 result schema for `gamePayload.payload`.

## Remaining Boundary

These fixtures do not make the backend authoritative adapter real. They are safe inputs for a future backend adapter test plan only after explicit user approval.
