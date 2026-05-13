# Fixture To Object State Matrix

Status: PLANNING_ONLY.

| Fixture | Object states | Notes |
|---|---|---|
| `01_base_idle.json` | scene.base.grid:idle | Object IDs remain planning mappings; final assets missing. |
| `02_base_no_win_spin.json` | scene.round_completion.ready:final_state_ready | Object IDs remain planning mappings; final assets missing. |
| `03_base_cluster_win_single_cascade.json` | scene.base.grid.cell.c1.r1.cascade_removed:cascade_remove, scene.base.grid.cell.c1.r5.new_symbol:cascade_refill, scene.base.grid.cluster.highlight.1:cluster_flash | Object IDs remain planning
mappings; final assets missing. |
| `04_base_cluster_win_multi_cascade.json` | scene.base.total_cascade_win_display:show_total_cascade_win | Object IDs remain planning mappings; final assets missing. |
| `05_golden_square_created.json` | scene.base.grid.cell.c3.r3.golden_overlay:golden_square_create | Object IDs remain planning mappings; final assets missing. |
| `06_golden_square_persistent_cascade.json` | scene.base.grid.cell.c3.r3.golden_overlay:golden_square_persist | Object IDs remain planning mappings; final assets missing. |
| `07_rainbow_activation.json` | scene.base.rainbow.activation:rainbow_activate, scene.base.grid.cell.c3.r3.golden_overlay:affected_by_rainbow | Object IDs remain planning mappings; final assets missing. |
| `08_bronze_coin_reveal.json` | scene.base.coin_reveal.bronze:bronze_coin_reveal | Object IDs remain planning mappings; final assets missing. |
| `09_silver_coin_reveal.json` | scene.base.coin_reveal.silver:silver_coin_reveal | Object IDs remain planning mappings; final assets missing. |
| `10_gold_coin_reveal.json` | scene.base.coin_reveal.gold:gold_coin_reveal | Object IDs remain planning mappings; final assets missing. |
| `11_pot_of_gold_special_reveal.json` | scene.base.special_reveal.pot_of_gold:special_reveal_candidate | Object IDs remain planning mappings; final assets missing. |
| `12_four_leaf_clover_special_reveal.json` | scene.base.special_reveal.four_leaf_clover:special_reveal_candidate | Object IDs remain planning mappings; final assets missing. |
| `13_feature_mode_1_entry.json` | scene.feature.mode_1.panel:feature_mode_entry | Object IDs remain planning mappings; final assets missing. |
| `14_feature_mode_2_entry.json` | scene.feature.mode_2.panel:feature_mode_entry | Object IDs remain planning mappings; final assets missing. |
| `15_feature_mode_3_entry.json` | scene.feature.mode_3.panel:feature_mode_entry | Object IDs remain planning mappings; final assets missing. |
| `16_bonus_buy_mode_selection.json` | scene.bonus_buy.mode_selection:mode_selection | Object IDs remain planning mappings; final assets missing. |
| `17_bonus_buy_purchased_feature_start.json` | scene.bonus_buy.mode_selection:purchased_feature_start, scene.feature.mode_2.panel:feature_mode_entry | Object IDs remain planning mappings; final assets missing. |
| `18_big_win_tier.json` | scene.win_tier.big:big_win_effect | Object IDs remain planning mappings; final assets missing. |
| `19_huge_win_tier.json` | scene.win_tier.huge:huge_win_effect | Object IDs remain planning mappings; final assets missing. |
| `20_mega_win_tier.json` | scene.win_tier.mega:mega_win_effect | Object IDs remain planning mappings; final assets missing. |
| `21_max_win_cap_reached.json` | scene.max_win.cap_overlay:cap_reached, scene.max_win.pre_cap_amount:show_pre_cap, scene.max_win.capped_amount:show_capped | Object IDs remain planning mappings; final assets missing. |
| `22_round_completion_ready.json` | scene.round_completion.ready:ready | Object IDs remain planning mappings; final assets missing. |
| `23_reconnect_state_restore.json` | scene.reconnect.restore_state:restore_available | Object IDs remain planning mappings; final assets missing. |
| `24_error_or_recovery_pending_state.json` | scene.reconnect.restore_state:recovery_pending | Object IDs remain planning mappings; final assets missing. |
