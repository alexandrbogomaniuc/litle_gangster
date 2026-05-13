# Source Patch Planning Summary

Status: COMPLETED_PATCH_READY_PLAN_NO_SOURCE_PATCH_APPLIED
Sprint: ProtocolAndSchemaMapper source patch planning for `presentationPayload.gamePayload`

## Decision

Prepare future source changes for reusable support of `presentationPayload.gamePayload`, but do not apply them in this sprint.

Recommended extension point:

```json
{
  "presentationPayload": {
    "gamePayload": {
      "gameKey": "little-gangster",
      "schemaVersion": "v0.3",
      "payload": {}
    }
  }
}
```

## Source Evidence Summary

| Source path | Current behavior | Patch required | Evidence label |
|---|---|---|---|
| `Gamesv1/docs/gs/schemas/*.response.schema.json` | Canonical response JSON schemas define `presentationPayload` with `additionalProperties: false` and no `gamePayload`. | Yes. Add optional `gamePayload` schema to every runtime-envelope
response schema. | PROVEN_CANONICAL_SCHEMA_BLOCKER |
| `Gamesv1/packages/core-protocol/src/schemas.ts` | Zod helper `PresentationPayloadSchema` is strict and lacks `gamePayload`. | Yes. Add `GamePayloadExtensionSchema` and optional `gamePayload`; keep schema strict. |
PROVEN_ZOD_SCHEMA_BLOCKER |
| `Gamesv1/packages/core-protocol/src/IGameTransport.ts` | `RuntimeEnvelopeResponse.presentationPayload` is `Record<string, unknown>`. | Yes for exported helper type clarity, not runtime behavior. | PROVEN_INTERFACE_PERMISSIVE |
| `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Parser already preserves `presentationPayload` as a record. | No required functional patch; add regression coverage if desired. | PROVEN_TRANSPORT_PERMISSIVE |
| `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts` | Local Zod parse consumes generic fields and returns no `gamePayload` field. Unknown keys are not exposed in mapped model. | Yes. Add pass-through field and
tests. | PROVEN_MAPPER_GAP |
| `new-games-server/src/index.ts` | `runtimeEnvelope` accepts optional record payload; 7001 branch emits `mathBridge`; no 8001 branch. | Yes later for emission helper and 8001 branch after approval. | PROVEN_SERVER_PERMISSIVE;
NOT_FOUND_8001 |
| `Gamesv1/games/7001/src/app/runtime/*` | Reads/emits `mathBridge` as 7001-specific reference pattern. | No immediate patch; add compatibility tests before changing. | CANDIDATE_PATTERN |


## Patch Required Summary

| Area | Patch needed | Decision | Evidence label |
|---|---|---|---|
| Canonical JSON schemas | Yes | Add optional `gamePayload` to all runtime-envelope response schemas. | PROVEN_CANONICAL_SCHEMA_BLOCKER |
| Core Zod schema | Yes | Add optional strict `GamePayloadExtensionSchema`. | PROVEN_ZOD_SCHEMA_BLOCKER |
| Transport interface | Yes | Export/document `GamePayloadExtension` and `PresentationPayload` type. | PROVEN_TYPE_CLARITY_GAP |
| HTTP transport parser | No required functional change | Parser is record-permissive; add tests only. | PROVEN_TRANSPORT_PERMISSIVE |
| UI-kit mapper | Yes | Preserve `gamePayload` untouched in mapped presentation model. | PROVEN_MAPPER_GAP |
| New-games-server | Yes later | Add generic helper and 8001 payload branch only after approval/runtime owner proof. | NOT_FOUND_8001 |
| 7001 `mathBridge` | No immediate change | Keep as reference/legacy; do not migrate in first patch. | CANDIDATE_PATTERN |

## Implementation Boundary

No source patch was applied. No backend adapter implementation, production client code, package scaffolding, DB action, wallet call, donor browsing, asset capture, registration artifact, public export, or release approval occurred.
