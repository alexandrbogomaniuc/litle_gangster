# External Reviewer Copy-Paste Report

## Sprint Identity
- Project: Little Gangster
- Project path: `[PROJECT_ROOT]`
- Sprint: Mantis/ExtGame scope correction for current-GS integration
- Date: 2026-05-11
- Tasks run: ProtocolAndSchemaMapper current-GS clarification, advisory-checklist doc patching, skill-suite checklist patching, SprintReporter
- Tasks not run: MathModelDesigner implementation, AuthorizedReferenceResearcher, ReferenceAssetInventory, ArtSceneMapper, ArtDirectionAndReplacementPlanner, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester,
RTPAndReleaseAuditor
- Public GitHub push: not performed

## User Instruction Received
Create a scope-correction package that treats the Mantis/ExtGame information as an advisory checklist, not as selected Little Gangster architecture. Patch project docs and relevant skill requirements so ExtGame remains candidate/unverified
unless current GS source/config proves it. Add missing validation checklist items for VABS/Lasthands/history, transaction/state/round completion, restart/FRB/OCB, RNG/certification, template parameters, and future QA. Do not run
implementation skills, generate code/math/registration, browse donor URLs, capture assets, call wallet endpoints, execute DB/Cassandra, approve release, or push to public GitHub.

## Source Documents/Evidence Inspected
- `[SKILL_SUITE_ROOT]/AGENTS.md`
- `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/ProtocolAndSchemaMapper/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/MathModelDesigner/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/GameServerRegistrar/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/WalletAndLaunchTester/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/RTPAndReleaseAuditor/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md`
- `[SKILL_SUITE_ROOT]/references/SPRINT_REPORTING_STANDARD.md`
- `[PROJECT_ROOT]/AGENTS.md`
- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- Existing Little Gangster protocol/runtime docs under `[PROJECT_ROOT]/03_protocol/`
- Existing ExtGame/Mantis placeholder docs under `[PROJECT_ROOT]/03_protocol/`, `/04_math/`, and `/08_qa/`
- Current Staging GS/new-games source signals under explicit manifest/Staging roots only
- Sanitized Mantis checklist content supplied in the user prompt

## Files Created
- `[PROJECT_ROOT]/03_protocol/mantis_lessons_current_gs_checklist.md`
- `[PROJECT_ROOT]/03_protocol/current_gs_integration_lane_validation.md`
- `[PROJECT_ROOT]/03_protocol/current_gs_little_gangster_contract_questions.md`
- `[PROJECT_ROOT]/03_protocol/vabs_lasthands_history_checklist.md`
- `[PROJECT_ROOT]/03_protocol/transaction_state_round_completion_checklist.md`
- `[PROJECT_ROOT]/03_protocol/restart_frb_ocb_promo_checklist.md`
- `[PROJECT_ROOT]/03_protocol/rng_testing_certification_checklist.md`
- `[PROJECT_ROOT]/03_protocol/template_parameter_checklist_from_mantis.md`
- `[PROJECT_ROOT]/03_protocol/mantis_scope_correction_report.md`
- `[PROJECT_ROOT]/03_protocol/current_gs_source_signal_scan.md`
- `[PROJECT_ROOT]/04_math/mantis_math_runtime_checklist.md`
- `[PROJECT_ROOT]/04_math/v0_3_mantis_requirements_for_next_math_retry.md`
- `[PROJECT_ROOT]/07_registration/mantis_template_parameter_registration_checklist.md`
- `[PROJECT_ROOT]/07_registration/current_gs_registration_lane_questions.md`
- `[PROJECT_ROOT]/08_qa/mantis_based_gs_integration_test_checklist.md`
- `[PROJECT_ROOT]/08_qa/vabs_lasthands_history_test_checklist.md`
- `[PROJECT_ROOT]/08_qa/process_transaction_equivalent_test_checklist.md`
- `[PROJECT_ROOT]/08_qa/restart_frb_ocb_test_checklist.md`
- `[PROJECT_ROOT]/08_qa/rng_bot_certification_test_checklist.md`
- `[PROJECT_ROOT]/08_qa/client_quality_performance_gate.md`
- `[PROJECT_ROOT]/00_skill_reports/MantisScopeCorrection/skill_report.md`
- `[PROJECT_ROOT]/00_skill_reports/MantisScopeCorrection/validation_checklist.md`
- `[PROJECT_ROOT]/00_skill_reports/MantisScopeCorrection/blockers.md`
- `[PROJECT_ROOT]/00_skill_reports/MantisScopeCorrection/handoff.json`
- `[SKILL_SUITE_ROOT]/references/MANTIS_EXTERNAL_COLLABORATION_CHECKLIST.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_history/20260511T092307+0100_MantisScopeCorrection.md`

