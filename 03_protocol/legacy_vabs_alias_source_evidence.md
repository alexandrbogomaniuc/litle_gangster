# Legacy VABS Alias Source Evidence

Date: 2026-05-15

This evidence summary uses sanitized route names only. It intentionally excludes raw
private URLs, SIDs, signatures, tokens, emails, passwords, and secrets.

| Label | Source | Finding |
| --- | --- | --- |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/WEB-INF/struts-config.xml` | Registers history/VBA action paths including round,
token, and VBA access actions. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/api/history/vba/HistoryByRoundAction.java` | Reads
`ROUNDID`, `LANG`, whole-session controls, resolves `gameSessionId`, and redirects to `/vabs/show.jsp` semantics. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/api/history/vba/HistoryByTokenAction.java` | Reads
language/timezone inputs, resolves a session, and redirects to `/vabs/show.jsp` semantics. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/api/vba/GetVBAAction.java` | Builds a VBA/VABS visual URL
with `VIEWSESSID` and `GAMEID` semantics. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/web/history/GameHistoryListAction.java` | Populates visual
`historyUrl` values using `/vabs/show.jsp` semantics. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/gamehistory.jsp` | Presents history rows that can open visual history windows. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/gamehistoryXML.jsp` | Emits a visual history URL field for history integration. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/support/supporthistory.jsp` | Opens support-history visual URLs in a VAB window. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/vabs/VabEngine/VabEngineMain.jspf` | Reads `hideClose`, `VIEWSESSID`, `TIMEZONE`,
round/session controls, and requests visual archive data. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/vabs/html5template.jspf` | Reads visual replay language/session parameters. |
| PROVEN_SOURCE | `gs-server/common/src/main/java/com/dgphoenix/casino/common/cache/data/bank/BankInfo.java` | Defines `ENABLE_IN_GAME_HISTORY`,
`GAME_HISTORY_URL`, and `OPEN_GAME_HISTORY_IN_SAME_WINDOW`. |
| PROVEN_SOURCE | `gs-server/common/src/main/java/com/dgphoenix/casino/common/web/BaseAction.java` | Defines launch parameter key for
`gameHistoryUrl`. |
| PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/BaseStartGameAction.java` | Resolves game
history URL from request/bank/default builder and passes it to launch. |
| PROVEN_SOURCE | `Gamesv1/docs/gs/bootstrap-config-contract.md` | Documents browser `historyPolicy.gameHistoryUrl` and source keys for in-game
history. |
| PROVEN_SOURCE | `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Posts canonical JSON history requests to `/slot/v1/gethistory`
and treats them as read-only. |
| PROVEN_SOURCE | `new-games-server/src/index.ts` | Registers current 8001 history routes and existing canonical `/slot/v1/gethistory`. |
| PROVEN_SOURCE | `new-games-server/src/games/little-gangster/history/historyRoutes.ts` | Current 8001 route foundation maps `VIEWSESSID`, `LANG`,
`TIMEZONE`, and `hideClose` inputs, but only on canonical 8001 route paths. |
| LIKELY_SOURCE | legacy VABS session handling and current 8001 route request merge | `VIEWSESSID` can map to `gameSessionId` for 8001, but a separate
view-session id has not been disproven. |
| CANDIDATE_SOURCE | `new-games-server/src/games/little-gangster/history/` | Future alias parser can reuse current security helpers and visual
renderer. |
| NOT_FOUND | `new-games-server/src/games/little-gangster/history/` | No `/vabs/show.jsp` alias route implementation exists. |
| NOT_FOUND | registration schema/docs searched | No explicit 8001 `vabsUrl`, `vbaUrl`, `historyUrl`, or `historyBaseUrl` registration field was
proven. |
| BLOCKED | BO/CM runtime acceptance | Actual BO/CM acceptance of canonical new-games routes without alias remains untested. |

## Evidence Limits

- Crazy Rooster / 7001 is not authoritative for Little Gangster.
- Legacy evidence proves alias semantics, not the final 8001 route implementation.
- Current 8001 source proves canonical route foundation, not BO/CM compatibility.
