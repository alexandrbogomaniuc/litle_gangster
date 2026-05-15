# 8001 VABS Visual History Route Apply Rollback Plan

Date: 2026-05-15

## Scope

This sprint created a Little Gangster 8001 VABS/VBA/Lasthands visual history route
foundation in Staging source only. The foundation supports deterministic replay JSON,
safe visual HTML rendering, media manifest metadata, guarded 8001 route registration,
and non-production fixture storage.

No durable DB/object storage, screenshot capture, video capture, wallet call,
registration artifact, client code, or release approval was created.

## Staging Source Files Created

- `new-games-server/src/games/little-gangster/history/historyTypes.ts`
- `new-games-server/src/games/little-gangster/history/historyPayloadBuilder.ts`
- `new-games-server/src/games/little-gangster/history/historyStorageProvider.ts`
- `new-games-server/src/games/little-gangster/history/visualReplayRenderer.ts`
- `new-games-server/src/games/little-gangster/history/mediaManifest.ts`
- `new-games-server/src/games/little-gangster/history/historySecurity.ts`
- `new-games-server/src/games/little-gangster/history/historyFixtures.ts`
- `new-games-server/src/games/little-gangster/history/historyRoutes.ts`
- `new-games-server/src/games/little-gangster/history/index.ts`
- `new-games-server/test/little-gangster/history-routes.test.ts`
- `new-games-server/test/little-gangster/visual-replay-renderer.test.ts`
- `new-games-server/test/little-gangster/history-payload-builder.test.ts`
- `new-games-server/test/little-gangster/media-manifest.test.ts`
- `new-games-server/test/little-gangster/history-security.test.ts`
- `new-games-server/test/little-gangster/history-storage-provider.test.ts`

## Staging Source Files Modified

- `new-games-server/src/index.ts`

## Rollback Steps

1. Remove the created history route foundation directory:
   `new-games-server/src/games/little-gangster/history/`.
2. Remove the six created history route tests from
   `new-games-server/test/little-gangster/`.
3. In `new-games-server/src/index.ts`, remove the
   `registerLittleGangsterHistoryRoutes` import.
4. In `new-games-server/src/index.ts`, remove the guarded
   `registerLittleGangsterHistoryRoutes(app);` registration call.
5. Re-run targeted Little Gangster lifecycle/backend adapter tests to confirm the
   previous guarded 8001 payload/lifecycle path remains intact.

## DB And Storage Rollback

No DB, Cassandra, object storage, screenshot storage, video storage, or media retention
state was created. No DB rollback is required.

## Still Blocked After Rollback Or Apply

- `durable_history_storage_unproven`
- `durable_media_storage_not_implemented`
- `screenshot_capture_not_implemented`
- `video_capture_not_implemented`
- `backoffice_cm_vabs_compatibility_unproven`
- `vabs_runtime_wallet_history_tests_missing`
- `wallet_launch_history_tests_missing`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`
