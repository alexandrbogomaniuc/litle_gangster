# Backend Adapter Target Location Decision

Status: DECISION_READY_FOR_APPROVAL_NOT_APPLIED.

## Recommended Target

Recommended future target:

```text
[STAGING_ROOT]/platform-source/platform/new-games-server/src/games/little-gangster/
```

Recommended integration point:

```text
[STAGING_ROOT]/platform-source/platform/new-games-server/src/index.ts
```

Evidence label: PROVEN_CANDIDATE.

The existing `new-games-server/src/index.ts` owns `/slot/v1/playround`, `/slot/v1/featureaction`,
`/slot/v1/resumegame`, `/slot/v1/gethistory`, `/slot/v1/closegame`, and the shared `runtimeEnvelope(...)` helper.
It already emits a 7001-specific presentation payload branch. That makes it the most direct future target for an
8001 payload emission branch.

## Alternative Target

Alternative future target:

```text
[STAGING_ROOT]/platform-source/platform/Gamesv1/games/8001/src/app/runtime/
```

Evidence label: NOT_FOUND_TODAY.

Targeted inspection found no `Gamesv1/games/8001` package. This path should not be created until a future user
approves a source implementation sprint and the team decides whether Little Gangster needs a Gamesv1 browser package.

## Split Recommendation

The future adapter should be split into four backend-owned concerns:

| Concern | Recommended location | Evidence label |
|---|---|---|
| Math/result owner module | future runtime package or server module | REQUIRED_NOT_PROVEN |
| Presentation payload adapter | `new-games-server/src/games/little-gangster/presentationPayload.ts` | RECOMMENDED |
| Persistence/history mapper | `new-games-server/src/games/little-gangster/statePersistence.ts` and `historyMapper.ts` | RECOMMENDED |
| Test fixture bridge | `new-games-server/src/games/little-gangster/fixtures.ts` | RECOMMENDED_NON_PRODUCTION_ONLY |

## 7001 Reference Boundary

`Gamesv1/games/7001/src/app/runtime/RuntimeOutcomeMapper.ts` and
`Gamesv1/games/7001/src/app/runtime/provisionalMathSource.ts` are reference-only. They show how a game can adapt
math/presentation hints, but they do not prove Little Gangster runtime ownership.

