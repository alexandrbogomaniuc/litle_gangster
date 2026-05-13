# Source Patch Apply Rollback Plan

Sprint: ProtocolAndSchemaMapper source patch apply for `presentationPayload.gamePayload`

Pre-patch git root: `[DEV_ROOT]`

Pre-patch branch: `Codex`

Pre-patch commit hash : [REDACTED_FIXTURE]

## Git Topology Caveat

The Staging source resolves to the parent git root `[DEV_ROOT]`, and the Staging subtree is
reported as untracked from that parent repository. Because of this, rollback cannot rely solely on tracked-file
checkout unless the source is later placed under a clean tracked baseline.

## Files To Revert

- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/opengame.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/playround.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/featureaction.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/resumegame.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/gethistory.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/docs/gs/schemas/closegame.response.schema.json`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/schemas.ts`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/IGameTransport.ts`
- `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`

## Rollback If Files Become Tracked

Do not run this without explicit user approval:

```text
git -C [STAGING_ROOT] checkout -- <changed target paths>
```

## Manual Rollback Guidance

If the Staging subtree remains untracked, manually remove only the `gamePayload` additions from the files listed
above:

- Remove the `gamePayload` JSON Schema property from each `presentationPayload.properties` object.
- Remove `GamePayloadExtensionSchema` and the optional `gamePayload` field from core-protocol `schemas.ts`.
- Remove `GamePayloadExtension`, `PresentationPayload`, and the `PresentationPayload` replacement type from
  `IGameTransport.ts`.
- Remove `PresentationGamePayload`, `GamePayloadSchema`, optional `gamePayload`, and passthrough mapping from
  `PremiumPresentationMapper.ts`.

## Rollback Verification

After rollback, run:

```text
python3 -m json.tool <six response schema files>
rg -n "gamePayload" <changed target paths>
```

Expected rollback result: no `gamePayload` occurrences remain in the reverted target files, and JSON schemas
still parse.
