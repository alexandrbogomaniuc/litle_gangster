# External Reviewer Copy-Paste Report

## 1. Sprint Identity

Sprint: BackendAdapterImplementationPlanning

Skills run: ProtocolAndSchemaMapper backend adapter implementation planning, SprintReporter

Project: Little Gangster

Date: 2026-05-12

## 2. User Instruction Received

Use the 24 strict `presentationPayload.gamePayload` fixtures to define the exact future backend adapter
implementation plan, tests, source files, approval gates, and rollback strategy. Do not implement the backend
adapter, do not modify Staging source, do not create `Gamesv1/games/8001`, do not run GameClientBuilder
implementation, do not run registration, DB/Cassandra, wallet/API, public export, donor browsing, asset capture, or
release approval.

## 3. Source Documents/Evidence Inspected

- Skill suite AGENTS/SKILL_INDEX and ProtocolAndSchemaMapper/SprintReporter skill docs.
- Little Gangster AGENTS, project manifest, assumptions, and decisions log.
- Strict fixture update docs, validator, validation CSV, and 24 strict fixture examples.
- Applied source patch evidence bundle and source patch apply reports.
- Schema and adapter planning outputs, including `gamePayload` contract, adapter input/output contract, and blockers.
- v0.3 result schema, math package, runtime handoff, RNG boundary, state persistence, round completion, and animation state contracts.
- Static fixture renderer documentation and limitations.
- Read-only Staging sources:
  - `Gamesv1/packages/core-protocol/src/schemas.ts`
  - `Gamesv1/packages/core-protocol/src/IGameTransport.ts`
  - `Gamesv1/packages/ui-kit/src/shell/presentation/PremiumPresentationMapper.ts`
  - `new-games-server/src/index.ts`
  - `Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts`
  - `Gamesv1/games/7001/src/app/runtime/provisionalMathSource.ts`
- Optional read-only test context:
  - `Gamesv1/tests/contract/browser-runtime.contract.test.ts`
  - `Gamesv1/tests/game/presentation-mapper.test.ts`
  - `new-games-server/test/ngs-contract.e2e.test.ts`

## 4. Files Created

- `03_protocol/backend_adapter_implementation_planning_report.md`
- `03_protocol/backend_adapter_target_location_decision.md`
- `03_protocol/backend_adapter_input_contract.md`
- `03_protocol/backend_adapter_output_contract.md`
- `03_protocol/backend_adapter_file_plan.md`
- `03_protocol/backend_adapter_state_persistence_plan.md`
- `03_protocol/backend_adapter_history_lasthands_plan.md`
- `03_protocol/backend_adapter_fixture_test_plan.md`
- `03_protocol/backend_adapter_approval_gates.md`
- `03_protocol/backend_adapter_implementation_blockers.md`
- `06_resulting_code/planning/backend_adapter_implementation_plan_summary.md`
- `06_resulting_code/planning/backend_adapter_file_plan_for_future_patch.md`
- `06_resulting_code/planning/backend_adapter_fixture_usage_plan.md`
- `06_resulting_code/planning/gameclientbuilder_after_backend_adapter_plan.md`
- `08_qa/backend_adapter_unit_test_plan.md`
- `08_qa/backend_adapter_schema_test_plan.md`
- `08_qa/backend_adapter_history_recovery_test_plan.md`
- `08_qa/backend_adapter_fixture_regression_plan.md`
- `09_release/backend_adapter_implementation_approval_gate.md`
- `03_protocol/patch_proposals/backend_adapter_file_plan.diff.md`
- `03_protocol/patch_proposals/new_games_server_8001_payload_branch.diff.md`
- `03_protocol/patch_proposals/backend_adapter_tests.diff.md`
- `00_skill_reports/ProtocolAndSchemaMapper/backend_adapter_implementation_planning_skill_report.md`
- `00_skill_reports/ProtocolAndSchemaMapper/backend_adapter_implementation_planning_validation_checklist.md`
- `00_skill_reports/ProtocolAndSchemaMapper/backend_adapter_implementation_planning_blockers.md`
- `10_sprint_reports/sprint_report_history/20260512_105117_BackendAdapterImplementationPlanning.md`

## 5. Files Modified

