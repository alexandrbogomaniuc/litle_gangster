# v0.3 Result Schema Field Aliases

Status: planning contract documentation only. No payout logic, runtime implementation, registration artifact, or release approval is changed by this file.

## Canonical Result Field Rules

- Use fully-qualified `base_game.*` paths for base-game cascade, golden-square, rainbow, coin, and special reveal fields.
- Use `feature_mode_state.spins_or_rounds_remaining` as the canonical feature remaining-count field.
- Use `state_persistence.lastAction_or_current_gs_equivalent` as the canonical reconnect/history state field.
- Use `bonus_buy_state.selected_mode` and `bonus_buy_state.cost_x_bet` for bonus-buy mode and cost.
- Browser/client code must not produce authoritative RNG, outcome, win, wallet/accounting, or registration fields.

## Patched Aliases

| Old/reference field | Canonical field | Status |
|---|---|---|
| `activation_source` | `base_game.activation_source` | patched in art/scene references where present |
| `affected_golden_squares` | `base_game.affected_golden_squares` | patched in art/scene references where present |
| `animationHints.desktop_layout` | `animationHints` | patched in art/scene references where present |
| `animationHints.mobile_layout` | `animationHints` | patched in art/scene references where present |
| `animationHints.superTurbo` | `animationHints` | patched in art/scene references where present |
| `animationHints.turbo` | `animationHints` | patched in art/scene references where present |
| `baseGame.clusters` | `base_game.clusters` | patched in art/scene references where present |
| `baseGame.featureTriggers` | `base_game.feature_triggers` | patched in art/scene references where present |
| `baseGame.grid` | `base_game.grid_before` | patched in art/scene references where present |
| `bet.amount` | `bet` | patched in art/scene references where present |
| `bonusBuy` | `bonus_buy_state` | patched in art/scene references where present |
| `bonus_buy_state.mode_selection` | `bonus_buy_state.selected_mode` | patched in art/scene references where present |
| `bonus_buy_state.purchase_cost_x_bet` | `bonus_buy_state.cost_x_bet` | patched in art/scene references where present |
| `cascade_index` | `base_game.cascade_index` | patched in art/scene references where present |
| `cascade_steps` | `base_game.cascade_steps` | patched in art/scene references where present |
| `cascade_steps[].cascade_index` | `base_game.cascade_steps[].cascade_index` | patched in art/scene references where present |
| `cascade_steps[].cascade_win` | `base_game.cascade_steps[].cascade_win` | patched in art/scene references where present |
| `cascade_steps[].clusters` | `base_game.cascade_steps[].clusters` | patched in art/scene references where present |
| `cascade_steps[].coin_reveals` | `base_game.cascade_steps[].coin_reveals` | patched in art/scene references where present |
| `cascade_steps[].dropped_cells` | `base_game.cascade_steps[].dropped_cells` | patched in art/scene references where present |
| `cascade_steps[].golden_square_events` | `base_game.cascade_steps[].golden_square_events` | patched in art/scene references where present |
| `cascade_steps[].golden_squares_after` | `base_game.cascade_steps[].golden_squares_after` | patched in art/scene references where present |
| `cascade_steps[].golden_squares_before` | `base_game.cascade_steps[].golden_squares_before` | patched in art/scene references where present |
| `cascade_steps[].grid_after` | `base_game.cascade_steps[].grid_after` | patched in art/scene references where present |
| `cascade_steps[].grid_before` | `base_game.cascade_steps[].grid_before` | patched in art/scene references where present |
| `cascade_steps[].new_symbols` | `base_game.cascade_steps[].new_symbols` | patched in art/scene references where present |
| `cascade_steps[].rainbow_activation_events` | `base_game.cascade_steps[].rainbow_activation_events` | patched in art/scene references where present |
| `cascade_steps[].removed_cells` | `base_game.cascade_steps[].removed_cells` | patched in art/scene references where present |
| `cascade_steps[].special_reveals` | `base_game.cascade_steps[].special_reveals` | patched in art/scene references where present |
| `cascade_steps[].total_cascade_win` | `base_game.cascade_steps[].total_cascade_win` | patched in art/scene references where present |
| `cascade_steps[].winning_clusters` | `base_game.cascade_steps[].winning_clusters` | patched in art/scene references where present |
| `cascade_win` | `base_game.cascade_win` | patched in art/scene references where present |
| `clusters` | `base_game.clusters` | patched in art/scene references where present |
| `coin_reveals` | `base_game.coin_reveals` | patched in art/scene references where present |
| `coin_reveals[].cascade_index` | `base_game.coin_reveals[].cascade_index` | patched in art/scene references where present |
| `coin_reveals[].position` | `base_game.coin_reveals[].position` | patched in art/scene references where present |
| `coin_reveals[].source_event` | `base_game.coin_reveals[].source_event` | patched in art/scene references where present |
| `coin_reveals[].tier` | `base_game.coin_reveals[].tier` | patched in art/scene references where present |
| `coin_reveals[].value_units` | `base_game.coin_reveals[].value_units` | patched in art/scene references where present |
| `coin_reveals[].value_x_bet` | `base_game.coin_reveals[].value_x_bet` | patched in art/scene references where present |
| `dropped_cells` | `base_game.dropped_cells` | patched in art/scene references where present |
| `feature_mode_state.mode_status` | `feature_mode_state.feature_complete` | patched in art/scene references where present |
| `feature_mode_state.spins_awarded` | `feature_mode_state.spins_or_rounds_remaining` | patched in art/scene references where present |
| `feature_mode_state.spins_remaining` | `feature_mode_state.spins_or_rounds_remaining` | patched in art/scene references where present |
| `feature_triggers` | `base_game.feature_triggers` | patched in art/scene references where present |
| `final_grid` | `base_game.final_grid` | patched in art/scene references where present |
| `freeSpins` | `feature_mode_state` | patched in art/scene references where present |
| `golden_square_events` | `base_game.golden_square_events` | patched in art/scene references where present |
| `golden_square_positions` | `base_game.golden_square_positions` | patched in art/scene references where present |
| `golden_squares_after` | `base_game.golden_squares_after` | patched in art/scene references where present |
| `golden_squares_before` | `base_game.golden_squares_before` | patched in art/scene references where present |
| `grid_before` | `base_game.grid_before` | patched in art/scene references where present |
| `initial_grid` | `base_game.initial_grid` | patched in art/scene references where present |
| `lastAction` | `state_persistence.lastAction_or_current_gs_equivalent` | patched in art/scene references where present |
| `new_symbols` | `base_game.new_symbols` | patched in art/scene references where present |
| `persistence_scope` | `base_game.persistence_scope` | patched in art/scene references where present |
| `rainbow_activation_events` | `base_game.rainbow_activation_events` | patched in art/scene references where present |
| `rainbow_activation_events[].activation_source` | `base_game.activation_source` | patched in art/scene references where present |
| `rainbow_activation_events[].affected_golden_squares` | `base_game.affected_golden_squares` | patched in art/scene references where present |
| `rainbow_positions` | `base_game.rainbow_positions` | patched in art/scene references where present |
| `removed_cells` | `base_game.removed_cells` | patched in art/scene references where present |
| `round_completion.error_state` | `round_completion.current_gs_equivalent_status` | patched in art/scene references where present |
| `round_completion.ready` | `round_completion.final_state_ready` | patched in art/scene references where present |
| `special_reveals` | `base_game.special_reveals` | patched in art/scene references where present |
| `special_reveals[].confidence` | `base_game.special_reveals[].confidence` | patched in art/scene references where present |
| `special_reveals[].position` | `base_game.special_reveals[].position` | patched in art/scene references where present |
| `special_reveals[].reveal_type` | `base_game.special_reveals[].reveal_type` | patched in art/scene references where present |
| `special_reveals[].source_event` | `base_game.special_reveals[].source_event` | patched in art/scene references where present |
| `special_reveals[].value` | `base_game.special_reveals[].value` | patched in art/scene references where present |
| `state_persistence.lastAction` | `state_persistence.lastAction_or_current_gs_equivalent` | patched in art/scene references where present |
| `total_cascade_win` | `base_game.total_cascade_win` | patched in art/scene references where present |
| `walletAccounting` | `wallet_accounting_boundary` | patched in art/scene references where present |

## Renderer Or Developer Helpers

| Helper | Meaning |
|---|---|
| `help_rules.cluster_rules` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `help_rules.feature_modes` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `help_rules.max_win_cap` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `help_rules.win_tiers` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `runtime_result_owner` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `settings` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `settings.music` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |
| `settings.sound` | Renderer/developer helper only; not an authoritative result schema field. Keep outside payout/result authority. |

## Boundary

Current GS result owner remains unproven. Registration metadata is not executable math import. Full GameClientBuilder remains blocked; planning-only review may consume these canonical names after runtime API review.
