# Backend Adapter Implementation Planning Report

Sprint: ProtocolAndSchemaMapper backend adapter implementation planning

Status: PLANNING_COMPLETE_IMPLEMENTATION_BLOCKED.

This report defines the future Little Gangster backend/runtime adapter plan. It does not implement the adapter, does
not modify Staging source, does not create `Gamesv1/games/8001`, and does not unlock GameClientBuilder
implementation.

## Source-Backed Findings

| Finding | Evidence label | Meaning |
|---|---|---|
| `presentationPayload.gamePayload` is present in patched core-protocol schema/type files. | PROVEN | The reusable envelope extension is available for future server output. |
| UI-kit `PremiumPresentationMapper` preserves `gamePayload` untouched. | PROVEN | Future clients can receive game-specific render payloads without UI-kit game logic. |
| `new-games-server/src/index.ts` has a generic `runtimeEnvelope(...)` helper with optional `presentationPayload`. | PROVEN | A future adapter can feed a completed presentation payload into the current envelope builder. |
| `new-games-server/src/index.ts` has 7001-only `buildCrazyRoosterPresentationPayload(...)`. | PROVEN_REFERENCE_ONLY | 7001 is a reference branch, not Little Gangster proof. |
| `Gamesv1/games/8001` was not found in targeted inspection. | NOT_FOUND | A Little Gangster runtime package does not currently exist in the inspected Staging tree. |
| `new-games-server/src/games/little-gangster/adapter.ts` was not found. | NOT_FOUND | No approved backend adapter exists today. |
| 24 strict fixtures validate against patched response schemas and v0.3 result schema. | PROVEN_TEST_CONTRACT | Fixtures are valid expected-output examples for future adapter tests. |

## Direct Planning Answer

The future adapter should be implemented as a backend-owned module that converts an authoritative v0.3 Little
Gangster result into a canonical `/slot/v1` response envelope containing:

- canonical `wallet`, `round`, `feature`, `restore`, `idempotency`, `retry`, and optional `history` fields;
- generic presentation fields for current shell/UI-kit compatibility;
- `presentationPayload.gamePayload.gameKey = "little-gangster"`;
- `presentationPayload.gamePayload.schemaVersion = "v0.3"`;
- `presentationPayload.gamePayload.payload = <v0.3 render payload>`.

Recommended first implementation target is `new-games-server/src/games/little-gangster/`, plus a small explicit
8001 emission branch in `new-games-server/src/index.ts`. This is the least speculative target because the current
server already owns `/slot/v1` envelope construction. A later `Gamesv1/games/8001` package can consume that output
from the browser side after the backend path exists.

## Implementation Remains Blocked

Implementation is blocked until explicit approval for Staging source changes and until the runtime owner decision is
made. This planning sprint does not prove the 8001 runtime owner and does not prove a production result API contract.

