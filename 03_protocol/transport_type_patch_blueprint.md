# Transport Type Patch Blueprint

Status: PATCH_BLUEPRINT_ONLY_NOT_APPLIED
Targets:

- `Gamesv1/packages/core-protocol/src/IGameTransport.ts`
- `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` for review/tests only

## Current Behavior

| Source | Current behavior | Patch required | Evidence label |
|---|---|---|---|
| `IGameTransport.ts` | `RuntimeEnvelopeResponse.presentationPayload` is `Record<string, unknown>`. | Type clarity patch recommended. | PROVEN_INTERFACE_PERMISSIVE |
| `GsHttpRuntimeTransport.ts` | `parseRuntimeEnvelope` stores `presentationPayload` from `asRecord(record.presentationPayload)` and returns it unchanged. | No functional parser patch required. | PROVEN_TRANSPORT_PERMISSIVE |

## Recommended Type Addition

Add reusable types without narrowing existing runtime behavior too aggressively:

```ts
export interface GamePayloadExtension<TPayload extends Record<string, unknown> = Record<string, unknown>> {
  gameKey: string;
  schemaVersion: string;
  payload: TPayload;
}

export interface PresentationPayload extends Record<string, unknown> {
  gamePayload?: GamePayloadExtension;
}
```

Then update:

```ts
presentationPayload: PresentationPayload;
```

## Parser Decision

`GsHttpRuntimeTransport.ts` is already permissive enough to carry `gamePayload`. The patch should not transform or validate `gamePayload` in the transport parser unless the platform decides transport should enforce schema locally.

Recommended parser test instead:

- mock runtime response contains `presentationPayload.gamePayload`
- `GsHttpRuntimeTransport.playround()` returns the nested object unchanged
- no wallet/accounting field is inferred from `gamePayload`

## Compile/Test Commands For Future Patch

From `Gamesv1` workspace root:

```bash
node --experimental-transform-types tests/contract/browser-runtime.contract.test.ts
corepack pnpm run test:contract
```

If TypeScript workspace build coverage is available:

```bash
corepack pnpm --filter @games/premium-slot build
```

## Evidence Labels

- PROVEN_INTERFACE_PERMISSIVE: current interface already uses `Record<string, unknown>`.
- PROVEN_TRANSPORT_PERMISSIVE: current parser preserves record-shaped presentation payload.
- REQUIRED_TYPE_CLARITY: exported types should document the canonical extension.
