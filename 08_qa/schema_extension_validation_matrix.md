# Schema Extension Validation Matrix

Status: TEST_PLAN_ONLY

| Area | Validation | Expected result | Evidence label |
|---|---|---|---|
| Core schema | Generic presentation payload without extension validates. | Pass | REQUIRED_REGRESSION |
| Core schema | Valid `presentationPayload.gamePayload` validates after patch. | Pass | REQUIRED_NEW_SCHEMA_TEST |
| Core schema | `gamePayload` missing `gameKey` fails. | Fail | REQUIRED_NEGATIVE_TEST |
| Core schema | `gamePayload` missing `schemaVersion` fails. | Fail | REQUIRED_NEGATIVE_TEST |
| Core schema | Unknown top-level presentation key still fails unless deliberately allowed. | Fail | STRICTNESS_GUARD |
| Transport | HTTP runtime transport preserves valid `gamePayload`. | Pass | REQUIRED_TRANSPORT_TEST |
| Server | 8001 payload builder emits valid `gamePayload`. | Pass after server patch | REQUIRED_SERVER_TEST |
| History/recovery | Stored/replayed payload can restore v0.3 render state. | Pass after persistence design | REQUIRED_RECOVERY_TEST |
| Safety | Browser-supplied payload cannot override authoritative result. | Pass | AUTHORITY_GUARD |
