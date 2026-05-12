# Fixture Strict Schema Update Plan

Status: PLAN_ONLY_FIXTURES_NOT_UPDATED_THIS_SPRINT

## Required Changes After Schema Patch Approval

| Fixture area | Current planning shape | Strict-runtime shape needed | Evidence label |
|---|---|---|---|
| `presentationPayload.gamePayload` | Present as pending extension. | Keep under patched schema wrapper. | REQUIRED_SCHEMA_ALIGNMENT |
| `stateVersion` | May use fixture strings. | Use non-negative integers. | PROVEN_SCHEMA_CONFLICT |
| `round.status` | Some planning states are lowercase/custom. | Use `NONE`, `IN_PROGRESS`, or `FINAL`. | PROVEN_SCHEMA_CONFLICT |
| `restore` | Uses planning aliases in some examples. | Use `hasUnfinishedRound`, `unfinishedRoundId`, `resumeStateVersion`, `opaqueRestorePayload`. | PROVEN_SCHEMA_CONFLICT |
| `idempotency` | Uses planning aliases in some examples. | Use `isDuplicate`, `duplicateOfRequestId`, `replaySafe`. | PROVEN_SCHEMA_CONFLICT |
| `symbolGrid` | Symbolic render labels may exist. | Generic `symbolGrid` should use numeric IDs; symbolic labels remain inside game payload. | PROVEN_MAPPER_CONFLICT |
| `counters` | v0.3 fields may be rich/non-integer. | Generic counters stay integer array; rich data stays in `gamePayload.payload`. | REQUIRED_SCHEMA_ALIGNMENT |

## Fixture Policy

Keep current fixtures as planning fixtures. Add strict-runtime variants only after schema patch approval, so the static renderer can compare planning and strict envelopes without pretending either is production proof.
