# v0.3 Scene Contract Patch Report

## Summary

- Result schema changed: false.
- Scene/art mapping changed: true.
- HTML inspector changed: true.
- Mismatches found: 63 unique field-name/helper mismatches.
- Mismatches patched: 55 unique aliases.
- Unresolved mismatches: 0.

## Key Patches

- `feature_mode_state.spins_remaining` -> `feature_mode_state.spins_or_rounds_remaining`.
- `lastAction` / `state_persistence.lastAction` -> `state_persistence.lastAction_or_current_gs_equivalent`.
- Base-game shorthand fields such as `cascade_steps[]`, `coin_reveals[]`, and `golden_squares_before` now use `base_game.*` canonical paths.
- `bonus_buy_state.mode_selection` -> `bonus_buy_state.selected_mode`.
- `bonus_buy_state.purchase_cost_x_bet` -> `bonus_buy_state.cost_x_bet`.
- `round_completion.ready` -> `round_completion.final_state_ready`.

## Renderer Helpers

`settings.*`, `help_rules.*`, and `runtime_result_owner` are documented as renderer/developer helpers rather than authoritative result schema fields.
