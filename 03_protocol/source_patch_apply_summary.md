# Source Patch Apply Summary

Sprint: ProtocolAndSchemaMapper source patch apply for `presentationPayload.gamePayload`

Status: applied within approved scope

## Direct Result

The reusable optional `presentationPayload.gamePayload` extension was applied to the approved Staging source
schema/type/mapper targets.

The patch does not implement a Little Gangster backend adapter, does not create an 8001 runtime package, and
does not add production client code.

## Staging Files Modified

- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/opengame.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/playround.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/featureaction.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/resumegame.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/gethistory.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/closegame.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/schemas.ts`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/IGameTransport.ts`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`

## Staging Files Reviewed But Not Modified

- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts`
- `[STAGING_ROOT]/platform-source/platform/new-games-server/src/index.ts`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/games/7001/src/app/runtime/provisionalMathSource.ts`

## Patch Details

Evidence label: PROVEN_APPLIED

- JSON response schemas now allow optional `presentationPayload.gamePayload`.
- The parent `presentationPayload` object remains strict with `additionalProperties: false`.
- Core-protocol Zod runtime schema now includes optional `gamePayload`.
- Core transport types now expose `GamePayloadExtension` and `PresentationPayload`.
- UI-kit presentation mapper now preserves `gamePayload` untouched in `RoundPresentationModel`.
- Existing 7001 `mathBridge` behavior was not removed or migrated.

## New-Games Server Decision

Evidence label: LIKELY_ALREADY_PERMISSIVE

`new-games-server/src/index.ts` was not modified. Its runtime-envelope helper already accepts an optional
`presentationPayload?: Record<string, unknown>`, and adding a Little Gangster or sample emission branch would
cross into backend/runtime adapter behavior that this sprint forbids.

Blocker retained: `new_games_server_8001_payload_branch_missing`.

## Gate Status

- Backend adapter implementation allowed: false
- GameClientBuilder implementation allowed: false
- Registration generation allowed: false
- Wallet/API testing allowed: false
- Release allowed: false
