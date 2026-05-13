# Runtime API Inspection Report

Sprint: RuntimeApiInspection

## Scope

This inspection was limited to the project, reusable skill suite, public export, `[STAGING_ROOT]`, and manifest-declared roots. No donor browsing, asset capture, DB/Cassandra action, wallet call, client implementation, or registration
generation was performed.

## Direct Answers

| Question | Answer | Evidence status |
|---|---|---|
| Does current source prove the selected runtime owner for Little Gangster/8001? | No. Generic New Games runtime evidence exists, but no Little Gangster/8001 runtime package, game adapter, or registered game-specific runtime owner was
found. | NOT_FOUND for 8001, CANDIDATE for New Games |
| Does current source prove `/slot/v1` or equivalent runtime endpoints? | Yes for the generic current GS/Gamesv1 contract. It does not by itself select Little Gangster. | PROVEN generic, CANDIDATE for Little Gangster |
| What endpoints are proven generically? | `bootstrap`, `opengame`, `playround`, `featureaction`, `resumegame`, `gethistory`, `closegame` under `/slot/v1`. | PROVEN generic |
| Does source provide `RuntimeEnvelopeResponse` or equivalent? | Yes. Core protocol defines the envelope and the HTTP transport parses it. | PROVEN generic |
| Does source prove `presentationPayload` is the place where v0.3 result data should live? | It proves `presentationPayload` is the browser-visible rendering payload. It does not prove the v0.3 Little Gangster payload shape is accepted yet.
| LIKELY/CANDIDATE |
| Is there an adapter pattern from game math output to runtime envelope? | Yes as a reference pattern for existing sample/template games, but not a reusable Little Gangster v0.3 adapter. | LIKELY generic, NOT_FOUND for 8001 |
| Does source prove where RNG/outcome generation happens for Little Gangster? | No. The sample New Games server generates provisional outcomes for existing examples, but Little Gangster/8001 outcome ownership remains unproven. | CANDIDATE
generic, NOT_FOUND for 8001 |
| Does source prove `math_package.json` can be consumed directly? | No direct consumption of Little Gangster `math_package.json` was found. Registration/runtime metadata references are not executable math import proof. | NOT_FOUND |
| Does source prove history/recovery behavior? | Generic `/slot/v1/gethistory`, `resumegame`, WebGS history bridge, and GS VABS/Lasthand concepts exist. Little Gangster-specific replay/history payload remains unproven. | PROVEN generic,
BLOCKED for 8001 |

## Evidence Inspected

| Evidence path | Meaning | Status |
|---|---|---|
| `platform-source/platform/Gamesv1/docs/PROJECT.md` | States canonical browser endpoint prefix `/slot/v1/*` and operations. | PROVEN generic |
| `platform-source/platform/Gamesv1/packages/core-protocol/src/IGameTransport.ts` | Defines `RuntimeEnvelopeResponse` and operation methods. | PROVEN generic |
| `platform-source/platform/Gamesv1/packages/core-protocol/src/schemas.ts` | Defines strict runtime envelope and presentation payload schema. | PROVEN generic |
| `platform-source/platform/Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Parses runtime envelope and posts to `/slot/v1/*` endpoints. | PROVEN generic |
| `platform-source/platform/new-games-server/src/index.ts` | Implements generic `/slot/v1/*` endpoints and provisional sample outcome/presentation generation. | PROVEN generic, CANDIDATE owner |
| `platform-source/platform/gs-server/.../NewGamesInternalApiServlet.java` | Provides internal New Games session, wallet reserve/settle, and history bridge. | PROVEN bridge |
| `platform-source/platform/Gamesv1/games/premium-slot/src/app/runtime/RuntimeOutcomeMapper.ts` | Existing client-side mapper from runtime envelope to presentation model. | LIKELY reusable pattern |
| `platform-source/platform/Gamesv1/docs/PRESENTATION_LAYER_ARCHITECTURE.md` | Documents canonical mapping from GS `presentationPayload` to UI structures. | PROVEN generic |

## Source Hit Summary

`/slot/v1` endpoints, core protocol envelope parsing, and WebGS New Games internal bridge are present. 8001/Little Gangster source hits were not found after excluding donor/raw-asset paths; incidental numeric hash/test values are not game
evidence.

## Decision

The runtime API inspection completed, but it does not unblock implementation. `/slot/v1` remains the strongest candidate lane for planning because it is proven generically in the current source. It is not selected as the Little Gangster
production runtime until a Little Gangster/8001 backend adapter/package or registration-to-runtime path is proven.

## Implementation Gate

GameClientBuilder implementation remains blocked. A later implementation sprint must first prove:

- Little Gangster/8001 route/registration exists or is generated and approved.
- The backend/runtime owner is selected and source-backed.
- The v0.3 payload adapter from backend math result to runtime envelope is implemented or fixture-approved.
- `presentationPayload` schema extension/compatibility for v0.3 fields is approved.
- History/recovery payload shape is proven.
- Browser remains renderer-only and non-authoritative for RNG/outcomes.
