# Core Protocol gamePayload Patch Blueprint

Status: PATCH_BLUEPRINT_ONLY_NOT_APPLIED
Primary targets:

- `Gamesv1/docs/gs/schemas/*.response.schema.json`
- `Gamesv1/packages/core-protocol/src/schemas.ts`

## A. Exact Schema Change Needed

Add an optional `presentationPayload.gamePayload` field to every runtime envelope response schema that contains `presentationPayload`.

The extension should require:

- `gameKey`: non-empty string
- `schemaVersion`: non-empty string
- `payload`: object with arbitrary nested JSON properties

## B. Zod Blueprint

Use the existing `JsonObjectSchema` helper rather than `z.unknown()` for the first reusable patch:

```ts
const GamePayloadExtensionSchema = z
  .object({
    gameKey: z.string().min(1),
    schemaVersion: z.string().min(1),
    payload: JsonObjectSchema,
  })
  .strict();
```

Then add it to `PresentationPayloadSchema`:

```ts
gamePayload: GamePayloadExtensionSchema.optional(),
```

Keep `.strict()` on `PresentationPayloadSchema` so only known top-level keys are accepted.

## C. JSON Schema Blueprint

For each runtime-envelope response schema, add this property under `presentationPayload.properties`:

```json
"gamePayload": {
  "type": "object",
  "additionalProperties": false,
  "required": ["gameKey", "schemaVersion", "payload"],
  "properties": {
    "gameKey": { "type": "string", "minLength": 1 },
    "schemaVersion": { "type": "string", "minLength": 1 },
    "payload": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

Do not add `gamePayload` to the required list. It must be optional for backward compatibility.

## D. Should gamePayload Be Optional?

Yes. Evidence label: REQUIRED_BACKWARD_COMPATIBILITY. Existing games and runtime envelope fixtures must remain valid without game-specific payloads.

## E. z.unknown vs z.record vs Typed Game Schema

| Option | Decision | Evidence label |
|---|---|---|
| `z.unknown()` | Not recommended for the first core patch because it accepts primitives. | STRICTNESS_GUARD |
| `JsonObjectSchema` / `z.record(z.string(), z.unknown())` | Recommended for core reusable schema because render payloads should be object-shaped but game-specific. | RECOMMENDED |
| Typed by game | Future game-package responsibility, not core-protocol responsibility. | REQUIRED_GAME_LAYER_VALIDATION |

## F. Should Schema Remain Strict?

Yes. Keep the parent presentation schema strict and add only the known optional extension. Do not use `.passthrough()` at the presentation root because it would hide accidental payload drift.

## G. mathBridge Policy

Do not add or migrate `mathBridge` in the first `gamePayload` patch. Keep 7001 behavior unchanged and add compatibility tests. A future migration may wrap 7001-style data in `gamePayload`, but that is separate work.

## H. Required Backward Compatibility Tests

- Existing response fixtures validate unchanged.
- Response fixture with valid `gamePayload` validates.
- Response with malformed `gamePayload` fails.
- Response with unknown top-level presentation field still fails.
- 7001 `mathBridge` behavior remains unchanged in its current practical path.

## Evidence Labels

- PROVEN_CANONICAL_SCHEMA_BLOCKER: response JSON schemas use `additionalProperties: false` in `presentationPayload`.
- PROVEN_ZOD_SCHEMA_BLOCKER: Zod `PresentationPayloadSchema` is strict and lacks `gamePayload`.
- REQUIRED_BACKWARD_COMPATIBILITY: existing runtime envelopes must continue without game extensions.
