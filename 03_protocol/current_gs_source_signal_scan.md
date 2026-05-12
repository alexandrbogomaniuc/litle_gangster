# Current GS Source Signal Scan

Scan scope:

- `Staging/platform-source/platform/gs-server`
- `Staging/platform-source/platform/new-games-server`
- `Staging/platform-source/platform/new-games-client`
- `Staging/platform-source/platform/Gamesv1`
- `Staging/runtime/gs-release-zero`

No donor browsing, asset capture, DB/Cassandra action, wallet call, or client build occurred.

## Registration / Config Signals

| Signal | Status | Evidence | Meaning |
|---|---|---|---|
| `GameTInfoCF` template cache | PROVEN | `CassandraBaseGameInfoTemplatePersister.java:14-52`; `CachesHolder.java:41-53`. | Game templates are loaded/persisted via Cassandra/cache. |
| `GameInfoCF` bank game cache | PROVEN | `CassandraBaseGameInfoPersister.java:39-54`, `173-181`. | Bank/currency game config is serialized as `jcn` and `scn`. |
| `BankInfoCF` bank config | PROVEN | `CassandraBankInfoPersister.java:23-126`; `BankInfoCache.xml:112-142`. | Bank properties hold routing and wallet/config fields. |
| `scn` / `jcn` | PROVEN | `AbstractCassandraPersister.java:25-28`; `CassandraBaseGameInfoPersister.java:44-54`. | Safe registration generation needs a proven serializer or import path. |
| `ExtGameIds` mapping | PROVEN as table/cache, not lane | `CassandraExternalGameIdsPersister.java:24-36`. | External ID mapping exists, but does not prove ExtGame architecture. |
| Game 8001 registered | NOT_FOUND | Targeted scan found 8001 only in project docs and one unrelated test value. | 8001 registration is missing. |

## Runtime Lane Signals

| Signal | Status | Evidence | Meaning |
|---|---|---|---|
| New Games route keys | PROVEN | `BankInfo.java:852-862`; `BaseStartGameAction.java:95-104`. | GS has explicit New Games route/client/API/internal URL keys. |
| New Games launch redirect | PROVEN | `BaseStartGameAction.java:819-904`, `918-941`. | GS can redirect matching game IDs to New Games client with runtime params. |
| Legacy template fallback | PROVEN | `BaseStartGameAction.java:1019-1032`. | Legacy WebSocket/template path still exists. |
| New Games internal WebGS bridge | PROVEN | `NewGamesInternalApiServlet.java:62-67`, `156-299`, `301-375`. | WebGS handles session validation, reserve, settle, history write/read for New Games. |
| `/slot/v1` New Games API | PROVEN for Staging source | `new-games-server/src/index.ts:1590-1935`. | New Games server exposes browser runtime endpoints. |
| Gamesv1 `slot-browser-v1` client contract | PROVEN in Gamesv1 package | `GsHttpRuntimeTransport.ts:31-33`; `schemas.ts:26-35`, `190-241`. | Useful client/runtime contract reference, not final proof for 8001. |

## RNG / Result Signals

| Signal | Status | Evidence | Meaning |
|---|---|---|---|
| Classic GS RNG utilities | CANDIDATE | `RNG.java:20-120`; `InternalRNG.java:15-156`. | GS has RNG utilities, but 8001 consumption is unproven. |
| Legacy game processor infrastructure | CANDIDATE | `SPGameProcessor.java:22-65`; `AbstractGameProcessor.java:43-95`. | Legacy GS can host games; no Little Gangster processor exists. |
| New Games backend sample result generation | LIKELY/CANDIDATE | `new-games-server/src/index.ts:453-465`, `472-565`, `1165-1321`. | Current New Games server generates sample outcomes before wallet settle. |
| WebGS internal bridge result generation | NOT_FOUND | WebGS servlet handles session/wallet/history, not math evaluation. | Bridge is not final result-owner evidence. |
| Browser authoritative RNG | NOT_FOUND/DO_NOT_USE | `GsHttpRuntimeTransport.ts:48-53` has request ID fallback only. | Browser production result generation remains forbidden. |

## ExtGame / Mantis Checklist Signals

| Signal | Status | Evidence | Meaning |
|---|---|---|---|
| ExtGame current source support | CANDIDATE/UNVERIFIED | `ExtGameTransport.ts:3-7` is deprecated alias; `ExtGameIds` table exists. | Does not prove selected ExtGame endpoint architecture. |
| `processTransactions` | CANDIDATE as internal persistence processor | `TransactionDataTracker.java:253-254`; `CassandraTransactionDataPersister.java:410-422`. | This is an internal transaction-data process, not proof of Mantis external-game API. |
| `restartGame` / FRB restart | PROVEN as GS concept | `RestartGameAction.java:18-130`; `GameServer.java:596-616`; `AbstractGameProcessor.java:78-83`. | Must be verified if FRB/OCB applies to 8001. |
| VABS/VBA/history | PROVEN as GS concept | `GetVBAAction.java:19-65`; `struts-config.xml:362-370`, `587-590`; `NewGamesInternalApiServlet.java:301-375`. | Little Gangster history/VBA contract is still unverified. |
| OCB / Cash Bonus flags | PROVEN as bank concepts | `BankInfo.java:972-976`, `1022-1026`. | 8001 promo support decision remains pending. |

## Direct Answers

1. ExtGame external endpoint support: CANDIDATE/UNVERIFIED. No selected Little Gangster ExtGame endpoint was proven.
2. `processTransactions` support: internal transaction processor found; Mantis external-game API equivalent not proven.
3. `restartGame` support: PROVEN as GS concept; Little Gangster usage blocked.
4. VABS/VBA/Lasthands/history support: PROVEN as GS concepts; Little Gangster contract blocked.
5. New-games `slot-browser-v1` support: LIKELY/CANDIDATE with concrete Staging code.
6. Legacy `template.jsp` support: PROVEN.
7. Most supported lane right now: New Games / `slot-browser-v1` as candidate only.
8. Blocked questions: 8001 registration, final runtime owner, math consumption path, serializer/admin import path, VABS/history contract, promo/FRB/OCB decision.
