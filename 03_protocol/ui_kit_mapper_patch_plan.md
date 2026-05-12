# UI-Kit Mapper Patch Plan

Status: PLAN_ONLY_NO_SOURCE_PATCH
Primary file to patch later: `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`

## Current Source State

| Area | Finding | Evidence label |
|---|---|---|
| Local presentation mapper schema | Consumes generic fields such as reel stops, symbol grid, messages, cues, counters, and labels. | PROVEN_GENERIC_MAPPER |
| Unknown extension fields | The mapper does not expose a typed `gamePayload` or game-extension output today. | PROVEN_MAPPER_GAP |
| 7001 behavior | 7001 reads `mathBridge` from raw presentation payload outside the generic mapper pattern. | CANDIDATE_PATTERN |

## Future Patch Options

| Option | Impact | Recommendation |
|---|---|---|
| Add `gamePayload` passthrough to mapped presentation model. | Shared UI-kit can preserve game-specific renderer payloads. | RECOMMENDED |
| Add `extensions` map for unknown presentation payload fields. | More flexible, but less typed and easier to misuse. | ACCEPTABLE_WITH_STRONG_TESTS |
| Require each game client to read raw presentation payload directly. | Avoids shared mapper patch, but duplicates fragile logic. | NOT_RECOMMENDED |
| Add `littleGangsterV03` directly to UI-kit mapper. | Simple for one game, poor reuse for future games. | FALLBACK_ONLY |

## Required Tests Later

- Mapper accepts standard generic payloads with no extension.
- Mapper preserves `gamePayload` without mutating nested payload data.
- Mapper does not treat `gamePayload.payload` as wallet/accounting truth.
- Mapper rejects malformed extension metadata if schema validation is added at this layer.
- 7001 `mathBridge` behavior remains compatible until migrated.

## Implementation Status

No UI-kit source was modified in this sprint. A UI-kit patch is required if the shared presentation mapper must expose `gamePayload` to future client code.

## Source Patch Apply Update - 2026-05-12

Evidence label: PROVEN_APPLIED

The UI-kit mapper patch has now been applied:

- `PresentationGamePayload` was added to the mapper contract.
- The local presentation payload parser accepts optional `gamePayload`.
- `mapPlayRoundToPresentation` preserves `gamePayload` untouched when present.

Evidence label: PROVEN_BY_TEST

The targeted mapper smoke test confirmed the nested payload survives mapping unchanged.
