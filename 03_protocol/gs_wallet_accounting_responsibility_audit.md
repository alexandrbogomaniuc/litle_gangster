# GS Wallet/Accounting Responsibility Audit

Date: 2026-05-15
Status: read-only audit, no endpoint calls, no source changes

## Purpose

This audit corrects the Little Gangster 8001 test and implementation boundary before
wallet/launch/history testing. The browser/game client and visual renderer must not be
treated as real wallet owners. They may display balance and send approved runtime
operations, but wallet mutation, provider settlement, session persistence, durable
history, pending transaction handling, and BO/CM access belong to GS/platform layers
unless current GS source proves a different owner.

Crazy Rooster / 7001 is not authoritative and was not used as a successful template.

## Wallet And Config Ownership Findings

- PROVEN_SOURCE: `BankInfo` defines wallet manager/config keys such as `WPM_CLASS`,
  `CWM_TYPE`, common-wallet request client class, balance URL, wager URL, refund URL,
  auth URL, and refund support. Evidence: Staging
  `gs-server/common/.../BankInfo.java` lines 56-110.
- PROVEN_SOURCE: `BankInfo` also carries balance-refresh and pending-operation
  behavior flags, including client refresh settings and
  `TRY_RESOLVE_PENDING_OPERATIONS_ON_AUTH`. Evidence: `BankInfo.java` lines 813-826.
- PROVEN_SOURCE: `CommonWalletManager` performs debit and credit using the configured
  wallet client, receives/normalizes wallet response balance, updates wallet operation
  status, and records statistics. Evidence:
  `gs-server/common-wallet/.../CommonWalletManager.java` lines 167-225 and 490-525.
- PROVEN_SOURCE: GS has an internal new-games wallet bridge with `/wallet/reserve` and
  `/wallet/settle` handlers. These handlers validate session/counter/idempotency,
  invoke `WalletProtocolFactory` / common-wallet client, and return operation/balance
  data. Evidence:
  `gs-server/game-server/web-gs/.../NewGamesInternalApiServlet.java` lines 64-67,
  156-221, 224-299, and 635-689.
- PROVEN_SOURCE: wallet operation persistence exists in `WopCF` with game-session and
  round fields. Evidence:
  `gs-server/cassandra-cache/.../CassandraWalletOperationInfoPersister.java`
  lines 26-67.

Conclusion: real wallet balance ownership is split between GS wallet managers and the
external wallet/casino provider. The browser/client and Little Gangster renderer are
not the real balance owner. The 8001 runtime/lifecycle wrapper must carry action and
accounting intent plus references, then rely on approved GS/wallet paths for real
settlement.

## Session And History Ownership Findings

- PROVEN_SOURCE: `GameSession` contains account, bank, game, start/end, income/payout,
  round counts, last player bet id, real-money flag, external session id, language,
  profile/model, and last payment operation id fields. Evidence:
  `gs-server/common/.../GameSession.java` lines 18-78.
- PROVEN_SOURCE: `CassandraGameSessionPersister` stores `GameSessionCF` and includes
  account id, game id, mode, start/end, income, payout, round counts, language, bank id,
  bonus fields, previous/next session ids, and model field. Evidence:
  `gs-server/cassandra-cache/.../CassandraGameSessionPersister.java` lines 37-146.
- PROVEN_SOURCE: `CassandraBetPersister`, `CassandraTempBetPersister`,
  `CassandraRoundGameSessionPersister`, and `CassandraShortBetInfoPersister` provide
  bet/round/session storage surfaces. Evidence: read-only source hits in
  `gs-server/cassandra-cache/common-persisters/src/main/java/com/dgphoenix/casino/cassandra/persist/`.
- PROVEN_SOURCE: GS close-session flow uses `AbstractGameProcessor.closeGameSession`,
  `DBLink.finishGameSession`, last-hand handling, bet update/new-bet persistence, game
  session finish, and history flush. Evidence:
  `AbstractGameProcessor.java` lines 105-156 and `DBLink.java` lines 592-643.
- PROVEN_SOURCE: legacy VBA/history code resolves history by round/session and builds
  sanitized `/vabs/show.jsp` route shapes using session id, game id, round id, language,
  and whole-session flags. Evidence:
  `HistoryByRoundAction.java` lines 35-89 and `GetVBAAction.java` lines 25-50.
- PROVEN_SOURCE: GS exposes internal new-games history write/read handlers that persist
  archive fields and read bet history via player-bet persistence. Evidence:
  `NewGamesInternalApiServlet.java` lines 301-360 and 520-608.

Conclusion: GS/Cassandra own durable session, bet, round, last-hand, and history storage.
Little Gangster currently provides lifecycle/history payloads and route foundations, but
durable 8001 storage remains unproven and release-blocking.

## Pending, Stuck, Error, And Logging Findings

- PROVEN_SOURCE: `CommonWalletManager` rejects an incomplete previous wallet operation
  before debit and marks unresolved credit operations as pending with a high-priority
  wallet tracker task. Evidence: `CommonWalletManager.java` lines 170-174 and 540-548.
