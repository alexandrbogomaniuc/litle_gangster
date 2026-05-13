# BSG Common Wallet Contract

Status: mapped from uploaded BSG CW summary and targeted GS constants; live wallet calls not executed.

## Scope

BSG Common Wallet is the wallet/casino protocol layer only. It covers launch parameters used by Common Wallet start actions and wallet operations between GS/BSG and the External Casino/External System side. It does not define the
browser/client runtime protocol or new-games `/slot/v1/*` runtime contract.

## Response Format

Verified from uploaded BSG CW summary:

- XML over HTTP/HTTPS.
- BSG-side root: `BSGSYSTEM`.
- EC/ES-side root: `EXTSYSTEM`.
- Root includes `REQUEST`, `TIME`, and `RESPONSE`.
- `RESPONSE.RESULT` is documented as `OK|ERROR`, with examples also showing `FAILED` for some wallet failures.
- Do not assume JSON for BSG CW unless later live source proves a different adapter.

GS constants support `EXTSYSTEM`, `RESULT_OK`, and `RESULT_FAILED` in `CCommonWallet.java:47-53`.

## Launch Routes

From uploaded BSG CW summary:

- Guest/free style route: `cwguestlogin.do`
  - documented params: `bankId`, `gameId`, `lang`, optional `homeUrl`.
- Authorized route: `cwstartgamev2.do`
  - documented params: `bankId`, `gameId`, `mode`, `token`, `lang`.
  - documented `mode` values: `real`, `free`.

From source:

- `CWStartGameAction.java:55-56` documents the authorized `cwstartgamev2.do` shape with `gameId`, `mode`, `token`, and `bankId` placeholders.
- `CWStartGameAction.java:99-108` parses game id/mode/lang and calls Common Wallet auth with the provided token.
- `BaseStartGameAction.java:1107-1122` builds a `cwstartgamev2.do` URL for an incomplete crash-style launch redirect with `bankId`, `gameId`, `MODE`, optional `lang`, `CDN`, and cashier URL.

## Authenticate

Verified from uploaded BSG CW summary:

- Request params:
  - `token`
  - `hash`
- Hash input order:
  - `token`
  - `PASS_KEY`
- Success response fields:
  - required: `userId`, `balance`
  - optional: `username`, `firstname`, `lastname`, `email`, `currency`
- Errors include invalid token, invalid hash, and internal error.

Source constants:

- `CCommonWallet.java:4`, `20`, `36-44`, `53` define user/balance/XML tags.
- `CanexRequest.java:AUTH` targeted evidence parses `token`, `bankId`, and `gameId` for the Canex request adapter, but the uploaded BSG CW contract remains the source for the exact hash order.

Blockers:

- Raw PASS_KEY value intentionally unavailable.
- Live wallet client request builder was not fully inspected; future WalletAndLaunchTester must validate against fixture/secret reference.

## Bet / Result

Verified from uploaded BSG CW summary:

- Request params include:
  - `userId`
  - `bet`
  - `win`
  - `roundId`
  - `gameId`
  - `gameSessionId`
  - `hash`
- `bet` format: `bet_amount|transactionId`
- `win` format: `win_amount|transactionId`
- Hash input order:
  - `userId`
  - `bet`
  - `win`
  - optional `isRoundFinished`
  - `roundId`
  - `gameId`
  - `PASS_KEY`
- Optional params include:
  - `token`
  - `negativeBet`
  - `clientType`
  - `promoWinAmount`
  - promo identifiers
  - `jpWin`
  - `jpContribution`
  - `jpContributionDetails`

Source constants/evidence:

- `CCommonWallet.java:4-24` names `userId`, `bet`, `win`, `negativeBet`, `isRoundFinished`, `roundId`, `gameId`, `gameSessionId`, and `casinoTransactionId`.
- `CCommonWallet.java:67-69` names `promoWinAmount` and promo identifiers.
- `CommonGameWallet` targeted evidence shows `negativeBet`, `jpContribution`, and `jpWin` are stored on common game wallets.
- `CWMType.java:6-10` documents multiple win sending modes involving `winAmount`, `negativeBetAmount`, and `isRoundFinished`.
- `CWMType.java:29-108` implements conditions such as win-only, win-accumulated, win-or-round-finished, and round-finished-only.

Required tester implications:

- Bet and win must remain separated.
- Transaction IDs must be unique and idempotency-tested.
- `isRoundFinished` affects credit/send behavior depending on `CWM_TYPE`.
- Zero-win final operations may be required depending on configured `CWM_TYPE`; this remains a future wallet-test/config validation point.
- Optional jackpot, promo, and negative-bet fields are conditional and must not be forced unless config/source proves support for the target bank/game.

## Refund Bet

Verified from uploaded BSG CW summary:

- Request params:
  - `userId`
  - `casinoTransactionId`
  - `hash`
- Hash input order:
  - `userId`
  - `casinoTransactionId`
  - `PASS_KEY`
- Optional details:
  - `token`
  - `gameId`
  - `amount`
  - `roundId`
- BSG ignores Refund Bet error code `302` for five minutes after an original Bet/Result timeout or non-protocol error.

Source constants:

- `CCommonWallet.java:24` defines `casinoTransactionId`.

## Balance And Accounting Expectations

- Authenticate returns initial balance.
- Bet/Result updates balance according to separated bet/win operation fields.
- Refund Bet reverses a failed or uncertain bet transaction according to documented fail-safe behavior.
- GS source shows wallet balance refresh and server balance handling around launch/sit-out paths in `CWStartGameAction.java:238-291`.
- New-games runtime client reads wallet balance from runtime envelopes as `wallet.balanceMinor`; this is separate from BSG CW XML and is part of the browser/GS runtime layer.

## Unknowns / Blockers

- Exact configured `CWM_TYPE` for future game 8001 is unknown.
- Actual 8001 wallet registration does not exist yet.
- Raw PASS_KEY unavailable by design.
- Test token/user raw values unavailable by design.
- Live wallet client implementation and endpoint response behavior must be fixture-tested in WalletAndLaunchTester.
- Idempotency details for EC/ES side beyond uploaded BSG CW summary need future tests.
