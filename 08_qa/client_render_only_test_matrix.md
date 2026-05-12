# Client Render-Only Test Matrix

Status: TEST_PLAN_ONLY. No client code or tests were run.

| Test area | Required check | Status |
|---|---|---|
| No local RNG authority | Client has no production path that generates symbol outcomes. | planned |
| No local win authority | Client never calculates authoritative total win or cap. | planned |
| Render from payload | Cascade, reveal, win tier, feature, and restore animations use runtime payload only. | planned |
| Fixture isolation | Planning fixture is not shipped as production runtime. | planned |
| Wallet separation | Client displays wallet values only from envelope. | planned |
| Registration separation | Client does not treat registration metadata as result schema. | planned |
| Asset safety | Production bundle excludes donor/scaffold assets. | planned |
| Implementation gate | Build fails or stops if runtime owner/result API remain unproven. | planned |

