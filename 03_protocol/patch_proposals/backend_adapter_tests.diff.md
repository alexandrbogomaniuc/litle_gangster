# Backend Adapter Tests Proposal

NOT APPLIED

PROPOSAL ONLY

DO NOT TREAT AS SOURCE PATCH

## Proposed Test Cases

```diff
+ test("all strict fixtures validate as adapter expected outputs", ...)
+ test("adapter emits presentationPayload.gamePayload for v0.3 result", ...)
+ test("adapter keeps wallet/accounting outside gamePayload", ...)
+ test("adapter rejects browser-authoritative result input", ...)
+ test("adapter preserves max-win cap state", ...)
+ test("adapter maps reconnect restore state", ...)
+ test("adapter maps gethistory replay payload", ...)
+ test("7001 mathBridge behavior is unchanged", ...)
```

## Required Validation Commands

```text
python3 06_resulting_code/planning/fixtures/validate_strict_schema_fixtures.py
tsx new-games-server/test/little-gangster/adapter.test.ts
tsx new-games-server/test/little-gangster/schema.test.ts
tsx new-games-server/test/little-gangster/history-recovery.test.ts
```

Exact commands must be rechecked during the future implementation sprint against local package scripts.

