# Client Runtime Protocol Notes

Status: partial

## Verified Frontend Architecture Evidence

Uploaded documentation says the legacy/template client stack uses:

- PIXI.js Legacy
- Vue.js 2.6
- Webpack 4
- Babel
- Mustache
- Node.js v16.20.2
- JSP-style launch template with `version.json`, `validator.js`, and `game.js`

Live explicit source paths add a newer new-games lane:

- `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/new-games-client/package.json` uses Vite + TypeScript with `pixi.js`.
- `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/package.json` uses Vite, TypeScript, `pixi.js` v8, `@gamesv1/core-protocol`, `@gamesv1/pixi-engine`, and `@gamesv1/ui-kit`.
- `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/premium-slot/package.json` shows the same Vite/pixi v8-style template lane.

Conclusion: later GameClientBuilder must not assume a single stack. It must reconcile the uploaded legacy documentation with the explicit new-games 7001/premium-slot source path selected for this project.

## Launch Param Intake

For actual 7001 runtime:

- `GsRuntimeClient.ts:96-120` reads `sid`/`SID`/`sessionId`, `bankId`, `gameIdNumeric`/`gameId`, `ngsApiUrl`, `gsInternalBaseUrl`, token, player id, language, and bootstrap refs.
- `DEFAULT_GAME_ID` is `7001` in `GsRuntimeClient.ts:20-22`.
- `CONTRACT_VERSION` is `slot-browser-v1` in `GsRuntimeClient.ts:20`.

For portal/preloader client:

- `new-games-client/src/main.ts` routes `gameId=7001` to a Crazy Rooster client URL and passes existing query params onward.
- The portal client also reads `sid`/`SID`/`sessionId`, `bankId`, `gameIdNumeric`/`gameId`, `ngsApiUrl`, and `gsInternalBaseUrl`.

## Browser To GS Runtime Operations

Verified from 7001 runtime:

- `bootstrap()` creates a `GS_HTTP_RUNTIME` transport with `baseUrl`, `token`, `bankId`, `playerId`, `gameId`, `sessionId`, `gsInternalBaseUrl`, language, and `internalClientCode` (`GsRuntimeClient.ts:173-199`).
- It calls `transport.bootstrap(...)` with `contractVersion`, `sessionId`, `gameId`, and `bootstrapRef` (`GsRuntimeClient.ts:201-211`).
- It then calls `transport.opengame(...)` with request counter, current state version, selected bet/feature choice, `idempotencyKey`, and `clientOperationId` (`GsRuntimeClient.ts:227-236`).
- `playround(...)` calls `transport.playround(...)` with selected bet, request counter, idempotency key, client operation id, and current state version (`GsRuntimeClient.ts:265-290`).
- `gethistory(...)` calls `transport.gethistory(...)` with `contractVersion`, `sessionId`, request counter, and history query (`GsRuntimeClient.ts:296-313`).
- `featureaction(...)` calls `transport.featureaction(...)` with selected bet/feature choice, request counter, idempotency key, and current state version (`GsRuntimeClient.ts:316-355`).
- `close(...)` calls `transport.closegame(...)` with close reason, selected bet/feature nulls, request counter, idempotency key, and current state version (`GsRuntimeClient.ts:361-392`).

Runbook corroborates the canonical endpoint chain as `/slot/v1/bootstrap`, `/slot/v1/opengame`, `/slot/v1/playround`, `/slot/v1/resumegame`, `/slot/v1/featureaction`, `/slot/v1/gethistory`, `/slot/v1/closegame`.

## Runtime State / Idempotency Clues

Verified from 7001 source:

- Browser runtime increments `requestCounter` for open/play/feature/close.
- Browser runtime sends `idempotencyKey` and `clientOperationId`.
- Browser runtime stores `balanceMinor`, request counter, state version, bootstrap ref, resume ref, unfinished round, and last round id via `SessionRuntimeStore`.
- `ConfigManager.ts` targeted evidence marks runtime policies for request counter, idempotency key, client operation id, current state version, and unfinished round restore.

## Balance / Result Display Clues

Verified from 7001 runtime:

- Runtime extracts wallet balance from `response.wallet.balanceMinor`.
- Runtime extracts round id from `response.round.roundId`.
- Runtime maps `presentationPayload` through stores/mappers before visual rendering.

These are browser/GS runtime concepts and do not replace the BSG CW XML wallet fields.

## Demo / Provisional Runtime Boundary

Verified from 7001 source:

- If provisional math is requested or no session id is present with demo requested, `GsRuntimeClient` falls back to demo runtime (`GsRuntimeClient.ts:161-170`).
- Demo/provisional flows are useful development references but are not release proof for Little Gangster 8001.

## Unknowns / Blockers

- The actual `@gamesv1/core-protocol` transport implementation was not inspected because its package root was not explicitly allowed for this sprint.
- The Game Server implementation behind `/slot/v1/*` was not fully mapped in this sprint.
- Exact message schemas for `BootstrapResponse`, `OpenGameResponse`, `PlayRoundResponse`, `FeatureActionResponse`, and history rows remain partial until the core protocol package and GS API implementation are provided as explicit paths.
- RNG/result ownership is unknown for future 8001 until MathModelDesigner and GameClientBuilder provide final math/runtime integration evidence.
