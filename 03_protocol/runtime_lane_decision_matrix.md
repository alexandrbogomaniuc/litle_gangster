# Runtime Lane Decision Matrix

Status: new-games lane is the strongest candidate; release-ready lane is not fully proven for 8001.

## Decision Summary

Little Gangster should target the new-games `slot-browser-v1` / HTTP runtime lane as the best supported candidate, with limits. It should not target the legacy JSP/WebSocket/PIXI-Vue-Webpack lane unless the user explicitly changes direction
after GameClientBuilder review.

Reason: explicit 7001/premium-slot sources use Vite, Pixi v8, `@gamesv1/core-protocol`, `GS_HTTP_RUNTIME`, and `slot-browser-v1`, and the GS launch code routes configured game ids to new-games client URLs.

## Lane Matrix

| Lane | Evidence found | Files inspected | Required client files | Required server endpoints | Required GS registration/config | Blockers | Confidence |
|---|---|---|---|---|---|---|---|
| A. Legacy JSP/WebSocket/PIXI-Vue-Webpack | Uploaded docs describe the legacy stack; legacy `template.jsp` reads bank/session/game params, loads `version.json`, `validator.js`, `game.js`, and exposes `getParams()`; `BaseStartGameAction`
builds `/<mode>/mp/template.jsp` with `WEB_SOCKET_URL`. | `template.jsp:52-114`, `template.jsp:250-330`, `BaseStartGameAction.java:1019-1032`; suite client architecture summary. | `version.json`, `validator.js`, `game.js`, legacy HTML5
folder from `swfLocation`. | legacy `/websocket/mplobby` plus MQ/game servlet route. | `BaseGameInfoTemplate`/game info with `servlet`, `swfLocation`, possibly `gsClassName`; bank/game records. | Not proven as the intended lane for
7001-style new slot; uploaded docs conflict with explicit 7001 source lane. | Medium for legacy existence; Low for Little Gangster fit. |
| B. New-games `slot-browser-v1` / HTTP runtime | 7001 package imports `@gamesv1/core-protocol`; `GsRuntimeClient` uses `CONTRACT_VERSION = slot-browser-v1`; transport mode `GS_HTTP_RUNTIME`; runbook names `/slot/v1/*`; GS redirects
configured game ids to new-games client URL with `ngsApiUrl`, `gsInternalBaseUrl`, `ngsContract=v1`; WebGS exposes internal bridge `/gs-internal/newgames/v1/*`. | `Gamesv1/games/7001/package.json:16-27`; `premium-slot/package.json:12-23`;
`GsRuntimeClient.ts:1-23`, `96-130`, `173-237`, `265-392`; `GS_7001_NEWGAMES_RUNBOOK.md:10-18`, `59-66`; `BaseStartGameAction.java:878-940`; `WEB-INF/web.xml:164-170`; `NewGamesInternalApiServlet.java:54-67`. | Game-specific Vite/Pixi v8
client, `GsRuntimeClient.ts`, runtime mappers, `game.settings.json`, math package files, approved assets, package build. | Browser-facing `new-games-api` `/slot/v1/bootstrap`, `/opengame`, `/playround`, `/resumegame`, `/featureaction`,
`/gethistory`, `/closegame`; WebGS internal `/gs-internal/newgames/v1/session/validate`, `/wallet/reserve`, `/wallet/settle`, `/history/write`, `/history/read`. | Bank 6275 route properties include `NEW_GAMES_ROUTE_GAME_ID`,
`NEW_GAMES_CLIENT_URL`, `NEW_GAMES_API_URL`, `NEW_GAMES_GS_INTERNAL_BASE_URL`; 8001 needs route/client/API config and game metadata. | `new-games-server` source not inspected; `@gamesv1/core-protocol` package root not inspected; 8001
route/config not generated; 7001 final proof pending in docs. | High as target candidate; Medium for release readiness. |
| C. Another lane | No evidence for another production lane for this project. | Targeted searches found legacy and new-games lanes only. | Unknown. | Unknown. | Unknown. | No evidence. | Low. |
| D. Unknown / blocked | Final player-release-ready 8001 lane remains blocked until new-games server/core protocol and 8001 config are inspected/generated. | Project protocol blockers and source docs. | Unknown final 8001 package until
build skill. | Unknown exact 8001 server runtime until `new-games-server` is inspected. | Unknown exact 8001 registration. | `new_games_server_source_path_missing`, `core_protocol_package_not_inspected`, `game_8001_registration_missing`,
`scn_serializer_missing`. | High that blockers exist. |

## Lane Decision For Little Gangster

Decision: use Lane B, new-games `slot-browser-v1` / HTTP runtime, as the planning lane.

Limits:

- This is not a release approval.
- GameClientBuilder must not copy 7001 blindly.
- GameClientBuilder must inspect/verify the approved target source lane when it runs.
- GameServerRegistrar is blocked until 8001 registration and rollback artifacts can be generated safely.
- WalletAndLaunchTester is blocked until a local ignored secret/fixture strategy and runtime endpoints exist.

## Why Not Legacy Lane As Default?

Legacy lane exists and is documented, but the explicit 7001 and premium-slot source paths use the new Vite/Pixi v8 lane:

- 7001 dependencies include `@gamesv1/core-protocol`, `@gamesv1/pixi-engine`, `@gamesv1/ui-kit`, and `pixi.js` v8: `Gamesv1/games/7001/package.json:16-27`.
- Premium-slot shows the same new-games dependency pattern: `Gamesv1/games/premium-slot/package.json:12-23`.
- The runtime client is built around `GS_HTTP_RUNTIME`, not the legacy websocket lobby: `GsRuntimeClient.ts:173-199`.

## Why Not 7001 As Blind Template?

7001 is useful but not enough by itself:

- Handoff says 7001 route should use game-specific client 5175 and warns not to use the general Plinko client as Crazy Rooster truth: `CRAZY_ROOSTER_7001_FRESH_AGENT_HANDOFF_20260505.md:60-68`, `163-168`.
- 7001 final status says proof is still pending and Docker was unavailable for proof capture: `GS_7001_FINAL_STATUS.md:24-39`.
- 7001 math/config is Crazy Rooster-specific and cannot become Little Gangster math without MathModelDesigner.

Recommendation for future GameClientBuilder: use premium-slot/new-games lane as architecture base and 7001 as a concrete integration reference, not a copy source of truth. Do not use legacy Dragonstone-style docs as the client runtime lane,
but keep them as Cassandra/config registration evidence.
