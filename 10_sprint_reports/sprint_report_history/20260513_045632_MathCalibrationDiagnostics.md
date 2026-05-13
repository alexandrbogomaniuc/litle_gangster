# Sprint Report - Math Calibration Diagnostics

Created: 2026-05-13T03:56:32Z

## Goal

Diagnose why smoke simulator observed returns were very low and decide whether limited tuning is safe.

## Outcome

Calibration diagnostics completed. The simulator runs, but sanity status is `runs_but_not_reliable_for_calibration`. No simulator patch was applied and no tuning was performed.

## Results

- rtp_96: mean observed return multiplier 0.205943 over 30,000 rounds.
- rtp_94: mean observed return multiplier 0.208106 over 30,000 rounds.
- rtp_92: mean observed return multiplier 0.198437 over 30,000 rounds.

## Findings

- Low return is not tiny sample size only.
- Target RTP uses percent-style profile values; observed return is emitted as a multiplier.
- Cluster-equivalent bet denominator is not modeled.
- Free-spin, feature-mode, and bonus-buy EV paths are incomplete for calibration.
- Jackpot remains disabled by default.

## Files Created

- 04_math/authoritative_server_math_v1/simulation/calibration_diagnostics_report.md
- 04_math/authoritative_server_math_v1/simulation/calibration_diagnostic_results.json
- 04_math/authoritative_server_math_v1/simulation/calibration_next_tuning_actions.md
- 00_skill_reports/MathModelDesigner/calibration_diagnostics_skill_report.md
- 00_skill_reports/MathModelDesigner/calibration_diagnostics_validation_checklist.md
- 00_skill_reports/MathModelDesigner/calibration_diagnostics_blockers.md

## Files Modified

- 00_skill_reports/MathModelDesigner/handoff.json
- project_manifest.json
- assumptions.md
- decisions_log.md
- 10_sprint_reports/sprint_report_latest.md

## Validations

- project_manifest.json parses.
- MathModelDesigner handoff.json parses.
- calibration_diagnostic_results.json parses.
- simulator compiles and runs.
- all three RTP models covered.
- no Staging, backend, client, registration, DB, wallet, donor, asset, or release work performed.

## Blockers

- rtp_denominator_and_unit_model_pending
- free_spin_feature_mode_simulation_pending
- bonus_buy_ev_model_pending
- provisional_weights_paytable_not_certified

## Next Recommended Prompt

Use the reusable skill suite at `[SKILL_SUITE_ROOT]` and the project at `[PROJECT_ROOT]`. Run only `MathModelDesigner simulator model-completeness fix` in fast-lane mode. Patch only the non-production simulator under
`04_math/authoritative_server_math_v1/simulation/` to add explicit RTP denominator/percent reporting from game settings and integrate free-spin, feature-mode, and bonus-buy EV smoke paths. Do not touch Staging, backend adapter, client code,
registration, DB, wallet, donor assets, public export, or release gates. Stop after compact SprintReporter.
