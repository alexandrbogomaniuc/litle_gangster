# GameClientBuilder Contract Requirements For v0.3

Status: planning-only handoff. This file does not authorize implementation, runtime code, registration generation, wallet calls, or release approval.

## Required Before Full Build

- Current GS runtime/result owner must be proven.
- Result API contract must be reviewed against `result_schema.json`.
- Browser/client result authority must remain false.
- Registration metadata must remain separate from executable math and animation payloads.
- Wallet/accounting state must remain separate from rendering.

## Canonical Fields The Client May Render After Runtime API Review

- `base_game.cascade_steps[]` and nested removed/drop/refill/cluster/win fields.
- `base_game.golden_squares_before`, `base_game.golden_square_events`, `base_game.golden_squares_after`, `base_game.golden_square_positions`.
- `base_game.rainbow_positions`, `base_game.rainbow_activation_events`, `base_game.affected_golden_squares`, `base_game.activation_source`.
- `base_game.coin_reveals[]` and `base_game.special_reveals[]`.
- `feature_mode_state.*`, including `feature_mode_state.spins_or_rounds_remaining`.
- `bonus_buy_state.selected_mode`, `bonus_buy_state.cost_x_bet`, and purchased feature state.
- `max_win_cap.*`.
- `winRatio`, `winTier`, and `win_tier_source`.
- `round_completion.*`.
- `state_persistence.*`, including `state_persistence.lastAction_or_current_gs_equivalent`.

## Must Not Be Browser-Produced

- RNG values, authoritative outcomes, cascade decisions, wins, caps, wallet/accounting state, round completion authority, or registration metadata.

## Renderer Helpers

Settings/help/developer-boundary labels may appear in inspector or scene docs, but they are not authoritative result schema fields. They must be kept out of payout, settlement, and RNG logic.
