# Game Payload Extension Test Matrix

Status: TEST_PLAN_ONLY

| Scenario | Payload | Expected result | Evidence label |
|---|---|---|---|
| Little Gangster v0.3 payload | `gameKey=little-gangster`, `schemaVersion=v0.3`, nested v0.3 payload | Accepted after schema patch | REQUIRED_POSITIVE_TEST |
| Future game payload | Different `gameKey`, valid schema version, nested unknown payload | Accepted if generic extension is approved | REUSABILITY_TEST |
| Missing game key | No `gameKey` | Rejected | REQUIRED_NEGATIVE_TEST |
| Missing schema version | No `schemaVersion` | Rejected | REQUIRED_NEGATIVE_TEST |
| Wrong payload location | v0.3 payload spread across unrelated envelope fields | Rejected or not recommended | BOUNDARY_GUARD |
| Wallet data in payload | Wallet/accounting fields inside `gamePayload.payload` | Rejected by policy/test | SAFETY_GUARD |
| Browser-generated outcome | Client attempts to submit authoritative outcome | Rejected by backend tests | AUTHORITY_GUARD |
