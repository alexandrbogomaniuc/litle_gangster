# Slot V1 Endpoint Contract

## Status

Generic `/slot/v1` support is PROVEN in Staging source. Little Gangster/8001 selection is CANDIDATE/BLOCKED because no 8001 runtime adapter or package was found.

## Proven Generic Endpoints

| Endpoint | Method | Generic purpose | Evidence status |
|---|---:|---|---|
| `/slot/v1/bootstrap` | POST | Resolve session/config/assets/runtime policies. | PROVEN |
| `/slot/v1/opengame` | POST | Open or resume browser-visible runtime state. | PROVEN |
| `/slot/v1/playround` | POST | Submit a base spin/round action. | PROVEN |
| `/slot/v1/featureaction` | POST | Submit feature decisions such as buy-feature confirmation or collect. | PROVEN |
| `/slot/v1/resumegame` | POST | Restore unfinished runtime state. | PROVEN |
| `/slot/v1/gethistory` | POST | Read history without advancing gameplay state. | PROVEN |
| `/slot/v1/closegame` | POST | Close the runtime session. | PROVEN |

## Common Request Fields

The current generic contract uses:

- `sessionId`
- `requestCounter`
- `currentStateVersion`
- `clientOperationId`
- `idempotencyKey`
- `selectedBet`
- `selectedFeatureChoice`
- `historyQuery`
- `closeReason`

These are field names only; no live values or secrets are stored.

## Evidence Labels

- `Gamesv1/docs/PROJECT.md`: PROVEN generic endpoint prefix and operation names.
- `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts`: PROVEN browser transport methods.
- `new-games-server/src/index.ts`: PROVEN generic server endpoint handlers.
- `gs-server/.../NewGamesInternalApiServlet.java`: PROVEN internal GS bridge for session/wallet/history.

## Little Gangster Status

No `8001`, `LittleGangster`, or Little Gangster runtime package was found in source paths after excluding donor/raw-asset paths. Therefore `/slot/v1` is not selected as final for Little Gangster; it is the strongest candidate contract for
the next backend/runtime adapter proof.
