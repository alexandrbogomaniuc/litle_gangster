# New Games Server 8001 Payload Branch Proposal

NOT APPLIED

PROPOSAL ONLY

DO NOT TREAT AS SOURCE PATCH

## Proposed Integration Sketch

```diff
 import { adaptLittleGangsterV03ToRuntimeEnvelope } from "./games/little-gangster/adapter";

 app.post("/slot/v1/playround", async (request, reply) => {
   ...
+  if (session?.gameId === 8001) {
+    const authoritativeResult = buildOrLoadApprovedLittleGangsterResult(...);
+    return adaptLittleGangsterV03ToRuntimeEnvelope(authoritativeResult, {
+      sessionId: body.sessionId,
+      requestCounter: body.requestCounter,
+      currentStateVersion: body.currentStateVersion,
+      clientOperationId: body.clientOperationId,
+      wallet: backendWalletResult,
+    });
+  }
   ...
 });
```

## Safety Notes

- The future branch must not use strict fixtures as production outcomes.
- The future branch must not trust browser-provided result payloads.
- Wallet/accounting must stay outside `gamePayload`.
- 7001 `mathBridge` behavior must remain unchanged unless separately approved.

