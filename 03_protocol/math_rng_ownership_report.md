# Math / RNG / Result Ownership Report

Status: server/backend-side RNG/result ownership is required, but exact 8001 owner remains blocked. Classic GS, new-games backend, a game-specific server package, GS game processor, or another current runtime component remain candidates.

## Direct Answers

### Who should generate RNG/results for Little Gangster?

Expected default: a server/backend runtime must generate authoritative real-money RNG/results. The browser client must not be the authority for real-money outcomes.

Evidence:

- 7001 browser client calls `transport.playround(...)` and receives a `PlayRoundResponse`: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/src/app/runtime/GsRuntimeClient.ts:265-293`.
- Browser presentation maps `PlayRoundResponse.presentationPayload`, not raw local RNG, into visual outcome models: `RuntimeOutcomeMapper.ts:20-28`, `RuntimeOutcomeMapper.ts:54-80`.
- `GsRuntimeClient` extracts wallet balance and runtime state from response envelopes: `GsRuntimeClient.ts:65-83`, `GsRuntimeClient.ts:215-237`.

For 8001, exact owner remains UNKNOWN/BLOCKED until current GS source/config/docs prove which runtime owns executable math/results.

### Does GS own RNG/result generation?

UNKNOWN/BLOCKED.

What is proven:

- WebGS owns launch/session bridge and internal wallet/history bridge.
- `NewGamesInternalApiServlet` handles session validation, wallet reserve, wallet settle, history write, and history read:
`[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/gs-server/game-server/web-gs/src/main/java/com/dgphoenix/casino/web/api/newgames/NewGamesInternalApiServlet.java:62-67`, `93-114`.
- It reserves/settles wallet amounts but does not show slot RNG/result generation in the inspected code: `NewGamesInternalApiServlet.java:156-220`, `224-298`.

What is not proven:

- Whether WebGS, a new-games backend, a game-specific server package, GS game processor, or another backend service generates final slot results for 8001.
- Gamesv1/Crazy Rooster/slot-browser-v1 must be treated as candidate direction evidence, not guaranteed truth.

### Does a new-games backend own RNG/result generation?

CANDIDATE/UNPROVEN.

Evidence:

- 7001 runbook says `new-games-api` is the slot contract and GS bridge for `/slot/v1/*`: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/GS_7001_NEWGAMES_RUNBOOK.md:10-18`.
- The canonical browser-facing endpoint chain is `/slot/v1/bootstrap`, `/opengame`, `/playround`, `/resumegame`, `/featureaction`, `/gethistory`, `/closegame`: `GS_7001_NEWGAMES_RUNBOOK.md:59-66`.
- `GS_NEWGAMES_DOCKER_FINALIZATION_STATUS.md` says the older 7000 lane proved `/slot/v1/*`, GS-integrated authority calls, authoritative history rows, and replay verification: `GS_NEWGAMES_DOCKER_FINALIZATION_STATUS.md:72-101`.

Blocker:

- `new-games-server/src/index.ts` was not an explicit allowed source path, so this sprint cannot prove its RNG/result implementation.

### Is there any evidence that the browser client may generate real-money results?

No release-safe evidence.

Evidence of non-release/dev math only:

- 7001 client has demo/provisional math paths: `GsRuntimeClient.ts:161-170`, `GsRuntimeClient.ts:269-272`, `GsRuntimeClient.ts:320-331`, `GsRuntimeClient.ts:402-421`.
- `provisionalMathSource.ts` imports math JSON files and generates provisional presentation hints: `provisionalMathSource.ts:1-8`, `108-181`.
- 7001 simulation script states: `Simulation only. GS/fixture runtime remains authoritative for production outcomes.`: `scripts/run-math-sim.mjs:106-114`.

Decision: do not treat browser/client RNG as real-money authority for Little Gangster.

### Where should the math package live?

Design/simulation package should live in the game project under `04_math/` first. Later integration should produce a game/runtime math package under the selected build/runtime lane, similar to 7001's `math/` folder and `game.settings.json`
references.

Evidence:

- 7001 has math package files under `Gamesv1/games/7001/math/`.
- 7001 `game.settings.json` references `runtimeTarget: slot-browser-v1` and `mathManifestPath: math/math-package-manifest.json`: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/game.settings.json:70-80`.
- 7001 client reads `mathPackageVersion` from runtime/bootstrap envelopes: `GsRuntimeClient.ts:44-52`, `GsRuntimeClient.ts:219-220`.

### Is math imported into GS during registration, or implemented as runtime code/config?

UNKNOWN for final 8001, but evidence points to runtime code/config, not simple Cassandra registration import.

Known:

- 7001 math package exists as game package files and runtime metadata, not as a proven Cassandra import.
- Cassandra/game registration summaries mention RTP/max win/display/config records, but they do not prove executable math is stored in Cassandra.
- New-games `/slot/v1/*` backend source is required to prove how math package is loaded.

Decision until proven otherwise:

- Treat math as backend/runtime logic/config consumed by the new-games runtime.
- Treat Cassandra registration as metadata, route, bank/game config, display RTP/max win, and client path registration unless source proves executable math import.

### What fields in Cassandra registration merely display RTP/MAX_WIN versus actually drive math?

UNKNOWN/BLOCKED.

Evidence:

- Suite Cassandra summary says Dragonstone/game 838 examples include RTP and max win fields: `[SKILL_SUITE_ROOT]/references/CASSANDRA_REGISTRATION_SUMMARY.md:11-12`.
- No inspected source proves those fields drive executable math.

Safe rule: GameServerRegistrar must not assume registration RTP/max win drives math. It should record display/config values and block executable math integration until the runtime loader is proven.

### What must MathModelDesigner output for later integration?

MathModelDesigner should output:

- `math_model_summary.md`
- `math_package.json`
- RTP variants for `96.0`, `94.0`, `92.0`
- paytables
- reel strips or weighted tables
- bonus/free-spin/buy-feature rules
- volatility and max-win reports
- simulation configs and seed reports
- backend/runtime integration notes naming expected runtime owner as UNKNOWN until `new-games-server` is inspected
- a machine-readable math manifest that GameClientBuilder and GameServerRegistrar can reference without claiming registration imports executable math

## Current Conclusion

MathModelDesigner can run now with limitations. It can design and simulate math, but it must not claim final runtime ownership, certified RTP, or release readiness until the new-games backend and registration pipeline are inspected and
tested.
