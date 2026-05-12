# Fixture To Scene State Matrix

Status: PLANNING_ONLY.

| Fixture | Scene states | Notes |
|---|---|---|
| `01_base_idle.json` | base_game_scene.idle | Non-production renderer expectation only. |
| `02_base_no_win_spin.json` | base_game_scene.no_win, round_completion.ready | Non-production renderer expectation only. |
| `03_base_cluster_win_single_cascade.json` | cascade_sequence.remove, cascade_sequence.drop, cascade_sequence.refill, big_win_scene.small_label | Non-production renderer expectation only. |
| `04_base_cluster_win_multi_cascade.json` | cascade_sequence.step_0, cascade_sequence.step_1, cascade_sequence.total_win | Non-production renderer expectation only. |
| `05_golden_square_created.json` | golden_square_overlay.created | Non-production renderer expectation only. |
| `06_golden_square_persistent_cascade.json` | golden_square_overlay.before, cascade_sequence.step_0, golden_square_overlay.after | Non-production renderer expectation only. |
| `07_rainbow_activation.json` | rainbow_activation_scene.activate, golden_square_overlay.affected | Non-production renderer expectation only. |
| `08_bronze_coin_reveal.json` | coin_reveal_scene.bronze | Non-production renderer expectation only. |
| `09_silver_coin_reveal.json` | coin_reveal_scene.silver | Non-production renderer expectation only. |
| `10_gold_coin_reveal.json` | coin_reveal_scene.gold | Non-production renderer expectation only. |
| `11_pot_of_gold_special_reveal.json` | coin_reveal_scene.pot_of_gold | Non-production renderer expectation only. |
| `12_four_leaf_clover_special_reveal.json` | coin_reveal_scene.four_leaf_clover | Non-production renderer expectation only. |
| `13_feature_mode_1_entry.json` | feature_mode_selection.entry, feature_mode_selection.mode_1 | Non-production renderer expectation only. |
| `14_feature_mode_2_entry.json` | feature_mode_selection.entry, feature_mode_selection.mode_2 | Non-production renderer expectation only. |
| `15_feature_mode_3_entry.json` | feature_mode_selection.entry, feature_mode_selection.mode_3 | Non-production renderer expectation only. |
| `16_bonus_buy_mode_selection.json` | bonus_buy_panel.mode_selection | Non-production renderer expectation only. |
| `17_bonus_buy_purchased_feature_start.json` | bonus_buy_panel.purchased, feature_mode_selection.mode_2 | Non-production renderer expectation only. |
| `18_big_win_tier.json` | big_win_scene.big | Non-production renderer expectation only. |
| `19_huge_win_tier.json` | big_win_scene.huge | Non-production renderer expectation only. |
| `20_mega_win_tier.json` | big_win_scene.mega | Non-production renderer expectation only. |
| `21_max_win_cap_reached.json` | max_win_cap_scene.cap_overlay, big_win_scene.mega | Non-production renderer expectation only. |
| `22_round_completion_ready.json` | round_completion_state.ready | Non-production renderer expectation only. |
| `23_reconnect_state_restore.json` | state_recovery_reconnect_scene.restore_state, reconnect_modal.restore | Non-production renderer expectation only. |
| `24_error_or_recovery_pending_state.json` | error_modal.recovery_pending, reconnect_modal.restore | Non-production renderer expectation only. |
