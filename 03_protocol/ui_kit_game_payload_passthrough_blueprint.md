# UI-Kit gamePayload Passthrough Blueprint

Status: PATCH_BLUEPRINT_ONLY_NOT_APPLIED
Target: `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`

## Current Behavior

`PresentationPayloadSchema.safeParse(payloadObject)` parses known generic fields. The mapper returns `RoundPresentationModel` with reels, symbol grid, counters, messages, sound cues, animation cues, and labels. It does not expose `gamePayload`.

Evidence label: PROVEN_MAPPER_GAP.

## Recommended Patch

Add a schema and model field that preserves `gamePayload` untouched:

```ts
const GamePayloadSchema = z
  .object({
    gameKey: z.string().min(1),
    schemaVersion: z.string().min(1),
    payload: z.record(z.string(), z.unknown()),
  })
  .strict()
  .optional();
```

Add to local `PresentationPayloadSchema`:

```ts
gamePayload: GamePayloadSchema,
```

Add to `RoundPresentationModel`:

```ts
gamePayload?: z.infer<typeof GamePayloadSchema>;
```

Return it from `mapPlayRoundToPresentation`:

```ts
gamePayload: payload.gamePayload,
```

## Should Mapper Transform gamePayload?

No. It should pass `gamePayload` through untouched. Game-specific renderers should validate `gamePayload.payload` against their own result schema.

## Required Tests

- Existing presentation mapper tests pass unchanged.
- Mapper returns `gamePayload` when present.
- Mapper preserves `gameKey`, `schemaVersion`, and nested payload identity/shape.
- Mapper still throws when required generic `reelStops` is missing.
- Mapper rejects malformed `gamePayload` metadata if local schema validation is active.

## Evidence Labels

- PROVEN_GENERIC_MAPPER: current mapper handles generic presentation fields.
- PROVEN_MAPPER_GAP: current mapped model drops/excludes extension data.
- RECOMMENDED_PASSTHROUGH: shared mapper should not interpret game-specific v0.3 payload.
