# External Reviewer Copy-Paste Report

## Sprint identity

- Repository/project: `[PROJECT_ROOT]`
- Sprint goal: Focused Stage 4 retry/extension to audit third-party/new-game GS integration, runtime lane, Crazy Rooster template validity, math/RNG ownership, registration blockers, and release readiness.
- Date/time: 2026-05-08T15:39:47+01:00
- Skill(s) involved: ProtocolAndSchemaMapper, SprintReporter
- Current status: Protocol mapping extended. New-games `slot-browser-v1` / HTTP runtime is recommended as the planning lane, but release-ready runtime ownership remains partial/blocked.

## User instruction received

The user instructed Codex to use `[SKILL_SUITE_ROOT]` and `[PROJECT_ROOT]`, running only ProtocolAndSchemaMapper and SprintReporter. The sprint had to double-check documentation and explicit source paths for third-party/new game development
and how a new game links to the Game Server. The user explicitly forbade MathModelDesigner, art skills, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, RTPAndReleaseAuditor, AuthorizedReferenceResearcher,
ReferenceAssetInventory, donor browsing, asset capture, client build, math generation, Cassandra/DB actions, wallet calls, raw secrets, and full donor URL/token persistence.

## Source documents inspected

- path/name: `[SKILL_SUITE_ROOT]/AGENTS.md`
  - readable: yes
  - used for: suite safety rules
  - important findings: no broad search, no guessed protocol/schema, no raw secrets, no DB apply, blockers instead of hallucination
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
  - readable: yes
  - used for: skill order and boundaries
  - important findings: ProtocolAndSchemaMapper maps launch/runtime/wallet/Cassandra only; it must not investigate donor gameplay or execute Cassandra
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/.agents/skills/ProtocolAndSchemaMapper/SKILL.md`
  - readable: yes
  - used for: mapper workflow and forbidden actions
  - important findings: unknown source/schema areas must be blockers
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md`
  - readable: yes
  - used for: report format
  - important findings: report must list exact files changed, validations, blockers, risks, and next prompt
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/AGENTS.md`
  - readable: yes
  - used for: project-local safety rules
  - important findings: no broad search, no raw secrets, no full tokenized donor URL, no DB apply, reports/handoffs after every skill
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/project_manifest.json`
  - readable: yes
  - used for: project state and explicit paths
  - important findings: prior stages completed through ReferenceAssetInventory; current protocol status was partial; next skill was MathModelDesigner
  - unreadable/blocker notes: none

