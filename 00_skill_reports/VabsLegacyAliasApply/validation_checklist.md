# VABS Legacy Alias Apply Validation Checklist

Date: 2026-05-15

- [x] `project_manifest.json` parses.
- [x] `VabsLegacyAliasApply/handoff.json` parses.
- [x] Alias apply source changes JSON parses.
- [x] Only allowed Staging files were created/modified.
- [x] `legacyAliasTypes.ts` exists.
- [x] `legacyAliasMapper.ts` exists.
- [x] `legacyAliasRoutes.ts` exists.
- [x] `legacyAliasSecurity.ts` exists.
- [x] Alias mapper maps `VIEWSESSID`.
- [x] Alias mapper maps `GAMEID`.
- [x] Alias mapper maps `LANG`.
- [x] Alias mapper maps `TIMEZONE`.
- [x] Alias mapper maps `hideClose`.
- [x] Wrong `GAMEID` is rejected/blocked.
- [x] Root alias support is implemented and documented.
- [x] Scoped alias support is implemented and documented.
- [x] Canonical new-games history routes are preserved.
- [x] No raw token/signature/private URL is emitted by alias response in targeted test.
- [x] `viewSessionId` equivalence blocker is preserved.
- [x] BO/CM acceptance remains unproven.
- [x] Durable storage remains blocked and not implemented.
- [x] Screenshot capture remains blocked and not implemented.
- [x] Video capture remains blocked and not implemented.
- [x] Release/certification flags remain false.
- [x] Targeted tests ran and passed.
- [x] Rollback plan exists.
- [x] No GameClientBuilder implementation was created.
- [x] No `Gamesv1/games/8001` package was created.
- [x] No registration artifact was generated.
- [x] No DB/Cassandra action occurred.
- [x] No wallet/API call occurred.
- [x] No donor browsing occurred.
- [x] No asset capture occurred.
- [x] No release approval occurred.
