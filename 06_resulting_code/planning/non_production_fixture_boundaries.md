# Non-Production Fixture Boundaries

Status: REQUIRED.

The fixture pack is planning/test data only.

## Allowed

- Static renderer planning.
- Scene/object mapping review.
- Future HTML or static renderer prototype review if the user explicitly approves that later.
- Contract discussion with backend/runtime owners.

## Forbidden

- Production runtime use.
- Browser-authoritative RNG or outcome generation.
- Wallet reserve, settle, collect, or balance mutation.
- Registration metadata generation.
- Release approval.
- Packaging donor/scaffold assets.
- Treating fixture totals as certified math or payout proof.

## Required Labels

Every fixture must remain marked:

- `fixtureType=non_production_renderer_fixture`
- `nonProduction=true`
- `authoritativeOutcome=false`
- `browserGenerated=false`
- `runtimeEnvelopeStatus=candidate_unproven`
- `presentationPayloadExtensionStatus=pending_schema_review`
