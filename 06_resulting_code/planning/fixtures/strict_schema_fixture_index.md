# Strict Schema Fixture Index

Status: VALIDATED_NON_PRODUCTION_FIXTURES.

| Fixture | Target patched response schema | Response valid | v0.3 payload valid |
|---|---|---:|---:|
| `01_base_idle.json` | `opengame.response.schema.json` | True | True |
| `02_base_no_win_spin.json` | `playround.response.schema.json` | True | True |
| `03_base_cluster_win_single_cascade.json` | `playround.response.schema.json` | True | True |
| `04_base_cluster_win_multi_cascade.json` | `playround.response.schema.json` | True | True |
| `05_golden_square_created.json` | `playround.response.schema.json` | True | True |
| `06_golden_square_persistent_cascade.json` | `playround.response.schema.json` | True | True |
| `07_rainbow_activation.json` | `playround.response.schema.json` | True | True |
| `08_bronze_coin_reveal.json` | `playround.response.schema.json` | True | True |
| `09_silver_coin_reveal.json` | `playround.response.schema.json` | True | True |
| `10_gold_coin_reveal.json` | `playround.response.schema.json` | True | True |
| `11_pot_of_gold_special_reveal.json` | `playround.response.schema.json` | True | True |
| `12_four_leaf_clover_special_reveal.json` | `playround.response.schema.json` | True | True |
| `13_feature_mode_1_entry.json` | `featureaction.response.schema.json` | True | True |
| `14_feature_mode_2_entry.json` | `featureaction.response.schema.json` | True | True |
| `15_feature_mode_3_entry.json` | `featureaction.response.schema.json` | True | True |
| `16_bonus_buy_mode_selection.json` | `featureaction.response.schema.json` | True | True |
| `17_bonus_buy_purchased_feature_start.json` | `featureaction.response.schema.json` | True | True |
| `18_big_win_tier.json` | `playround.response.schema.json` | True | True |
| `19_huge_win_tier.json` | `playround.response.schema.json` | True | True |
| `20_mega_win_tier.json` | `playround.response.schema.json` | True | True |
| `21_max_win_cap_reached.json` | `playround.response.schema.json` | True | True |
| `22_round_completion_ready.json` | `closegame.response.schema.json` | True | True |
| `23_reconnect_state_restore.json` | `resumegame.response.schema.json` | True | True |
| `24_error_or_recovery_pending_state.json` | `gethistory.response.schema.json` | True | True |

Schema distribution:

- `closegame.response.schema.json`: 1
- `featureaction.response.schema.json`: 5
- `gethistory.response.schema.json`: 1
- `opengame.response.schema.json`: 1
- `playround.response.schema.json`: 15
- `resumegame.response.schema.json`: 1
