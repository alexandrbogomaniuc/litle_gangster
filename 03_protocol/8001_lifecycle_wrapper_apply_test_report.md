# Little Gangster 8001 Lifecycle Wrapper Apply Test Report

Created: 2026-05-15

## Targeted Tests

Command:

```sh
npx tsx --test test/little-gangster/*.test.ts
```

Result: passed.

- tests: 13
- pass: 13
- fail: 0

Coverage included:

- adapter still returns `presentationPayload.gamePayload`
- lifecycle wrapper preserves `presentationPayload.gamePayload`
- `mathProfileId` survives wrapper mapping
- RTP and volatility fields survive wrapper mapping
- 100x bonus-buy purchase/result fields survive wrapper mapping
- 125x/150x remain blocked
- lifecycle state is present
- action accounting representation is present
- round completion representation is present
- reconnect/persistence representation is present
- blocker flags are present
- release and certification flags remain false
- VABS visual route implementation remains pending

## Isolated Little Gangster TypeScript Check

Command:

```sh
npx -p typescript@5.8.2 -p @types/node@22.13.4 tsc --noEmit --module NodeNext --moduleResolution NodeNext --target ES2022 --strict --skipLibCheck
src/games/little-gangster/*.ts src/games/little-gangster/lifecycle/*.ts
```

Result: passed.

## Broader Index Typecheck

Command:

```sh
npx -p typescript@5.8.2 -p @types/node@22.13.4 tsc --noEmit --module NodeNext --moduleResolution NodeNext --target ES2022 --strict --skipLibCheck
src/index.ts src/games/little-gangster/*.ts src/games/little-gangster/lifecycle/*.ts
```

Result: blocked by existing checkout/server typecheck issues.

Observed status:

- `full_index_typecheck_exit=2`
- `total_typecheck_errors=40`
- no lifecycle-wrapper-specific type error remained after adding the missing 100x
  `totalWinCredits` integration field

Existing blockers include missing local type declarations for server dependencies and
strictness issues in the broader `src/index.ts` route file.
