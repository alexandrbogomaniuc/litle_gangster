# Fixture Schema Adjustments After Adapter Review

Status: ADJUSTMENTS_IDENTIFIED_NOT_APPLIED.

## Why Adjustments Are Needed

The 24 fixture examples are valid planning JSON and safe non-production artifacts. They are not strict `/slot/v1` protocol fixtures yet.

## Required Adjustments If Used For Protocol Tests

| Area | Current fixture style | Required strict-runtime style | Evidence label |
|---|---|---|---|
| `presentationPayload.gamePayload` | present | allowed only after schema extension | BLOCKED_SCHEMA_REVIEW |
| `stateVersion` | string fixture IDs | integer state version | STRICT_SCHEMA_ADJUSTMENT |
| `round.status` | lowercase/custom status | `NONE`, `IN_PROGRESS`, `FINAL` | STRICT_SCHEMA_ADJUSTMENT |
| `restore` | `hasOpenRound`, `roundId` | `hasUnfinishedRound`, `unfinishedRoundId`, `resumeStateVersion`, `opaqueRestorePayload` | STRICT_SCHEMA_ADJUSTMENT |
| `idempotency` | `duplicate` | `isDuplicate`, `duplicateOfRequestId`, `replaySafe` | STRICT_SCHEMA_ADJUSTMENT |
| `symbolGrid` | symbolic strings | numeric symbol IDs for shared mapper | MAPPER_ADJUSTMENT |

## Preserve Planning Value

Keep current human-readable fixtures for scene review. Add strict-runtime fixture variants later only if the schema team approves `gamePayload` and the test owner needs machine validation.
