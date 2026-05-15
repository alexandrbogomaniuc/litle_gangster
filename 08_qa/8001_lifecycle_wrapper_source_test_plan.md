# 8001 Lifecycle Wrapper Source Test Plan

Status: planning only. No tests were created in Staging and no Staging source was modified.

Crazy Rooster / 7001 is not authoritative. Current adapter is payload mapper only. Lifecycle wrapper is required.

## Future Test Files

- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/test/little-gangster/lifecycle-wrapper.test.ts`
- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/test/little-gangster/state-reconnect.test.ts`
- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/test/little-gangster/accounting-boundary.test.ts`
- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/test/little-gangster/vabs-visual-history-route.test.ts`
- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/test/little-gangster/pending-stuck-recovery.test.ts`

## Route Tests

- `/slot/v1/opengame` initializes 8001 wrapper state.
- `/slot/v1/playround` produces 8001 `presentationPayload.gamePayload` through wrapper.
- `/slot/v1/featureaction` handles cascade/free-spin/100x bonus-buy action types.
- `/slot/v1/resumegame` returns recoverable 8001 state.
- `/slot/v1/closegame` respects pending round/settlement state.
- Candidate VABS routes return round, session, and whole-session replay payloads.

## State Tests

- Open game to base idle.
- Base spin pending to cascade active.
- Cascade active to feature triggered or round complete.
- Free spins active to settlement pending.
- Bonus-buy purchase pending to bonus-buy feature active.
- Cap reached to settlement pending.
- Reconnect pending to restored current state.
- Restart required remains explicit.

## Accounting Tests

- Every paid base spin has accounting representation.
- Every free spin/feature spin has result/action representation.
- 100x bonus-buy purchase has purchase/debit representation.
- 100x bonus-buy feature result is separate from purchase debit.
- Balance comes from settlement/process result.
- Wrapper does not call wallet endpoint directly.
- Wallet/accounting references are carried.

## VABS/History Tests

- Round replay includes math profile, RTP/volatility, cascades, feature state, wallet refs, and deterministic replay refs.
- Session replay returns multiple rounds in order.
- Whole-session replay includes session metadata.
- Last hand payload includes the most recent completed or recoverable round.
- VABS display payload and Lasthands display payload exist.

## Pending/Stuck Tests

- Duplicate idempotency key is rejected or replayed safely.
- Pending base spin can recover.
- Pending bonus-buy purchase can recover without duplicate debit.
- Pending settlement remains visible.
- Stuck transaction review state is explicit.

## Blocked Tests

- Backoffice/Casino Manager VABS HTML compatibility: blocked until route expectations are proven.
- Wallet endpoint integration: blocked until WalletAndLaunchTester is explicitly approved.
- Registration-driven launch: blocked until GameServerRegistrar generation/apply is approved.
