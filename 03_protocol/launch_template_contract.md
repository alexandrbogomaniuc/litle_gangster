# Launch / Template Contract

Status: mapped for legacy JSP and new-games routing; no browser launched.

## BSG Common Wallet Launch Routes

From uploaded BSG CW summary:

- `cwguestlogin.do`
  - params: `bankId`, `gameId`, `lang`, optional `homeUrl`
- `cwstartgamev2.do`
  - params: `bankId`, `gameId`, `mode`, `token`, `lang`
  - documented mode values: `real`, `free`

From GS source:

- `CWStartGameAction.java:55-56` documents the authorized launch shape for `cwstartgamev2.do`.
- `CWStartGameAction.java:99-108` parses `gameId`, detects new-games routing, reads game mode/lang, and calls Common Wallet auth with the launch token.
- `CWStartGameAction.java:217-220` can save the token into account info when `bankInfo.isAddTokenMode()` is enabled; future logging must avoid raw token leakage.

## Legacy JSP Shell

Evidence: `[DEV_ROOT]/GSRefactor-beta-local-procedure-live-20260307/gs-server/game-server/web-gs/src/main/webapp/real/mp/template.jsp`

The JSP shell:

- Reads `bankId` from request and looks up `BankInfo` (`template.jsp:52-65`).
- Requires `SID`/session id (`template.jsp:70-75`).
- Requires `gameId` (`template.jsp:76-81`).
- Reads game template `swfLocation` and builds a game path (`template.jsp:102-114`).
- Loads `<templateJsPath>/version.json`, then `<templateJsPath>/validator.js`, then `<templateJsPath>/game.js` (`template.jsp:250-260`).
- Normalizes legacy query params for `BANKID`, `SID`, `GAMEID`, `MODE`, `LANG`, `GAMESERVERID`, and `WEB_SOCKET_URL` (`template.jsp:264-277`).
- Exposes `getParams()` with lower-case and upper-case launch fields including `bankId`, `sessionId`, `gameId`, `mode`, `websocket`, `WEB_SOCKET_URL`, `SID`, `BANKID`, and `GAMEID` (`template.jsp:310-328`).
- Exposes `getLobbyPath()` and `getGamePath()` using `lobbyUrl` and `gamePath` (`template.jsp:417-422`).

No `window.gameConfig` literal was proven in the live JSP path inspected in this sprint; uploaded docs mention `window.gameConfig` in `active_template.jsp.bak`, but this live template primarily exposes `getParams()` and path helpers.

## New-Games Routing

Evidence:

- `CWStartGameAction.java:416-423` routes to new-games when `newGamesRouteEnabled`.
- `BaseStartGameAction.java:878-904` builds an `ActionRedirect` to `newGamesClientUrl` and adds:
  - `bankId`
  - `sessionId`
  - `gameId`
  - `gameIdNumeric`
  - `lang`
  - `mode`
  - `gameServerId`
  - `ngsApiUrl`
  - `gsInternalBaseUrl`
  - `ngsContract=v1`
  - optional home/cashier URL
- `BaseStartGameAction.java:917-935` resolves the new-games client URL from per-game bank properties and has a default 7001 branch for default new-games banks.
- `BankInfoCache.xml:113-142` and `BankInfoCache.xml:895-925` show new-games route, gamelist, client URL, API URL, and GS internal base URL properties for the local bank export, with URLs redacted here.

## Legacy Multiplayer Template Redirect

Evidence:

- `BaseStartGameAction.java:1023-1031` redirects legacy multiplayer flow to `/<mode>/mp/template.jsp` with `bankId`, `sessionId`, `gameId`, `lang`, `mode`, `WEB_SOCKET_URL`, and `gameServerId`.
- This is separate from new-games `/slot/v1/*` browser runtime.

## Canonical 7001 Runbook Clues

Evidence: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/GS_7001_NEWGAMES_RUNBOOK.md`

- Dedicated new-games services:
  - `new-games-api` on port `6400`, role `/slot/v1/*` bridge (`lines 10-14`).
  - `new-games-client` on port `5174`, browser client host (`lines 15-18`).
- Bank properties required to expose 7000 and 7001 include `NEW_GAMES_ROUTE_GAME_ID=7000,7001` and gamelist title/lang entries (`lines 43-51`).
- Canonical endpoint chain for 7001: `bootstrap`, `opengame`, `playround`, `resumegame`, `featureaction`, `gethistory`, `closegame` under `/slot/v1/*` (`lines 59-66`).
- The example launch URL in the runbook contains a token; it is redacted in all generated outputs.

## Real / Free / Demo / Test Mode

- BSG CW docs define authorized `mode` values as `real` and `free`.
- The 7001 source includes demo fallback/runtime controls in `GsRuntimeClient.ts:161-170`, but those are browser/runtime development paths, not BSG CW mode definitions.
- Future launch tests must separately cover REAL, FREE/guest if supported, and any internal QA/demo mode using safe fixture/session references.

## Unknowns / Blockers

- Exact Little Gangster game 8001 client URL and bank route entries do not exist yet.
- `window.gameConfig` was not verified in the live template path inspected; later GameClientBuilder must reconcile uploaded docs vs live template.
- New-games core transport implementation is imported from `@gamesv1/core-protocol`; its package root was not inspected because it was not an explicit allowed path.
- No launch tests were executed in this sprint.
