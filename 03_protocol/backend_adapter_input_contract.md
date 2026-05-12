# Backend Adapter Input Contract

Status: DEFINED_FOR_FUTURE_IMPLEMENTATION_NOT_APPLIED.

The future adapter input must be backend-owned. Browser/client input may carry user intent and correlation IDs, but
must never carry authoritative results.

## Required Input Shape

| Input group | Required fields | Owner | Evidence label |
|---|---|---|---|
| Authoritative v0.3 result | `gameId`, `roundId`, `spinId`, `operationId`, `stateVersion`, `mathVersion`, `rtpVariant` | backend/runtime | REQUIRED_V0_3 |
| Outcome detail | `base_game`, cascade steps, removed/dropped/refilled cells, golden squares, rainbow events, coin/special reveals | backend/runtime | REQUIRED_V0_3 |
| Feature state | `feature_mode_state`, `bonus_buy_state`, selected feature action result | backend/runtime | REQUIRED_V0_3 |
| Win and cap | `bet`, `totalWin`, `winRatio`, `winTier`, `max_win_cap` | backend/runtime | REQUIRED_V0_3 |
| Round completion | `round_completion` with finality flags | backend/runtime | REQUIRED_V0_3 |
| Persistence | `state_persistence` including current grid, pending cascades, golden-square state, feature mode, cap state, recovery state | backend/runtime | REQUIRED_V0_3 |
| Wallet/accounting | balance, previous balance, currency, reserve/settle result, bet/win minor units | wallet/runtime | PROVEN_GENERIC_BOUNDARY |
| Runtime correlation | `sessionId`, request counter, state version, idempotency key, client operation id | runtime | PROVEN_GENERIC |
| History/Lasthand | persisted replay snapshot, archival data, VABS/VBA-equivalent references if selected by runtime | runtime | REQUIRED_HISTORY_NOT_PROVEN_8001 |
| Fixture metadata | non-production fixture id and safety markers | test harness only | NON_PRODUCTION_ONLY |

## Input Rules

- Evidence label: PROVEN_BOUNDARY. The browser must not provide RNG output, result totals, cap decisions, reveal
  decisions, wallet truth, or history truth.
- Evidence label: REQUIRED. Future implementation must reject or ignore any client-provided authoritative result
  fields.
- Evidence label: REQUIRED. Non-production fixture metadata may appear only in test paths and must not enter live
  production round generation.

