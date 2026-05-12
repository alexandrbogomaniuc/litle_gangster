# Core Protocol gamePayload Schema Tests

Status: TEST_PLAN_ONLY

## Positive Tests

- Existing runtime response fixture without `gamePayload` remains valid.
- Runtime response fixture with valid `presentationPayload.gamePayload` is valid.
- `gamePayload.payload` accepts nested v0.3 render object data.

## Negative Tests

- Missing `gameKey` fails.
- Missing `schemaVersion` fails.
- Non-object `payload` fails if `JsonObjectSchema` is selected.
- Unknown top-level `presentationPayload` key still fails.
- Wallet/accounting fields inside `gamePayload` fail policy review even if structurally valid.

## Required Files To Add Later

- A positive `gamePayload` runtime response fixture.
- Negative contract cases inside browser-runtime contract test or a dedicated schema test.

## Source Patch Apply Results - 2026-05-12

Evidence label: PROVEN

Patch-specific schema checks were run:

- Six canonical response JSON schemas parse.
- Each `presentationPayload` schema occurrence accepts valid `gamePayload`.
- Each `presentationPayload` schema occurrence rejects an unknown top-level presentation field.
- `RuntimeEnvelopeResponseSchema` accepts valid `gamePayload`.
- `RuntimeEnvelopeResponseSchema` rejects an unknown top-level presentation field.

Remaining test gap: add durable checked-in tests in the platform repo when source-test modification is approved.
