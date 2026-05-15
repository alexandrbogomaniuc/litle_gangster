# 8001 Wallet Accounting Boundary Contract

Date: 2026-05-15
Status: boundary contract, no runtime tests executed

## Correct Boundary

The browser/client is not the real wallet owner. The Little Gangster renderer is not the
real wallet owner. `presentationPayload.gamePayload` is not a wallet ledger.

The 8001 runtime/lifecycle wrapper must provide:

- action/accounting intent for paid base spins, cascades, free spins, feature spins,
  bonus-buy purchase debit, bonus-buy feature result, cap enforcement, and close/restart
  transitions;
- action id, client operation id, idempotency key, round id, game session id, and
  request counter;
- wallet/accounting reference placeholders, including reserve/debit, settle/credit, and
  rollback/refund references when provided by GS;
- state persistence metadata for reconnect, pending actions, restart/FRB transitions,
  and history reconstruction;
- result payload, math profile identity, RTP/volatility identity, and history payload;
- blocker flags when wallet/history/storage/release requirements are not proven.

The 8001 runtime/lifecycle wrapper must not:

- store or mutate the real casino balance directly;
- call real wallet endpoints without explicit approval and safe environment evidence;
- treat repeated `getBalance` as a substitute for reserve/settle state;
- implement durable stuck-transaction storage unless GS source assigns that owner;
- approve wallet, registration, certification, or release gates.

## GS And Wallet Provider Boundary

Current GS/WebGS owns the approved wallet bridge and session context:

- BankInfo carries wallet manager/client/auth/balance/wager/refund settings.
- CommonWalletManager and the internal new-games servlet call configured wallet clients.
- Wallet/casino provider remains the authoritative ledger for real-money settlement.
- GS maps wallet result balances into account/wallet state and persists wallet
  operations.

## Balance Rule

Balance shown by the client must come from the latest approved runtime envelope or
settlement/process response. If the wrapper has only a placeholder or fixture balance,
the response must remain non-production and blocked.

## Real Endpoint Test Rule

Real wallet endpoint tests require explicit approval, known safe environment, approved
host/config references, and no raw secrets in reports. This sprint did not call wallet,
GS, BO/CM, Cassandra, or DB endpoints.

## 8001 Current Status

- Lifecycle wrapper action accounting is implemented for representation.
- VABS visual route and legacy alias foundations are implemented for planning/testing.
- Durable history storage is not implemented.
- BO/CM acceptance is untested.
- Wallet/launch/history runtime tests are missing.
- GameClientBuilder remains blocked.
- GameServerRegistrar generation remains blocked.
- Release and certification remain false.
