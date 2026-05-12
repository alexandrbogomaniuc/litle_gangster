# UI-Kit Payload Mapping Test Matrix

Status: TEST_PLAN_ONLY

| Scenario | Expected result | Evidence label |
|---|---|---|
| Generic presentation payload without extension | Existing mapped model remains stable. | REQUIRED_REGRESSION |
| Presentation payload with `gamePayload` | Mapper preserves or exposes extension without mutation. | REQUIRED_MAPPER_TEST |
| Presentation payload with malformed `gamePayload` metadata | Mapper/schema rejects or reports validation error. | REQUIRED_NEGATIVE_TEST |
| 7001 `mathBridge` payload | Existing 7001 behavior remains compatible until deliberate migration. | REQUIRED_COMPATIBILITY_TEST |
| Little Gangster renderer consumes v0.3 payload | Client renderer reads backend-supplied payload only. | CLIENT_RENDER_ONLY_TEST |
| Unknown future game payload | Mapper does not drop reusable extension if generic policy is adopted. | FUTURE_REUSE_TEST |
