# GL Settings Registration Dependency Audit

Status: generation blocked.

Direct answer:

- GL/template settings are mapped to math/runtime/registration dependencies in `09_release/consolidation_gate/math_config_gl_dependency_matrix.md`.
- They are not final values and must not be generated as registration artifacts yet.

Registration-safe categories:

- game id, title, bank/sub-casino, route/client/API/internal base settings.
- RTP display/config fields.
- model selection metadata.
- bet and denomination metadata.
- max-win/cap display metadata.
- feature flags.

Not registration-owned:

- executable math.
- RNG.
- cluster evaluation.
- cascade generation.
- bonus-buy outcome generation.
- jackpot award logic.
- wallet settlement truth.
- VABS replay truth.

Current blockers:

- game_8001_registration_missing.
- selected_runtime_lane_not_final.
- scn_serializer_missing.
- math_import_not_proven.
- runtime_result_owner_unproven.
- production_client_path_missing.
- approved_release_assets_missing.
- wallet_launch_tests_missing.

Conclusion:

- GameServerRegistrar artifact generation remains blocked.

## Simulation Config Refinement Update

The refined game settings profiles include GL/template fields for `rtp_96`, `rtp_94`, and `rtp_92`. Fixed-line fields are represented as compatibility metadata only because Little Gangster is a cluster game. Registration remains
metadata/config/routing only and must not import executable math.
