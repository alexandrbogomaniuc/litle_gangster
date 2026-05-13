# Current GS Integration Lane Validation

Status: partial validation from current Staging source/config/docs.

## Source Boundary

Inspected only allowed Staging-derived current roots and project/suite documentation. No donor browser work, wallet calls, DB/Cassandra execution, code build, math implementation, or registration generation occurred.

Current Staging source path note:

- The team update named `platform-source/new-games-server`, `platform-source/new-games-client`, and `platform-source/Gamesv1`.
- Those exact paths were missing.
- `runtime/new-games-runtime/docker-compose.yml` references `platform-source/platform/new-games-server`, `platform-source/platform/new-games-client`, and `platform-source/platform/Gamesv1`, and those paths exist.
- This sprint inspected those compose-derived Staging paths only for source signals and records the path mismatch for future manifest cleanup.

## Lane Validation

| Lane | Evidence | Status | Confidence |
|---|---|---|---|
| new-games / `slot-browser-v1` | `Gamesv1/README.md:7-13` says browser to GS HTTP runtime only, `/slot/v1/*`, browser presentation-only, GS authoritative for session/wallet/DB/restore/requestCounter/idempotency/routing/config.
`new-games-server/src/index.ts:1590-1990` implements `/slot/v1/bootstrap`, `/opengame`, `/playround`, `/featureaction`, `/resumegame`, `/gethistory`, `/closegame`. `BaseStartGameAction.java:878-904` adds `ngsApiUrl`, `gsInternalBaseUrl`,
and `ngsContract=v1`. | candidate direction only; not selected until direct current-GS validation is complete | partial |
| legacy template / WebSocket | `BaseStartGameAction.java:1019-1032` still redirects to `/<mode>/mp/template.jsp` with `WEB_SOCKET_URL`. Existing protocol docs mapped `template.jsp`. | proven legacy support | medium |
| ExtGame external endpoint | `CassandraExternalGameIdsPersister.java:25-31` and `GameSessionInfo.java:16-30` prove external game id mapping concepts. `Gamesv1/docs/protocol/extgame.md:1-11` marks ExtGame as archived legacy marker and
points canonical contracts to `docs/gs/*`. No Start/Enter external endpoint requirement for Little Gangster was proven. | candidate / unverified | low for Little Gangster |
| process-transaction-equivalent | Current new-games server uses `/v1/placebet` and `/v1/collect` internally and `/slot/v1/playround`/`featureaction` in browser contract. GS has an internal `processTransactions` method in Cassandra
transaction tracking code, but that is not proof of the Mantis external API. | equivalent needed, exact API not ExtGame-proven | partial |
| history / VABS / Lasthand | `HistoryByRoundAction.java:31-80`, `GetVBAAction.java:22-67`, `NewGamesInternalApiServlet.java:62-67`, and `BankInfo`/Lasthand source signals prove GS history/VABS/Lasthand concepts exist. | proven GS concepts;
Little Gangster contract still open | partial |

## Current Conclusion

No runtime lane is trusted or selected yet. New-games `slot-browser-v1` / HTTP runtime has useful candidate signals, but Gamesv1/Crazy Rooster/slot-browser-v1 must not be treated as guaranteed truth until current GS source/config/docs are
verified directly for Little Gangster. ExtGame remains advisory and unverified for current GS. The Mantis checklist should be used to avoid missing state, transaction, history, restart, FRB/OCB, RNG, and certification validation items.

## What Is Still Blocked

- Exact Little Gangster 8001 registration/config path.
- Whether current release configuration includes 8001 route fields.
- Exact runtime lane owner: classic GS, new-games backend, game-specific server package, GS game processor, mixed lane, or other.
- Exact production RNG owner and certified RNG integration.
- Exact feature/buy/FRB/OCB support for Little Gangster.
- Exact VABS/Lasthands renderer/package requirements for Little Gangster.
- Exact mapping from v0.3 donor-parity math state to `/slot/v1/*` result envelope.
- Whether registration configures metadata/routing/display values only or has any executable math import hook. Current assumption: registration is metadata/config/routing unless source proves otherwise.
