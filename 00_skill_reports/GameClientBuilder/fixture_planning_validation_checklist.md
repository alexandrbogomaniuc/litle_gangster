# GameClientBuilder Fixture Planning Validation Checklist

| Check | Result |
|---|---|
| `project_manifest.json` parses | pass |
| GameClientBuilder `handoff.json` parses | pass after update |
| `fixture_schema.json` parses | pass |
| All fixture example JSON files parse | pass |
| Fixture example count is 24 | pass |
| Every fixture has `fixtureType=non_production_renderer_fixture` | pass |
| Every fixture has `nonProduction=true` | pass |
| Every fixture has `authoritativeOutcome=false` | pass |
| Every fixture has `browserGenerated=false` | pass |
| Every fixture has `runtimeEnvelopeStatus=candidate_unproven` | pass |
| Every fixture has `presentationPayloadExtensionStatus=pending_schema_review` | pass |
| No fixture contains raw donor URL/token | pass |
| No fixture contains raw PASS_KEY, SID, signature, email, private link, session/auth/key/jwt/hash values beyond fake fixture IDs/field names | pass |
| No fixture contains donor/scaffold asset paths | pass |
| No `package.json` exists under `06_resulting_code` | pass |
| No `src/` exists under `06_resulting_code` | pass |
| No `public/` exists under `06_resulting_code` | pass |
| No `dist/` or `build/` exists under `06_resulting_code` | pass |
| No media/binary assets exist under `06_resulting_code` | pass |
| No client implementation code was generated | pass |
| No runtime adapter implementation code was generated | pass |
| No registration artifact was generated | pass |
| No DB/Cassandra action occurred | pass |
| No wallet/API call occurred | pass |
| No donor browsing occurred | pass |
| No asset capture occurred | pass |
| No release approval occurred | pass |
| Reports state fixtures are non-production planning artifacts only | pass |
