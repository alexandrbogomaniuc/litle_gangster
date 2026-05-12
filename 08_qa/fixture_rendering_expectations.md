# Fixture Rendering Expectations

Status: TEST_PLAN_ONLY.

A future renderer prototype may use these fixtures only after explicit user approval.

Expected behavior:

- The renderer reads static JSON fixtures from planning/test data only.
- It maps `presentationPayload.gamePayload.payload` to v0.3 scene/object states.
- It displays scene states listed in `expectedSceneStates`.
- It displays object states listed in `expectedObjectStates`.
- It never generates symbols, cascades, wins, cap decisions, feature progression, wallet state, or history truth.
- It fails closed if a fixture is missing required non-production boundary flags.
- It must not package donor/scaffold assets or any `02_reference_assets` path.
