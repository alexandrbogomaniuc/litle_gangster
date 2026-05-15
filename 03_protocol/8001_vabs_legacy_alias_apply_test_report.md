# 8001 VABS Legacy Alias Apply Test Report

Date: 2026-05-15

## Targeted Tests

Command:

```sh
npx tsx --test test/little-gangster/vabs-legacy-alias-routes.test.ts test/little-gangster/vabs-legacy-alias-mapper.test.ts
test/little-gangster/vabs-legacy-alias-security.test.ts test/little-gangster/history-routes.test.ts
test/little-gangster/visual-replay-renderer.test.ts test/little-gangster/history-security.test.ts
```

Working directory:

```text
[STAGING_SOURCE_ROOT_REDACTED]/new-games-server
```

Result: pass.

Summary:

- Tests: 9
- Pass: 9
- Fail: 0

## Coverage Confirmed

- Alias mapper maps `VIEWSESSID`.
- Alias mapper maps `GAMEID`.
- Alias mapper maps `LANG`.
- Alias mapper maps `TIMEZONE`.
- Alias mapper maps `hideClose`.
- Wrong `GAMEID` is blocked.
- Root alias support is represented.
- Scoped alias support is represented.
- Alias visual response can be built through the existing visual history foundation.
- Canonical new-games history route definitions are preserved.
- Unsafe alias input is rejected or stripped.
- Alias response includes no raw token/signature/private URL patterns.
- `view_session_id_equivalence_unproven_for_8001` blocker is preserved.
- BO/CM acceptance remains untested.
- Durable storage remains blocked and not implemented.
- Release/certification flags remain false.

## Typecheck Status

Fast-lane targeted `tsx --test` execution passed.

Full repository typecheck was not run in this sprint. This checkout still does not expose
a local TypeScript compiler in `new-games-server` (`node_modules/.bin` is absent), and
no dependency installation was performed.
