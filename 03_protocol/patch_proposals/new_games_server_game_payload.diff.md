# Proposal: New-Games-Server gamePayload

NOT APPLIED
PROPOSAL ONLY
DO NOT TREAT AS SOURCE PATCH

## Target File

`new-games-server/src/index.ts`

## Proposed Helper Snippet

```diff
 PROPOSAL ONLY - NOT APPLIED
+function buildGamePayloadExtension(input: {
+  gameKey: string;
+  schemaVersion: string;
+  payload: Record<string, unknown>;
+}): Record<string, unknown> {
+  return {
+    gameKey: input.gameKey,
+    schemaVersion: input.schemaVersion,
+    payload: input.payload,
+  };
+}
```

## Future 8001 Emission Snippet

```diff
 PROPOSAL ONLY - NOT APPLIED
+function buildLittleGangsterPresentationPayload(input: LittleGangsterAdapterInput): Record<string, unknown> {
+  const renderPayload = adaptLittleGangsterV03Result(input);
+  return {
+    featureMode: renderPayload.feature_mode_state?.mode ?? "NONE",
+    reelStops: renderPayload.genericReelStops,
+    symbolGrid: renderPayload.genericSymbolGrid,
+    uiMessages: renderPayload.uiMessages ?? [],
+    animationCues: renderPayload.animationCues ?? [],
+    audioCues: renderPayload.audioCues ?? [],
+    counters: renderPayload.genericCounters ?? [],
+    labels: renderPayload.genericLabels ?? {},
+    gamePayload: buildGamePayloadExtension({
+      gameKey: "little-gangster",
+      schemaVersion: "v0.3",
+      payload: renderPayload,
+    }),
+  };
+}
```

## Notes

Do not add the 8001 branch until runtime owner and backend adapter implementation are approved. Keep wallet/accounting fields outside `gamePayload`.