- `00_skill_reports/ProtocolAndSchemaMapper/handoff.json`
- `project_manifest.json`
- `assumptions.md`
- `decisions_log.md`
- `10_sprint_reports/sprint_report_latest.md`

## 6. Files Deleted

None.

## 7. Actions Performed

- Converted the strict fixture checkpoint into a patch-ready backend adapter implementation plan.
- Selected `new-games-server/src/games/little-gangster/` plus a guarded 8001 branch in `new-games-server/src/index.ts`
  as the recommended future target.
- Defined backend-owned adapter input and schema-valid `/slot/v1` output contracts.
- Defined state persistence, reconnect, history, Lasthand/VABS planning requirements.
- Defined future adapter file list and future test file list without creating implementation files.
- Created Markdown-only `.diff.md` proposal docs marked `NOT APPLIED` and `PROPOSAL ONLY`.
- Created approval gate stating implementation remains blocked until explicit future approval.
- Updated manifest, assumptions, decisions, and ProtocolAndSchemaMapper handoff.

## 8. Validations Run

- `python3 -m json.tool project_manifest.json`: passed.
- `python3 -m json.tool 00_skill_reports/ProtocolAndSchemaMapper/handoff.json`: passed.
- `python3 06_resulting_code/planning/fixtures/validate_strict_schema_fixtures.py`: passed.
- Strict fixture validation output: 24 fixtures, 24 response-schema valid, 24 v0.3 result-schema valid.
- Required backend adapter planning files exist and are non-empty: passed.
- Required `06_resulting_code/planning` files exist and are non-empty: passed.
- Required `08_qa` files exist and are non-empty: passed.
- `09_release/backend_adapter_implementation_approval_gate.md` exists and is non-empty: passed.
- Patch proposal `.diff.md` files exist, are non-empty, and include `NOT APPLIED` / `PROPOSAL ONLY`: passed.
- No real `.diff` or `.patch` file exists in `03_protocol/patch_proposals`: passed.
- Staging hashes match the previously recorded source patch evidence: passed.
- `Gamesv1/games/8001` was not created: passed.
- `new-games-server/src/games/little-gangster/` was not created: passed.
- No `package.json`, `src`, `public`, `dist`, or `build` exists under `06_resulting_code`: passed.

## 9. Key Findings

- `new-games-server/src/index.ts` is the most direct future target because it owns the current `/slot/v1` endpoints
  and the `runtimeEnvelope(...)` helper.
- `Gamesv1/games/8001` does not exist in the targeted Staging inspection, so creating it remains a separate
  architecture/approval decision.
- 7001 `RuntimeOutcomeMapper` and `provisionalMathSource` are useful reference patterns only; they do not prove
  Little Gangster runtime ownership.
- The 24 strict fixtures are suitable as non-production expected-output examples for future adapter tests.
- Implementation remains blocked because no user approval was given for this sprint to modify Staging source or
  create backend adapter files.

## 10. Direct Answer: Where Adapter Should Live

Recommended future target:

`new-games-server/src/games/little-gangster/`

Recommended integration point:

`new-games-server/src/index.ts`

The future branch should be guarded for game id 8001 and must call the adapter only after an authoritative backend
result exists.

## 11. Direct Answer: What Adapter Input Is

The adapter input should be a backend-owned authoritative v0.3 result plus runtime context:

- v0.3 result object;
- session, round, operation, request counter, idempotency, and state version;
- backend RNG/result metadata;
- wallet/accounting result;
- round completion and max-win cap state;
- persistence, recovery, history, and Lasthand/VABS context;
- fixture/test metadata only in non-production tests.

## 12. Direct Answer: What Adapter Output Is

The adapter output should be a schema-valid `/slot/v1` runtime envelope with:

- wallet/accounting fields outside `gamePayload`;
- canonical `round`, `feature`, `restore`, `idempotency`, `retry`, and optional `history`;
- generic presentation fields for UI-kit compatibility;
- `presentationPayload.gamePayload.gameKey = "little-gangster"`;
- `presentationPayload.gamePayload.schemaVersion = "v0.3"`;
- `presentationPayload.gamePayload.payload` containing the v0.3 render payload.

## 13. Direct Answer: Whether Implementation Can Start

No. Backend adapter implementation remains blocked until the user explicitly approves Staging source modification and
the 8001 runtime owner/implementation target is accepted.

