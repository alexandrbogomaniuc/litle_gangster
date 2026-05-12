# Proposal: UI-Kit Presentation Mapper gamePayload

NOT APPLIED
PROPOSAL ONLY
DO NOT TREAT AS SOURCE PATCH

## Target File

`Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`

## Proposed Snippet

```diff
 PROPOSAL ONLY - NOT APPLIED
+const GamePayloadSchema = z
+  .object({
+    gameKey: z.string().min(1),
+    schemaVersion: z.string().min(1),
+    payload: z.record(z.string(), z.unknown()),
+  })
+  .strict()
+  .optional();
+
 export interface RoundPresentationModel {
   labels: Record<string, string>;
+  gamePayload?: z.infer<typeof GamePayloadSchema>;
 }
 
 const PresentationPayloadSchema = z.object({
   reelStops: ReelStopsSchema,
+  gamePayload: GamePayloadSchema,
 });
 
 return {
   labels: payload.labels,
+  gamePayload: payload.gamePayload,
 };
```

## Notes

Pass through `gamePayload` untouched. Do not transform v0.3 payload inside the shared mapper.
