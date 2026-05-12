# Current GS Registration/RNG Audit Blockers

## Blocking Issues

- `game_8001_registration_missing`: no current Staging registration/config evidence for Little Gangster/8001 was found.
- `scn_serializer_missing`: the serializer/admin/cache generation path for `scn`/`jcn` registration payloads is not proven.
- `runtime_result_owner_unproven`: final Little Gangster RNG/result owner is not proven.
- `math_import_evidence_not_found`: no evidence was found that game registration imports executable math.
- `gamesv1_lane_candidate_not_final`: Gamesv1/slot-browser-v1 has supporting evidence but remains candidate, not final truth.
- `core_protocol_package_not_fully_inspected_for_8001`: core protocol exists, but final 8001 runtime integration remains unproven.
- `new_games_server_final_8001_math_integration_unproven`: New Games backend sample/provisional outcome generation exists, but 8001 integration is not proven.
- `vabs_lasthands_history_contract_unverified`: history/VABS/Lasthand behavior exists in current GS concepts but is not mapped for Little Gangster.
- `process_transaction_equivalent_unverified_for_current_gs`: reserve/settle bridge is proven, but Mantis-style processTransactions equivalence is not selected.

## Non-Blocking But Important

- The previous patch touched v0.3 package/config files outside the requested scope, but the changes reviewed were boundary metadata/doc wording only.
- Staging path layout differs from earlier direct path expectations; actual source paths were under `platform-source/platform/...`.

## Required Before Registrar Generation

- Confirm selected integration lane.
- Confirm game ID and bank/casino assignment.
- Prove route/client/runtime endpoint values.
- Prove scn/jcn serializer/admin update process.
- Confirm registration template fields against current GS schema/config.
- Generate rollback/spec files first; do not apply to DB without explicit approval.

## Required Before Client Build

- Confirm result owner and runtime contract.
- Confirm v0.3 result schema with cascade/golden-square/rainbow/coin/feature-mode states.
- Confirm scene map coverage for any new v0.3 animation states.
- Keep scaffold assets blocked from release.