## 14. Decisions Made

- Use `new-games-server/src/games/little-gangster/` as the recommended future adapter module path.
- Treat `Gamesv1/games/8001` as a possible later browser/game package target, not the first backend adapter target.
- Split future adapter work into result types, presentation payload mapping, state persistence, history mapping,
  fixture bridge, adapter composition, and tests.
- Use the 24 strict fixtures as non-production expected-output contracts.
- Keep backend adapter implementation and GameClientBuilder implementation blocked.

## 15. Assumptions

- The patched local `presentationPayload.gamePayload` schema support remains the planning baseline.
- The strict fixtures remain non-production and are safe only for adapter test planning.
- The future backend adapter will be implemented in Staging only after a separate explicit approval.
- Wallet/accounting truth stays outside `gamePayload`.

## 16. Blockers

- Backend adapter implementation is not approved.
- 8001 runtime owner remains unproven.
- No `new-games-server` 8001 payload emission branch exists.
- No `Gamesv1/games/8001` package exists.
- Little Gangster result API contract remains unproven as production behavior.
- History/Lasthand/VABS storage format remains unproven for Little Gangster.
- Full TypeScript typecheck remains blocked by existing Staging repo config issues.
- Staging git baseline remains unusual/untracked from the resolved parent repo.
- GameClientBuilder implementation remains blocked.

## 17. Risks

- Implementing under `new-games-server` before resolving runtime ownership could create a temporary adapter that later
  needs to move.
- Fixture-based tests can prove shape compatibility but not real production RNG, payout, wallet, or history behavior.
- Staging source patch preservation remains important because prior source files appear untracked from the parent git
  root.
- Future 8001 branch must not trust browser-provided result data.

## 18. Anti-Hallucination Checks

- No backend adapter implementation was created.
- No Staging source was modified in this sprint.
- No `Gamesv1/games/8001` package was created.
- No GameClientBuilder implementation or production client code was generated.
- No registration artifact, DB/Cassandra action, wallet/API call, donor browsing, asset capture, public export, or
  release approval occurred.
- Source claims are tied to inspected files or explicit `NOT_FOUND` checks.
- Patch proposals are Markdown-only and marked `NOT APPLIED`.

## 19. Current Trust Level

High for the planning shape and file/test list.

Medium for implementation readiness because explicit approval, runtime owner decision, and source patch execution are
still required.

Low for release readiness because backend adapter implementation, client build, registration, wallet tests, asset
approval, and release audit remain blocked.

## 20. Next Recommended Step

Remain blocked unless the user explicitly approves a backend adapter apply sprint that modifies Staging source.

If approved, run ProtocolAndSchemaMapper backend adapter apply with tightly limited scope: create the planned
`new-games-server/src/games/little-gangster/` adapter files, add a guarded 8001 branch, add tests, record rollback,
and do not run GameClientBuilder implementation.

## 21. Exact Next Recommended Codex Prompt

```text
Use the reusable skill suite at:
[SKILL_SUITE_ROOT]

Use the existing project at:
[PROJECT_ROOT]

Run only this sprint:
1. ProtocolAndSchemaMapper backend adapter apply for Little Gangster v0.3
2. SprintReporter

This is explicit approval to modify Staging source only for the planned backend adapter patch.

Allowed future implementation scope:
- create new-games-server/src/games/little-gangster/resultTypes.ts
- create new-games-server/src/games/little-gangster/presentationPayload.ts
- create new-games-server/src/games/little-gangster/statePersistence.ts
- create new-games-server/src/games/little-gangster/historyMapper.ts
- create new-games-server/src/games/little-gangster/fixtures.ts
- create new-games-server/src/games/little-gangster/adapter.ts
- add guarded 8001 branch in new-games-server/src/index.ts
- add backend adapter tests under new-games-server/test/little-gangster/

Do not create Gamesv1/games/8001 unless explicitly approved.
Do not run GameClientBuilder implementation.
Do not generate production client code.
Do not run registration, DB/Cassandra, wallet/API, public export, donor browsing, asset capture, or release approval.
```

## 22. Questions For External Reviewer

- Should the next sprint approve a `new-games-server` backend adapter patch, or should runtime ownership be decided
  outside Codex first?
