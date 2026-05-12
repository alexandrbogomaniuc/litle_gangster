# Source Patch Order And Rollback

Status: PLAN_ONLY_NO_SOURCE_PATCH_APPLIED

## Recommended Patch Order

1. Patch canonical JSON response schemas in `Gamesv1/docs/gs/schemas`.
2. Patch `Gamesv1/packages/core-protocol/src/schemas.ts` to mirror the canonical schema.
3. Patch `Gamesv1/packages/core-protocol/src/IGameTransport.ts` for exported type clarity.
4. Add/adjust browser-runtime contract fixtures/tests for `gamePayload`.
5. Patch `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts` for pass-through.
6. Add/adjust `Gamesv1/tests/game/presentation-mapper.test.ts`.
7. Patch `new-games-server/src/index.ts` only after schema patch acceptance and runtime-owner approval.
8. Add new-games-server tests for sample emission and wallet/accounting separation.
9. Defer Little Gangster/8001 adapter implementation until explicit approval.

## Rollback Plan

Each future patch should be committed separately or otherwise staged separately:

| Patch group | Rollback action |
|---|---|
| JSON schema patch | Revert schema-file changes and fixture additions. |
| Zod/type patch | Revert `schemas.ts` and `IGameTransport.ts` changes. |
| UI-kit mapper patch | Revert mapper model/schema/test changes. |
| New-games-server patch | Revert helper/branch/tests; preserve schema patch if accepted independently. |
| 8001 adapter patch | Revert only 8001 package/module changes. |

## Stop Conditions

- Any existing generic runtime fixture fails after schema patch.
- 7001 build or mapper tests regress.
- UI-kit mapper mutates nested `gamePayload.payload`.
- Server test shows wallet/accounting leakage into `gamePayload`.
- Any test indicates browser-produced payload is treated as authoritative.

## Approval Boundary

Approval is required before modifying any Staging source file. This sprint did not apply source patches.
