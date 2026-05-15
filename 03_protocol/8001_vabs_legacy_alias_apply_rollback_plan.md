# 8001 VABS Legacy Alias Apply Rollback Plan

Date: 2026-05-15

## Scope

This sprint implemented a narrow Little Gangster 8001 legacy VABS alias foundation in
Staging source. The alias maps sanitized legacy-style parameters into the existing 8001
visual history route foundation.

No durable history storage, durable media storage, screenshot capture, video capture,
wallet call, DB/Cassandra action, client code, registration artifact, BO/CM call,
certification, or release approval was created.

## Staging Source Files Created

- `new-games-server/src/games/little-gangster/history/legacyAliasTypes.ts`
- `new-games-server/src/games/little-gangster/history/legacyAliasMapper.ts`
- `new-games-server/src/games/little-gangster/history/legacyAliasRoutes.ts`
- `new-games-server/src/games/little-gangster/history/legacyAliasSecurity.ts`
- `new-games-server/test/little-gangster/vabs-legacy-alias-routes.test.ts`
- `new-games-server/test/little-gangster/vabs-legacy-alias-mapper.test.ts`
- `new-games-server/test/little-gangster/vabs-legacy-alias-security.test.ts`

## Staging Source Files Modified

- `new-games-server/src/games/little-gangster/history/index.ts`
- `new-games-server/src/index.ts`

## Rollback Steps

1. Remove the four alias source files from
   `new-games-server/src/games/little-gangster/history/`.
2. Remove the three alias test files from `new-games-server/test/little-gangster/`.
3. In `new-games-server/src/games/little-gangster/history/index.ts`, remove alias exports
   for types, mapper, security helpers, and route registration.
4. In `new-games-server/src/index.ts`, remove the
   `registerLittleGangsterLegacyAliasRoutes` import and registration call.
5. Re-run targeted canonical history tests to confirm `/slot/v1/8001/history/...` routes
   remain unchanged.

## DB And Storage Rollback

No DB, Cassandra, object storage, screenshot storage, video storage, or durable history
state was created. No DB rollback is required.
