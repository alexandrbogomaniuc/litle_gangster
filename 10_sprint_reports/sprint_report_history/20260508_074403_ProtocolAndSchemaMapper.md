# External Reviewer Copy-Paste Report

## Sprint identity

- Repository/project: `[PROJECT_ROOT]`
- Sprint goal: Run ProtocolAndSchemaMapper and SprintReporter only for workflow test stage 4.
- Date/time: 2026-05-08T07:44:03+0100
- Skill(s) involved: ProtocolAndSchemaMapper, SprintReporter
- Current status: Protocol mapping completed as `partial_sufficient_for_math_handoff`; MathModelDesigner recommended next.

## User instruction received

The user instructed Codex to use the reusable skill suite at `[SKILL_SUITE_ROOT]` and the existing project at `[PROJECT_ROOT]`, running only ProtocolAndSchemaMapper and SprintReporter. The sprint had to map protocol layers, BSG Common
Wallet, launch/template, browser/client runtime clues, Game Server runtime clues, Cassandra/config registration, wallet hash rules, blockers, and handoff to MathModelDesigner. The user explicitly forbade browser launch, donor investigation,
asset capture, donor downloads, wallet calls, Cassandra/DB actions, raw secrets, full donor URLs, release approval, and later workflow skills.

## Source documents inspected

- path/name: `[SKILL_SUITE_ROOT]/AGENTS.md`
  - readable: yes
  - used for: suite safety rules
  - important findings: no broad search, no guessed protocol/schema, no raw secrets, no DB apply, blockers instead of hallucination
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
  - readable: yes
  - used for: skill order and boundaries
  - important findings: ProtocolAndSchemaMapper maps launch/runtime/wallet/Cassandra; it must not investigate donor gameplay or execute Cassandra
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/.agents/skills/ProtocolAndSchemaMapper/SKILL.md`
  - readable: yes
  - used for: required workflow and forbidden actions
  - important findings: required to separate layers and mark unknowns as blockers
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md`
  - readable: yes
  - used for: report format
  - important findings: report must include files changed, validations, blockers, assumptions, risks, and next prompt
  - unreadable/blocker notes: none

- path/name: suite references under `[SKILL_SUITE_ROOT]/references`
  - readable: yes
  - used for: uploaded BSG CW summary, verified facts, protocol layer model, client architecture summary, Cassandra summary, security rules
  - important findings: BSG CW is XML wallet/casino protocol with `BSGSYSTEM`/`EXTSYSTEM`; BSG hash orders are documented; `RCasinoSCKS` evidence is required for config registration; legacy client docs use Webpack/Vue/PIXI
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/project_manifest.json`
  - readable: yes
  - used for: project state, roots, bank, coin denominations, secret references, next skill
  - important findings: prior stages complete through ReferenceAssetInventory; asset inventory has 29 scaffold assets blocked from release
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/assumptions.md`
  - readable: yes
  - used for: existing blockers and assumptions
  - important findings: raw PASS_KEY/test tokens intentionally unavailable; asset release blockers remain
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/decisions_log.md`
  - readable: yes
  - used for: prior decisions and sprint history
  - important findings: ProjectCreator, AuthorizedReferenceResearcher, and ReferenceAssetInventory completed; next skill was ProtocolAndSchemaMapper
  - unreadable/blocker notes: none

- path/name: prior handoffs under `[PROJECT_ROOT]/00_skill_reports/{ProjectCreator,AuthorizedReferenceResearcher,ReferenceAssetInventory}/handoff.json`
  - readable: yes
  - used for: workflow state and prior outputs
  - important findings: Chrome MCP donor observation succeeded partially; ReferenceAssetInventory captured 29 scaffold assets and blocked them from release
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/01_reference_research/scenario_coverage.md`
  - readable: yes
  - used for: context only
  - important findings: intro/base/menu/info and one safe demo spin observed; deep gameplay remains incomplete
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/01_reference_research/network_observations.md`
  - readable: yes
  - used for: sanitized runtime metadata context only
  - important findings: demo RGS `authenticate`, `gameLaunch`, `keepAlive`, and `bet` metadata were observed earlier; no response bodies saved
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/02_reference_assets/final_inventory.csv` and `[PROJECT_ROOT]/02_reference_assets/asset_ownership_register.csv`
  - readable: yes
  - used for: inventory count/status only
  - important findings: all 29 captured reference assets are `scaffold_internal_only`, `blocked_from_release`, and replacement required
  - unreadable/blocker notes: asset bodies were not inspected