## Files Modified
- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/03_protocol/protocol_contract_summary.json`
- `[PROJECT_ROOT]/03_protocol/extgame_external_collaboration_lessons.md`
- `[PROJECT_ROOT]/03_protocol/extgame_api_requirements_matrix.md`
- `[PROJECT_ROOT]/03_protocol/extgame_template_parameter_checklist.md`
- `[PROJECT_ROOT]/03_protocol/extgame_transaction_state_contract.md`
- `[PROJECT_ROOT]/03_protocol/extgame_vba_history_requirements.md`
- `[PROJECT_ROOT]/04_math/extgame_math_runtime_requirements.md`
- `[PROJECT_ROOT]/08_qa/extgame_testing_certification_requirements.md`
- `[SKILL_SUITE_ROOT]/references/EXTGAME_EXTERNAL_COLLABORATION_REQUIREMENTS.md`
- `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/ProtocolAndSchemaMapper/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/MathModelDesigner/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/GameServerRegistrar/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/WalletAndLaunchTester/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/RTPAndReleaseAuditor/SKILL.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_latest.md`

## Files Deleted
- None.

## Actions Performed
- Converted the Mantis/ExtGame material from selected-architecture wording into advisory checklist wording.
- Added a current-GS lane validation package that keeps ExtGame as candidate/unverified and records new-games `slot-browser-v1` as candidate evidence only, not selected truth.
- Ran targeted source-signal inspection only within the explicit current Staging roots available through project context.
- Added checklist docs for launch modes, template parameters, VABS/Lasthands/history, transaction-state handling, restart/FRB/OCB/promo handling, RNG/certification, and client quality gates.
- Patched MathModelDesigner requirements so the next v0.3 retry includes round completion state, win ratio/tier, max-win cap fields, bet mapping, state/lastAction handoff, process-equivalent accounting fields, and RNG boundaries.
- Patched GameServerRegistrar requirements so template fields from Mantis are candidate fields that must be verified against current GS before generation.
- Patched WalletAndLaunchTester requirements so process-equivalent, restart/resume, VABS/history, FRB/OCB, close-session, and redacted debugging checks are lane-dependent validation gates.
- Patched RTPAndReleaseAuditor requirements so local testing, bot testing, certification, source/runnable environment, RNG, VABS/history, and performance checks are explicit future gates.
- Updated manifest, assumptions, decisions log, protocol summary, and skill handoff.

## Validations Run
- Parsed `[PROJECT_ROOT]/project_manifest.json`.
- Parsed `[PROJECT_ROOT]/00_skill_reports/MantisScopeCorrection/handoff.json`.
- Parsed `[PROJECT_ROOT]/03_protocol/protocol_contract_summary.json`.
- Verified all required new checklist/report files exist and are non-empty.
- Ran a wording scan for prohibited selected-architecture claims.
- Ran a redaction scan for raw SIDs, signature values, tokens, private links, email addresses, tokenized URLs, and raw secret-looking assignments.
- Confirmed no donor browsing, asset capture, client code generation, math implementation, registration artifact generation, DB/Cassandra action, wallet/API call, release approval, or public GitHub push occurred.

## Key Findings
- Current GS source shows ExtGame-related concepts and archived/extgame documentation, but this does not prove Little Gangster should use an external endpoint architecture.
- Current GS/new-games evidence provides candidate `slot-browser-v1` HTTP runtime signals, but that lane must be verified directly against current GS before trust or selection.
- Legacy template/JSP support is present as a fallback/candidate lane, not selected by this sprint.
- GS source signals show VABS/VBA/Lasthands/history concepts exist, but the Little Gangster runtime contract for those remains unverified.
- Restart/resume concepts exist in GS/new-games signals, but FRB/OCB/promo transitions remain lane-dependent checklist items.
- Mantis `processTransactions` lessons are useful as accounting/state checklist items, but not proof that the current Little Gangster API is named or shaped that way.
- Production RNG ownership and certification path remain unverified for the current GS lane.

## Decisions Made
- Mantis/ExtGame material is now recorded as an advisory integration checklist only.
- ExtGame is not selected.
- No runtime lane is selected. New-games `slot-browser-v1` remains a candidate direction requiring direct current-GS verification.
- The next workflow skill should remain MathModelDesigner retry because v0.3 math/result contract still needs donor-parity and current-GS checklist updates.
- No release, math, client build, wallet, registration, or protocol approval gate was advanced.

## Assumptions
- The current Staging tree is the canonical active source root for GS/new-games/Crazy Rooster work.
- Exact source paths that differ from the expected Staging layout are blockers or path-mapping evidence, not permission to search unrelated old worktrees.
- Sanitized Mantis checklist content supplied in the prompt is sufficient for advisory checklist extraction.
- Current GS source/config must decide the final integration lane.

## Blockers
- `extgame_lane_unverified_for_current_gs`
- `vabs_lasthands_history_contract_unverified`
- `process_transaction_equivalent_unverified_for_current_gs`
- `round_completion_contract_unverified_for_current_gs`
- `production_rng_owner_unverified_for_current_gs`
- `frb_ocb_promo_support_decision_pending`
- `current_gs_expected_staging_paths_mismatch`
- `math_parity_retry_required`
- Existing runtime, wallet, registration, asset, and release blockers remain in force.

## Risks
- If ExtGame wording leaks back into selected-architecture docs, downstream implementation could target the wrong runtime lane.
- If current GS transaction/state semantics are not proven before implementation, wallet accounting and round recovery could be wrong.
- If VABS/Lasthands/history behavior is not verified, release certification and player support flows may fail.
- If v0.3 math retry omits round completion, win tiering, max-win cap, or state handoff fields, GameClientBuilder and WalletAndLaunchTester will inherit avoidable gaps.

## Anti-Hallucination Checks
- ExtGame is labelled advisory/candidate/unverified unless current GS proves otherwise.
- No file states ExtGame is selected.
- No file states Little Gangster must implement an external endpoint.
- No raw Mantis text was stored.
- No private links, emails, raw secrets, SIDs, signature values, donor assets, screenshots, HAR, or full donor URLs were stored.
- Unknowns are marked as blockers or pending validation rather than guessed.
- Current GS source scan uses `proven`, `likely`, `candidate`, `not found`, or `blocked` instead of claiming complete coverage.

## Current Trust Level
Partially trustworthy.

The scope correction and checklist patching are validated and trustworthy. Final runtime architecture, transaction/state implementation, VABS/history ownership, production RNG ownership, and FRB/OCB behavior remain partially trusted until
current GS source/config and later tests prove them.

## Next Recommended Step
Run MathModelDesigner retry to update the v0.3 donor-feature-parity math/result contract using the Mantis advisory checklist and current-GS validation questions. Do not proceed to GameClientBuilder until v0.3 result/state/round-completion
handoff is updated.

## Exact Next Recommended Codex Prompt
Use the reusable skill suite at `[SKILL_SUITE_ROOT]` and the existing project at `[PROJECT_ROOT]`. Run only MathModelDesigner and SprintReporter. Do not browse donor URLs, capture assets, generate client code, generate Cassandra
registration, execute DB/Cassandra, call wallet endpoints, ask for secrets, store secrets, approve release, or push to GitHub. Goal: update the v0.3 donor-feature-parity math/result contract using the Mantis advisory checklist and
current-GS validation docs. Treat ExtGame as advisory/candidate only unless current GS proves it. Add or verify cascade/golden-square/rainbow/coin/feature modes, round completion state, winRatio/winTier, max-win cap fields, cluster bet
mapping, state/lastAction/Lasthands handoff fields, process-transaction-equivalent accounting handoff, restart/resume and FRB/OCB blockers, RNG boundary, and no active double-up unless donor evidence appears. Stop after SprintReporter.
