# Runtime Payload Adapter Gap Analysis

## Status

The v0.3 payload adapter is DEFINED_AS_REQUIREMENTS_NOT_IMPLEMENTED_NOT_PROVEN.

## Proven Generic Inputs

- `/slot/v1` generic endpoints exist.
- `RuntimeEnvelopeResponse` exists.
- `presentationPayload` is the browser-visible payload.
- Existing sample/template games map runtime responses into presentation models.

## Missing Little Gangster Adapter Proof

| Gap | Status | Why it blocks implementation |
|---|---|---|
| 8001 runtime owner | NOT_FOUND | Client cannot target an unproven result source. |
| v0.3 payload location | BLOCKED | Current generic `presentationPayload` schema is strict and not yet v0.3-aware. |
| v0.3 field serialization | BLOCKED | Cascade/golden/rainbow/coin/feature/cap/state fields need reviewed payload form. |
| history/recovery payload | BLOCKED | Replay/reconnect must preserve enough v0.3 state. |
| math package consumption | NOT_FOUND | No backend source proves direct use of project `math_package.json`. |

## Required Adapter Output

The backend/runtime must produce an envelope where:

- wallet/accounting truth remains in `wallet` and `round`;
- feature decisions remain in `feature`;
- restore/recovery remains in `restore`;
- idempotency/retry remains in `idempotency` and `retry`;
- v0.3 animation/result render state is exposed in `presentationPayload` or a reviewed equivalent.

## Decision

Do not generate client code until this adapter is proven or fixture-approved.

## FixturePlanning Update

Static non-production fixture examples now define the renderer-facing data that a future backend/runtime adapter must eventually emit or translate.

The preferred planning extension is `presentationPayload.gamePayload`, with `presentationPayload.littleGangsterV03` documented as fallback only.

Remaining gaps:

- Little Gangster / 8001 runtime owner remains unproven.
- v0.3 result API remains unproven.
- `presentationPayload.gamePayload` remains pending schema review.
- Backend/runtime adapter implementation remains required before production client implementation.
