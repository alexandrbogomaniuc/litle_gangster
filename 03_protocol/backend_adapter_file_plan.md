# Backend Adapter File Plan

Status: PATCH_READY_PLAN_NOT_APPLIED.

No implementation files were created in this sprint.

## Recommended Future Files

| Future file | Purpose | Evidence label |
|---|---|---|
| `new-games-server/src/games/little-gangster/resultTypes.ts` | Type definitions for authoritative v0.3 result input and backend-owned metadata. | RECOMMENDED |
| `new-games-server/src/games/little-gangster/presentationPayload.ts` | Convert v0.3 result into generic presentation fields plus `gamePayload`. | RECOMMENDED |
| `new-games-server/src/games/little-gangster/statePersistence.ts` | Map v0.3 state persistence into runtime restore/state records. | RECOMMENDED |
| `new-games-server/src/games/little-gangster/historyMapper.ts` | Serialize/deserialize Lasthand/history/VABS-friendly render snapshots. | RECOMMENDED |
| `new-games-server/src/games/little-gangster/fixtures.ts` | Load or reference strict non-production fixtures for tests only. | RECOMMENDED_NON_PRODUCTION |
| `new-games-server/src/games/little-gangster/adapter.ts` | Compose input, presentation payload, envelope, persistence, and history mapping. | RECOMMENDED |
| `new-games-server/test/little-gangster/adapter.test.ts` | Unit tests for all 24 strict fixture outputs. | REQUIRED_TEST |
| `new-games-server/test/little-gangster/schema.test.ts` | Schema validation tests against patched response schemas. | REQUIRED_TEST |
| `new-games-server/test/little-gangster/history-recovery.test.ts` | Reconnect/history/Lasthand payload tests. | REQUIRED_TEST |
| `new-games-server/src/index.ts` | Add a guarded 8001 branch that calls the adapter after implementation approval. | REQUIRED_INTEGRATION |

## Explicit Non-Targets

- Do not create `Gamesv1/games/8001` until separately approved.
- Do not move fixture JSON into production source.
- Do not place production RNG/result generation in browser/client code.
- Do not add registration, DB, wallet-live, or release code in the adapter patch.

