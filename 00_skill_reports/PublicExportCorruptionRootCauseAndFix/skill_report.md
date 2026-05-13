# PublicExportCorruptionRootCauseAndFix Skill Report

Sprint: PublicExportCorruptionRootCauseAndFix

## Outcome

- Public export corruption was treated as confirmed from the external contradiction for commit `ca854797d2d67def46f17dd989164b71ce49cc44`.
- Root cause status: not proven from current local files.
- Proven process failure: prior validation trusted export-local validation and did not require an independent project-local GitHub raw validator.
- Fix applied: project-local raw validator created, public export rebuilt with newline-preserving copy/redaction, replacement commit pushed, and GitHub raw validated from outside the public export.

## Replacement Commit

- Pushed commit: `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c`
- GitHub raw validation passed: true
- Public export validation passed: true

## GitHub Raw Line Counts

- README.md: 49
- REVIEWER_START_HERE.md: 44
- scripts/validate_public_export.py: 193
- _skill_suite_snapshot/WorkflowOrchestrator/SKILL.md: 67

## Files Created

- `00_skill_reports/PublicExportCorruptionRootCauseAndFix/skill_report.md`
- `00_skill_reports/PublicExportCorruptionRootCauseAndFix/validation_checklist.md`
- `00_skill_reports/PublicExportCorruptionRootCauseAndFix/blockers.md`
- `00_skill_reports/PublicExportCorruptionRootCauseAndFix/handoff.json`
- `00_skill_reports/PublicExportCorruptionRootCauseAndFix/root_cause_report.md`
- `scripts/validate_github_raw_public_export.py`

## Files Modified

- `project_manifest.json`
- `assumptions.md`
- `decisions_log.md`
- `00_skill_reports/PublicGitExport/handoff.json`
- `00_skill_reports/CheckpointGitReviewPush/handoff.json`

## Public Export Commit

The public export repo committed 116 file changes under the replacement checkpoint. The key public-export changes were README/reviewer metadata, newline-preserving validator replacement, sanitized/redacted artifact updates, removal of
raw/corrupt-prone files, and addition of the corruption-fix report folder.

## Gates

- Backend/client/registration implementation: not run.
- Staging source modification: not run.
- Wallet/API/DB/donor browsing/asset capture: not run.
- Release approval: false.
