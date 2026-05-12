# History Recovery Adapter Test Matrix

Status: TEST_PLAN_ONLY. No wallet/API/history tests were run.

| Test area | Required check | Evidence label | Status |
|---|---|---|---|
| `resumegame` unfinished round | Runtime returns unfinished round and restore payload. | PROVEN_GENERIC | planned |
| `gethistory` read-only | History request does not advance state. | PROVEN_GENERIC | planned |
| v0.3 replay state | History/replay can reconstruct cascades and reveals. | REQUIRED_EXTENSION | blocked |
| golden-square restore | Persisted state restores golden overlays. | REQUIRED_V0_3 | blocked |
| feature restore | Feature mode and remaining spins/rounds restore correctly. | REQUIRED_V0_3 | blocked |
| cap restore | Max-win cap state remains consistent after reconnect. | REQUIRED_V0_3 | blocked |
| VABS/Lasthands | Current-GS replay integration handles v0.3 payload. | BLOCKED_PENDING_PROOF | blocked |
| idempotency replay | Duplicate operation does not double-settle. | PROVEN_GENERIC | planned |

