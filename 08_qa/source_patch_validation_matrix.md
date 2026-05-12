# Source Patch Validation Matrix

Status: TEST_PLAN_ONLY

| Validation | Command or method | Required before source patch accepted |
|---|---|---|
| JSON schema contract test | `node --experimental-transform-types tests/contract/browser-runtime.contract.test.ts` | Yes |
| Presentation mapper test | `node --experimental-transform-types tests/game/presentation-mapper.test.ts` | Yes |
| Gamesv1 contract suite | `corepack pnpm run test:contract` | Yes |
| Gamesv1 template suite | `corepack pnpm run test:template` | Yes |
| 7001 compatibility build | `corepack pnpm --filter @games/7001 build` | Yes if 7001 dependency graph is affected |
| new-games-server build | `npm run build` | Yes after server patch |
| new-games-server e2e tests | `npm test` | Yes after server patch |
| No wallet/accounting leakage | Review/test `gamePayload` fixture and server output | Yes |
| Browser renderer-only boundary | Adapter/client tests | Yes before GameClientBuilder implementation |

## Source Patch Apply Results - 2026-05-12

| Validation | Result | Evidence label |
|---|---|---|
| JSON schema parse | Passed | PROVEN |
| JSON schemas accept optional `gamePayload` | Passed | PROVEN |
| JSON schemas reject unknown top-level presentation fields | Passed | PROVEN |
| Core Zod schema accepts `gamePayload` | Passed | PROVEN |
| Core Zod schema keeps parent strictness | Passed | PROVEN |
| Browser runtime contract tests | Passed, 10 passed / 0 failed | PROVEN |
| Presentation mapper tests | Passed with local navigator shim, 4 passed / 0 failed | PROVEN_WITH_ENV_SHIM |
| UI-kit preserves `gamePayload` | Passed | PROVEN |
| Root TypeScript typecheck | Failed on existing config issues | PRE_EXISTING_CONFIG_FAILURE |
| UI-kit TypeScript typecheck | Failed on existing config/rootDir issues | PRE_EXISTING_CONFIG_FAILURE |
| New-games-server tests | Not run; server source not patched | NOT_RUN_NOT_MODIFIED |
