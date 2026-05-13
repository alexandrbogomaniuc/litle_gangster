# Fixture Index

Status: NON_PRODUCTION_PLANNING_ONLY.

These fixtures are static renderer planning data. They are not production runtime proof, backend implementation, wallet payloads, registration metadata, or release approval.

| Fixture | Purpose | Expected scene states | Expected object IDs |
|---|---|---|---|
| `01_base_idle.json` | Preview the 6x5 base grid with no active round outcome. | base_game_scene.idle | scene.base.grid |
| `02_base_no_win_spin.json` | Preview a backend-provided completed spin with no clusters or win. | base_game_scene.no_win, round_completion.ready | scene.round_completion.ready |
| `03_base_cluster_win_single_cascade.json` | Preview one cluster removal, drop, refill, and win highlight cascade. | cascade_sequence.remove, cascade_sequence.drop, cascade_sequence.refill, big_win_scene.small_label |
scene.base.grid.cell.c1.r1.cascade_removed, scene.base.grid.cell.c1.r5.new_symbol, scene.base.grid.cluster.highlight.1 |
| `04_base_cluster_win_multi_cascade.json` | Preview ordered multi-cascade playback with cumulative win display. | cascade_sequence.step_0, cascade_sequence.step_1, cascade_sequence.total_win | scene.base.total_cascade_win_display |
| `05_golden_square_created.json` | Preview a new golden-square overlay from backend result state. | golden_square_overlay.created | scene.base.grid.cell.c3.r3.golden_overlay |
| `06_golden_square_persistent_cascade.json` | Preview golden-square before/after persistence through a cascade. | golden_square_overlay.before, cascade_sequence.step_0, golden_square_overlay.after |
scene.base.grid.cell.c3.r3.golden_overlay |
| `07_rainbow_activation.json` | Preview rainbow activation and affected golden-square cells. | rainbow_activation_scene.activate, golden_square_overlay.affected | scene.base.rainbow.activation, scene.base.grid.cell.c3.r3.golden_overlay |
| `08_bronze_coin_reveal.json` | Preview bronze coin reveal tier. | coin_reveal_scene.bronze | scene.base.coin_reveal.bronze |
| `09_silver_coin_reveal.json` | Preview silver coin reveal tier. | coin_reveal_scene.silver | scene.base.coin_reveal.silver |
| `10_gold_coin_reveal.json` | Preview gold coin reveal tier. | coin_reveal_scene.gold | scene.base.coin_reveal.gold |
| `11_pot_of_gold_special_reveal.json` | Preview pot_of_gold special reveal candidate. | coin_reveal_scene.pot_of_gold | scene.base.special_reveal.pot_of_gold |
| `12_four_leaf_clover_special_reveal.json` | Preview four_leaf_clover special reveal candidate. | coin_reveal_scene.four_leaf_clover | scene.base.special_reveal.four_leaf_clover |
| `13_feature_mode_1_entry.json` | Preview feature mode entry panel for mode_1. | feature_mode_selection.entry, feature_mode_selection.mode_1 | scene.feature.mode_1.panel |
| `14_feature_mode_2_entry.json` | Preview feature mode entry panel for mode_2. | feature_mode_selection.entry, feature_mode_selection.mode_2 | scene.feature.mode_2.panel |
| `15_feature_mode_3_entry.json` | Preview feature mode entry panel for mode_3. | feature_mode_selection.entry, feature_mode_selection.mode_3 | scene.feature.mode_3.panel |
| `16_bonus_buy_mode_selection.json` | Preview bonus-buy mode selector without purchase/accounting authority. | bonus_buy_panel.mode_selection | scene.bonus_buy.mode_selection |
| `17_bonus_buy_purchased_feature_start.json` | Preview purchased feature start state, without wallet settlement authority. | bonus_buy_panel.purchased, feature_mode_selection.mode_2 | scene.bonus_buy.mode_selection,
scene.feature.mode_2.panel |
| `18_big_win_tier.json` | Preview backend-provided big win tier presentation. | big_win_scene.big | scene.win_tier.big |
| `19_huge_win_tier.json` | Preview backend-provided huge win tier presentation. | big_win_scene.huge | scene.win_tier.huge |
| `20_mega_win_tier.json` | Preview backend-provided mega win tier presentation. | big_win_scene.mega | scene.win_tier.mega |
| `21_max_win_cap_reached.json` | Preview max-win cap overlay using backend-capped values. | max_win_cap_scene.cap_overlay, big_win_scene.mega | scene.max_win.cap_overlay, scene.max_win.pre_cap_amount, scene.max_win.capped_amount |
| `22_round_completion_ready.json` | Preview final-state-ready markers and backend-owned round completion. | round_completion_state.ready | scene.round_completion.ready |
| `23_reconnect_state_restore.json` | Preview reconnect restore from backend-provided state persistence payload. | state_recovery_reconnect_scene.restore_state, reconnect_modal.restore | scene.reconnect.restore_state |
| `24_error_or_recovery_pending_state.json` | Preview recoverable error/retry display without wallet/API call. | error_modal.recovery_pending, reconnect_modal.restore | scene.reconnect.restore_state |
