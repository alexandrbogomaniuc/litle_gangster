# Backend Adapter Fixture Test Plan

Status: TEST_PLAN_ONLY_NOT_RUN.

The 24 strict fixtures are the expected-output contract for future adapter tests.

## Fixture Use

| Use | Allowed? | Evidence label |
|---|---:|---|
| Non-production adapter unit tests | yes | PROVEN_STRICT_FIXTURE_CONTRACT |
| Schema validation examples | yes | PROVEN_STRICT_FIXTURE_CONTRACT |
| Client planning examples | yes | PROVEN_NON_PRODUCTION |
| Production runtime proof | no | BLOCKED |
| Wallet/accounting proof | no | BLOCKED |
| Release proof | no | BLOCKED |

## Future Test Shape

For each strict fixture:

1. Build an adapter input object from the embedded v0.3 payload and fake test metadata.
2. Call the future backend adapter.
3. Assert the output includes `presentationPayload.gamePayload`.
4. Validate the full envelope against the patched response schema selected in `strict_schema_validation_results.csv`.
5. Validate `presentationPayload.gamePayload.payload` against `result_schema.json`.
6. Assert wallet/accounting values remain outside `gamePayload`.
7. Assert non-production fixture metadata is not emitted in production-mode tests.

## Regression Coverage

The future test suite must cover base idle, no-win, cascade, golden-square, rainbow, coin reveal, special reveal,
feature modes, bonus buy, win tiers, max-win cap, round completion, reconnect restore, and history/recovery states.

