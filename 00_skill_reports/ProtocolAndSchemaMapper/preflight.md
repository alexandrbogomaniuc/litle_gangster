# ProtocolAndSchemaMapper Preflight

Date/time: 2026-05-08T07:44:03+0100

## Scope

Allowed skills for this sprint:

- ProtocolAndSchemaMapper
- SprintReporter

Forbidden in this sprint:

- No browser launch or donor/reference gameplay investigation.
- No asset capture or donor asset body inspection.
- No wallet endpoint calls.
- No Cassandra/DB execution.
- No raw secret value extraction, storage, or reporting.

## Required Input Reports

| Input | Exists | Readable | Result |
|---|---:|---:|---|
| `[SKILL_SUITE_ROOT]/AGENTS.md` | yes | yes | suite rules read |
| `[SKILL_SUITE_ROOT]/SKILL_INDEX.md` | yes | yes | skill order read |
| `[SKILL_SUITE_ROOT]/.agents/skills/ProtocolAndSchemaMapper/SKILL.md` | yes | yes | skill instructions read |
| `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md` | yes | yes | reporting instructions read |
| `[PROJECT_ROOT]/project_manifest.json` | yes | yes | manifest parsed before edits |
| `[PROJECT_ROOT]/00_skill_reports/ProjectCreator/handoff.json` | yes | yes | prior handoff read |
| `[PROJECT_ROOT]/00_skill_reports/AuthorizedReferenceResearcher/handoff.json` | yes | yes | prior handoff read |
| `[PROJECT_ROOT]/00_skill_reports/ReferenceAssetInventory/handoff.json` | yes | yes | prior handoff read |
| `[PROJECT_ROOT]/01_reference_research/scenario_coverage.md` | yes | yes | observed coverage read as context only |
| `[PROJECT_ROOT]/01_reference_research/network_observations.md` | yes | yes | sanitized metadata read as context only |
| `[PROJECT_ROOT]/02_reference_assets/final_inventory.csv` | yes | yes | inventory count/status read; asset bodies not inspected |
| `[PROJECT_ROOT]/02_reference_assets/asset_ownership_register.csv` | yes | yes | ownership status read; asset bodies not inspected |

## Suite Reference Summaries

| Reference | Available | Result |
|---|---:|---|
| `SOURCE_DOCUMENT_INDEX.md` | yes | Uploaded docs index available |
| `VERIFIED_FACTS.md` | yes | Evidence-backed facts available |
| `PROTOCOL_LAYER_MODEL.md` | yes | Layer separation rules available |
| `BSG_COMMON_WALLET_SUMMARY.md` | yes | Wallet request/response/hash summary available |
| `CLIENT_BUILD_AND_ARCHITECTURE_SUMMARY.md` | yes | Legacy client stack summary available |
| `CASSANDRA_REGISTRATION_SUMMARY.md` | yes | Cassandra/config summary available |
| `SECURITY_AND_SECRET_HANDLING.md` | yes | Redaction rules available |
| `ANTI_HALLUCINATION_RULES.md` | yes | Unknown/blocker rules available |

## Explicit Source Path Verification

| Path | Exists | Readable | Type | Used for | Blocker |
|---|---:|---:|---|---|---|
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/new-games-client` | yes | yes | directory | portal/preloader client runtime clues | none |
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001` | yes | yes | directory | Crazy Rooster/new-games slot runtime reference | none |
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server` | yes | yes | directory | launch/runtime/wallet/Cassandra clues | none |
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/premium-slot` | yes | yes | directory | base slot runtime/template reference | none |
| `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/game-server/web-gs/src/main/webapp/real/mp/template.jsp` | yes | yes | file | legacy JSP launch/template shell | none |
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/cwv3/CWStartGameAction.java` | yes | yes | file | `cwstartgamev2.do` launch routing | none
|
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/BaseStartGameAction.java` | yes | yes | file | new-games and legacy template redirects |
none |
| `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/runtime/export_localmachine/com.abs.casino.common.cache.BankInfoCache.xml` | yes | yes | file | bank config, coin values, new-games properties |
secret-bearing; redacted in notes |
| `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/docker-compose.yml` | yes | yes | file | local Cassandra/keyspace service evidence | none |
| `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/GS_7001_NEWGAMES_RUNBOOK.md` | yes | yes | file | canonical 7001 new-games flow | contains a test token example; redacted in outputs |
| `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/common/src/main/java/com/abs/casino/common/cache/data/bank/BankInfo.java` | yes | yes | file | PASS_KEY property names only | none |
| `[DEV_ROOT]/runtime-patches/commonwallet/commonWallet.jsp` | yes | yes | file | test token reference location only | secret-bearing; values not extracted |
| `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/deploy/scripts/phase4-protocol-wallet-canary-probe.sh` | yes | yes | file | canary/test token reference logic only | secret-bearing; values not extracted |

## Targeted Search Boundary

Targeted searches were limited to the explicit paths above and to user-listed protocol terms such as `cwstartgamev2`, `cwguestlogin`, `window.gameConfig`, `version.json`, `validator.js`, `game.js`, `bankinfocf`, `gametinfocf`, `gameinfocf`,
`R Casino SCKS`, `roundId`, `isRoundFinished`, `jpWin`, `jpContribution`, `promoWinAmount`, `negativeBet`, and `project_build.sh`.

No broad search was run over `[USER_HOME]`, `[USER_HOME]/Documents`, parent folders, sibling repositories, Desktop, Downloads, or system directories.

## Secret Handling

- PASS_KEY values were not intentionally read, copied, persisted, or reported.
- Test token values were not intentionally read, copied, persisted, or reported.
- Secret-bearing source files are referenced by path/property names only.
- Generated outputs use placeholder values such as `PASS_KEY_FIXTURE_DO_NOT_USE`.

## Preflight Blockers

- The core `@gamesv1/core-protocol` package implementation is referenced by the 7001 and premium-slot clients but was not inspected because its package root was not one of the explicit allowed paths.
- Live wallet client implementation for `com.abs.casino.payment.wallet.client.v4.CanexCWClient` was not found inside the targeted inspected files; BSG wallet contract relies on uploaded BSG CW docs plus available GS constants.
- Registration serialization for `scn` remains blocked unless a real serializer/tool is provided in a later GameServerRegistrar sprint.
