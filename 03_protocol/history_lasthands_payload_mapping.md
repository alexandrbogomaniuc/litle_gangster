# History / Lasthands Payload Mapping

Status: GENERIC_HISTORY_PROVEN; LITTLE_GANGSTER_REPLAY_BLOCKED.

## Generic Evidence

Generic source and fixtures prove:

- `/slot/v1/gethistory`;
- optional envelope `history`;
- read-only history behavior;
- history records can carry round IDs and serialized round data;
- GS bridge concepts exist for history/write/read.

Evidence label: PROVEN_GENERIC.

## Required Little Gangster History Contents

| Content | Required for | Evidence label |
|---|---|---|
| `roundId` | locate round and correlate replay | PROVEN_GENERIC |
| bet amount and win amount | history display and accounting audit | PROVEN_GENERIC |
| collected/final status | replay and unfinished-state guard | PROVEN_GENERIC |
| v0.3 `presentationPayload` or replay snapshot | reconstruct cascades, reveals, feature state | REQUIRED_EXTENSION |
| state version and operation correlation | reconnect and idempotency audit | PROVEN_GENERIC_PLUS_EXTENSION |
| round completion state | avoid replaying incomplete states as final | REQUIRED_EXTENSION |
| restore payload for unfinished rounds | reconnect after interruption | PROVEN_GENERIC_BLOCKED_FOR_8001 |
| VABS/Lasthands equivalent fields | platform replay compatibility | BLOCKED_PENDING_CURRENT_GS_PROOF |

## Boundary

History is not a new outcome generator. History must either store the reviewed presentation payload or deterministically reconstruct it from backend-owned persisted state.

## Open Questions

- Does Little Gangster use `/slot/v1/gethistory`, VABS/Lasthands, or both?
- Is v0.3 presentation state stored as-is or reconstructed?
- What is the exact serialized payload size/format limit?
- Which component signs or verifies history/replay payloads, if any?

