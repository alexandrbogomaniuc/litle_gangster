# History Recovery Adapter Requirements

Status: REQUIREMENTS_DEFINED_8001_NOT_PROVEN.

## Generic Evidence

| Source | Finding | Evidence label |
|---|---|---|
| `GsHttpRuntimeTransport.ts` | `/slot/v1/gethistory` is read-only and requires a history payload. | PROVEN_GENERIC |
| `new-games-server/src/index.ts` | `/slot/v1/resumegame` and `/slot/v1/gethistory` exist; local history rows carry round and archive data. | PROVEN_GENERIC |
| `new-games-server/src/index.ts` | VABS-style archive builder emits betData and servletData for current sample flow. | CANDIDATE_PATTERN |
| 7001 VABS docs | Existing game path documents emitted replay-support metadata and `presentationPayload`. | CANDIDATE_PATTERN |

## Required Little Gangster History State

| State | Required location | Evidence label |
|---|---|---|
| `roundId`, `spinId` | envelope `round`, history row, v0.3 payload | REQUIRED |
| `stateVersion`, `clientOperationId`, idempotency key | envelope and history metadata | REQUIRED |
| bet, win, final/capped win | envelope `round` and audit history | REQUIRED |
| final grid and cascade sequence | v0.3 game payload or reconstructable backend state | REQUIRED_EXTENSION |
| golden-square, rainbow, coin/special reveal state | v0.3 game payload or reconstructable backend state | REQUIRED_EXTENSION |
| feature mode and bonus-buy state | envelope `feature` plus game payload | REQUIRED_EXTENSION |
| max-win cap and round completion | envelope `round` plus game payload | REQUIRED_EXTENSION |
| VABS/Lasthand replay data | platform history bridge payload | BLOCKED_FOR_8001 |

## Adapter Requirement

The backend adapter must either persist the reviewed v0.3 `gamePayload` snapshot or persist enough backend-owned state to reconstruct it exactly for replay and reconnect.

## Open Blockers

- Exact 8001 history storage path not found.
- VABS/Lasthand shape for Little Gangster not proven.
- Payload size and serialization constraints not reviewed.
- No automated history/recovery adapter tests exist yet.
