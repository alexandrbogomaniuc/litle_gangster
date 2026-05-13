# Current GS New Game Registration Process

## Direct Answer

Current GS registration is a cache/config process centered on game templates, bank-game records, and bank routing properties. Evidence supports `GameTInfoCF`, `GameInfoCF`, and `BankInfoCF` as key configuration stores. Registration does not
appear to import executable math into GS.

## Evidence Table

| Question | Answer | Status | Evidence |
|---|---|---|---|
| What is the actual current-GS registration process? | Create or update game template config, bank-specific game config, and bank route/config values, then load through Cassandra/cache serialization. | PROVEN |
`Staging/platform-source/platform/gs-server/game-server/common-gs/.../CachesHolder.java:41-53`; `.../CassandraBaseGameInfoTemplatePersister.java:14-52`; `.../CassandraBaseGameInfoPersister.java:39-54`;
`.../CassandraBankInfoPersister.java:23-126`. |
| Which records/configs are needed? | Template record in `GameTInfoCF`, bank game record in `GameInfoCF`, bank properties in `BankInfoCF`, and optional external ID mapping in `ExtGameIds`. | PROVEN | Persister constants and registered
caches above; `CassandraExternalGameIdsPersister.java:24-36`. |
| Which fields are known? | `gameId`, `gameName`, `defaultGameInfo`, `gameType`, `group`, `variableType`, `gsClassName`, `coinsString`, `langsString`, `propertiesString`, `servlet`, `title`, `swfLocation`, `additionalParams`, `isFrbGame`,
plus bank route keys. | PROVEN | `BaseGameInfoTemplate.java:42-55`; runtime cache exports under `Staging/runtime/gs-release-zero/runtime/export_localmachine/`. |
| Which bank route fields matter for New Games? | `NEW_GAMES_ROUTE_GAME_ID`, `NEW_GAMES_CLIENT_URL`, optional `NEW_GAMES_CLIENT_URL_<gameId>`, `NEW_GAMES_API_URL`, `NEW_GAMES_GS_INTERNAL_BASE_URL`, and catalog title/lang/suite fields. |
PROVEN | `BankInfo.java:852-862`; `BaseStartGameAction.java:95-104`, `878-904`, `918-941`; `BankInfoCache.xml:112-142`, `895-925`. |
| Does registration select a runtime lane? | It can route launch traffic to New Games if bank properties and game ID matching enable it, otherwise legacy template routing remains available. | PROVEN | `BaseStartGameAction.java:819-839`,
`878-904`, `1019-1032`; `GameListExtAction.java:113-123`, `357-364`. |
| Does registration load executable math? | No direct evidence found. Registration stores config/display/routing/template properties, not reel strips, cluster paytables, feature rules, or executable math. | NOT_FOUND | No registration
persister inspected consumes `math_package.json`, paytables, reel strips, cluster rules, or simulator output. |
| Does registration include client/static path? | Yes, legacy templates expose `swfLocation`; New Games uses bank client URL routing and optional per-game client URL key. | PROVEN | `BaseGameInfoTemplate.java:52`;
`BaseStartGameAction.java:918-941`. |
| Does registration include backend runtime path? | New Games bank config includes API and GS internal base URLs; exact Little Gangster runtime endpoint is not registered yet. | PROVEN for route fields, BLOCKED for 8001 |
`BankInfo.java:858-862`; `BaseStartGameAction.java:883-904`. |
| Does registration require `scn`/`jcn`? | `GameInfoCF` explicitly stores `scn` and `jcn`; template/bank persisters inherit serialized/JSON config behavior. Serializer/admin/cache process remains blocked for generation. | PROVEN with
blocker | `AbstractCassandraPersister.java:25-28`; `CassandraBaseGameInfoPersister.java:44-54`, `173-181`. |

## What GameServerRegistrar Must Later Generate

Generate-only artifacts, no DB apply:

- A registration plan for the selected game ID, currently expected as 8001 unless the manifest changes.
- `GameTInfoCF` template JSON/spec with game name, title, template fields, route/servlet/static-path values, RTP display, volatility, cap/max-win metadata, and feature flags.
- `GameInfoCF` bank/currency assignment specs for the chosen bank/currency set.
- `BankInfoCF` patch specs to include the game ID in New Games routing if that lane is selected, including game-specific client URL and API/internal base URL references where needed.
- Optional `ExtGameIds` mapping only if current GS lane requires it.
- Serializer/import instructions for `scn`/`jcn`, plus rollback specs.
- Validation checklist and dry-run diff.

Do not generate:

- Executable math import.
- CQL apply commands.
- Cassandra writes.
- Production route changes.

## Unresolved

- `game_8001_registration_missing`
- `scn_serializer_missing`
- `selected_runtime_lane_not_final`
- `math_result_owner_unproven`
