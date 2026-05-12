# UI-Kit gamePayload Passthrough Tests

Status: TEST_PLAN_ONLY

## Required Tests

- `mapPlayRoundToPresentation` returns existing mapped fields unchanged when no `gamePayload` exists.
- `mapPlayRoundToPresentation` returns `gamePayload` when present.
- Nested `gamePayload.payload` is preserved untouched.
- Mapper does not interpret v0.3 payload as wallet/accounting truth.
- Mapper still throws on missing required generic fields such as `reelStops`.
- 7001 `RuntimeOutcomeMapper` remains compatible with existing `mathBridge` behavior.

## Proposed Test File

`Gamesv1/tests/game/presentation-mapper.test.ts`

## Source Patch Apply Results - 2026-05-12

Evidence label: PROVEN

Patch-specific UI-kit checks were run:

- Existing presentation mapper test suite passed with a Node environment shim for `navigator`.
- A targeted mapper smoke test confirmed `gamePayload.gameKey` is preserved.
- The targeted mapper smoke test confirmed nested `gamePayload.payload` is preserved untouched.

Remaining test gap: add a checked-in assertion to `presentation-mapper.test.ts` when source-test modification is
approved.
