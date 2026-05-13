# Backend Runtime Adapter Proof Report

Sprint: ProtocolAndSchemaMapper backend/runtime adapter proof  
Status: PROOF_COMPLETED_WITH_BLOCKERS. This is planning/proof documentation only.

No client code, runtime code, backend adapter implementation, registration artifact, DB/Cassandra action, wallet/API call, donor browsing, asset capture, public export, GitHub update, or release approval occurred.

## Direct Answers

| Question | Answer | Evidence label |
|---|---|---|
| Who should own Little Gangster runtime result generation? | A backend/runtime component must own it. The strongest candidate is a future New Games `/slot/v1` game-specific adapter, but no Little Gangster/8001 owner is proven.
Browser/client ownership is forbidden. | PROVEN_BOUNDARY; CANDIDATE_OWNER; NOT_FOUND_8001 |
| Can current `/slot/v1` envelope support Little Gangster v0.3? | The generic envelope can carry wallet, round, feature, restore, idempotency, retry, history, and `presentationPayload`. The current strict core schema does not yet accept a
v0.3 game extension. | PROVEN_GENERIC; BLOCKED_SCHEMA_EXTENSION |
| Can `presentationPayload.gamePayload` be used today? | Not under the strict core `PresentationPayloadSchema`, because unknown root fields are rejected. It is the recommended extension to propose, but it requires core-protocol schema
review/change. | BLOCKED_PENDING_SCHEMA_CHANGE |
| Is `presentationPayload.littleGangsterV03` needed as fallback? | It is a fallback only if the schema/runtime team rejects a reusable generic `gamePayload`. It also requires schema review/change. | CANDIDATE_FALLBACK |
| What backend adapter must exist? | A server-side Little Gangster adapter must transform authoritative result output into v0.3 render payload, then wrap it in the generic `/slot/v1` envelope. | REQUIRED_NOT_IMPLEMENTED |
| Can current new-games server/core-protocol support this without schema changes? | No for canonical strict schema validation. The HTTP transport and server payload builder are permissive records in places, but the exported strict Zod
schema blocks unknown presentation fields. | CONFLICTING_EVIDENCE; BLOCKED_SCHEMA_EXTENSION |
| Are the 24 fixtures compatible? | They are compatible with the proposed adapter concept and safe for planning. They are not strictly compatible with current core schema without adjustments to status casing, numeric state version,
restore/idempotency field names, numeric symbol grids, and the `gamePayload` extension. | PLANNING_COMPATIBLE; STRICT_SCHEMA_CONFLICT |
| What history/recovery state is needed? | Store or reconstruct v0.3 presentation state, round identity, bet/win, state version, operation/idempotency correlation, restore state, and VABS/Lasthand-equivalent replay payload. Exact 8001
persistence remains unproven. | REQUIRED; BLOCKED_FOR_8001 |
| Can GameClientBuilder implementation start? | No. Runtime owner 8001, result API contract, schema extension, backend adapter implementation, final assets, and explicit build approval remain missing. | BLOCKED |
| Can a static prototype start later? | Yes only as a fixture-only non-production renderer prototype after explicit user approval. It must not be treated as production implementation or runtime proof. | CONDITIONAL_PLANNING_ONLY |

## Source Evidence Summary

| Source | Finding | Evidence label |
|---|---|---|
| `Gamesv1/packages/core-protocol/src/schemas.ts:146-164` | `PresentationPayloadSchema` defines generic fields and ends with `.strict()`, so `gamePayload` and `littleGangsterV03` are not accepted today. | PROVEN_SCHEMA_BLOCKER |
| `Gamesv1/packages/core-protocol/src/schemas.ts:190-205` | `RuntimeEnvelopeResponseSchema` embeds the strict `PresentationPayloadSchema`. | PROVEN_SCHEMA_BLOCKER |
| `Gamesv1/packages/core-protocol/src/IGameTransport.ts:131-145` | The TypeScript transport interface uses `presentationPayload: Record<string, unknown>`, which is permissive. | PROVEN_INTERFACE_PERMISSIVE |
| `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts:55-108` | HTTP parser treats envelope groups as records and does not validate specific presentation root keys. | PROVEN_TRANSPORT_PERMISSIVE |
| `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts:65-73` | Shared UI mapper consumes generic reel/grid/message/cue/counter/label fields and does not expose a game extension. | PROVEN_GENERIC_MAPPER |
| `new-games-server/src/index.ts:514-575` | Existing Crazy Rooster payload builder emits generic fields plus `mathBridge`, proving a practical game-specific extension pattern. | CANDIDATE_PATTERN |
| `new-games-server/src/index.ts:1860-1868` | `/slot/v1/playround` only emits the special presentation payload when `session.gameId === 7001`; no 8001 branch exists. | NOT_FOUND_8001 |
| `Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts:54-80` | Game 7001 reads `presentationPayload.mathBridge` as a custom bridge. This is a reference pattern, not Little Gangster proof. | CANDIDATE_PATTERN |
| Targeted 8001/Little Gangster source scan | Only incidental 8001 test/reference hits were found; no Little Gangster runtime package, route, or adapter was found. | NOT_FOUND_8001 |

## Core Conclusion

The backend/runtime adapter path is now defined, but implementation is blocked. The most useful future path is to add a reviewed generic `presentationPayload.gamePayload` extension, then implement a Little Gangster backend adapter that
produces that payload from a server-owned authoritative result.

Because current source has both permissive runtime records and strict canonical Zod schemas, the safe conclusion is: **schema extension review is required before production implementation**.
