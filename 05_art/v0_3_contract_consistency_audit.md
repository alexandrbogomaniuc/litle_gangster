# v0.3 Math/Art/Runtime Contract Consistency Audit

## Scope

This audit compared `result_schema.json` canonical fields with v0.3 ArtSceneMapper references in animation maps, object maps, scene maps, object-state CSV, the result-state mapping report, and the HTML inspector. No math implementation,
payout logic, client code, registration artifact, donor browsing, asset capture, DB/Cassandra action, wallet call, or release approval occurred.

## Result

- Contract consistency audit completed: true.
- Result schema changed: false.
- Scene mapping changed: true.
- HTML inspector changed: true.
- Unique mismatches/helpers found: 63.
- Unique aliases patched: 55.
- Unresolved mismatches: 0.

## Specific Known Issues

- `feature_mode_state.spins_remaining` was found and patched to `feature_mode_state.spins_or_rounds_remaining`.
- `lastAction` and `state_persistence.lastAction` were found and patched to `state_persistence.lastAction_or_current_gs_equivalent`.
- Scene/art shorthand references that omitted `base_game.` were patched to fully qualified schema paths.
- Bonus-buy `mode_selection` and `purchase_cost_x_bet` references were patched to `selected_mode` and `cost_x_bet`.

## Coverage

Core animation-relevant v0.3 fields remain mapped for cascades, golden-square state, rainbow activation, coin and special reveals, feature modes, bonus buy, max-win cap, win tiers, round completion, and state persistence. Metadata,
wallet/accounting boundary, RNG debug, and registration fields are documented as boundaries and must not be browser-authoritative.

## Remaining Blockers

- runtime_result_owner_unproven
- result_api_contract_review_required_before_full_client_build
- full_game_client_builder_blocked_until_runtime_contract_review
- release_math_not_approved
- approved_release_assets_missing
