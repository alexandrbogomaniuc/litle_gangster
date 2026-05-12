# Cassandra / Config Registration Contract

Status: partial; generate-only.

## Safety Boundary

This sprint did not generate CQL and did not execute Cassandra or any DB action. Later GameServerRegistrar must default to generate-only and must produce rollback.

## Verified Cassandra/Config Evidence

From suite reference summaries:

- Bank configuration evidence points to `RCasinoSCKS.bankinfocf`, not `RCasinoKS.banks`.
- `bankinfocf` has `key bigint PRIMARY KEY`, `jcn text`, and `scn blob`.
- `jcn` contains complete bank JSON config; `scn` is serialized binary config.
- Dragonstone/game 838 examples update `gametinfocf` and `gameinfocf` under `rcasinoscks`.
- `RCasinoKS_schema.cql` exists but is not sufficient alone for registration.

From explicit docker compose:

- Local compose creates/updates both `RCasinoKS` and `RCasinoSCKS` keyspaces (`docker-compose.yml:59-62`).

From explicit BankInfo export:

- Bank 6275 exists with `id=6275`, `externalBankId=6275`, and default currency `MQC` (`BankInfoCache.xml:786-791`).
- Bank 6275 coin values are `1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 100` (`BankInfoCache.xml:797-842`).
- Bank 6275 Common Wallet properties include request client class and auth/balance/wager/refund URLs with URLs redacted (`BankInfoCache.xml:846-888`).
- Bank 6275 new-games properties include `NEW_GAMES_ROUTE_GAME_ID=7000,7001`, gamelist title/langs, client URL, API URL, and GS internal base URL with URLs redacted (`BankInfoCache.xml:895-925`).

From explicit 7001 runbook:

- Canonical local lane uses `bankId=6275`, `subCasinoId=507`, `gameId=7001`, and new-games `/slot/v1/*` flow, with token redacted (`GS_7001_NEWGAMES_RUNBOOK.md:53-66`).
- Bank config must route both `7000` and `7001` via `NEW_GAMES_ROUTE_GAME_ID=7000,7001` (`GS_7001_NEWGAMES_RUNBOOK.md:43-51`).

## Required Registration Artifacts For Future Game 8001

GameServerRegistrar must produce, at minimum:

- Generated CQL/config patch for game 8001.
- Rollback CQL/config patch.
- Dry-run validation report.
- Explicit route/client-path settings for new-games client or legacy template, depending on approved build path.
- RTP config references for target RTP models.
- Bet config references for min/default/max bet and coin ladder.
- Video-capture setting if documented/required by final requirements.
- Asset/client release path references only after GameClientBuilder produces an approved dist/release pack.

## Candidate Config Fields To Verify Later

These are not approved values for 8001 yet; they are evidence-backed patterns to verify during GameServerRegistrar:

- `RCasinoSCKS.gametinfocf`
- `RCasinoSCKS.gameinfocf`
- `RCasinoSCKS.bankinfocf`
- `jcn`
- `scn`
- `servlet`
- `swfLocation`
- new-games route properties such as `NEW_GAMES_ROUTE_GAME_ID`, `NEW_GAMES_CLIENT_URL`, `NEW_GAMES_API_URL`, `NEW_GAMES_GS_INTERNAL_BASE_URL`

## Generate-Only Default

Project manifest rule:

- `game_server.db_apply_mode = generate_only`
- `game_server.production_db_apply_allowed = false`

No later skill may apply CQL or modify DB unless the user explicitly authorizes a dev/stage apply and the skill has validated rollback.

## Blockers

- No game 8001 registration record exists yet.
- Exact `gametinfocf`/`gameinfocf` records for 8001 are unknown.
- `scn` blob/Java serialization remains blocked unless a real serializer/tool is provided.
- New-games release artifact paths for 8001 are unknown until GameClientBuilder.
- RTP/math package reference is unknown until MathModelDesigner.
- The core release registration docs referenced by 7001 docs live outside the explicit inspected path and were not inspected in this sprint.
