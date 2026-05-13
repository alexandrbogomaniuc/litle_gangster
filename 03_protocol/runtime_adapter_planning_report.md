# Runtime Adapter Planning Report

Sprint: ProtocolAndSchemaMapper runtime adapter planning

Status: PLANNING_ONLY. No client code, runtime code, registration artifacts, DB changes, wallet calls, donor browsing, asset capture, or release approval were performed.

## Direct Answers

| Question | Answer | Evidence label |
|---|---|---|
| What is the generic `/slot/v1` runtime envelope structure? | A generic envelope with `ok`, `requestId`, `sessionId`, `requestCounter`, `stateVersion`, `wallet`, `round`, `feature`, `presentationPayload`, `restore`, `idempotency`, `retry`,
and optional `history`. | PROVEN_GENERIC |
| What request/response fields are proven? | Generic operation fields include `sessionId`, `requestCounter`, `currentStateVersion`, `idempotencyKey`, `clientOperationId`, `selectedBet`, `selectedFeatureChoice`, and `historyQuery`; response
fields are the envelope groups above. | PROVEN_GENERIC |
| Where does `presentationPayload` fit? | It is the browser-visible rendering payload inside the runtime envelope, separate from wallet/accounting, round authority, feature authority, restore, idempotency, and retry. | PROVEN_GENERIC |
| Can v0.3 result schema be placed into `presentationPayload` directly? | Not safely as a root object under the current strict generic schema. It needs reviewed schema extension or a reviewed Little Gangster game payload subobject. |
BLOCKED_PENDING_SCHEMA_REVIEW |
| Does `presentationPayload` require extension/review? | Yes. v0.3 cascade, golden-square, rainbow, coin, feature-mode, cap, round-completion, and persistence fields exceed the current generic presentation fields. |
PROVEN_GENERIC_SCHEMA_GAP |
| What adapter is needed from backend runtime output to v0.3 result schema? | A backend-owned result adapter must transform authoritative Little Gangster math/result output into the v0.3 result schema, then project renderable fields into
the `/slot/v1` envelope. | REQUIRED_NOT_IMPLEMENTED |
| What adapter is needed from v0.3 result schema to client animation state? | A client-side render mapper may consume the runtime payload and map v0.3 fields to scene/object IDs, but only after backend/runtime emits the reviewed payload. |
PLANNING_ALLOWED |
| What backend-owned fields must never be produced by browser? | RNG draws, symbol outcomes, cluster/cascade results, win amounts, cap decisions, feature progression, bonus-buy accounting, wallet mutations, round completion, state
persistence, and history truth. | PROVEN_BOUNDARY |
| What fields must be persisted for reconnect/recovery? | Round/spin IDs, state version, client operation/idempotency correlation, current/final grid, pending cascades, golden-square state, feature state, bonus-buy state, cap state, last
action, and recovery payload. | REQUIRED_FROM_V0_3 |
| What history/VABS/Lasthands fields must be preserved? | At minimum the envelope history record must link round ID, bet/win, collected/final status, and enough presentation or replay state to reconstruct v0.3 render state. Exact
VABS/Lasthands bridge remains unproven for 8001. | PROVEN_GENERIC_BLOCKED_FOR_8001 |
| Can GameClientBuilder implementation start? | No. Runtime owner and result API contract remain unproven for Little Gangster/8001. | BLOCKED |
| Can a minimum fixture be created later? | Yes, for planning/mock rendering only, if clearly marked non-production and derived from this contract. It must not claim runtime proof or outcome authority. | PLANNING_ONLY_ALLOWED |

## Evidence Inspected

| Source | Meaning | Evidence label |
|---|---|---|
| `Gamesv1/packages/core-protocol/src/IGameTransport.ts` | Defines `RuntimeEnvelopeResponse` and `/slot/v1` operation types. | PROVEN_GENERIC |
| `Gamesv1/packages/core-protocol/src/schemas.ts` | Defines strict generic envelope schema and strict `PresentationPayloadSchema`. | PROVEN_GENERIC |
| `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Parses envelope, posts to `/slot/v1/*`, and enforces request/state counter behavior in transport. | PROVEN_GENERIC |
| `new-games-server/src/index.ts` | Implements generic `/slot/v1/*`, wallet reserve/settle bridge, history read/write bridge, and reference presentation payload generation. | PROVEN_GENERIC; CANDIDATE_OWNER |
| `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts` | Maps generic `presentationPayload` to UI structures and validates reel/grid shape. | PROVEN_GENERIC_MAPPER |
| `Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts` | Shows a game-specific bridge pattern using `presentationPayload.mathBridge`; not Little Gangster. | CANDIDATE_PATTERN |
| `Gamesv1/docs/gs/browser-runtime-api-contract.md` | Documents endpoint names, request headers, idempotency, and response envelope. | PROVEN_GENERIC |
| `Gamesv1/docs/gs/internal-slot-runtime-contract.md` | Documents internal GS/slot engine responsibilities and server-side outcome boundary. | CANDIDATE_INTERNAL_DESIGN |
| `Gamesv1/docs/gs/rng-ownership-decision.md` | Recommends server-side/internal slot-engine RNG, never browser RNG. | PROVEN_BOUNDARY |
| `Gamesv1/docs/gs/fixtures/*.response.json` | Confirms fixture envelope groups and generic presentation payload keys. | PROVEN_GENERIC |

## Adapter Boundary

The planned adapter has two sides:

1. Backend/runtime adapter:
   - input: authoritative Little Gangster runtime/math outcome;
   - output: generic `/slot/v1` `RuntimeEnvelopeResponse`;
   - owns wallet, round, feature, restore, idempotency, retry, history, and v0.3 render payload production.

2. Client render adapter:
   - input: reviewed `presentationPayload` v0.3 render subobject or equivalent;
   - output: scene/object animation states;
   - owns display sequencing only, not outcome authority.

## Recommended Payload Strategy

The safest planning shape is:

- keep generic envelope fields unchanged;
- keep `wallet`, `round`, `feature`, `restore`, `idempotency`, `retry`, and `history` in their existing envelope groups;
- place v0.3 render data in a reviewed game-specific presentation extension such as `presentationPayload.littleGangsterV03` or a formally approved equivalent;
- do not overload `labels`, `counters`, or animation cues with authoritative v0.3 state.

Because current generic `PresentationPayloadSchema` is strict, this extension must be reviewed before implementation.

## Go/No-Go

Planning may continue. Full GameClientBuilder implementation remains blocked.

