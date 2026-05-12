# Backend Adapter Schema Test Plan

Status: TEST_PLAN_ONLY.

Future schema tests should run:

- patched response schema validation for opengame;
- patched response schema validation for playround;
- patched response schema validation for featureaction;
- patched response schema validation for resumegame;
- patched response schema validation for gethistory;
- patched response schema validation for closegame;
- v0.3 result schema validation for every `gamePayload.payload`;
- negative test for missing `gamePayload.gameKey`;
- negative test for missing `gamePayload.schemaVersion`;
- negative test for non-object `gamePayload.payload`;
- negative test proving unknown top-level presentation fields remain rejected by canonical schema.

