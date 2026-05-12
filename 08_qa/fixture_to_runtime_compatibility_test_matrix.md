# Fixture To Runtime Compatibility Test Matrix

Status: TEST_PLAN_ONLY_NOT_RUN.

| Test | Fixture set | Expected result | Evidence label |
|---|---|---|---|
| JSON parse | 24 planning fixtures | All parse as JSON. | PROVEN_PROJECT_FIXTURES |
| Planning boundary | 24 planning fixtures | All are `non_production_renderer_fixture`, non-authoritative, and browserGenerated false. | PROVEN_PROJECT_FIXTURES |
| Core schema dry run | 24 planning fixtures | Expected to fail today because fixtures are planning approximations. | STRICT_SCHEMA_CONFLICT |
| Runtime variant conversion | Future strict fixture variants | Numeric grids, integer stateVersion, core restore/idempotency names. | REQUIRED_LATER |
| No sensitive values | All fixtures | No raw secrets, private links, donor URLs, or asset paths. | REQUIRED_TEST |
| Scene coverage | 24 fixtures | Each v0.3 feature category maps to expected scene/object states. | REQUIRED_TEST |
