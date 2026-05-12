# Proposal: Core Protocol Schemas gamePayload

NOT APPLIED
PROPOSAL ONLY
DO NOT TREAT AS SOURCE PATCH

## Target Files

- `Gamesv1/docs/gs/schemas/opengame.response.schema.json`
- `Gamesv1/docs/gs/schemas/playround.response.schema.json`
- `Gamesv1/docs/gs/schemas/featureaction.response.schema.json`
- `Gamesv1/docs/gs/schemas/resumegame.response.schema.json`
- `Gamesv1/docs/gs/schemas/gethistory.response.schema.json`
- `Gamesv1/docs/gs/schemas/closegame.response.schema.json`
- `Gamesv1/packages/core-protocol/src/schemas.ts`

## Proposed JSON Schema Snippet

```diff
 PROPOSAL ONLY - NOT APPLIED
 "presentationPayload": {
   "type": "object",
   "additionalProperties": false,
   "required": ["featureMode", "reelStops", "symbolGrid", "uiMessages", "animationCues", "audioCues", "counters", "labels"],
   "properties": {
+    "gamePayload": {
+      "type": "object",
+      "additionalProperties": false,
+      "required": ["gameKey", "schemaVersion", "payload"],
+      "properties": {
+        "gameKey": { "type": "string", "minLength": 1 },
+        "schemaVersion": { "type": "string", "minLength": 1 },
+        "payload": { "type": "object", "additionalProperties": true }
+      }
+    },
     "featureMode": { "type": "string" }
   }
 }
```

## Proposed Zod Snippet

```diff
 PROPOSAL ONLY - NOT APPLIED
+const GamePayloadExtensionSchema = z
+  .object({
+    gameKey: z.string().min(1),
+    schemaVersion: z.string().min(1),
+    payload: JsonObjectSchema,
+  })
+  .strict();
+
 const PresentationPayloadSchema = z
   .object({
     featureMode: z.string().min(1),
+    gamePayload: GamePayloadExtensionSchema.optional(),
     reelStops: z.array(z.number().int()),
   })
   .strict();
```

## Notes

Keep `gamePayload` optional. Keep the parent schema strict. Do not add `mathBridge` in this patch.
