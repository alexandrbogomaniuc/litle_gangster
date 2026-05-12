# New-Games-Server gamePayload Blueprint

Status: PATCH_BLUEPRINT_ONLY_NOT_APPLIED
Target: `new-games-server/src/index.ts`

## Current Behavior

| Source area | Behavior | Evidence label |
|---|---|---|
| `runtimeEnvelope` helper | Accepts optional `presentationPayload?: Record<string, unknown>`. | PROVEN_SERVER_PERMISSIVE |
| 7001 playround branch | Emits `buildCrazyRoosterPresentationPayload(...)` when `session.gameId === 7001`. | PROVEN_7001_BRANCH |
| 7001 buy-feature branch | Emits the same 7001 presentation payload for feature action. | PROVEN_7001_BRANCH |
| 8001/Little Gangster branch | Not found. | NOT_FOUND_8001 |

## Where Should gamePayload Be Included?

Inside server-created `presentationPayload`, next to existing generic fields:

```ts
return {
  featureMode: "...",
  reelStops,
  symbolGrid,
  uiMessages,
  animationCues,
  audioCues,
  counters,
  labels,
  gamePayload: {
    gameKey: "little-gangster",
    schemaVersion: "v0.3",
    payload: littleGangsterV03RenderPayload,
  },
};
```

## Is a Generic Payload Builder Needed?

Recommended. A small helper should wrap game-specific render payloads consistently:

```ts
function buildGamePayloadExtension(input: {
  gameKey: string;
  schemaVersion: string;
  payload: Record<string, unknown>;
}): Record<string, unknown> {
  return {
    gameKey: input.gameKey,
    schemaVersion: input.schemaVersion,
    payload: input.payload,
  };
}
```

## Should an 8001 Branch Be Added Now Or Later?

Later. Evidence label: BLOCKED_RUNTIME_OWNER. The branch should not be added until Little Gangster/8001 runtime owner and authoritative result source are proven or explicitly approved for implementation.

## Fixture/Sample Payload For Validation

Use a strict-runtime variant of one non-production fixture, not a production result. The sample must:

- use fake round/session/operation identifiers
- include numeric `stateVersion`
- use canonical `round.status`
- place v0.3 render state only under `presentationPayload.gamePayload.payload`
- keep wallet/accounting in `wallet`, not in `gamePayload`

## Wallet/Accounting Separation

`gamePayload` must not include authoritative wallet balances, reserve/settle results, raw player secrets, raw session credentials, or production RNG seed material.

## Future Tests

- Server emits `gamePayload` for a controlled test fixture only after schema patch.
- 7001 existing `mathBridge` path remains unchanged.
- 8001 branch is absent or disabled until runtime owner approval.
- Browser request cannot inject authoritative `gamePayload` into a server response.
