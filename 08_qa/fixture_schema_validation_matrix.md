# Fixture Schema Validation Matrix

Status: TEST_PLAN_ONLY.

| Check | Expected |
|---|---|
| `fixture_schema.json` parses | pass |
| All 24 example JSON files parse | pass |
| Fixture count | 24 |
| `fixtureType` | `non_production_renderer_fixture` |
| `nonProduction` | true |
| `authoritativeOutcome` | false |
| `browserGenerated` | false |
| `runtimeEnvelopeStatus` | `candidate_unproven` |
| `presentationPayloadExtensionStatus` | `pending_schema_review` |
| Donor/scaffold asset path scan | no matches |
| Secret/token/session/email/private-link scan | no raw values; fixture IDs only |
| `06_resulting_code` implementation file scan | no package/app/build/runtime files |