- path/name: `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/game-server/web-gs/src/main/webapp/real/mp/template.jsp`
  - readable: yes
  - used for: legacy launch/template contract
  - important findings: reads `bankId`, `SID`, `gameId`; loads `version.json`, `validator.js`, `game.js`; exposes `getParams()`, `getLobbyPath()`, and `getGamePath()`
  - unreadable/blocker notes: no `window.gameConfig` literal verified in this live template path

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/cwv3/CWStartGameAction.java`
  - readable: yes
  - used for: `cwstartgamev2.do` launch routing
  - important findings: parses launch fields, calls Common Wallet auth, routes new-games, invokes routing bridges
  - unreadable/blocker notes: token values were not persisted

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/BaseStartGameAction.java`
  - readable: yes
  - used for: new-games and legacy template redirect params
  - important findings: new-games redirect adds `bankId`, `sessionId`, `gameId`, `gameIdNumeric`, `lang`, `mode`, `gameServerId`, `ngsApiUrl`, `gsInternalBaseUrl`, `ngsContract`
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001`
  - readable: yes
  - used for: 7001 runtime reference
  - important findings: actual 7001 runtime uses Vite/PIXI v8-style new-games lane, `slot-browser-v1`, `GS_HTTP_RUNTIME`, request counters, idempotency keys, and `/slot/v1/*` operations
  - unreadable/blocker notes: imported `@gamesv1/core-protocol` package root was not inspected because it was not an explicit allowed path

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/premium-slot`
  - readable: yes
  - used for: base slot runtime/template reference
  - important findings: premium-slot mirrors the new-games Vite/PIXI v8 lane and documents runtime flow through `GsRuntimeClient.bootstrap()`
  - unreadable/blocker notes: core protocol package still not inspected

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/new-games-client`
  - readable: yes
  - used for: portal/preloader/new-games routing clues
  - important findings: routes 7001 params onward and uses Vite + TypeScript + Pixi
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/runtime/export_localmachine/com.abs.casino.common.cache.BankInfoCache.xml`
  - readable: yes
  - used for: bank 6275, coin values, new-games route properties, Common Wallet config structure
  - important findings: bank 6275 exists; coin values are `1,2,3,4,5,10,15,20,25,50,100`; new-games route properties include 7000 and 7001; URLs/secrets redacted
  - unreadable/blocker notes: secret-bearing values were not persisted

- path/name: `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/docker-compose.yml`
  - readable: yes
  - used for: local Cassandra keyspace evidence
  - important findings: compose creates/updates `RCasinoKS` and `RCasinoSCKS`
  - unreadable/blocker notes: no DB command executed

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/GS_7001_NEWGAMES_RUNBOOK.md`
  - readable: yes
  - used for: canonical 7001 new-games proof flow
  - important findings: `new-games-api` handles `/slot/v1/*`; `new-games-client` hosts browser; canonical flow includes bootstrap/open/play/resume/feature/history/close; launch example was redacted
  - unreadable/blocker notes: raw token example not persisted

- path/name: `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/common/src/main/java/com/abs/casino/common/cache/data/bank/BankInfo.java`
  - readable: yes
  - used for: PASS_KEY property names only
  - important findings: property constants include `INTEGRATION_PASS_KEY`, `CT_PASS_KEY`, and `BONUS_PASS_KEY`
  - unreadable/blocker notes: raw values not read or stored

- path/name: `[DEV_ROOT]/runtime-patches/commonwallet/commonWallet.jsp` and `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/deploy/scripts/phase4-protocol-wallet-canary-probe.sh`
  - readable: yes
  - used for: secret-reference existence only
  - important findings: contain token/probe logic references
  - unreadable/blocker notes: literal token values not persisted

## Files created

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
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_history/20260508_074403_ProtocolAndSchemaMapper.md`

## Files modified

- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_latest.md`

## Files deleted

none

## Actions performed

- Read the requested suite rules, skill index, skill instructions, project manifest, assumptions, decisions, prior handoffs, reference research summaries, and asset inventory summaries.
- Verified explicit source paths by existence/readability/type without searching broad folders.
- Performed targeted source inspection only inside explicit paths.
- Created ProtocolAndSchemaMapper preflight report.
- Created protocol layer model separating launch/template, browser runtime, Game Server runtime, BSG Common Wallet, Cassandra/config, math/result, and wallet/External Casino layers.
- Created BSG Common Wallet contract with Authenticate, Bet/Result, Refund Bet, response format, hash orders, idempotency/refund implications, optional fields, and blockers.
- Created wallet hash rules with fake fixture values only.
- Created launch/template contract for BSG launch routes, legacy JSP shell, new-games redirect, and canonical 7001 runbook clues.
- Created client runtime notes documenting the legacy docs vs new-games source stack split and the partial `slot-browser-v1` runtime contract.
- Created Cassandra/config registration contract with generate-only safety and 6275/507/coin/new-games config evidence.
- Created Game Server runtime contract with launch classes, routing bridges, wallet clues, and runtime blockers.
- Created protocol blockers list and machine-readable protocol summary.
- Created three JSON schema helper files for wallet request fixture shapes.
- Updated manifest status/current skill/next skill and added a protocol summary section.
- Updated decisions and assumptions with sprint decisions, architecture split, and remaining blockers.
- Created ProtocolAndSchemaMapper skill report, blockers, validation checklist, and handoff.
- Ran validation and fixed one source-derived token placeholder query example before final validation.
- Ran SprintReporter and wrote latest plus history report.

## Validations run

- command/check: `project_manifest.json` JSON parse
  - result: pass
  - evidence: parsed by targeted Python validation
  - not run reason if skipped: not skipped

- command/check: `03_protocol/protocol_contract_summary.json` JSON parse
  - result: pass
  - evidence: parsed by targeted Python validation
  - not run reason if skipped: not skipped

- command/check: `00_skill_reports/ProtocolAndSchemaMapper/handoff.json` JSON parse
  - result: pass
  - evidence: parsed by targeted Python validation
  - not run reason if skipped: not skipped

- command/check: message schema JSON parse
  - result: pass
  - evidence: `wallet_authenticate`, `wallet_bet_result`, and `wallet_refund_bet` schemas parsed
  - not run reason if skipped: not skipped

- command/check: required `03_protocol` Markdown outputs exist
  - result: pass
  - evidence: 8 required Markdown files exist and are non-empty
  - not run reason if skipped: not skipped

- command/check: redaction scan for raw donor token, runbook token example, known raw pass value, full tokenized donor URL, and token/session/auth/key/jwt/signature/hash query values
  - result: pass after one rewrite
  - evidence: final scan clear; first pass found one placeholder query example and it was rewritten
  - not run reason if skipped: not skipped

- command/check: protocol-layer separation checks
  - result: pass
  - evidence: BSG CW wallet/casino-only language, browser runtime separation, launch/template separation, Cassandra/wallet separation, XML/EXTSYSTEM preservation all present
  - not run reason if skipped: not skipped

- command/check: generate-only/no CQL/DB action check
  - result: pass
  - evidence: outputs state generate-only and no CQL generated/executed; no DB command was run
  - not run reason if skipped: not skipped

- command/check: no donor gameplay, no asset capture, no later skills
  - result: pass
  - evidence: sprint boundary recorded; later skill report dirs absent for MathModelDesigner through RTPAndReleaseAuditor
  - not run reason if skipped: not skipped

- command/check: suite JSON schema validation for manifest
  - result: skipped
  - evidence: local Python environment lacks `jsonschema`
  - not run reason if skipped: `No module named 'jsonschema'`

- command/check: SprintReporter output validation
  - result: pass
  - evidence: 26/26 checks passed; required sections present, latest/history files exist, history equals latest, redaction scan clear
  - not run reason if skipped: not skipped

## Key findings

- BSG Common Wallet is XML wallet/casino protocol, not browser runtime protocol.
- `BSGSYSTEM`/`EXTSYSTEM` response roots were preserved; JSON was not assumed for BSG CW.
- `cwstartgamev2.do` is launch/GS routing. It authenticates and redirects; it is not generic frontend bootloader logic.
- Legacy JSP template reads bank/session/game params, loads `version.json`, `validator.js`, and `game.js`, and exposes `getParams()`/path helpers.
- New-games routing passes `bankId`, `sessionId`, `gameId`, `gameIdNumeric`, `lang`, `mode`, `gameServerId`, `ngsApiUrl`, `gsInternalBaseUrl`, and `ngsContract=v1`.
- 7001 source proves a new-games slot runtime lane using `slot-browser-v1`, `GS_HTTP_RUNTIME`, request counters, current state version, idempotency keys, and client operation IDs.
- Uploaded docs describe a legacy Webpack/Vue/PIXI lane, while explicit 7001/premium-slot sources show a newer Vite/PIXI v8 lane. This is a real architecture split for GameClientBuilder to decide, not a contradiction to guess away.
- Bank 6275, subCasinoId 507, and coin values are verified from explicit path/user inputs.
- Cassandra/config registration remains partial and generate-only. No registration CQL was created.

## Decisions made

- Decision: mark protocol mapping as `partial_sufficient_for_math_handoff`.
  - Source: validation result plus explicit blockers

- Decision: recommend MathModelDesigner next.
  - Source: workflow order and sufficient math inputs: RTPs, volatility, bet range, coin values, and separated protocol layers

- Decision: keep `approval_gates.protocol_mapping_approved` false.
  - Source: user review still required; mapping is partial, not final release approval

- Decision: record legacy docs vs new-games source stack split.
  - Source: uploaded client architecture summary and explicit 7001/premium-slot package evidence

- Decision: keep all asset release blockers.
  - Source: ReferenceAssetInventory handoff and asset ownership register

## Assumptions

- MathModelDesigner can begin with protocol boundaries plus RTP/bet inputs even though core protocol/server implementation remains partial.
- The final 8001 client stack will be decided later by GameClientBuilder using explicit source paths and user approval.
- Raw PASS_KEY and test token values remain intentionally unavailable and are not required for math design.
- Registration generation waits until math/client/build outputs exist.

## Blockers

- `core_protocol_package_not_inspected`: `@gamesv1/core-protocol` package root was not explicit; provide path or allow targeted inspection.
- `slot_v1_server_implementation_partial`: `/slot/v1/*` server implementation not fully mapped; provide explicit new-games server/API source path.
- `game_8001_registration_missing`: no 8001 registration artifacts exist yet.
- `scn_serializer_missing`: `RCasinoSCKS.scn` serialized config cannot be safely generated without a real serializer/tool.
- `math_result_ownership_unknown`: RNG/result ownership for 8001 remains unknown until MathModelDesigner/runtime integration.
- `pass_key_value_intentionally_unavailable`: raw PASS_KEY intentionally not stored; future tests need local ignored secret reference or fake fixture.
- `test_token_values_intentionally_unavailable`: raw test tokens intentionally not stored.
- `scaffold_assets_block_release`: all captured scaffold assets remain blocked from release.

## Risks

- High: If the new-games core protocol package differs from the inferred runtime notes, GameClientBuilder and WalletAndLaunchTester may need to adjust message details.
- High: Registration cannot be generated safely until `scn` serialization/config-generation tooling is available.
- Medium: Legacy docs and new-games source stack differ; choosing the wrong client lane could waste build time.
- Medium: Wallet retry/idempotency behavior needs fixture/live-safe tests later.
- Medium: Asset ownership remains a release blocker.

## Anti-hallucination checks

- Did the agent search outside allowed paths? no
- Did the agent guess missing facts? no, unknowns were recorded as blockers
- Did the agent claim 100% coverage? no
- Did the agent ask for raw secrets? no
- Did the agent execute DB changes? no
- Did the agent approve unknown assets? no
- Did the agent separate BSG CW from browser runtime? yes
- Did the agent create handoff files? yes

## Current trust level

partially trustworthy

Why: The mapping is evidence-backed for BSG CW, launch/template, wallet hash orders, 7001 new-games client clues, and Cassandra/config boundaries. It is still partial because the imported core protocol package, server-side `/slot/v1/*`
implementation, future 8001 registration, and `scn` serialization tooling were not fully available under the allowed paths.

## Next recommended step

Run MathModelDesigner and SprintReporter only.

Exact next Codex prompt:

```text
Use the reusable skill suite at:
[SKILL_SUITE_ROOT]

Use the existing project at:
[PROJECT_ROOT]

Run only these skills for this sprint:
1. MathModelDesigner
2. SprintReporter

Do not run ArtSceneMapper, ArtDirectionAndReplacementPlanner, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, RTPAndReleaseAuditor, AuthorizedReferenceResearcher, ReferenceAssetInventory, or ProtocolAndSchemaMapper.

Use the target RTPs 96.0, 94.0, and 92.0; volatility target high; min/default/max bet 0.20/1.00/100.00; and coin denominations from project_manifest.json. Read 03_protocol outputs first. Design internal math only; do not generate client
code, do not investigate donor gameplay, do not capture assets, do not generate or execute Cassandra, and do not assume final RNG/result ownership without evidence. Produce math blockers where required, then run SprintReporter.
```

## Questions for external reviewer

- Did the report correctly keep BSG Common Wallet separate from browser runtime?
- Did the mapper overstate the new-games runtime contract without inspecting `@gamesv1/core-protocol`?
- Are the wallet hash orders and XML/EXTSYSTEM assumptions aligned with the uploaded BSG CW docs?
- Is MathModelDesigner the correct next skill despite the remaining runtime/server blockers?
- Are any secret-bearing values or full donor URLs present in the generated protocol files?
