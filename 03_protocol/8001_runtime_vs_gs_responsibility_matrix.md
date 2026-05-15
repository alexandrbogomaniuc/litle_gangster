# 8001 Runtime vs GS Responsibility Matrix

Date: 2026-05-15
Status: read-only audit

Evidence labels: `PROVEN_SOURCE`, `LIKELY_SOURCE`, `CANDIDATE_SOURCE`, `NOT_FOUND`,
`BLOCKED`.

| # | Responsibility | Owner Classification | Evidence / Blocker |
| --- | --- | --- | --- |
| 1 | launch URL handling | current GS/WebGS plus registration/config; browser consumes launch | PROVEN_SOURCE: start-game/session helpers and
BankInfo launch/history config exist. Exact 8001 launch lane remains BLOCKED pending safe tests. |
| 2 | open game | current GS/session layer plus new-games runtime endpoint; lifecycle coordinates 8001 state | PROVEN_SOURCE:
`StartGameSessionHelper.startGame` validates account, bank, game, mode, FRB, and old session state. |
| 3 | resume game | GS session persistence plus Little Gangster lifecycle reconnect state | PROVEN_SOURCE for GS session storage; PROVEN_SOURCE for
lifecycle reconnect hints. Runtime test BLOCKED. |
| 4 | close game | current GS/WebGS game processor and DBLink finish/session persistence | PROVEN_SOURCE: `AbstractGameProcessor.closeGameSession` and
`DBLink.finishGameSession`. |
| 5 | balance display | browser/client displays balance from runtime envelope | PROVEN_SOURCE: Gamesv1 HUD displays `state.balance`; it is not the
ledger owner. |
| 6 | real wallet balance storage | wallet/casino provider and GS account/wallet state | PROVEN_SOURCE: common-wallet client returns balance; GS
applies to account info. Browser/client owner: false. |
| 7 | wallet auth | current GS wallet manager/client configured by BankInfo | PROVEN_SOURCE: BankInfo common-wallet auth/request-client keys. |
| 8 | bet/debit | GS internal bridge/common-wallet manager plus wallet provider | PROVEN_SOURCE: new-games `/wallet/reserve`; CommonWalletManager
debit/wager. Runtime provides intent/reference. |
| 9 | win/credit | GS internal bridge/common-wallet manager plus wallet provider | PROVEN_SOURCE: new-games `/wallet/settle`; CommonWalletManager
credit/wager. Runtime provides result/reference. |
| 10 | refund/rollback | GS common-wallet manager plus wallet provider | LIKELY_SOURCE: BankInfo refund config and common-wallet operation statuses.
Exact 8001 rollback path BLOCKED. |
| 11 | pending/stuck transaction state | current GS wallet operation tracker/persistence | PROVEN_SOURCE: pending statuses, wallet tracker tasks,
`PendDataArchCF`, `WopCF`. Runtime only marks pending intent. |
| 12 | idempotency | runtime/new-games request layer and GS internal bridge | PROVEN_SOURCE: Gamesv1 request idempotency keys; new-games-server and
internal servlet idempotency maps. Production persistence BLOCKED. |
| 13 | session persistence | Cassandra/GS session persistence | PROVEN_SOURCE: `GameSessionCF` and `GameSessionManager`. |
| 14 | round persistence | Cassandra/GS bet/round persistence | PROVEN_SOURCE: `BetCF`/temp bet, `RoundGameSessionCF`, short bet info. |
| 15 | last hand | GS DBLink/Lasthand plus VABS/history flow; runtime provides payload | PROVEN_SOURCE: DBLink reads/saves Lasthand on close. 8001
durable last-hand path BLOCKED. |
| 16 | VABS visual route | Little Gangster new-games history/alias foundation plus GS/BO route config | PROVEN_SOURCE: 8001 route/alias foundations
applied. BO/CM acceptance BLOCKED. |
| 17 | VABS durable storage | GS/Cassandra history/bet storage | PROVEN_SOURCE for legacy storage; 8001 durable source BLOCKED. |
| 18 | BO/CM history access | BO/CM using GS/configured visual route | PROVEN_SOURCE for legacy `/vabs/show.jsp` shape; 8001 BO/CM acceptance BLOCKED.
|
| 19 | roundFinished decision | game runtime/lifecycle derives completion; GS settlement/history consumes it | PROVEN_SOURCE: lifecycle round
completion contract; DBLink uses helper on close. Exact 8001 GS mapping BLOCKED. |
| 20 | restart/FRB transition | current GS/WebGS FRB/session helpers plus lifecycle restart flag | PROVEN_SOURCE:
`StartGameSessionHelper.restartGame4FRB`; 8001 runtime tests BLOCKED. |
| 21 | cap enforcement | server-side game runtime/lifecycle, reflected through GS registration/config | PROVEN_SOURCE: lifecycle cap representation;
final registration mapping BLOCKED. |
| 22 | SD_KEYS/KPI reporting | registration/config and GS reporting, fed by runtime math profile identity | LIKELY_SOURCE from prior registration
audits; exact current GS keys BLOCKED. |
| 23 | logs/monitoring | GS/WebGS statistics/logging plus new-games-server request logs | PROVEN_SOURCE: `StatisticsManager` calls in
wallet/session/history flows. |
| 24 | registration field storage | GameServerRegistrar planning into GS/Cassandra config/cache | PROVEN_SOURCE for BankInfo/GameInfo-style config
keys; generation remains BLOCKED. |

## Boundary Summary

Browser/client real wallet owner: no.

Game runtime real wallet owner: blocked/no for production. It can own action intent and
local test fallback state, but real settlement must pass through approved GS/wallet
paths.

Current GS/wallet provider balance owner: current GS wallet managers and the external
wallet/casino provider.

Pending/stuck transaction owner: current GS wallet operation tracking and persistence,
with exact 8001 bridge behavior still requiring approved tests.
