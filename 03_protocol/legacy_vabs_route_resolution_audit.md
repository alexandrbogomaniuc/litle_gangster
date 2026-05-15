# Legacy GS VBA/VABS/Lasthands Route-Resolution Audit

Generated: 2026-05-15

## Scope

This sprint audited route-resolution evidence before implementing Little Gangster 8001
VABS/VBA/Lasthands visual history routes. Staging source was inspected read-only. No
source patch, route implementation, registration generation, wallet call, DB action, or
release approval occurred.

Crazy Rooster / 7001 is not authoritative. It was treated only as candidate evidence for
new-games and client-shell behavior.

## Route Resolution Finding

Recommended model: Model E, hybrid.

GS/CM/backoffice should resolve a configured or generated visual history URL that can
serve legacy-compatible VABS access patterns. Little Gangster should implement its
game-specific visual replay builder under the new-games 8001 history module while
keeping compatibility with legacy route parameters such as `VIEWSESSID`, `ROUNDID`,
`GAMEID`, `SESSION`, `LANG`, and whole-session selection.

## Legacy / GS Evidence

- PROVEN_SOURCE: `gs-server/game-server/web-gs/src/main/webapp/WEB-INF/struts-config.xml`
  maps `/vabs/historyByRound` to `HistoryByRoundAction`, `/vabs/historyByToken` to
  `HistoryByTokenAction`, and `/getvba` to `GetVBAAction`.
- PROVEN_SOURCE: `HistoryByRoundAction` reads `ROUNDID`, resolves the game session by
  round, and redirects to `/vabs/show.jsp`. With `WHOLE_SESSION=true`, it redirects to a
  session-level VABS URL without `ROUNDID`.
- PROVEN_SOURCE: `GetVBAAction` resolves a `gameSessionId` and redirects to
  `/vabs/show.jsp` with `VIEWSESSID`, `STARTDATE`, `ENDDATE`, and `GAMEID`.
- PROVEN_SOURCE: `GameHistoryListAction` writes per-row `historyUrl` values using
  `/vabs/show.jsp` with session/date/game parameters.
- PROVEN_SOURCE: `gamehistory.jsp` opens the entry `historyUrl` in a VAB popup window.
- PROVEN_SOURCE: `gamehistoryXML.jsp` exposes a `vab_url` field.
- PROVEN_SOURCE: `/vabs/show.jsp` includes the HTML5 VABS template, which reads
  `VIEWSESSID`, `ROUNDID`, `GAMEID`, `SESSION`, and `online`, then requests archived bet
  data through the GS proxy servlet.
- LIKELY_SOURCE: `GameHistoryURLBuilder` builds `/gamehistory.do` URLs used upstream of
  the list page that later exposes visual VABS links.

## New-Games Evidence

- PROVEN_SOURCE: `new-games-server/src/index.ts` exposes `/slot/v1/gethistory`.
- PROVEN_SOURCE: `/slot/v1/gethistory` returns a runtime envelope with `feature.mode =
  "HISTORY"` and `history.records`; it is JSON history, not a visual VABS page.
- PROVEN_SOURCE: `new-games-server/src/games/little-gangster/historyMapper.ts` already
  prepares history replay and VABS field payloads for 8001.
- PROVEN_SOURCE: the current Little Gangster adapter/lifecycle wrapper preserves
  `presentationPayload.gamePayload`, history payload placeholders, blocker flags, and
  100x bonus-buy planning fields.
- NOT_FOUND: no implemented 8001 visual HTML route or legacy-compatible VABS route was
  found in new-games-server.

## Gamesv1 / Client Evidence

- PROVEN_SOURCE: `Gamesv1/packages/core-protocol/src/IGameTransport.ts` defines
  `HistoryRequest`, `HistoryQuery`, and `gethistory`.
- PROVEN_SOURCE: `GsHttpRuntimeTransport` posts to `/slot/v1/gethistory` and expects
  history records in a runtime envelope.
- CANDIDATE_SOURCE: 7001 client source wires a History control, but current behavior
  opens help/rules rather than a proven runtime visual history viewer. This is not
  authoritative for 8001.
- NOT_FOUND: no Gamesv1 visual VABS renderer, whole-session route resolver, or
  backoffice-compatible visual route was proven.

## Registration / Config Evidence

- PROVEN_SOURCE: bootstrap docs expose `historyPolicy.gameHistoryUrl` and source keys
  including `ENABLE_IN_GAME_HISTORY`, `GAME_HISTORY_URL`, and
  `OPEN_GAME_HISTORY_IN_SAME_WINDOW`.
- PROVEN_SOURCE: legacy start-game flow passes `GAME_HISTORY_URL` into game launch when
  in-game history is enabled.
- LIKELY_SOURCE: legacy bank config can provide a history action URL or game history URL.
- NOT_FOUND: release-registration schema evidence did not show explicit `vabsUrl`,
  `vbaUrl`, `historyBaseUrl`, or `gameHistoryUrl` fields.
- BLOCKED: the exact 8001 registration/config field shape for visual history is not yet
  proven.

## Lasthands Finding

NOT_FOUND: no separate Lasthands route-resolution path was proven in this audit. Treat
Lasthands as a release-blocking visual history test requirement until source/config
evidence proves the exact route or acceptable substitute.

## Conclusion

Little Gangster should not implement only `/slot/v1/gethistory` JSON and call visual
history done. The next implementation plan should preserve the existing JSON history
route, add a game-specific 8001 visual history module, and provide legacy-compatible
entry or redirect behavior for GS/CM/backoffice VABS access.
