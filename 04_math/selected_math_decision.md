# Selected Math Decision

Decision: `Option 2 - Switch selected model to a new provisional 6x5 cluster/ways-style model`.

## Selected Model

- Selected version: `v0.2_6x5_cluster_provisional`
- Selected layout: `6x5_cluster_provisional`
- Selected package path: `04_math/alternatives/v0_2_6x5_cluster/math_package.json`
- Previous package: `v0.1 5x3 fixed-20-line`, preserved but superseded for downstream planning.

## Why Option 2

Reference research reported a 6x5 cluster-style donor/reference game. The previous 5x3 fixed-line model was internally usable as a provisional original model, but it would create a real mismatch for scene mapping, art planning, client
rendering, and backend result schemas.

The 6x5 model is still provisional. It is not donor-true math, not release-approved math, and not final backend integration. It is the correct selected layout for the next workflow stage.

## ArtSceneMapper Guidance

ArtSceneMapper should map a 6x5 target game scene. It should not use the old 5x3 model as the target board layout. Donor/reference art remains scaffold/reference only and is not release-approved.

## Remaining Decision Boundaries

- Full RTP certification remains pending.
- Runtime owner remains unproven.
- Browser client must not own real-money RNG/results.
- GS/Cassandra registration remains metadata/config/routing unless later source proves executable math import.