- path/name: existing protocol outputs under `[PROJECT_ROOT]/03_protocol/`
  - readable: yes
  - used for: previous Stage 4 mapping baseline
  - important findings: BSG CW already separated from browser runtime; client/runtime and registration remained partial
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/cwv3/CWStartGameAction.java`
  - readable: yes
  - used for: CW launch flow
  - important findings: reads game/mode/lang, decides new-games route, authenticates through Common Wallet, creates/resolves session, and redirects to new-games when enabled
  - unreadable/blocker notes: no raw token values persisted

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/BaseStartGameAction.java`
  - readable: yes
  - used for: new-games redirect and legacy template redirect
  - important findings: new-games redirect passes `bankId`, `sessionId`, `gameId`, `gameIdNumeric`, `lang`, `mode`, `gameServerId`, `ngsApiUrl`, `gsInternalBaseUrl`, `ngsContract`; legacy redirect goes to `/<mode>/mp/template.jsp` with
  websocket params
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/game-server/web-gs/src/main/webapp/real/mp/template.jsp`
  - readable: yes
  - used for: legacy JSP lane
  - important findings: reads bank/session/game params, loads `version.json`, `validator.js`, then `game.js`, and exposes `getParams()`
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/web/api/newgames/NewGamesInternalApiServlet.java`
  - readable: yes
  - used for: WebGS internal new-games bridge
  - important findings: exposes session validation, wallet reserve, wallet settle, history write, and history read; maps wallet reserve/settle to Common Wallet client calls
  - unreadable/blocker notes: proves wallet/session/history bridge, not final slot RNG/result owner

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/webapp/WEB-INF/web.xml`
  - readable: yes
  - used for: servlet mapping
  - important findings: maps `NewGamesInternalApiServlet` to `/gs-internal/newgames/v1/*`
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001`
  - readable: yes
  - used for: Crazy Rooster runtime/reference evidence
  - important findings: 7001 uses Vite/Pixi v8, `@gamesv1/core-protocol`, `GS_HTTP_RUNTIME`, `slot-browser-v1`, and math package files; final proof docs still mark 7001 proof pending
  - unreadable/blocker notes: asset bodies were not inspected or moved

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/premium-slot`
  - readable: yes
  - used for: base template/architecture reference
  - important findings: same new-games dependency pattern as 7001, including `@gamesv1/core-protocol`, `@gamesv1/pixi-engine`, `@gamesv1/ui-kit`, Pixi v8, Vite
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/new-games-client`
  - readable: yes
  - used for: portal/general preloader client
  - important findings: routes 7001 away from generic control plane to game-specific client; also contains older Plinko/general flow that should not be Crazy Rooster truth
  - unreadable/blocker notes: none

- path/name: `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/runtime/export_localmachine/com.abs.casino.common.cache.BankInfoCache.xml`
  - readable: yes
  - used for: bank 6275 route and coin config
  - important findings: bank 6275 exists; coin values are `1,2,3,4,5,10,15,20,25,50,100`; new-games route config currently includes 7000 and 7001
  - unreadable/blocker notes: secret-bearing values were not persisted

- path/name: `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/docker-compose.yml`
  - readable: yes
  - used for: Cassandra keyspace evidence
  - important findings: compose creates/updates `RCasinoKS` and `RCasinoSCKS`
  - unreadable/blocker notes: no DB/Cassandra command executed

- path/name: `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/common/src/main/java/com/abs/casino/common/cache/data/bank/BankInfo.java`
  - readable: yes
  - used for: PASS_KEY property names only
  - important findings: property constants exist for `INTEGRATION_PASS_KEY`, `CT_PASS_KEY`, and `BONUS_PASS_KEY`
  - unreadable/blocker notes: raw values were not printed or persisted

## Files created

- `[PROJECT_ROOT]/03_protocol/third_party_game_gs_integration_audit.md`
- `[PROJECT_ROOT]/03_protocol/runtime_lane_decision_matrix.md`
- `[PROJECT_ROOT]/03_protocol/math_rng_ownership_report.md`
- `[PROJECT_ROOT]/03_protocol/registration_evidence_map.md`
- `[PROJECT_ROOT]/03_protocol/crazy_rooster_template_validity.md`
- `[PROJECT_ROOT]/03_protocol/player_release_integration_blockers.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/third_party_gs_integration_skill_report.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/third_party_gs_integration_validation_checklist.md`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/third_party_gs_integration_blockers.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_history/20260508_153947_ThirdPartyGSIntegrationAudit.md`

## Files modified

- `[PROJECT_ROOT]/03_protocol/protocol_contract_summary.json`
- `[PROJECT_ROOT]/00_skill_reports/ProtocolAndSchemaMapper/handoff.json`
- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_latest.md`

## Files deleted

none

## Actions performed

- Read the required suite, skill, project, manifest, existing Stage 4 protocol, and handoff files.
- Verified existing project state and prior blockers.
- Performed targeted inspection inside explicit source roots only.
- Mapped third-party/new-game launch flow from GS launch to `cwstartgamev2.do`, then to new-games client or legacy template depending on route config.
- Mapped new-games client redirect parameters and legacy template parameters.
- Identified which params are visual/runtime config vs wallet/session-only values.
- Inspected WebGS `NewGamesInternalApiServlet` and mapped internal session/wallet/history bridge responsibilities.
- Confirmed the WebGS bridge does not prove slot RNG/result generation.
- Compared runtime lanes and recommended new-games `slot-browser-v1` / HTTP runtime as the Little Gangster planning lane, with release blockers.
- Reviewed Crazy Rooster 7001 template validity and marked it useful as reference but not a direct release-ready template.
- Answered where math should live: project math package first, later backend/new-games runtime code/config, not assumed Cassandra executable import.
- Extended registration evidence and kept registration generate-only.
- Updated protocol summary, project manifest, assumptions, decisions, and ProtocolAndSchemaMapper handoff.
- Ran validations and wrote SprintReporter latest/history reports.

## Validations run

- command/check: `project_manifest.json` JSON parse
  - result: pass
  - evidence: targeted Python JSON parse succeeded
  - not run reason if skipped: not skipped

- command/check: `03_protocol/protocol_contract_summary.json` JSON parse
  - result: pass
  - evidence: targeted Python JSON parse succeeded
  - not run reason if skipped: not skipped

- command/check: `00_skill_reports/ProtocolAndSchemaMapper/handoff.json` JSON parse
  - result: pass
  - evidence: targeted Python JSON parse succeeded
  - not run reason if skipped: not skipped

- command/check: required audit files exist and are non-empty
  - result: pass
  - evidence: all six required `03_protocol/*` audit files exist and are non-empty
  - not run reason if skipped: not skipped

- command/check: redaction scan for known raw donor token, prior runbook token example, known raw PASS_KEY value, and tokenized donor URL
  - result: pass
  - evidence: scan of new/updated outputs returned no raw values; redacted donor URLs from prior safe outputs remain redacted
  - not run reason if skipped: not skipped

- command/check: no new asset capture
  - result: pass
  - evidence: no files under `02_reference_assets` had modification time after the sprint start
  - not run reason if skipped: not skipped

- command/check: no later skill report dirs
  - result: pass
  - evidence: no `MathModelDesigner`, `ArtSceneMapper`, or `GameClientBuilder` report dirs were created
  - not run reason if skipped: not skipped

- command/check: explicit required question coverage
  - result: pass
  - evidence: audit files explicitly answer math import/location, GS RNG/result generation, launch URL, and release decision table questions
  - not run reason if skipped: not skipped

- command/check: schema validation against `project_manifest.schema.json`
  - result: skipped
  - evidence: local Python environment lacks `jsonschema`
  - not run reason if skipped: `No module named 'jsonschema'`

- command/check: live launch/runtime validation
  - result: skipped
  - evidence: user explicitly forbade browser work, wallet calls, build, and DB actions
  - not run reason if skipped: forbidden by sprint scope

## Key findings

- A new/third-party game should launch through GS first, using the `/startgame` wrapper or `/cwstartgamev2.do`, not by directly opening a static client URL.
- `cwstartgamev2.do` authenticates through Common Wallet, creates/resolves a GS session, and redirects to new-games client when route config is enabled.
- If new-games route is not enabled, the legacy path can redirect to `/<mode>/mp/template.jsp` with `WEB_SOCKET_URL`.
- New-games client receives `bankId`, `sessionId`, `gameId`, `gameIdNumeric`, `lang`, `mode`, `gameServerId`, `ngsApiUrl`, `gsInternalBaseUrl`, and `ngsContract`.
- `token` and PASS_KEY values are wallet/session/server concerns and must not become visual client logic.
- Little Gangster should plan around the new-games `slot-browser-v1` / HTTP runtime lane, with blockers.
- WebGS has an internal new-games bridge for session validation, wallet reserve, wallet settle, history write, and history read.
- The WebGS internal bridge proves wallet/session/history integration, not authoritative slot RNG/result generation.
- The browser-facing `/slot/v1/*` outcome lane is attributed by docs to `new-games-api`/`new-games-server`, but that source root was not an allowed inspection path.
- Crazy Rooster 7001 is useful as a reference, but not a direct release-ready template for Little Gangster.
- Math should be treated as backend/runtime logic/config until proven otherwise; Cassandra registration should not be assumed to import executable math.

## Decisions made

- Decision: recommend the new-games `slot-browser-v1` / HTTP runtime lane for Little Gangster planning.
  - Source: explicit 7001/premium-slot source evidence and GS route code

- Decision: keep protocol mapping partial, not approved.
  - Source: `new-games-server`, `@gamesv1/core-protocol`, 8001 registration, and `scn` serialization blockers

- Decision: keep MathModelDesigner as the next recommended skill, but only with limitations.
  - Source: workflow order plus enough math inputs, while final runtime ownership remains blocked

- Decision: mark GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, and release-to-players as blocked now.
  - Source: missing math package, approved art, runtime source proof, 8001 registration, secret fixture strategy, and release audit

- Decision: treat Crazy Rooster 7001 as integration reference only.
  - Source: 7001 final status/proof gaps and game-specific math/art identity

## Assumptions

- Little Gangster will be a server/backend-authoritative real-money slot; browser RNG is not acceptable for release outcomes.
- The `new-games-server` source will be provided or authorized later for targeted inspection.
- `@gamesv1/core-protocol` will be provided or authorized later for targeted inspection.
- MathModelDesigner can design and simulate math without final runtime owner proof, as long as it records the limitation.
- GameServerRegistrar will remain generate-only and will require rollback.
- Captured scaffold/reference assets remain blocked from release.

## Blockers

- `new_games_server_source_path_missing`: provide explicit path to `new-games-server` or authorize targeted inspection.
- `core_protocol_package_not_inspected`: provide explicit path to `@gamesv1/core-protocol` or authorize targeted inspection.
- `slot_v1_result_owner_unknown`: authoritative RNG/result owner for 8001 is not proven.
- `game_8001_registration_missing`: no 8001 route/config/game records exist.
- `scn_serializer_missing`: no safe serializer/config-generation tool verified for binary `scn`.
- `math_package_missing`: Little Gangster math package does not exist yet.
- `approved_release_assets_missing`: captured scaffold assets are not release-approved.
- `wallet_launch_tests_missing`: no 8001 wallet/launch tests exist.
- `rtp_validation_missing`: no Little Gangster RTP simulation/audit exists.

## Risks

- High: Building against the wrong runtime lane would waste implementation effort.
- High: If `new-games-server` owns result generation differently than inferred, MathModelDesigner/GameClientBuilder integration will need adjustment.
- High: Registration cannot be safely generated without `scn` serializer/config pipeline.
- Medium: Crazy Rooster 7001 has useful integration evidence but final 7001 proof docs still show proof gaps.
- Medium: Wallet/idempotency behavior needs later fixture/local-safe validation.
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

Why: The launch route, new-games redirect parameters, legacy template fallback, WebGS internal new-games bridge, and 7001/premium-slot client lane are backed by source evidence. The final player-release-ready runtime remains partial because
`new-games-server`, `@gamesv1/core-protocol`, 8001 registration, and `scn` serialization were not fully available under the allowed roots.

## Next recommended step

Run MathModelDesigner and SprintReporter only, with limitations.

## Exact next recommended Codex prompt

```text
Use the reusable skill suite at:
[SKILL_SUITE_ROOT]

Use the existing project at:
[PROJECT_ROOT]

Run only these skills for this sprint:
1. MathModelDesigner
2. SprintReporter

Do not run ArtSceneMapper, ArtDirectionAndReplacementPlanner, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, RTPAndReleaseAuditor, AuthorizedReferenceResearcher, ReferenceAssetInventory, or ProtocolAndSchemaMapper.

Use the target RTPs 96.0, 94.0, and 92.0; volatility target high; min/default/max bet 0.20/1.00/100.00; and coin denominations from project_manifest.json. Read 03_protocol outputs first, especially the third-party GS integration audit and
math/RNG ownership report. Design and simulate internal math only. Treat the browser client as non-authoritative for real-money RNG/results. Do not claim final runtime ownership, do not build client code, do not investigate donor gameplay,
do not capture assets, do not generate or execute Cassandra, and do not assume math is imported into GS registration unless source proves it. Produce math blockers where required, then run SprintReporter.
```

## Questions for external reviewer

- Did the audit correctly distinguish GS launch, new-games browser runtime, WebGS internal bridge, and BSG Common Wallet?
- Is the recommendation to plan for `slot-browser-v1` reasonable despite missing `new-games-server` source?
- Did the audit avoid treating Crazy Rooster 7001 as a copyable release template?
- Did the math/RNG report answer where the math package should live and whether GS RNG is proven?
- Are any raw secrets, raw token values, or full tokenized donor URLs present in the generated outputs?
