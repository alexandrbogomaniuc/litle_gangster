# Reviewer Start Here

This raw-safe checkpoint is intended for workflow review, not release approval.

Recommended review order:

- `GAME_STATUS_CURRENT.md`
- `project_manifest.json`
- `10_sprint_reports/sprint_report_latest.md`
- `09_release/current_release_blockers.md`
- `07_registration/current_registration_readiness.md`
- `03_protocol/runtime_api_inspection_report.md`
- `03_protocol/runtime_payload_adapter_gap_analysis.md`
- `03_protocol/backend_adapter_apply_summary.md`
- `03_protocol/8001_lifecycle_wrapper_apply_summary.md`
- `03_protocol/8001_vabs_visual_history_route_apply_summary.md`
- `03_protocol/8001_vabs_legacy_alias_apply_summary.md`
- `03_protocol/gs_wallet_accounting_responsibility_audit.md`
- `03_protocol/8001_runtime_vs_gs_responsibility_matrix.md`
- `08_qa/8001_wallet_launch_test_scope_correction.md`
- `07_registration/8001_wallet_config_registration_dependency.md`
- `00_skill_reports/ProtocolAndSchemaMapper/handoff.json`
- `00_skill_reports/GsResponsibilityBoundaryAudit/handoff.json`
- `_skill_suite_snapshot/ParallelMathValidator/SKILL.md`
- `_skill_suite_snapshot/WalletAndLaunchTester/SKILL.md`
- `_skill_suite_snapshot/GameServerRegistrar/SKILL.md`
- `_skill_suite_snapshot/RTPAndReleaseAuditor/SKILL.md`

Safety notes:

- Staging source code is not exported.
- Backend adapter, lifecycle wrapper, VABS visual route, and legacy alias changes
  are summarized only through public-safe reports.
- No production client implementation was generated.
- GameClientBuilder implementation remains blocked.
- GameServerRegistrar generation remains blocked.
- Wallet, launch, and history tests are missing.
- Certification false and release blocked.

Missing optional references:

- `03_protocol/runtime_payload_adapter_gap_analysis.md`: not present in private project at curation time; see `EXPORT_MANIFEST.md`.
- `09_release/WORKFLOW_CONTENT_INTEGRITY_AUDIT.md`: not present in private project at curation time; see `EXPORT_MANIFEST.md`.

Reviewer focus:

- Confirm the reusable workflow skill changes are substantive and not one-line
  placeholders.
- Confirm the GS/wallet responsibility boundary no longer implies the browser or
  renderer owns real casino balance.
- Confirm VABS/Lasthands review material covers canonical routes, legacy aliases,
  durable-storage blockers, and BO/CM acceptance blockers.
- Confirm no raw private URLs, tokenized URLs, donor hosts, asset bodies, or
  source-code bundles are present.
