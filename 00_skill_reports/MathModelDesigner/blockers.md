# MathModelDesigner Blockers

## Unresolved Blockers

- `new_games_server_source_path_missing`: backend `/slot/v1/*` source path is still missing.
- `core_protocol_package_not_inspected`: `@gamesv1/core-protocol` package root has not been inspected.
- `slot_v1_result_owner_unknown`: final authoritative RNG/result owner for 8001 is not proven.
- `runtime_math_integration_pending`: math package has not been integrated into backend/new-games runtime.
- `game_8001_registration_missing`: no 8001 GS/Cassandra route/config records exist.
- `scn_serializer_missing`: no safe serializer/config-generation tool verified for binary `scn`.
- `approved_release_assets_missing`: scaffold/reference assets are not release-approved.
- `wallet_launch_tests_missing`: no 8001 wallet/launch tests exist.
- `independent_multi_seed_certification_pending`: only one deterministic 1,000,000-round seed per RTP variant was run.
- `bonus_buy_ev_needs_review`: bonus buy price and EV need product/math review.
- `double_up_product_decision_pending`: optional double-up behavior needs product/regulatory confirmation.

## Partially Resolved

- `math_package_missing`: resolved for workflow purposes by creating `04_math/math_package.json`.
- `rtp_validation_missing`: partially resolved for workflow purposes by 1,000,000-round simulations that passed tolerance.

## Not Release Approved

The math package is not release-approved. Later runtime integration, independent validation, wallet/launch testing, and RTPAndReleaseAuditor are required.
