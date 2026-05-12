# Backend Adapter State Persistence Plan

Status: PLAN_ONLY_NOT_IMPLEMENTED.

## State To Persist

| State | Persistence rule | Evidence label |
|---|---|---|
| `stateVersion` / `currentStateVersion` | Increment only in backend/runtime after accepted state-changing operations. | PROVEN_GENERIC |
| `roundId` and `spinId` | Persist as backend correlation for play, feature actions, recovery, and history. | REQUIRED_V0_3 |
| Current grid | Persist after each accepted cascade step or feature transition. | REQUIRED_V0_3 |
| Pending cascades | Persist until no cascade/removal/drop/refill step remains. | REQUIRED_V0_3 |
| Golden-square state | Persist through cascades and feature transitions. | REQUIRED_V0_3 |
| Feature mode state | Persist active mode, remaining actions, completion state, and next allowed actions. | REQUIRED_V0_3 |
| Bonus-buy state | Persist purchase state and feature start state; wallet accounting remains outside payload. | REQUIRED_V0_3 |
| Max-win cap | Persist cap reached, pre-cap win, capped win, and cap step. | REQUIRED_V0_3 |
| Recovery state | Persist enough to reconstruct `presentationPayload.gamePayload.payload` on reconnect. | REQUIRED_RECOVERY |

## Runtime Envelope Mapping

- `stateVersion`: canonical envelope field.
- `restore.hasUnfinishedRound`: true when v0.3 round completion is false.
- `restore.unfinishedRoundId`: backend round id when unfinished.
- `restore.resumeStateVersion`: latest persisted backend state version.
- `restore.opaqueRestorePayload`: future backend-owned pointer or compact restore reference, not browser truth.
- `presentationPayload.gamePayload.payload.state_persistence`: renderable mirror of the state needed by client UI.

## Blocker

Evidence label: BLOCKED_8001_RUNTIME_OWNER. No 8001 persistence store or runtime owner is proven, so this plan cannot
be implemented until a backend target is approved.

