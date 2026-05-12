# Source Patch Test Plan

Status: TEST_PLAN_ONLY_NO_TESTS_RUN

## Future Commands

From `Gamesv1` workspace root:

```bash
node --experimental-transform-types tests/contract/browser-runtime.contract.test.ts
node --experimental-transform-types tests/game/presentation-mapper.test.ts
corepack pnpm run test:contract
corepack pnpm run test:template
```

From `new-games-server` root after any server patch:

```bash
npm run build
npm test
```

For 7001 compatibility after mapper/schema changes:

```bash
corepack pnpm --filter @games/7001 build
```

## Required Future Tests

| Test | Location | Expected result | Evidence label |
|---|---|---|---|
| Schema accepts valid `presentationPayload.gamePayload`. | Browser runtime contract test and JSON schema fixture. | Pass after patch. | REQUIRED_SCHEMA_TEST |
| Schema rejects malformed `gamePayload` missing `gameKey`. | Browser runtime contract test. | Fail validation. | REQUIRED_NEGATIVE_TEST |
| Schema rejects malformed `gamePayload` missing `schemaVersion`. | Browser runtime contract test. | Fail validation. | REQUIRED_NEGATIVE_TEST |
| Schema rejects non-object `gamePayload.payload`. | Browser runtime contract test. | Fail validation if `JsonObjectSchema` is selected. | REQUIRED_NEGATIVE_TEST |
| Existing response fixtures validate unchanged. | Browser runtime contract test. | Pass. | REQUIRED_BACKWARD_COMPATIBILITY |
| UI-kit mapper preserves `gamePayload` untouched. | Presentation mapper test. | Pass. | REQUIRED_MAPPER_TEST |
| 7001 existing behavior does not break. | 7001 build/tests. | Pass. | REQUIRED_COMPATIBILITY_TEST |
| New-games-server emits `gamePayload` for controlled fixture when enabled. | new-games-server e2e test. | Pass after server patch. | REQUIRED_SERVER_TEST |
| Wallet/accounting leakage into `gamePayload` is rejected by policy/test. | new-games-server test or adapter test. | Pass. | SAFETY_GUARD |
| Browser authority fields are not accepted from client request. | server/adapter test. | Pass. | AUTHORITY_GUARD |

## Tests Not Run This Sprint

No Staging tests were run because no Staging source patch was applied.
