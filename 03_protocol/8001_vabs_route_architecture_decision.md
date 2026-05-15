# 8001 VABS Route Architecture Decision

Generated: 2026-05-15

## Decision

Select Model E: hybrid route resolution.

## Architecture

- New-games-server should own the Little Gangster 8001 visual replay builder under
  `new-games-server/src/games/little-gangster/history/`.
- Route registration should be guarded for gameId `8001` in `new-games-server/src/index.ts`
  or a reusable route registrar discovered during implementation.
- The visual route should accept modern `/slot/v1/8001/history/...` access and provide
  legacy-compatible parameter handling or redirect support for `/vabs/show.jsp` style
  access.
- `/slot/v1/gethistory` remains the JSON history route and should not be mistaken for
  visual VABS completion.
- The in-game History button should use a bootstrap/configured route or backend-generated
  route record, not a hardcoded client path.
- CM/backoffice should use the configured/generated visual history URL and receive a
  visual page or clear blocked/not-found response.

## Required Route Shapes

Recommended modern routes:

- `GET /slot/v1/8001/history/round/:roundId`
- `GET /slot/v1/8001/history/session/:gameSessionId`
- `GET /slot/v1/8001/history/session/:gameSessionId/whole-session`
- `GET /slot/v1/8001/history/render/round/:roundId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId/whole-session`

Recommended legacy compatibility:

- accept or translate `VIEWSESSID`, `ROUNDID`, `GAMEID`, `SESSION`, `LANG`, `TIMEZONE`,
  `online`, and whole-session indicators;
- provide a route resolver or redirect path for `/vabs/show.jsp` semantics if GS/CM
  cannot be configured directly to the modern routes.

## Registration / Config Status

Registration/config is required but blocked on exact field shape. Evidence proves
bootstrap `historyPolicy.gameHistoryUrl` and legacy `GAME_HISTORY_URL` behavior. It does
not prove a release-registration field named `vabsUrl`, `vbaUrl`, or `historyBaseUrl`.

## Release Impact

GameClientBuilder, GameServerRegistrar generation, wallet/history tests, and release
remain blocked until the route implementation and configuration path are approved,
implemented, and tested.
