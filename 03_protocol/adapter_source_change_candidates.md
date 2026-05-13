# Adapter Source Change Candidates

Status: SOURCE_CHANGE_CANDIDATES_IDENTIFIED_NO_IMPLEMENTATION.

## Required If `gamePayload` Is Approved

| Source path | Candidate change | Evidence label | Implementation status |
|---|---|---|---|
| `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/schemas.ts` | Add `gamePayload` to `PresentationPayloadSchema` or add a reviewed passthrough field. | REQUIRED_SCHEMA_CHANGE | not implemented |
| `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/IGameTransport.ts` | Document/type the extension if the transport contract should make it explicit. | OPTIONAL_TYPE_HARDENING | not implemented |
| `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Optionally preserve/validate `gamePayload` explicitly. Current parser is permissive. | OPTIONAL_TRANSPORT_HARDENING | not
implemented |
| `[STAGING_ROOT]/platform-source/platform/Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts` | Decide whether shared mapper passes game extension through or leaves it to game-specific mapper. |
REQUIRED_MAPPER_POLICY | not implemented |
| `[STAGING_ROOT]/platform-source/platform/new-games-server/src/index.ts` | Add future 8001 branch and `buildLittleGangsterPresentationPayload`. | REQUIRED_8001_ADAPTER | not implemented |
| `[STAGING_ROOT]/platform-source/platform/Gamesv1/games/8001/...` | Future game package/mapper to consume `gamePayload` and scene/object maps. | REQUIRED_8001_PACKAGE | missing |
| `[STAGING_ROOT]/platform-source/platform/gs-server` | Validate or wire history/VABS/Lasthand storage for v0.3 replay payload. | REQUIRED_HISTORY_REVIEW | not implemented |

## Reference Only

| Source path | Why reference only | Evidence label |
|---|---|---|
| `Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts` | Proves a game-specific extension reader for `mathBridge`, not Little Gangster. | CANDIDATE_PATTERN |
| `Gamesv1/games/7001/src/app/runtime/provisionalMathSource.ts` | Proves a local provisional outcome-to-presentation adapter pattern, not production 8001. | CANDIDATE_PATTERN |
| `new-games-server/src/index.ts` Crazy Rooster payload builder | Proves one server-side presentation builder pattern. The branch is hard-coded for game 7001. | CANDIDATE_PATTERN |

## Do Not Change In This Sprint

No source files in Staging were modified. This document only identifies future implementation candidates.
