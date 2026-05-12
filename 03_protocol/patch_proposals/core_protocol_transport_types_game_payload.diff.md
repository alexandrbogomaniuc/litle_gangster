# Proposal: Core Protocol Transport Types gamePayload

NOT APPLIED
PROPOSAL ONLY
DO NOT TREAT AS SOURCE PATCH

## Target File

`Gamesv1/packages/core-protocol/src/IGameTransport.ts`

## Proposed Snippet

```diff
 PROPOSAL ONLY - NOT APPLIED
+export interface GamePayloadExtension<TPayload extends Record<string, unknown> = Record<string, unknown>> {
+  gameKey: string;
+  schemaVersion: string;
+  payload: TPayload;
+}
+
+export interface PresentationPayload extends Record<string, unknown> {
+  gamePayload?: GamePayloadExtension;
+}
+
 export interface RuntimeEnvelopeResponse {
   ok: boolean;
-  presentationPayload: Record<string, unknown>;
+  presentationPayload: PresentationPayload;
 }
```

## Parser Note

`GsHttpRuntimeTransport.ts` already preserves `presentationPayload` records. Add a regression test before changing parser logic.
