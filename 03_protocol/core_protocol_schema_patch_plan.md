# Core Protocol Schema Patch Plan

Status: PLAN_ONLY_NO_SOURCE_PATCH
Primary file to patch later: `Gamesv1/packages/core-protocol/src/schemas.ts`
Related file to review later: `Gamesv1/packages/core-protocol/src/IGameTransport.ts`
Related parser to review later: `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts`

## Current Source State

| Area | Finding | Evidence label |
|---|---|---|
| `PresentationPayloadSchema` | Fixed strict shape with no `gamePayload`, `littleGangsterV03`, or `mathBridge`. | PROVEN_SCHEMA_BLOCKER |
| `RuntimeEnvelopeResponseSchema` | Embeds strict `PresentationPayloadSchema`. | PROVEN_SCHEMA_BLOCKER |
| `IGameTransport.ts` | Interface is permissive with `Record<string, unknown>`. | PROVEN_INTERFACE_PERMISSIVE |
| `GsHttpRuntimeTransport.ts` | Parser preserves presentation payload record keys. | PROVEN_TRANSPORT_PERMISSIVE |

## Future Patch Steps

1. Add a reusable `GamePayloadExtensionSchema` to `schemas.ts`.
2. Add optional `gamePayload` to `PresentationPayloadSchema`.
3. Decide whether to keep optional legacy `mathBridge` for 7001 compatibility.
4. Add type exports or inferred TypeScript types for the extension.
5. Align `IGameTransport.ts` docs/types with the canonical schema.
6. Review `GsHttpRuntimeTransport.ts` so parser behavior and schema behavior do not contradict each other.
7. Add unit tests that prove strict schema accepts `gamePayload` and rejects malformed extensions.
8. Add regression tests that existing generic presentation payloads still validate.

## Patch Guardrails

- Do not make the browser authoritative for RNG or results.
- Do not place wallet/accounting data inside `gamePayload`.
- Do not store raw secrets, tokenized URLs, or session credentials in payload examples.
- Do not treat the future patch as approval for Little Gangster release.

## Implementation Status

No core protocol patch was made in this sprint. Future source patch planning remains the next ProtocolAndSchemaMapper step.

## Source Patch Apply Update - 2026-05-12

Evidence label: PROVEN_APPLIED

The approved core protocol patch has now been applied:

- `GamePayloadExtensionSchema` was added in `schemas.ts`.
- `PresentationPayloadSchema` now includes optional `gamePayload`.
- `RuntimeEnvelopeResponseSchema` continues to use the strict parent presentation schema.
- `IGameTransport.ts` now exposes `GamePayloadExtension` and `PresentationPayload`.

Evidence label: PRE_EXISTING_CONFIG_FAILURE

Full TypeScript typecheck is still blocked by existing repo configuration issues. Patch-specific Zod and JSON
schema validations passed.
