# Reviewer Start Here

Start with these files for the current checkpoint.

1. `10_sprint_reports/sprint_report_latest.md`
2. `project_manifest.json`
3. `04_math/authoritative_server_math_v1/rtp_volatility_profile_framework.md`
4. `04_math/authoritative_server_math_v1/rtp_volatility_profile_matrix.json`
5. `04_math/authoritative_server_math_v1/volatility_profile_design.md`
6. `04_math/authoritative_server_math_v1/volatility_profile_levers.json`
7. `04_math/authoritative_server_math_v1/simulation/profile_calibration_results.json`
8. `04_math/authoritative_server_math_v1/simulation/profile_calibration_report.md`
9. `04_math/authoritative_server_math_v1/simulation/profile_calibration_harness.py`
10. `04_math/authoritative_server_math_v1/simulation/simulate_authoritative_math.py`
11. `04_math/authoritative_server_math_v1/simulation_config_refinement/rtp_model_profiles.json`
12. `04_math/authoritative_server_math_v1/simulation_config_refinement/game_settings_profiles.json`
13. `00_skill_reports/MathModelDesigner/handoff.json`
14. `00_skill_reports/WorkflowOrchestrator/handoff.json`
15. `_skill_suite_snapshot/MathModelDesigner/SKILL.md`
16. `_skill_suite_snapshot/WorkflowOrchestrator/SKILL.md`

Review the math artifacts as planning and smoke-simulation evidence only.
Do not treat the simulator as certified production math.
Do not treat profile calibration as release approval.
Do not treat registration mapping as generated registration artifacts.
Do not treat renderer prototypes as production client code.

Important gates to verify:
Backend adapter implementation is still blocked.
GameClientBuilder implementation is still blocked.
GameServerRegistrar generation is still blocked.
Wallet and launch testing are still blocked.
Release approval is still false.
Final asset approval is still false.

Important math blockers to verify:
Bonus-buy EV remains pending.
Large-sample stability remains pending.
Max-win tail behavior remains unproven.
Certification-scale validation remains pending.

The raw-safe export method preserves physical line breaks.
It avoids the older collapsed-line export path.
GitHub raw validation should be treated as the source of truth.
