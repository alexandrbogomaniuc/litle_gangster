# Wallet Hash Rules

Status: mapped from uploaded BSG CW summary. No raw secrets used.

## Global Rule

Every BSG Common Wallet API request includes a `hash` parameter. The hash is MD5 hex over documented parameter values in exact documented order followed by `PASS_KEY`.

Rules from uploaded BSG CW summary:

- Do not reformat parameter values before hashing.
- Missing optional values contribute nothing; do not insert `null`, `nil`, or placeholder text for missing optionals.
- Store only secret references, never raw PASS_KEY values.

## Authenticate Hash Order

Canonical input order:

```text
token + PASS_KEY
```

Fixture-only example:

```text
token = [REDACTED_FIXTURE]
PASS_KEY = [REDACTED_FIXTURE]
md5_input = TOKEN_FIXTURE_DO_NOT_USEPASS_KEY_FIXTURE_DO_NOT_USE
```

Never persist a real token or real PASS_KEY in the project.

## Bet / Result Hash Order

Canonical input order:

```text
userId + bet + win + isRoundFinished_if_present + roundId + gameId + PASS_KEY
```

Where:

- `bet` is `bet_amount|transactionId`.
- `win` is `win_amount|transactionId`.
- `isRoundFinished` contributes only if present.
- Missing optional fields contribute no string.

Fixture-only example:

```text
userId = USER_FIXTURE
bet = 1.00|BET_TX_FIXTURE_001
win = 0.00|WIN_TX_FIXTURE_001
isRoundFinished = true
roundId = ROUND_FIXTURE_001
gameId = 8001
PASS_KEY = [REDACTED_FIXTURE]
md5_input = USER_FIXTURE1.00|BET_TX_FIXTURE_0010.00|WIN_TX_FIXTURE_001trueROUND_FIXTURE_0018001PASS_KEY_FIXTURE_DO_NOT_USE
```

## Refund Bet Hash Order

Canonical input order:

```text
userId + casinoTransactionId + PASS_KEY
```

Fixture-only example:

```text
userId = USER_FIXTURE
casinoTransactionId = BET_TX_FIXTURE_001
PASS_KEY = [REDACTED_FIXTURE]
md5_input = USER_FIXTUREBET_TX_FIXTURE_001PASS_KEY_FIXTURE_DO_NOT_USE
```

## Secret References

Stored secret reference only:

- Bank property references: `INTEGRATION_PASS_KEY`, `CT_PASS_KEY`, `BONUS_PASS_KEY`.
- Declaration evidence: `BankInfo.java:160-178`, `250-258`, `1541-1562`.
- Value source reference path: `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/runtime/export_localmachine/com.abs.casino.common.cache.BankInfoCache.xml`.

## Never Log Raw

Never log or persist raw values for:

- PASS_KEY or any property that acts as a pass key.
- `token`, session token, cashier token, test token, JWT, signature, or hash.
- Full donor/reference URLs that contain token-like query values.
- Wallet request/response bodies containing player, balance, or auth data unless a later test fixture explicitly redacts them.

## Validation Notes

- Hash order was not guessed; it comes from uploaded BSG CW summary.
- Message schemas created in this sprint are structural helpers only. They do not replace wallet hash validation.
- WalletAndLaunchTester must use fake fixture PASS_KEY values or local ignored secret references.
