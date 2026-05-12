# Backend Runtime Adapter Test Matrix

Status: TEST_PLAN_ONLY_NOT_RUN.

| Test | Purpose | Expected result | Evidence label |
|---|---|---|---|
| Adapter input validation | Verify authoritative backend result includes all v0.3 mandatory fields. | Missing field fails before envelope creation. | REQUIRED_TEST |
| Backend ownership boundary | Verify browser cannot submit symbol/cascade/win/cap outcomes. | Runtime ignores/rejects browser-authored result fields. | REQUIRED_TEST |
| Envelope projection | Verify wallet, round, feature, restore, idempotency, retry, and history are in correct envelope groups. | No accounting truth placed only in game payload. | REQUIRED_TEST |
| `gamePayload` schema validation | Verify approved schema accepts v0.3 payload. | `RuntimeEnvelopeResponseSchema` passes. | BLOCKED_SCHEMA_REVIEW |
| 8001 route selection | Verify gameId 8001 uses Little Gangster adapter. | 8001 payload contains `gameKey=little-gangster`. | BLOCKED_8001_NOT_FOUND |
| No client authority | Verify production client cannot generate final results. | Client receives only server result. | REQUIRED_TEST |
