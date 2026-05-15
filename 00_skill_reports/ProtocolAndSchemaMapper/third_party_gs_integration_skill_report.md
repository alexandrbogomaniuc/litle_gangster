# ProtocolAndSchemaMapper Third-Party GS Integration Extension Report

Date: 2026-05-08T15:39:47+01:00

## Sprint Scope

Run ProtocolAndSchemaMapper and SprintReporter only for a focused Stage 4 retry/extension. The goal was to double-check documentation and explicit
source paths for third-party/new game development, GS linking, runtime lane, math/RNG ownership, Cassandra/config registration, wallet boundary, and
player-release readiness.

## Actions Performed

- Read requested suite and project rules.
- Read existing Stage 4 protocol outputs and handoff.
- Inspected only explicit source paths listed by the user or project manifest.
- Performed targeted searches only for allowed terms inside explicit source roots.
- Extended the protocol mapping with:
  - third-party/new-game GS linking audit
  - runtime lane decision matrix
  - Crazy Rooster template validity review
  - math/RNG/result ownership report
  - registration evidence map
  - player-release blocker decision table
  - updated machine-readable protocol summary
- Updated project manifest, assumptions, decisions, and handoff.
- Did not run browser, donor research, asset inventory, math design, client build, registration generation, wallet tests, release audit, or
  DB/Cassandra actions.

## Key Evidence

- `CWStartGameAction.java:99-108` proves launch reads game/mode/lang and authenticates through Common Wallet token.
- `CWStartGameAction.java:416-435` proves configured games can redirect to the new-games module.
- `BaseStartGameAction.java:878-940` proves new-games redirect params and per-game client URL lookup.
- `BaseStartGameAction.java:1019-1032` proves legacy template redirect and websocket params.
- `template.jsp:250-330` proves legacy `version.json`, `validator.js`, `game.js`, and `getParams()` flow.
- `GsRuntimeClient.ts:96-130` proves browser launch param intake.
- `GsRuntimeClient.ts:173-237` proves `GS_HTTP_RUNTIME` bootstrap/open flow.
- `GsRuntimeClient.ts:265-392` proves play/history/feature/close calls use runtime transport with counters/idempotency.
- `NewGamesInternalApiServlet.java:54-67` and `WEB-INF/web.xml:164-170` prove WebGS internal new-games bridge exists at `/gs-internal/newgames/v1/*`.
- `NewGamesInternalApiServlet.java:156-298` and `635-690` prove WebGS bridge reserves/settles wallet amounts through wallet client calls.
- `GS_7001_NEWGAMES_RUNBOOK.md:10-18`, `59-66` identifies `new-games-api` and `/slot/v1/*` as the browser-facing slot contract lane.
- `GS_7001_FINAL_STATUS.md:20-39` keeps 7001 release proof pending.
- `BankInfoCache.xml:895-925` proves bank 6275 new-games route/client/API/internal URL properties for 7000/7001.

## Answers Reached

- Third-party/new games should launch through GS launch (`/startgame` wrapper or `/cwstartgamev2.do`) and then redirect to the selected client lane.
- Little Gangster should plan for the new-games `slot-browser-v1` / HTTP runtime lane with blockers.
- Crazy Rooster 7001 is a useful integration reference, not a direct release-ready template for Little Gangster.
- The browser client must not be authoritative for real-money RNG/results.
- WebGS internal bridge is proven for session/wallet/history, but not for slot RNG/result generation.
- A separate new-games backend likely owns `/slot/v1/*` outcomes, but source proof is blocked until `new-games-server` is explicitly available.
- MathModelDesigner can run next with limitations.
- GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, and release-to-players remain blocked.

## Safety Results

- Raw PASS_KEY values stored: no.
- Raw test tokens stored: no.
- Full donor URL/token persisted: no.
- DB/Cassandra actions: no.
- Browser work: no.
- Asset capture: no.
- Later skills run: no.

## Trust Level

Partially trustworthy. Launch, routing, WebGS bridge, and new-games client-lane evidence are backed by source lines. Final release/runtime ownership
remains partial because `new-games-server` and `@gamesv1/core-protocol` package roots were not inspected.
