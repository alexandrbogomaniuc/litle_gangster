# Registration Evidence Map

Status: partial; generate-only; no DB/Cassandra execution.

## Direct Answers

### What minimum records/configs are needed for a new game ID?

Minimum expected artifacts for 8001, pending exact serializer/tooling:

1. Game metadata/config for game 8001 in `RCasinoSCKS.gametinfocf` or equivalent template cache.
2. Bank-specific game config for bank 6275 in `RCasinoSCKS.gameinfocf`.
3. Bank route/config update in `RCasinoSCKS.bankinfocf` or exported bank config so `NEW_GAMES_ROUTE_GAME_ID` includes 8001 and the client/API/internal URLs are correct.
4. Optional per-game client URL property, likely `NEW_GAMES_CLIENT_URL_8001`, if 8001 must route to a game-specific client.
5. Gamelist title/lang values including Little Gangster if it should appear in the bank gamelist.
6. Rollback artifacts for every created/updated record/property.

Evidence:

- Suite references state Dragonstone/game 838 examples update `gametinfocf` and `gameinfocf` under `rcasinoscks`: `[SKILL_SUITE_ROOT]/references/CASSANDRA_REGISTRATION_SUMMARY.md:11-12`.
- Suite references state `bankinfocf` has `key`, `jcn`, and `scn`, where `jcn` contains bank JSON and `scn` is serialized binary config: `CASSANDRA_REGISTRATION_SUMMARY.md:7-10`.
- Compose creates/updates `RCasinoKS` and `RCasinoSCKS`: `[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/docker-compose.yml:59-62`.
- Bank 6275 route props currently include `NEW_GAMES_ROUTE_GAME_ID=7000,7001`, generic client/API/internal URL properties, and gamelist values for Plinko/Crazy Rooster:
`[DEV_ROOT]/docker-groups/refactoredgs-microservices/release-zero-20260423T141209Z/runtime/export_localmachine/com.abs.casino.common.cache.BankInfoCache.xml:895-925`.

### Is `gametinfocf` required?

LIKELY YES, but exact 8001 record shape is BLOCKED.

Evidence: suite Cassandra summary identifies game 838 examples updating `gametinfocf`: `CASSANDRA_REGISTRATION_SUMMARY.md:11-12`.

### Is bank-specific `gameinfocf` required?

LIKELY YES, but exact 8001 record shape is BLOCKED.

Evidence: suite Cassandra summary identifies game 838 examples updating `gameinfocf`: `CASSANDRA_REGISTRATION_SUMMARY.md:11-12`.

### Is `bankinfocf` only bank/wallet config or also game registration?

It is bank/wallet config and also participates in game routing/gamelist behavior for new-games.

Evidence:

- `bankinfocf` is documented as bank configuration with Common Wallet properties: `CASSANDRA_REGISTRATION_SUMMARY.md:7-10`.
- Bank 6275 export contains Common Wallet request class/auth/balance/wager/refund URL properties and new-games route/gamelist/client/API/internal URL properties in the same bank config: `BankInfoCache.xml:846-925`.
- 7001 runbook says bank properties must include `NEW_GAMES_ROUTE_GAME_ID=7000,7001` and gamelist title/lang values for routing/gamelist: `GS_7001_NEWGAMES_RUNBOOK.md:43-51`.

### Is `scn` required for any created/updated record?

For `bankinfocf`, yes according to uploaded summary evidence: `scn` exists and is serialized binary config. Whether every 8001 game record also requires `scn` is UNKNOWN from inspected source.

Evidence: `CASSANDRA_REGISTRATION_SUMMARY.md:7-10`.

### Can `scn` be generated safely?

NO_BLOCKED.

No serializer/import/admin/cache tool was verified in this sprint. GameServerRegistrar must not write guessed binary blobs.

### Is there a serializer/import/admin/cache tool?

UNKNOWN/BLOCKED.

Targeted searches found config/cache examples and support/admin forms, but no approved serializer/import tool for `RCasinoSCKS.scn` generation was proven in this sprint. Provide the exact tool/path or authorize a focused inspection.

### Is simple CQL enough, or generate-only until serializer is found?

Generate-only until serializer/config pipeline is found and reviewed.

Reasons:

- `scn` binary serialization is not safely generatable by hand.
- Registration touches multiple config layers.
- No DB/Cassandra execution is allowed by project rules.

### What rollback artifacts are required?

GameServerRegistrar must generate:

- rollback CQL/config for any `gametinfocf` create/update
- rollback CQL/config for any `gameinfocf` create/update
- rollback for bank property changes such as route id list, gamelist values, and per-game client URL
- before/after config snapshots or redacted diffs
- validation report proving no raw secrets and no scaffold assets in release config

## Evidence Table

| Area | Evidence | Status |
|---|---|---|
| Keyspaces | Compose creates `RCasinoKS` and `RCasinoSCKS`: `docker-compose.yml:59-62`. | known |
| Bank 6275 | Export has `id=6275`, default currency, limit, coin ladder: `BankInfoCache.xml:786-842`. | known |
| Coin ladder | Values `1,2,3,4,5,10,15,20,25,50,100`: `BankInfoCache.xml:797-842`. | known |
| Common Wallet bank properties | Request class/auth/balance/wager/refund properties: `BankInfoCache.xml:846-888`. | known, secret-safe |
| New-games bank route | `NEW_GAMES_ROUTE_GAME_ID=7000,7001` and client/API/internal URL props: `BankInfoCache.xml:895-925`. | known for 7000/7001 only |
| Per-game 7001 URL | 7001 handoff says `NEW_GAMES_CLIENT_URL_7001` was set through support action: `CRAZY_ROOSTER_7001_FRESH_AGENT_HANDOFF_20260505.md:60-68`. | known from handoff, not exported in inspected BankInfoCache |
| 8001 registration | No 8001 records/config inspected. | blocked |
| `scn` | `scn blob` documented, serializer not found. | blocked |

## 8001 Registration Decision

GameServerRegistrar cannot run safely yet. It must wait for MathModelDesigner and GameClientBuilder outputs, then generate registration and rollback only. It must not execute Cassandra by default.
