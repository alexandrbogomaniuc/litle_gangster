# External Reviewer Copy-Paste Report

## 1. Sprint Identity

- Sprint: SourcePatchPlanningGamePayload
- Skill: ProtocolAndSchemaMapper
- Project: Little Gangster
- Project root: `[PROJECT_ROOT]`
- Skill suite: `[SKILL_SUITE_ROOT]`
- Report generated: 2026-05-12 09:05:24

## 2. User Instruction Received

Run only ProtocolAndSchemaMapper source patch planning for `presentationPayload.gamePayload`, then SprintReporter. Do not run public export, GitHub push, Staging source patching, backend/runtime implementation, GameClientBuilder
implementation, client code generation, registration, DB/Cassandra, wallet calls, donor browsing, asset capture, or release approval.

## 3. Source Documents/Evidence Inspected

- igaming-codex-skills AGENTS.md, SKILL_INDEX.md, ProtocolAndSchemaMapper/SKILL.md, SprintReporter/SKILL.md
- project AGENTS.md, project_manifest.json, assumptions.md, decisions_log.md
- schema extension review docs under 03_protocol and ProtocolAndSchemaMapper reports
- backend/runtime adapter proof docs under 03_protocol
- fixture planning and static renderer context under 06_resulting_code
- v0.3 result/runtime boundary docs under 04_math/alternatives/v0_3_donor_feature_parity_provisional
- Staging core-protocol schemas.ts, IGameTransport.ts, and GsHttpRuntimeTransport.ts read-only
- Staging UI-kit PremiumPresentationMapper.ts read-only
- Staging new-games-server src/index.ts and nearby tests read-only
- Staging 7001 RuntimeOutcomeMapper.ts and provisionalMathSource.ts read-only
- Staging Gamesv1 docs/gs/schemas response schemas and contract/presentation mapper tests read-only

## 4. Files Created

