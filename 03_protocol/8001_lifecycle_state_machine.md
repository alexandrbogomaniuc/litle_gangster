# 8001 Lifecycle State Machine

Date: 2026-05-15
Status: planning only

## State Definitions

| State | Purpose | Allowed next states | Blocking notes |
| --- | --- | --- | --- |
| `session_start` | Entry point for validated launch/session context. | `open_game`, `error_pending` | Requires gameId 8001, bank/session/mode/lang
  context. |
| `open_game` | Create or resume runtime session. | `base_idle`, `reconnect_pending`, `restart_required`, `error_pending` | Registration settings and
  profile identity must be available. |
| `base_idle` | Player can perform base spin or approved feature purchase. | `base_spin_pending`, `bonus_buy_purchase_pending`, `close_pending`,
  `reconnect_pending` | No pending settlement. |
| `base_spin_pending` | Paid base spin action accepted and accounting/action record pending. | `cascade_active`, `feature_triggered`, `cap_reached`,
  `settlement_pending`, `error_pending`, `stuck_transaction_review` | Must have idempotency/action id. |
| `cascade_active` | Cascades are resolving and replayable state is changing. | `cascade_active`, `feature_triggered`, `cap_reached`,
  `settlement_pending`, `error_pending`, `reconnect_pending` | Browser must not determine wins. |
| `feature_triggered` | Feature entry has been triggered from base/cascade result. | `free_spins_active`, `settlement_pending`, `error_pending` |
  Feature state must be persisted before response. |
| `free_spins_active` | Free-spin or feature-spin sequence active. | `free_spins_active`, `cascade_active`, `cap_reached`, `settlement_pending`,
  `reconnect_pending`, `error_pending` | Action representation required for each feature spin result. |
| `bonus_buy_purchase_pending` | 100x bonus-buy purchase/debit is pending or accepted. | `bonus_buy_feature_active`, `settlement_pending`,
  `error_pending`, `stuck_transaction_review` | 125x/150x must remain blocked. |
| `bonus_buy_feature_active` | Purchased feature sequence active. | `bonus_buy_feature_active`, `cascade_active`, `cap_reached`, `settlement_pending`,
  `reconnect_pending`, `error_pending` | Carries declared BF_RTP target and 100x cost. |
| `cap_reached` | Cap/max-win condition reached or being enforced. | `settlement_pending`, `round_complete`, `error_pending` | Cap state must be
  persisted and visible to history. |
| `round_complete` | Game rules complete; no further cascade/free-spin/bonus-buy action pending. | `settlement_pending`, `settlement_complete`,
  `base_idle` | Requires round completion signature/helper proof later. |
| `settlement_pending` | Wallet/accounting settle or equivalent process result pending. | `settlement_complete`, `stuck_transaction_review`,
  `error_pending` | Do not replace with repeated getBalance polling. |
| `settlement_complete` | Accounting complete and balance/reference known. | `base_idle`, `close_pending`, `reconnect_pending` | History/Lasthands
  should be final for round. |
| `reconnect_pending` | Player reconnect requested during stored state. | `open_game`, `base_idle`, `cascade_active`, `free_spins_active`,
  `bonus_buy_feature_active`, `error_pending` | Must use persisted wrapper state. |
| `restart_required` | Legacy restart or FRB transition required. | `open_game`, `free_spins_active`, `error_pending` | Requires `restart=true`
  advisory and FRB checklist handling. |
| `close_pending` | Close-game/session requested. | `settlement_complete`, `error_pending`, `stuck_transaction_review` | Must preserve unfinished
  state if not round complete. |
| `error_pending` | Recoverable or terminal error requiring mapped response/log. | `open_game`, `base_idle`, `stuck_transaction_review`,
  `close_pending` | Must preserve safe error/logging data. |
| `stuck_transaction_review` | Pending/stuck accounting state requiring review/retry/rollback. | `settlement_pending`, `error_pending`,
  `close_pending` | Wallet/launch testing required before release. |

## Notes

This state machine is a planning contract. It does not implement wrapper code and does not approve wallet tests, DB changes, registration generation,
  client code, or release.
