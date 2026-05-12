# Presentation Payload Extension Test Matrix

Status: TEST_PLAN_ONLY_NOT_RUN.

| Test | Scope | Expected result | Evidence label |
|---|---|---|---|
| Strict schema rejects unknown pre-change | Baseline core schema | `gamePayload` fails before schema update. | PROVEN_CURRENT_BEHAVIOR |
| Strict schema accepts `gamePayload` post-review | Core protocol | Proposed extension passes. | BLOCKED_SCHEMA_CHANGE |
| Shared mapper behavior | UI kit | Generic mapper preserves or safely ignores extension without destroying game-specific access. | REQUIRED_REVIEW |
| Fallback field validation | Core protocol | `littleGangsterV03` passes only if fallback selected. | CONDITIONAL |
| Generic fields still valid | Core protocol and UI kit | `featureMode`, `reelStops`, `symbolGrid`, cues, counters, labels remain valid. | REQUIRED_TEST |
| No overloaded labels | Payload review | v0.3 authoritative render state is not hidden only in labels/counters. | REQUIRED_TEST |
