# Fixture To Runtime Schema Mapping

Status: COMPLETE_FOR_NON_PRODUCTION_STRICT_FIXTURES.

| Fixture | Target patched response schema | Validation result |
|---|---|---|
| `01_base_idle.json` | `opengame.response.schema.json` | passed |
| `02_base_no_win_spin.json` | `playround.response.schema.json` | passed |
| `03_base_cluster_win_single_cascade.json` | `playround.response.schema.json` | passed |
| `04_base_cluster_win_multi_cascade.json` | `playround.response.schema.json` | passed |
| `05_golden_square_created.json` | `playround.response.schema.json` | passed |
| `06_golden_square_persistent_cascade.json` | `playround.response.schema.json` | passed |
| `07_rainbow_activation.json` | `playround.response.schema.json` | passed |
| `08_bronze_coin_reveal.json` | `playround.response.schema.json` | passed |
| `09_silver_coin_reveal.json` | `playround.response.schema.json` | passed |
| `10_gold_coin_reveal.json` | `playround.response.schema.json` | passed |
| `11_pot_of_gold_special_reveal.json` | `playround.response.schema.json` | passed |
| `12_four_leaf_clover_special_reveal.json` | `playround.response.schema.json` | passed |
| `13_feature_mode_1_entry.json` | `featureaction.response.schema.json` | passed |
| `14_feature_mode_2_entry.json` | `featureaction.response.schema.json` | passed |
| `15_feature_mode_3_entry.json` | `featureaction.response.schema.json` | passed |
| `16_bonus_buy_mode_selection.json` | `featureaction.response.schema.json` | passed |
| `17_bonus_buy_purchased_feature_start.json` | `featureaction.response.schema.json` | passed |
| `18_big_win_tier.json` | `playround.response.schema.json` | passed |
| `19_huge_win_tier.json` | `playround.response.schema.json` | passed |
| `20_mega_win_tier.json` | `playround.response.schema.json` | passed |
| `21_max_win_cap_reached.json` | `playround.response.schema.json` | passed |
| `22_round_completion_ready.json` | `closegame.response.schema.json` | passed |
| `23_reconnect_state_restore.json` | `resumegame.response.schema.json` | passed |
| `24_error_or_recovery_pending_state.json` | `gethistory.response.schema.json` | passed |
