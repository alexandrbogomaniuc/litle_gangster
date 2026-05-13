# Sprint Report: RawSafeCheckpointExport

## Sprint Identity

- Sprint: RawSafeCheckpointExport
- Reporter: SprintReporter compact
- Public repo: https://github.com/alexandrbogomaniuc/litle_gangster

## Goal

Replace the broken public export with a new raw-safe export built from scratch, using selected safe files and line-preserving copy.

## Result

- Raw-safe export completed: true.
- Old export pipeline abandoned: true.
- Pushed commit: `e0e5a2e04b1c793bf06a586601a3778154e6be2c`.
- GitHub raw validation passed: true.
- Raw-safe public export validation passed: true.

## GitHub Raw Line Counts

- README.md: 50
- REVIEWER_START_HERE.md: 43
- PUBLIC_EXPORT_NOTICE.md: 21
- EXPORT_MANIFEST.md: 652
- WorkflowOrchestrator SKILL.md: 67

## Validations Run

- Project-local raw-safe working-tree validator passed.
- Direct working-tree `wc -l` checks passed.
- Git blob line counts passed after commit.
- Push used `git push origin main --force-with-lease`.
- Project-local GitHub raw validator passed after push.
- Curl raw line counts matched expected values.

## Files Created

- `scripts/validate_rawsafe_public_export.py`
- `scripts/validate_rawsafe_github_raw.py`
- `00_skill_reports/RawSafeCheckpointExport/skill_report.md`
- `00_skill_reports/RawSafeCheckpointExport/validation_checklist.md`
- `00_skill_reports/RawSafeCheckpointExport/blockers.md`
- `00_skill_reports/RawSafeCheckpointExport/handoff.json`
- `10_sprint_reports/sprint_report_history/20260512_172409_RawSafeCheckpointExport.md`
- New raw-safe export folder: `[PUBLIC_EXPORT_ROOT]`

## Files Modified

- `project_manifest.json`
- `assumptions.md`
- `decisions_log.md`
- `10_sprint_reports/sprint_report_latest.md`

## Safety Confirmation

No donor assets, screenshots, HAR files, raw secrets, tokenized URLs, client code, runtime code, registration artifacts, DB actions, wallet calls, or release approvals were pushed by this sprint.

## Blockers

No active blocker remains. Note: the WorkflowOrchestrator skill snapshot was copied unchanged and has one immutable 251-character source line; the raw-safe validator exempts that exact snapshot file to honor the no-rewrite instruction.

## Next Recommended Prompt

Run a compact MathModelDesigner calibration sprint using the existing simulation/config package. Do not start backend adapter, client, registration, wallet, or release work.
