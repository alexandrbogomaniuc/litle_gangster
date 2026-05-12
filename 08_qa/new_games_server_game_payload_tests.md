# New-Games-Server gamePayload Tests

Status: TEST_PLAN_ONLY

## Required Tests After Server Patch

- Controlled server path emits `presentationPayload.gamePayload` with `gameKey`, `schemaVersion`, and object payload.
- 7001 playround/featureaction still emits existing behavior until explicitly migrated.
- 8001 branch remains absent or disabled until runtime owner approval.
- Server ignores any client request attempt to provide authoritative `gamePayload` outcome data.
- Wallet/accounting values remain in `wallet` and round fields, not inside `gamePayload`.
- History/recovery response can store or reconstruct the render payload snapshot when approved.

## Commands Later

```bash
npm run build
npm test
```

## Source Patch Apply Results - 2026-05-12

Evidence label: NOT_RUN_NOT_MODIFIED

No server tests were run because `new-games-server/src/index.ts` was not modified. The existing runtime-envelope
helper already accepts record-shaped `presentationPayload`, and this sprint did not approve an 8001 emission branch
or backend adapter implementation.

Required future server tests remain open for the backend adapter implementation sprint.
