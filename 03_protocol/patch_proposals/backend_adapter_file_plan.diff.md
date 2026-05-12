# Backend Adapter File Plan Proposal

NOT APPLIED

PROPOSAL ONLY

DO NOT TREAT AS SOURCE PATCH

## Proposed Future Files

```text
new-games-server/src/games/little-gangster/resultTypes.ts
new-games-server/src/games/little-gangster/presentationPayload.ts
new-games-server/src/games/little-gangster/statePersistence.ts
new-games-server/src/games/little-gangster/historyMapper.ts
new-games-server/src/games/little-gangster/fixtures.ts
new-games-server/src/games/little-gangster/adapter.ts
new-games-server/test/little-gangster/adapter.test.ts
new-games-server/test/little-gangster/schema.test.ts
new-games-server/test/little-gangster/history-recovery.test.ts
```

## Proposed Responsibility Split

```diff
+ resultTypes.ts
+   exports LittleGangsterV03AuthoritativeResult
+   exports LittleGangsterAdapterContext
+
+ presentationPayload.ts
+   exports buildLittleGangsterPresentationPayload(result, context)
+   returns generic fields plus presentationPayload.gamePayload
+
+ statePersistence.ts
+   exports mapLittleGangsterRestoreState(result, context)
+
+ historyMapper.ts
+   exports mapLittleGangsterHistoryRecord(result, context)
+
+ adapter.ts
+   exports adaptLittleGangsterV03ToRuntimeEnvelope(result, context)
```

