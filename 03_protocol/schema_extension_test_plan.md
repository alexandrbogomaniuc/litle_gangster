# Schema Extension Test Plan

Status: TEST_PLAN_ONLY_NO_TESTS_RUN

## Core Protocol Tests

| Test | Expected result | Evidence label |
|---|---|---|
| Existing generic presentation payload validates unchanged. | Pass | REQUIRED_REGRESSION |
| Presentation payload with valid `gamePayload` validates. | Pass after schema patch | REQUIRED_NEW_SCHEMA_TEST |
| `gamePayload` missing `gameKey` fails. | Fail | REQUIRED_NEGATIVE_TEST |
| `gamePayload` missing `schemaVersion` fails. | Fail | REQUIRED_NEGATIVE_TEST |
| `gamePayload.payload` accepts unknown nested game data. | Pass if generic unknown payload is approved | REQUIRED_EXTENSION_BEHAVIOR |
| Malformed top-level unknown keys still fail unless explicitly allowed. | Fail | REQUIRED_STRICTNESS_GUARD |
| Legacy 7001 `mathBridge` behavior remains compatible until migrated. | Pass or deliberate migration result | REQUIRED_COMPATIBILITY_DECISION |

## UI-Kit Mapper Tests

| Test | Expected result | Evidence label |
|---|---|---|
| Mapper preserves `gamePayload` in mapped model or documented extension field. | Pass after mapper patch | REQUIRED_MAPPER_TEST |
| Mapper handles payloads without `gamePayload`. | Pass | REQUIRED_REGRESSION |
| Mapper does not convert `gamePayload.payload` into wallet/accounting truth. | Pass | SAFETY_GUARD |
| Mapper keeps 7001 behavior stable. | Pass or migration test updated | REQUIRED_COMPATIBILITY_TEST |

## New-Games-Server Tests

| Test | Expected result | Evidence label |
|---|---|---|
| 8001 playround envelope includes `presentationPayload.gamePayload`. | Pass after server patch | REQUIRED_8001_TEST |
| Browser request cannot override authoritative `gamePayload`. | Pass | REQUIRED_AUTHORITY_TEST |
| Resume/reconnect returns enough game payload state. | Pass after persistence patch | REQUIRED_RECOVERY_TEST |
| History/Lasthand/VABS can include or reconstruct v0.3 payload state. | Pass after history contract patch | REQUIRED_HISTORY_TEST |

## Fixture Compatibility Tests

| Test | Expected result | Evidence label |
|---|---|---|
| 24 planning fixtures validate against updated planning fixture schema. | Pass | REQUIRED_FIXTURE_TEST |
| Strict-runtime fixture variants validate against patched core schema. | Pass after fixture updates | REQUIRED_STRICT_SCHEMA_TEST |
| Static renderer can still load all 24 planning fixtures. | Pass | STATIC_RENDERER_REGRESSION |
