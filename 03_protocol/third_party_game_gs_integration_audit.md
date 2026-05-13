# Third-Party / New-Game GS Integration Audit

Status: partial, evidence-backed for launch and GS internal bridge; release runtime still blocked.

## Scope And Safety

This extension inspected only the Little Gangster project, the skill suite, uploaded/generated references, and explicit source paths listed by the user. It did not launch a browser, investigate donor gameplay, capture assets, call wallet
endpoints, build code, generate math, generate CQL, or execute DB/Cassandra actions.

## Direct Answers

### What launch URL should a new game use in local/dev?

Use the GS launch route, not a direct static client URL.

Evidence:

- The Crazy Rooster handoff says operator-flow testing should use the GS launch URL because it mints a fresh SID : [REDACTED_FIXTURE]
- The CW action source identifies `/cwstartgamev2.do` as the Struts launch action with `gameId`, `mode`, `token`, and `bankId`:
`[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/cwv3/CWStartGameAction.java:54-58`.
- `BaseStartGameAction` can also build a `/cwstartgamev2.do` URL for incomplete-round relaunch:
`[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/actions/enter/game/BaseStartGameAction.java:1107-1122`.

Sanitized local/dev pattern for Little Gangster, pending 8001 registration:

```text
/startgame?bankId=6275&subCasinoId=507&gameId=8001&mode=real&token = [REDACTED_FIXTURE]
```

Equivalent BSG/CW launch action pattern, if the environment exposes it directly:

```text
/cwstartgamev2.do?bankId=6275&gameId=8001&mode=real&token = [REDACTED_FIXTURE]
```

Exact 8001 launch URL remains BLOCKED until GameServerRegistrar creates/validates the 8001 route/config and a local ignored test token reference is available.

### Is it `cwstartgamev2.do`, `free/mp/template.jsp`, a new-games route, or a combination?

It is a combination:

- `cwstartgamev2.do` is the BSG/Common Wallet launch and GS session-routing entry point.
- If bank/game route config enables new-games, GS redirects to a new-games client URL with runtime params.
- If new-games route is not enabled and the game is a legacy multiplayer game, GS redirects to `/<mode>/mp/template.jsp`.

Evidence:

- `CWStartGameAction` parses raw game id, resolves `newGamesRouteEnabled`, reads mode/lang, and calls Common Wallet authentication: `CWStartGameAction.java:99-108`.
- If `newGamesRouteEnabled`, it calls `getNewGamesForward(...)` and returns that redirect: `CWStartGameAction.java:416-435`.
- Legacy route building points to `/<mode>/mp/template.jsp` and adds `WEB_SOCKET_URL`: `BaseStartGameAction.java:1019-1032`.

### What happens after `cwstartgamev2.do`?

Evidence-backed flow:

1. Load bank config from `BankInfoCache`: `CWStartGameAction.java:81-84`.
2. Parse `gameId`, decide whether the bank/game is a new-games route, resolve mode/lang: `CWStartGameAction.java:99-103`.
3. Authenticate externally through Common Wallet token : [REDACTED_FIXTURE]
4. Resolve or create GS session info/SID : [REDACTED_FIXTURE]
5. Shadow launch/session/gameplay/protocol route decisions: `CWStartGameAction.java:319-393`.
6. Redirect to new-games client if route is enabled: `CWStartGameAction.java:416-435`.
7. Otherwise continue legacy/MQ route and eventually legacy template: `CWStartGameAction.java:438-445` and `BaseStartGameAction.java:1019-1032`.

### Does GS redirect to template.jsp, new-games-client, or a game-specific client route?

Both are supported, selected by route/config:

- New-games: `BaseStartGameAction.getNewGamesForward(...)` redirects to a new-games client URL, including per-game URL overrides such as `NEW_GAMES_CLIENT_URL_<gameId>` if present: `BaseStartGameAction.java:878-940`.
- Legacy: `BaseStartGameAction.getMultiplayerForward(...)` redirects to `/<mode>/mp/template.jsp`: `BaseStartGameAction.java:1019-1032`.
- Crazy Rooster handoff says 7001 should redirect to the game-specific client on port 5175, while generic `NEW_GAMES_CLIENT_URL` remains the Plinko/general client: `CRAZY_ROOSTER_7001_FRESH_AGENT_HANDOFF_20260505.md:40-68`.

