# Runtime Adapter Test Matrix

Status: TEST_PLAN_ONLY. No tests were run.

| Test area | Required check | Evidence label | Status |
|---|---|---|---|
| Envelope shape | Adapter returns generic `/slot/v1` envelope groups. | PROVEN_GENERIC | planned |
| Presentation extension | v0.3 fields are accepted by reviewed schema. | REQUIRED_REVIEW | blocked |
| Backend authority | Browser cannot alter outcome fields. | REQUIRED_BOUNDARY | planned |
| Cascade payload | Each cascade step includes removed, dropped, new symbols, clusters, and wins. | REQUIRED_V0_3 | planned |
| Golden/rainbow/coin | Events render from backend payload only. | REQUIRED_V0_3 | planned |
| Feature/bonus buy | Feature actions and purchase state remain backend-owned. | REQUIRED_V0_3 | planned |
| Max-win cap | Cap is applied before payload reaches client. | REQUIRED_V0_3 | planned |
| Idempotency | Duplicate client operation returns safe duplicate/replay behavior. | PROVEN_GENERIC | planned |
| Counter/state version | Invalid counter/state version is rejected or retried by runtime rules. | PROVEN_GENERIC | planned |
| History/recovery | Replay/restore includes enough v0.3 state. | BLOCKED_FOR_8001 | blocked |

