# Presentation Payload Schema Review

Sprint: ProtocolAndSchemaMapper schema extension review
Status: COMPLETED_SOURCE_BACKED_REVIEW_NO_SOURCE_PATCH
Scope: documentation and planning only; no Staging source was modified.

## Direct Answers

| Question | Answer | Evidence label |
|---|---|---|
| What is the current `PresentationPayloadSchema` shape? | Core protocol defines `featureMode`, `reelStops`, `symbolGrid`, `uiMessages`, `animationCues`, `audioCues`, `counters`, and `labels`. | PROVEN_SOURCE:
`Gamesv1/packages/core-protocol/src/schemas.ts` |
| Is it strict? | Yes. The core protocol presentation schema is a strict object, so canonical validation rejects unknown root keys. | PROVEN_STRICT_SCHEMA |
| Does it allow unknown keys? | No for the canonical schema path. | PROVEN_SCHEMA_BLOCKER |
| Does it allow `gamePayload`? | No. `gamePayload` is not a field in the strict presentation schema. | PROVEN_SCHEMA_BLOCKER |
| Does it allow `littleGangsterV03`? | No. `littleGangsterV03` is not a field in the strict presentation schema. | PROVEN_SCHEMA_BLOCKER |
| Does it allow `mathBridge`? | No in the strict core schema. `mathBridge` exists in the 7001 runtime path as a practical reference pattern, not as canonical schema support. | PROVEN_SCHEMA_BLOCKER; CANDIDATE_PATTERN |
| Does it allow arbitrary game-specific payloads? | No in the strict schema. TypeScript transport and HTTP parser paths are more permissive records, which is conflicting practical evidence rather than schema approval. | CONFLICTING_EVIDENCE
|
| What validation rejects the 24 fixtures today? | The `gamePayload` extension key, candidate/string `stateVersion`, non-canonical restore/idempotency field names, some lowercase/custom round statuses, symbolic symbol grids, and non-generic
counter shapes. | STRICT_SCHEMA_CONFLICT |

## Source Evidence

| Source | Finding | Evidence label |
|---|---|---|
| `Gamesv1/packages/core-protocol/src/schemas.ts` | `PresentationPayloadSchema` is a fixed strict shape and `RuntimeEnvelopeResponseSchema` embeds it. | PROVEN_SOURCE |
| `Gamesv1/packages/core-protocol/src/IGameTransport.ts` | `RuntimeEnvelopeResponse` exposes `presentationPayload: Record<string, unknown>`. | PROVEN_INTERFACE_PERMISSIVE |
| `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | HTTP parser treats `presentationPayload` as a record and preserves returned keys. | PROVEN_TRANSPORT_PERMISSIVE |
| `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts` | UI-kit mapper consumes generic presentation fields and does not expose a game extension in the mapped model. | PROVEN_GENERIC_MAPPER |
| `new-games-server/src/index.ts` | 7001 presentation builder emits generic fields plus `mathBridge`; server envelope construction accepts record-like payloads. | CANDIDATE_PATTERN |
| `Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts` | 7001 client reads `presentationPayload.mathBridge` from raw payload. | CANDIDATE_PATTERN |
| `Gamesv1/games/7001/src/app/runtime/provisionalMathSource.ts` | 7001 provisional adapter maps math outcome to generic fields plus `mathBridge`. | CANDIDATE_PATTERN |
| Targeted 8001/Little Gangster search | No 8001/Little Gangster runtime branch or package was found in targeted source areas. | NOT_FOUND_8001 |

## Contract Split

Current source has a split contract:

- Canonical core schema is strict and does not approve `gamePayload`, `littleGangsterV03`, or `mathBridge`.
- Transport-level TypeScript and HTTP parsing are permissive enough to carry unknown presentation fields in practice.
- 7001 uses `mathBridge` as source-backed reference evidence, but this does not prove Little Gangster support.

## Fixture Strict-Schema Conflicts

| Fixture pattern | Current strict expectation | Evidence label |
|---|---|---|
| `presentationPayload.gamePayload` | Not present in `PresentationPayloadSchema`. | PROVEN_SCHEMA_CONFLICT |
| `runtimeEnvelope.stateVersion` fixture strings | Runtime envelope expects numeric state version in the generic contract. | PROVEN_SCHEMA_CONFLICT |
| `round.status` fixture values such as `idle` | Core round status expects canonical runtime status values. | PROVEN_SCHEMA_CONFLICT |
| `restore.hasOpenRound` and `restore.roundId` | Core restore uses canonical unfinished-round/recovery fields. | PROVEN_SCHEMA_CONFLICT |
| `idempotency.duplicate` | Core idempotency uses canonical duplicate/replay fields. | PROVEN_SCHEMA_CONFLICT |
| symbolic string `symbolGrid` | UI-kit generic mapper expects numeric grids for generic presentation mapping. | PROVEN_MAPPER_CONFLICT |
| v0.3 win ratio/tier if forced into generic counters | Core/UI-kit counter shapes are not a clean fit for v0.3 result semantics. | CONFLICTING_SCHEMA_SHAPE |

## Conclusion

`presentationPayload.gamePayload` is the best reusable direction for Little Gangster and future donor-inspired games, but it requires a schema/type/mapper/server patch before it can be treated as an approved runtime contract. `mathBridge`
should remain a reference pattern unless the platform team deliberately generalizes or migrates it.

## Source Patch Apply Update - 2026-05-12

Evidence label: PROVEN_APPLIED

The approved source patch added optional `presentationPayload.gamePayload` to the canonical JSON response
schemas and core-protocol Zod runtime schema.

The parent `presentationPayload` schema remains strict. Unknown top-level presentation fields are still rejected.

Evidence label: PROVEN_UI_KIT_PASSTHROUGH

The UI-kit presentation mapper now preserves `gamePayload` untouched in the mapped presentation model.

Evidence label: NOT_IMPLEMENTED_BY_SCOPE

No Little Gangster backend adapter or 8001 runtime package was created. Runtime owner and result API proof remain
open blockers.