For Little Gangster 8001, a game-specific client route is expected but not proven until `NEW_GAMES_CLIENT_URL_8001` or equivalent route/config is generated and validated.

### Which parameters are passed to the client?

New-games redirect params:

- `bankId`
- `sessionId`
- `gameId`
- `gameIdNumeric`
- `lang`
- `mode`
- `gameServerId`
- `ngsApiUrl`
- `gsInternalBaseUrl`
- `ngsContract`
- optional `homeUrl`
- optional cashier URL

Evidence: `BaseStartGameAction.java:893-914`.

Legacy template params/helpers:

- `bankId`
- `sessionId`
- `gameId`
- `lang`
- `mode`
- `WEB_SOCKET_URL`
- `GAMESERVERID`
- path helpers and `getParams()`

Evidence: `template.jsp:250-330`.

### Which parameters are mandatory for the client?

For the 7001 new-games browser runtime:

- `sessionId` or `SID` is mandatory for GS runtime; without it the client throws unless demo fallback is explicitly requested: `GsRuntimeClient.ts:96-130` and `GsRuntimeClient.ts:158-171`.
- `gameIdNumeric` or `gameId` selects the game id, defaulting to 7001 only in the 7001 package: `GsRuntimeClient.ts:105-120`.
- `bankId`, `ngsApiUrl`, and `gsInternalBaseUrl` are consumed by the runtime/transport config: `GsRuntimeClient.ts:173-199`.
- `ngsContract=v1` is passed by GS redirect: `BaseStartGameAction.java:902-904`.

For 8001, defaults must be updated. A 7001 `DEFAULT_GAME_ID` is not valid for Little Gangster.

### Which parameters are wallet/session-only and should not be handled by visual client logic?

- `token`: used by `CWStartGameAction` for Common Wallet authentication and must not be visual-client business logic. Evidence: `CWStartGameAction.java:106-108`; `GsRuntimeClient.ts:122` only reads it into transport config if present.
- raw PASS_KEY values: bank/server wallet configuration only; never client logic or logs. PASS_KEY constants only were verified at `BankInfo.java:167`, `BankInfo.java:178`, and `BankInfo.java:258`.
- `sessionId`/`SID`: runtime/session identifier, not visual logic.
- `bankId`, `gameServerId`, `gsInternalBaseUrl`, `ngsApiUrl`: routing/runtime integration config.

## New-Games Internal GS Bridge

The active GS source contains a servlet for internal new-games API bridge calls:

- `NewGamesInternalApiServlet` says it is an internal API used by new-games runtime and intentionally serves non-`.do` endpoints:
`[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/web/api/newgames/NewGamesInternalApiServlet.java:54-58`.
- It is mapped in WebGS at `/gs-internal/newgames/v1/*`: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/webapp/WEB-INF/web.xml:164-170`.
- It exposes session validation, wallet reserve, wallet settle, history write, and history read paths: `NewGamesInternalApiServlet.java:62-67` and `NewGamesInternalApiServlet.java:93-114`.

Important boundary: this servlet proves a GS bridge for session/wallet/history. It does not prove that WebGS itself generates slot RNG/results.

## Open Release Runtime Blocker

The 7001 runbook says `new-games-api` is the slot contract and GS bridge for `/slot/v1/*`: `GS_7001_NEWGAMES_RUNBOOK.md:10-18` and `GS_7001_NEWGAMES_RUNBOOK.md:59-66`.

The actual `new-games-server` source path is referenced in 7001 docs, but it was not an explicit allowed source root in this sprint. Therefore, the final player-release-ready `/slot/v1/*` implementation remains BLOCKED until the user
provides/authorizes that exact root.
