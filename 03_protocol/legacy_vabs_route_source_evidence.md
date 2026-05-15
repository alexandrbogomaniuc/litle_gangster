# Legacy VBA/VABS Route Source Evidence

Generated: 2026-05-15

All source inspection was read-only under the Staging source root. Raw private URLs,
tokens, signatures, SIDs, emails, passwords, and secrets are not persisted here.

| Evidence | Label | Source | Finding |
| --- | --- | --- | --- |
| Struts VABS routes | PROVEN_SOURCE | `gs-server/game-server/web-gs/src/main/webapp/WEB-INF/struts-config.xml` | `/vabs/historyByRound`,
`/vabs/historyByToken`, and `/getvba` are registered routes. |
| Round-to-VABS redirect | PROVEN_SOURCE | `HistoryByRoundAction` | Reads `ROUNDID`, resolves sessions, redirects to `/vabs/show.jsp`; whole-session
mode omits `ROUNDID`. |
| Token-to-VABS redirect | PROVEN_SOURCE | `HistoryByTokenAction` | Resolves token to round/session and redirects to `/vabs/show.jsp` with VABS
parameters. |
| Session-to-VABS redirect | PROVEN_SOURCE | `GetVBAAction` | Resolves `gameSessionId` and redirects to `/vabs/show.jsp` with session/date/game
parameters. |
| History-list visual URL | PROVEN_SOURCE | `GameHistoryListAction` | Populates `historyUrl` as `/vabs/show.jsp?...` for the JSP list. |
| Backoffice/list opener | PROVEN_SOURCE | `gamehistory.jsp` | Opens each `historyUrl` in a VAB popup/window. |
| XML API visual URL | PROVEN_SOURCE | `gamehistoryXML.jsp` | Emits a `vab_url` element. |
| VABS page | PROVEN_SOURCE | `vabs/show.jsp` and HTML5 template | Loads visual VABS template and archived bet data. |
| VABS data servlet | PROVEN_SOURCE | `web.xml` and `GameHistoryServlet` | `/gsproxy/VisualArchivingBetsV2.servlet` maps to the game-history servlet.
|
| Upstream list URL | LIKELY_SOURCE | `GameHistoryURLBuilder` | Builds `/gamehistory.do` URLs that lead to VABS list entries. |
| Bootstrap history policy | PROVEN_SOURCE | `Gamesv1/docs/gs/bootstrap-config-contract.md` | Exposes `historyPolicy.gameHistoryUrl` for browser
launch config. |
| New JSON history route | PROVEN_SOURCE | `new-games-server/src/index.ts` | `/slot/v1/gethistory` returns JSON runtime history. |
| Current 8001 history payload | PROVEN_SOURCE | `new-games-server/src/games/little-gangster/historyMapper.ts` | Produces JSON replay/VABS field
payloads, not visual route HTML. |
| Gamesv1 transport | PROVEN_SOURCE | `Gamesv1/packages/core-protocol/src/http/GsHttpRuntimeTransport.ts` | Posts to `/slot/v1/gethistory` and expects
JSON history records. |
| Gamesv1 visual VABS renderer | NOT_FOUND | `Gamesv1/packages` and 7001 source | No proven generic visual VABS renderer was found. |
| Release registration VABS URL field | NOT_FOUND | GS release registration docs/schema | No explicit visual history URL field was proven. |

## Sanitization Note

One legacy source file contains commented example host strings. Those strings were read
only as source context and are intentionally omitted from project docs.
