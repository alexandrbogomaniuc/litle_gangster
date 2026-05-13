# Workflow Gates

## Gate Names

- `GATE_0_PROJECT_CREATED`
- `GATE_1_DONOR_CAPTURED`
- `GATE_2_FEATURE_PARITY_LOCKED`
- `GATE_3_RUNTIME_LANE_LOCKED`
- `GATE_4_MATH_CONTRACT_LOCKED`
- `GATE_5_ART_REPLACEMENT_LOCKED`
- `GATE_6_CLIENT_BUILD_ALLOWED`
- `GATE_7_REGISTRATION_GENERATE_ALLOWED`
- `GATE_8_WALLET_TEST_ALLOWED`
- `GATE_9_RELEASE_AUDIT_ALLOWED`

## Implementation Blocks

GameClientBuilder implementation requires:

- `runtime_owner_proven=true`
- `result_api_contract_proven=true`
- `approved_assets_strategy_exists=true`
- `explicit_user_approval_for_client_code=true`

GameServerRegistrar generation requires:

- `registration_lane_proven=true`
- `scn_serializer_status=proven` or `scn_serializer_status=workaround_defined`
- `game_id_selected=true`
- `bank_source_selected=true`
- `rollback_strategy_exists=true`

WalletAndLaunchTester requires:

- `launch_url_or_test_environment_available=true`
- `safe_test_user_secret_reference_exists=true`
- `wallet_mock_or_stage_mode_selected=true`

Release audit approval requires:

- `math_approved=true`
- `client_build_approved=true`
- `registration_approved=true`
- `wallet_tests_approved=true`
- `final_assets_approved=true`

## Public Export Trust Gate

Public export validation requires:

1. Local validation before commit.
2. Commit created.
3. Local validation after commit.
4. Push succeeded.
5. Fresh post-push clone validation passed.
6. Pushed commit hash recorded.

Without step 5, reports must say local validation only.
