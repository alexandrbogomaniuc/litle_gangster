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
| `[REDACTED_LOCAL_PATH] | yes | yes | suite rules read |
| `[REDACTED_LOCAL_PATH] | yes | yes | skill order read |
| `[REDACTED_LOCAL_PATH] | yes | yes | skill instructions read |
| `[REDACTED_LOCAL_PATH] | yes | yes | reporting instructions read |
| `[REDACTED_LOCAL_PATH] | yes | yes | manifest parsed before edits |
| `[REDACTED_LOCAL_PATH] | yes | yes | prior handoff read |
| `[REDACTED_LOCAL_PATH] | yes | yes | prior handoff read |
| `[REDACTED_LOCAL_PATH] | yes | yes | prior handoff read |
| `[REDACTED_LOCAL_PATH] | yes | yes | observed coverage read as context only |
| `[REDACTED_LOCAL_PATH] | yes | yes | sanitized metadata read as context only |
| `[REDACTED_LOCAL_PATH] | yes | yes | inventory count/status read; asset bodies not inspected |
| `[REDACTED_LOCAL_PATH] | yes | yes | ownership status read; asset bodies not inspected |

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
| `[REDACTED_LOCAL_PATH] | yes | yes | directory | portal/preloader client runtime clues | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | directory | Crazy Rooster/new-games slot runtime reference | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | directory | launch/runtime/wallet/Cassandra clues | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | directory | base slot runtime/template reference | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | legacy JSP launch/template shell | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | `cwstartgamev2.do` launch routing | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | new-games and legacy template redirects | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | bank config, coin values, new-games properties | secret-bearing; redacted in notes |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | local Cassandra/keyspace service evidence | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | canonical 7001 new-games flow | contains a test token example; redacted in outputs |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | PASS_KEY property names only | none |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | test token reference location only | secret-bearing; values not extracted |
| `[REDACTED_LOCAL_PATH] | yes | yes | file | canary/test token reference logic only | secret-bearing; values not extracted |

## Targeted Search Boundary

Targeted searches were limited to the explicit paths above and to user-listed protocol terms such as `cwstartgamev2`, `cwguestlogin`,
`window.gameConfig`, `version.json`, `validator.js`, `game.js`, `bankinfocf`, `gametinfocf`, `gameinfocf`, `R Casino SCKS`, `roundId`,
`isRoundFinished`, `jpWin`, `jpContribution`, `promoWinAmount`, `negativeBet`, and `project_build.sh`.

No broad search was run over `[REDACTED_LOCAL_PATH], `[REDACTED_LOCAL_PATH], parent folders, sibling repositories, Desktop, Downloads, or system
directories.

## Secret Handling

- PASS_KEY values were not intentionally read, copied, persisted, or reported.
- Test token values were not intentionally read, copied, persisted, or reported.
- Secret-bearing source files are referenced by path/property names only.
- Generated outputs use placeholder values such as `PASS_KEY_FIXTURE_DO_NOT_USE`.

## Preflight Blockers

- The core `@gamesv1/core-protocol` package implementation is referenced by the 7001 and premium-slot clients but was not inspected because its
  package root was not one of the explicit allowed paths.
- Live wallet client implementation for `com.abs.casino.payment.wallet.client.v4.CanexCWClient` was not found inside the targeted inspected files; BSG
  wallet contract relies on uploaded BSG CW docs plus available GS constants.
- Registration serialization for `scn` remains blocked unless a real serializer/tool is provided in a later GameServerRegistrar sprint.