- `[PROJECT_ROOT]/03_protocol/source_patch_planning_summary.md`
- `[PROJECT_ROOT]/03_protocol/core_protocol_game_payload_patch_blueprint.md`
- `[PROJECT_ROOT]/03_protocol/transport_type_patch_blueprint.md`
- `[PROJECT_ROOT]/03_protocol/ui_kit_game_payload_passthrough_blueprint.md`
- `[PROJECT_ROOT]/03_protocol/new_games_server_game_payload_blueprint.md`
- `[PROJECT_ROOT]/03_protocol/little_gangster_adapter_blueprint.md`
- `[PROJECT_ROOT]/03_protocol/source_patch_order_and_rollback.md`
- `[PROJECT_ROOT]/03_protocol/source_patch_test_plan.md`
- `[PROJECT_ROOT]/03_protocol/source_patch_risks_and_blockers.md`
- `[PROJECT_ROOT]/06_resulting_code/planning/source_patch_readiness_summary.md`
- `[PROJECT_ROOT]/06_resulting_code/planning/game_payload_schema_contract_for_future_client.md`
- `[PROJECT_ROOT]/06_resulting_code/planning/fixture_strict_schema_update_plan.md`
- `[PROJECT_ROOT]/06_resulting_code/planning/static_renderer_schema_alignment_plan.md`
- `[PROJECT_ROOT]/06_resulting_code/planning/gameclientbuilder_after_schema_patch_plan.md`
- `[PROJECT_ROOT]/08_qa/source_patch_validation_matrix.md`
- `[PROJECT_ROOT]/08_qa/core_protocol_game_payload_schema_tests.md`
- `[PROJECT_ROOT]/08_qa/ui_kit_game_payload_passthrough_tests.md`
- `[PROJECT_ROOT]/08_qa/new_games_server_game_payload_tests.md`
- `[PROJECT_ROOT]/08_qa/little_gangster_adapter_contract_tests.md`
- `[PROJECT_ROOT]/09_release/schema_patch_approval_gate.md`
- `[PROJECT_ROOT]/03_protocol/patch_proposals/core_protocol_schemas_game_payload.diff.md`
- `[PROJECT_ROOT]/03_protocol/patch_proposals/core_protocol_transport_types_game_payload.diff.md`
- `[PROJECT_ROOT]/03_protocol/patch_proposals/ui_kit_presentation_mapper_game_payload.diff.md`
- `[PROJECT_ROOT]/03_protocol/patch_proposals/new_games_server_game_payload.diff.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/source_patch_planning_skill_report.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/source_patch_planning_validation_checklist.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/source_patch_planning_blockers.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/source_patch_planning_file_changes.json`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_history/20260512_090524_SourcePatchPlanningGamePayload.md`

## 5. Files Modified

- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/handoff.json`
- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_latest.md`

## 6. Files Deleted

- None.

## 7. Actions Performed

- Inspected the exact Staging source files and nearby tests read-only.
- Identified canonical JSON schemas, Zod helpers, transport types, UI-kit mapper, and server emission points affected by `gamePayload` support.
- Created patch-ready blueprint docs without applying source changes.
- Created `.diff.md` proposal documents that explicitly say NOT APPLIED and PROPOSAL ONLY.
- Created rollback, approval-gate, and future test plans.
- Updated ProtocolAndSchemaMapper handoff, project manifest, assumptions, and decisions log.
- Did not modify any file under `[STAGING_ROOT]`.

## 8. Validations Run

- PASS project_manifest.json parses
- PASS ProtocolAndSchemaMapper handoff.json parses
- PASS source_patch_planning_file_changes.json parses
- PASS required 03_protocol source patch planning files exist and are non-empty
- PASS required 06_resulting_code/planning files exist and are non-empty
- PASS required 08_qa files exist and are non-empty
- PASS 09_release/schema_patch_approval_gate.md exists and is non-empty
- PASS patch proposal .diff.md files exist and are non-empty
- PASS no real .diff or .patch file was created
- PASS patch proposals clearly state NOT APPLIED / PROPOSAL ONLY
- PASS approval required before source modification documented
- PASS no package.json/src/public/dist/build under 06_resulting_code
- PASS no raw email/secret-like values in sprint outputs
- PASS manifest and handoff source_patches_applied=false
- PASS manifest and handoff staging_source_modified=false
- PASS adapter and GameClientBuilder implementation allowed flags remain false
- PASS no Staging source write commands were run
- PASS Staging source does not contain applied gamePayload code

## 9. Key Findings

- The real patch must include canonical JSON response schemas under `Gamesv1/docs/gs/schemas`, not only `schemas.ts`.
- `schemas.ts` should add optional strict `GamePayloadExtensionSchema` and keep the parent presentation schema strict.
- The transport interface should expose `PresentationPayload` and `GamePayloadExtension` types.
- `GsHttpRuntimeTransport.ts` is already permissive enough to carry the extension; no functional parser change is required, but regression coverage is required.
- `PremiumPresentationMapper.ts` should pass through `gamePayload` untouched.
- New-games-server should add a reusable helper and later an 8001 branch only after runtime owner proof and explicit implementation approval.
- 7001 `mathBridge` should remain unchanged in the first patch and be protected by compatibility tests.

## 10. Direct Answer: What Source Files Need Patching

Required future patch targets:

- Gamesv1/docs/gs/schemas/opengame.response.schema.json
- Gamesv1/docs/gs/schemas/playround.response.schema.json
- Gamesv1/docs/gs/schemas/featureaction.response.schema.json
- Gamesv1/docs/gs/schemas/resumegame.response.schema.json
- Gamesv1/docs/gs/schemas/gethistory.response.schema.json
- Gamesv1/docs/gs/schemas/closegame.response.schema.json
- Gamesv1/packages/core-protocol/src/schemas.ts
- Gamesv1/packages/core-protocol/src/IGameTransport.ts
- Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts
- new-games-server/src/index.ts

Reviewed or test-only targets with no required functional patch in the first pass:

- Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts
- Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts
- Gamesv1/games/7001/src/app/runtime/provisionalMathSource.ts
- Gamesv1/tests/contract/browser-runtime.contract.test.ts
- Gamesv1/tests/game/presentation-mapper.test.ts
- new-games-server/test/ngs-contract.e2e.test.ts
- new-games-server/test/ngs-failure-reconnect.e2e.test.ts

## 11. Direct Answer: What Patch Is Recommended

Add optional `presentationPayload.gamePayload` with `gameKey`, `schemaVersion`, and object-shaped `payload`; keep parent schemas strict; keep `mathBridge` unchanged; expose a transport type; pass `gamePayload` through UI-kit untouched; add
server emission support later behind approved 8001 runtime ownership.

## 12. Direct Answer: Whether Any Source Was Modified

No. No Staging source was modified, and no source patch was applied.

## 13. Direct Answer: Whether Patch Can Be Applied Next With Approval

Yes for the schema/type/mapper patch set, if the user explicitly approves Staging source modification and the patch is limited to the planned files. Backend adapter implementation and full GameClientBuilder implementation remain separate
blocked steps.

## 14. Decisions Made

- Use `presentationPayload.gamePayload` as the recommended reusable extension point.
- Use optional `gamePayload` for backward compatibility.
- Use object-shaped payload at the core boundary rather than accepting primitives.
- Keep the parent presentation schema strict.
- Keep 7001 `mathBridge` unchanged in the first patch.
- Make UI-kit pass through `gamePayload` without interpreting v0.3 game data.
- Defer 8001 server branch and backend adapter implementation until explicit approval/runtime owner proof.

## 15. Assumptions

- Game-specific validation belongs in game/backend adapter packages after core transports accept the generic extension.
- Existing JSON schema contract tests are the strongest validation lane for canonical wire compatibility.
- `GsHttpRuntimeTransport.ts` should stay a transport/parser layer, not a game payload interpreter.

## 16. Blockers

- Explicit user approval is required before any Staging source patch can be applied.
- Canonical JSON response schemas still need gamePayload support.
- Core Zod PresentationPayloadSchema still needs gamePayload support.
- UI-kit mapper still needs gamePayload passthrough support.
- New-games-server still has no approved 8001 Little Gangster payload branch.
- Little Gangster/8001 runtime owner remains unproven.
- Backend adapter implementation remains unapproved.
- Full GameClientBuilder implementation remains blocked.

## 17. Risks

- Updating only Zod without JSON schemas would leave contract tests failing.
- Updating only schema without UI-kit passthrough would make payloads valid but inaccessible to shared client mapping.
- Allowing arbitrary top-level presentation fields would weaken schema drift detection.
- Migrating 7001 `mathBridge` in the same patch would increase regression risk.

## 18. Anti-Hallucination Checks

- Patch proposal files are Markdown `.diff.md`, not real patches.
- Proposal docs explicitly state NOT APPLIED and PROPOSAL ONLY.
- Validation checked that no real `.diff` or `.patch` files were created.
- Validation checked that no `gamePayload` code appeared in Staging source after the sprint.
- No public export, GitHub push, DB, wallet, donor browsing, asset capture, or release approval was run.

## 19. Current Trust Level

High for patch target identification and source behavior because the exact source files and tests were inspected. Medium for future 8001 server branch details because 8001 runtime owner remains unproven.

## 20. Next Recommended Step

If ready, explicitly approve ProtocolAndSchemaMapper source patch apply for the schema/type/mapper portion only. Otherwise remain blocked.

## 21. Exact Next Recommended Codex Prompt

```text
Use the reusable skill suite at:

[SKILL_SUITE_ROOT]

Use the existing project at:

[PROJECT_ROOT]

Run only this sprint:

1. ProtocolAndSchemaMapper source patch apply for presentationPayload.gamePayload
2. SprintReporter

This is explicit approval to modify only the listed Staging source files needed for reusable presentationPayload.gamePayload schema/type/mapper support. Do not implement the Little Gangster backend adapter, do not run GameClientBuilder
implementation, do not generate production client code, do not run public export/GitHub push, registration, DB/Cassandra, wallet calls, donor browsing, asset capture, or release approval.

Apply only the approved schema/type/mapper patch set, run the listed contract/mapper tests, record rollback notes, and keep adapter implementation and full GameClientBuilder blocked unless separately approved.
```
