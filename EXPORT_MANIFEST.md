# Export Manifest

Export type: raw-safe sanitized review checkpoint.

Checkpoint scope:

- Reusable workflow skill changes, including ParallelMathValidator.
- Lifecycle wrapper implementation summaries.
- VABS visual history route implementation summaries.
- VABS legacy alias implementation summaries.
- GS/wallet responsibility boundary correction docs.
- Public-safe skill snapshots and checkpoint reports.
- VisualPrototypeSandboxBuilder skill, references, and validator scripts.
- Visual sandbox builder adoption and future-game playbook docs.

Safety exclusions:

- No donor/scaffold asset bodies.
- No screenshots, HAR files, raw event logs, or captured media.
- No raw secrets, passwords, SIDs, signatures, tokenized URLs, or private URLs.
- No private local paths.
- No Staging source code.
- No production client implementation.
- No registration artifacts.
- No DB, Cassandra, wallet, GS, or BO/CM endpoint artifacts.
- No release approval.
- No local visual sandbox files, donor/reference assets, sandbox screenshots, or
  donor/reference script bodies.

Curation notes:

- Public metadata was rewritten for readable raw-safe review.
- Project docs were copied as public-safe copies with private paths, private
  hosts, donor hosts, tokenized URLs, and scaffold asset body paths removed or
  redacted.
- Skill snapshots were copied as text-only public-safe snapshots.
- Validator wording was updated to require accurate current status: no production
  client implementation was generated, while non-production planning/fixture
  materials may be documented separately.
- Long Markdown lines were wrapped in public copies for raw readability.

Included high-value paths:

- `README.md`
- `REVIEWER_START_HERE.md`
- `09_release/WORKFLOW_CONTENT_INTEGRITY_AUDIT.md`
- `_skill_suite_snapshot/ParallelMathValidator/`
- `_skill_suite_snapshot/WalletAndLaunchTester/SKILL.md`
- `_skill_suite_snapshot/GameServerRegistrar/SKILL.md`
- `_skill_suite_snapshot/RTPAndReleaseAuditor/SKILL.md`
- `_skill_suite_snapshot/VisualPrototypeSandboxBuilder/SKILL.md`
- `_skill_suite_snapshot/VisualPrototypeSandboxBuilder/references/`
- `_skill_suite_snapshot/VisualPrototypeSandboxBuilder/scripts/`
- `_skill_suite_snapshot/references/PUBLIC_EXPORT_SANITIZATION_RULES.md`
- `09_release/visual_sandbox_builder_skill_adoption.md`
- `09_release/future_game_visual_sandbox_builder_playbook.md`
- `09_release/visual_sandbox_builder_gate_matrix.md`
- `00_skill_reports/VisualPrototypeSandboxBuilderSkillCreation/`
- `03_protocol/gs_wallet_accounting_responsibility_audit.md`
- `03_protocol/8001_runtime_vs_gs_responsibility_matrix.md`
- `08_qa/8001_wallet_launch_test_scope_correction.md`

Known manifest notes:

- Private project files not present during curation: 03_protocol/runtime_payload_adapter_gap_analysis.md
- Reviewer references missing from export or represented as optional notes: 03_protocol/runtime_payload_adapter_gap_analysis.md,
  09_release/WORKFLOW_CONTENT_INTEGRITY_AUDIT.md
