# Math Quality Gate Blockers

## Open

- `full_6x5_multi_seed_validation_pending`: selected v0.2 needs longer independent multi-seed validation before release math approval.
- `new_games_server_source_path_missing`: current backend runtime source still needs inspection in a later permitted sprint.
- `core_protocol_package_not_inspected`: core protocol remains a runtime integration blocker.
- `slot_v1_result_owner_unknown`: exact production RNG/result owner remains unproven.
- `runtime_math_integration_pending`: math package has not been integrated into backend/new-games runtime.
- `game_8001_registration_missing`: registration is not generated or approved.
- `scn_serializer_missing`: serializer/config pipeline is still missing.
- `approved_release_assets_missing`: scaffold/reference assets remain blocked from release.
- `wallet_launch_tests_missing`: wallet and launch tests have not run.
- `bonus_buy_ev_needs_review`: bonus buy pricing and EV remain provisional.
- `double_up_product_decision_pending`: double-up remains placeholder pending product/regulatory decision.
- `staging_source_root_manifest_update_pending`: future source-inspection work must verify/update roots to `[STAGING_ROOT]` only.

## Resolved For Downstream Layout

- `layout_mismatch_5x3_vs_6x5`: resolved by selecting v0.2 6x5 cluster for ArtSceneMapper.

## Superseded But Preserved

- `v0_1_rtp_scaling_blocks_true_math_validation`: v0.1 remains preserved as audit history but is no longer the selected math package.
