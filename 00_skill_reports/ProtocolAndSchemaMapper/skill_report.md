# ProtocolAndSchemaMapper Skill Report

Date/time: 2026-05-08T07:44:03+0100

## Status

`partial_sufficient_for_math_handoff`

Protocol mapping succeeded for BSG Common Wallet, wallet hash rules, launch/template separation, and enough client/runtime/config boundary mapping to start MathModelDesigner. It remains partial for the new-games core protocol package,
server-side `/slot/v1/*` implementation, and future 8001 registration details.

## Inputs Read

- `[SKILL_SUITE_ROOT]/AGENTS.md`
- `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/ProtocolAndSchemaMapper/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md`
- Suite reference summaries under `[SKILL_SUITE_ROOT]/references`
- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- Prior handoffs for ProjectCreator, AuthorizedReferenceResearcher, and ReferenceAssetInventory
- Sanitized reference research/network summaries and asset inventory CSVs as context only
- Explicit source paths from the prompt/project manifest

## Outputs Created

- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/preflight.md`
- `[PROJECT_ROOT]/03_protocol/protocol_layer_model.md`
- `[PROJECT_ROOT]/03_protocol/bsg_common_wallet_contract.md`
- `[PROJECT_ROOT]/03_protocol/wallet_hash_rules.md`
- `[PROJECT_ROOT]/03_protocol/launch_template_contract.md`
- `[PROJECT_ROOT]/03_protocol/client_runtime_protocol_notes.md`
- `[PROJECT_ROOT]/03_protocol/cassandra_registration_contract.md`
- `[PROJECT_ROOT]/03_protocol/game_server_runtime_contract.md`
- `[PROJECT_ROOT]/03_protocol/protocol_blockers.md`
- `[PROJECT_ROOT]/03_protocol/protocol_contract_summary.json`
- `[PROJECT_ROOT]/03_protocol/message_schemas/wallet_authenticate.schema.json`
- `[PROJECT_ROOT]/03_protocol/message_schemas/wallet_bet_result.schema.json`
- `[PROJECT_ROOT]/03_protocol/message_schemas/wallet_refund_bet.schema.json`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/skill_report.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/blockers.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/validation_checklist.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/handoff.json`

## Files Modified

- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/assumptions.md`

## Key Findings

- BSG Common Wallet is XML wallet/casino protocol, not browser runtime protocol.
- BSG CW response roots remain `BSGSYSTEM`/`EXTSYSTEM`; JSON is not assumed for BSG CW.
- Launch/template routing is separate from browser runtime. `cwstartgamev2.do` authenticates and routes; it is not a Pixi bootloader.
- Legacy JSP shell reads `bankId`, `SID`, `gameId`, loads `version.json`, `validator.js`, `game.js`, and exposes `getParams()`/path helpers.
- New-games redirect passes `bankId`, `sessionId`, `gameId`, `gameIdNumeric`, `lang`, `mode`, `gameServerId`, `ngsApiUrl`, `gsInternalBaseUrl`, and `ngsContract=v1`.
- 7001 runtime uses `slot-browser-v1`, `GS_HTTP_RUNTIME`, request counters, idempotency keys, and `/slot/v1/*` operations.
- Bank 6275 and coin values were verified from explicit config export; URLs/secrets are redacted.
- Cassandra/config registration remains generate-only and partial. No CQL was generated or executed.

## Safety Results

- Raw secret values stored: no.
- Full donor URL stored: no.
- DB/Cassandra action executed: no.
- Donor gameplay investigated this sprint: no.
- Asset capture performed this sprint: no.
- Later workflow skills run: no.

## Next Recommended Skill

MathModelDesigner.

Reason: protocol boundaries, target RTPs, volatility, bet range, and coin denominations are mapped enough to begin math design. Remaining runtime/registration blockers are explicit and do not block math modeling.
