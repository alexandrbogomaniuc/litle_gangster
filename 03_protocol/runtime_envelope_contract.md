# Runtime Envelope Contract

## Status

`RuntimeEnvelopeResponse` is PROVEN as a generic current source contract. Little Gangster-specific contents remain adapter-dependent.

## Generic Envelope Fields

| Field | Purpose | Evidence status |
|---|---|---|
| `ok` | Success marker. | PROVEN |
| `requestId` | Correlates runtime response to client operation. | PROVEN |
| `sessionId` | Runtime session identifier. | PROVEN |
| `requestCounter` | Monotonic client/runtime sequencing. | PROVEN |
| `stateVersion` | Runtime state version. | PROVEN |
| `wallet` | Balance/currency/accounting summary. | PROVEN |
| `round` | Current round status, bet/win, and outcome hash. | PROVEN |
| `feature` | Feature mode, remaining actions, allowed actions, feature context. | PROVEN |
| `presentationPayload` | Browser-visible rendering payload. | PROVEN generic |
| `restore` | Unfinished round/recovery state. | PROVEN |
| `idempotency` | Duplicate/replay safety state. | PROVEN |
| `retry` | Client retry policy. | PROVEN |
| `history` | Optional history response payload. | PROVEN generic |

## Boundaries

Wallet fields are accounting state, not animation logic. `presentationPayload` is the renderer-facing payload, not wallet truth. Browser/client code must not generate authoritative outcomes, RNG, balance changes, or round completion.

## Little Gangster Gap

The generic envelope is ready for planning, but it does not yet define where all v0.3 fields live. The v0.3 adapter must either:

- extend `presentationPayload` with a Little Gangster v0.3 subobject, or
- map v0.3 fields into a reviewed generic presentation schema.

Either path requires runtime API review and source-backed approval before client implementation.
