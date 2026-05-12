# Fixture Validation Plan

Status: PLANNING_ONLY.

Validation checks before any future renderer prototype consumes these fixtures:

1. Parse `fixture_schema.json`.
2. Parse every JSON file under `examples/`.
3. Confirm the fixture example count is 24.
4. Confirm every fixture has `fixtureType=non_production_renderer_fixture`.
5. Confirm every fixture has `nonProduction=true`.
6. Confirm every fixture has `authoritativeOutcome=false`.
7. Confirm every fixture has `browserGenerated=false`.
8. Confirm every fixture has `runtimeEnvelopeStatus=candidate_unproven`.
9. Confirm every fixture has `presentationPayloadExtensionStatus=pending_schema_review`.
10. Confirm no fixture includes donor asset paths, media files, raw secrets, tokenized URLs, real session IDs, or wallet balances.
11. Confirm `06_resulting_code` still contains only README and planning documents/data.
12. Confirm no `package.json`, `src/`, `public/`, `dist/`, or `build/` exists under `06_resulting_code`.

Passing this plan does not approve production client implementation.
