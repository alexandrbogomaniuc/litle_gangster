# Sprint Report: MathCalibrationSprint

## Result

- Calibration sprint completed: yes.
- Simulator ran: yes.
- Scope: compact smoke calibration only, not certification.
- RTP models covered: `rtp_96`, `rtp_94`, `rtp_92`.

## Smoke Results

| Model | Rounds | Observed return multiplier | Status |
| --- | ---: | ---: | --- |
| `rtp_96` | 75 | 0.132 | smoke_not_calibrated |
| `rtp_94` | 75 | 0.349547 | smoke_not_calibrated |
| `rtp_92` | 75 | 0.1044 | smoke_not_calibrated |

The simulator produced structured output for all three models, but the 75-round results are smoke-only and not close enough to target RTP to unlock implementation or registration.

## Blocked Values

- Bonus-buy EV remains blocked; purchased feature EV is not modeled yet.
- Free-spin and feature-mode trigger/retrigger/mode probabilities remain provisional.
- Symbol weights and cluster paytable remain pending calibration.
- GL cluster bet mapping and registration compatibility values remain placeholders.
- Jackpot remains disabled by default pending product decision.

## Gate Status

- Backend adapter implementation remains blocked.
- Registration generation remains blocked.
- Exact values are not final or certified.

## Files Created

- `04_math/authoritative_server_math_v1/simulation/calibration_smoke_summary.md`
- `04_math/authoritative_server_math_v1/simulation/calibration_smoke_results.json`
- `04_math/authoritative_server_math_v1/simulation/calibration_blockers.md`
- `00_skill_reports/MathModelDesigner/calibration_sprint_skill_report.md`
- `00_skill_reports/MathModelDesigner/calibration_sprint_validation_checklist.md`
- `00_skill_reports/MathModelDesigner/calibration_sprint_blockers.md`
- `10_sprint_reports/sprint_report_history/20260512_174312_MathCalibrationSprint.md`

## Files Modified

- `00_skill_reports/MathModelDesigner/handoff.json`
- `project_manifest.json`
- `assumptions.md`
- `decisions_log.md`
- `10_sprint_reports/sprint_report_latest.md`

## Validation

- `project_manifest.json` parses.
- MathModelDesigner `handoff.json` parses.
- `calibration_smoke_results.json` parses.
- Simulator compiles and ran for all three models.
- No Staging, backend adapter, client, registration, DB, wallet, donor browsing, asset capture, or release work occurred.

## Next Prompt

Run a compact MathModelDesigner calibration continuation to add or validate bonus-buy EV, free-spin/feature-mode probabilities, and longer multi-seed RTP tuning. Do not start backend/client/registration implementation automatically.
