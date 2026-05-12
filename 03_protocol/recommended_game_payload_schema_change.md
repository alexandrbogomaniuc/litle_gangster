# Recommended Game Payload Schema Change

Status: PLANNING_ONLY_REQUIRES_SOURCE_PATCH_LATER
Recommended extension: `presentationPayload.gamePayload`
Fallback extension: `presentationPayload.littleGangsterV03`

## Recommended Shape

The reusable presentation extension should be a generic optional field on `PresentationPayloadSchema`:

```ts
const GamePayloadExtensionSchema = z.object({
  gameKey: z.string().min(1),
  schemaVersion: z.string().min(1),
  payload: z.unknown(),
}).strict();
```

For Little Gangster v0.3, the intended payload is:

```json
{
  "gameKey": "little-gangster",
  "schemaVersion": "v0.3",
  "payload": {
    "...": "v0.3 renderer payload"
  }
}
```

## Evidence Labels

| Claim | Evidence label |
|---|---|
| Core schema must be patched before this is approved. | PROVEN_SCHEMA_PATCH_REQUIRED |
| Transport/server paths can already carry record-like presentation payloads in practice. | CONFLICTING_EVIDENCE_PERMISSIVE_PATH |
| 7001 `mathBridge` proves an adapter-style payload has precedent. | CANDIDATE_PATTERN |
| 7001 `mathBridge` does not prove Little Gangster or reusable future-game support. | NOT_PROVEN_FOR_8001 |

## Compatibility Policy

A future patch should choose one of these compatibility paths:

1. Add `gamePayload` and keep `mathBridge` as legacy 7001-only compatibility until 7001 migrates.
2. Add `gamePayload` and migrate 7001 `mathBridge` into `gamePayload` through a deliberate migration plan.
3. Reject generic extension and add `littleGangsterV03` as a game-specific fallback.

Option 1 is the safest incremental path. It avoids breaking 7001 while creating the reusable contract Little Gangster needs.

## Not Approved In This Sprint

This document does not approve or apply any source patch. Backend adapter implementation remains blocked until the schema/type/server changes are explicitly approved and implemented in the correct source repositories.

## Source Patch Apply Update - 2026-05-12

Evidence label: PROVEN_APPLIED

The first incremental compatibility path was applied: optional `presentationPayload.gamePayload` was added while
leaving existing 7001 `mathBridge` behavior unchanged.

The applied reusable shape is:

```json
{
  "gameKey": "little-gangster",
  "schemaVersion": "v0.3",
  "payload": {}
}
```

Evidence label: BLOCKED_FOR_ADAPTER_IMPLEMENTATION

This schema change does not approve backend adapter implementation. A future 8001 adapter still needs explicit
approval, runtime owner proof, and tests.