- PROVEN_SOURCE: pending wallet/FRB operation archive storage exists in
  `PendDataArchCF`, including methods to save and retrieve wallet operations. Evidence:
  `CassandraPendingDataArchivePersister.java` lines 20-35 and 51-84.
- PROVEN_SOURCE: MQ/transaction code maps wallet operation internal status to approved,
  started, pending, or failed transaction status. Evidence:
  `MQServiceHandler.java` lines 705-720.
- PROVEN_SOURCE: failed/pending operation handling exists before enter-game flow and can
  invoke `WalletTrackerTask` then commit transaction state. Evidence:
  `FailedOperationHandleEnterProcessor.java` lines 25-66.
- PROVEN_SOURCE: the new-games internal API and new-games-server surface trace/error
  codes for reserve/settle/history failures, but those are integration errors rather
  than browser-owned wallet state. Evidence:
  `NewGamesInternalApiServlet.java` lines 70-123 and `new-games-server/src/index.ts`
  lines 1290-1315 and 1445-1481.

Conclusion: pending/stuck transaction ownership is current GS wallet-operation tracking
and persistence, with the wallet provider as settlement authority. The Little Gangster
wrapper must expose pending markers and idempotency references, but must not implement
the real stuck-transaction store unless GS source and an approved implementation plan
assign that responsibility.

## Browser And Gamesv1 Client Findings

- PROVEN_SOURCE: Gamesv1 transport interfaces send `opengame`, `playround`,
  `featureaction`, `resumegame`, `closegame`, and `gethistory` requests to GS runtime
  endpoints and receive `wallet`, `round`, `feature`, `presentationPayload`, `restore`,
  `idempotency`, and `retry` envelope objects. Evidence:
  `Gamesv1/packages/core-protocol/src/IGameTransport.ts` lines 141-186.
- PROVEN_SOURCE: the HTTP runtime transport posts actions to `/slot/v1/...` endpoints
  and treats `gethistory` as read-only. Evidence:
  `GsHttpRuntimeTransport.ts` lines 220-340.
- PROVEN_SOURCE: UI-kit HUD displays balance from runtime state and visibility config.
  Evidence: `PremiumTemplateHud.ts` lines 262-264 and `PremiumHudPolicy.ts` lines 42-43.

Conclusion: the browser/client displays wallet state and submits runtime operations. It
does not own real wallet balance, wallet auth, debit, credit, rollback, durable history,
or pending/stuck transaction recovery.

## Little Gangster Runtime And Lifecycle Wrapper Findings

- PROVEN_SOURCE: the lifecycle wrapper creates settlement state from runtime result
  wallet references and explicitly marks the balance source as settlement/process
  response, not repeated getBalance. Evidence:
  `new-games-server/src/games/little-gangster/lifecycle/actionAccounting.ts` lines
  9-30.
- PROVEN_SOURCE: lifecycle accounting represents paid base spin, cascade sequence, free
  spin/feature spin, bonus-buy purchase debit, bonus-buy feature result, cap
  enforcement, wallet accounting refs, idempotency key, and pending action marker.
  Evidence: `actionAccounting.ts` lines 49-100.
- PROVEN_SOURCE: lifecycle state persistence carries state version, round id,
  client operation id, idempotency key, pending action, feature/bonus-buy state,
  recoverable payload, reconnect hints, restart flag, math profile, RTP, and volatility.
  Evidence: `statePersistence.ts` lines 9-63.
- CANDIDATE_SOURCE: `new-games-server/src/index.ts` contains local session, balance,
  round, idempotency, and history fallback maps plus calls to internal GS wallet/history
  endpoints when configured. Evidence: lines 952-1082 and 1230-1515.

Conclusion: 8001 runtime/lifecycle wrapper owns representation and coordination:
action/accounting intent, idempotency keys, state persistence metadata, result payload,
history payload, reconnect/restart hints, and blockers. It is not proven to own real
casino wallet balance or durable wallet/history stores.

## Blocked Or Unproven Items

- BLOCKED: exact production 8001 durable history storage source remains unproven.
- BLOCKED: BO/CM acceptance of the 8001 root/scoped alias remains untested.
- BLOCKED: view-session id equivalence for 8001 remains unproven.
- BLOCKED: registration field shape for wallet/config/history URL settings remains
  unproven.
- BLOCKED: wallet/launch/history tests require explicit approved environment and
  endpoint permission.

## Audit Decision

The correct boundary is:

- browser/client: display and request orchestration only;
- Little Gangster runtime/lifecycle: deterministic result representation, lifecycle
  state, idempotency, action/accounting intent, and history payload references;
- GS/WebGS/current platform: session control, wallet bridge, wallet operation tracking,
  persistent session/bet/history stores, pending/stuck handling, logs/monitoring, and
  config/cache ownership;
- wallet/casino provider: real balance ledger and settlement authority.

WalletAndLaunchTester must verify this boundary later. It must not assume the game
client, renderer, or Little Gangster presentation payload owns wallet mutation.
