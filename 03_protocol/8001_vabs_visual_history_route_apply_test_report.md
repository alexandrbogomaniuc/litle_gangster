# 8001 VABS Visual History Route Apply Test Report

Date: 2026-05-15

## Targeted Tests

Command:

```sh
npx tsx --test test/little-gangster/history-routes.test.ts test/little-gangster/visual-replay-renderer.test.ts
test/little-gangster/history-payload-builder.test.ts test/little-gangster/media-manifest.test.ts test/little-gangster/history-security.test.ts
test/little-gangster/history-storage-provider.test.ts
```

Working directory:

```text
[STAGING_SOURCE_ROOT_REDACTED]/new-games-server
```

Result: pass.

Summary:

- Tests: 6
- Pass: 6
- Fail: 0

## Coverage Confirmed

- JSON round replay response can be built.
- JSON session replay response can be built.
- Whole-session replay flag is represented.
- Visual HTML/render response can be built.
- Media manifest can be built.
- `screenshotRefs` exists and is empty by default.
- `videoRefs` exists and is empty by default.
- Default evidence mode is `deterministic_replay_only`.
- In-game History route shape is represented.
- Backoffice/CM route shape is represented.
- `mathProfileId` is present.
- `bonusBuyCostMultiplier` is present.
- `declaredBfRtpTarget` is present.
- `actionSequence` is present.
- `walletAccountingRefs` placeholder is present.
- Fixture/render output is checked for raw token, signature, and private URL leakage.
- Fixture data is marked non-production.
- Durable storage remains blocked.
- Screenshot capture remains blocked.
- Video capture remains blocked.
- Release and certification flags remain false.

## Typecheck Status

Targeted runtime TypeScript execution passed through `tsx --test`.

Full or isolated `tsc` checking was not completed because this checkout does not expose
a local TypeScript compiler in `new-games-server` (`node_modules/.bin` is absent, and
`npx tsc` resolves to the placeholder package). No dependency installation was performed
in this sprint.
