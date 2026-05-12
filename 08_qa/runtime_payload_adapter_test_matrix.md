# Runtime Payload Adapter Test Matrix

Status: TEST PLAN ONLY. No runtime implementation was generated.

| v0.3 area | Adapter test | Required fixture/proof | Status |
|---|---|---|---|
| cascade | Payload includes ordered cascade steps, removed cells, dropped cells, and new symbols. | v0.3 playround fixture. | blocked |
| clusters | Payload includes cluster IDs, cells, symbol, and win amount. | v0.3 playround fixture. | blocked |
| golden squares | Payload includes before/after state and events. | v0.3 playround/feature fixture. | blocked |
| rainbow | Payload includes activation positions and affected cells. | v0.3 trigger fixture. | blocked |
| coin reveals | Payload includes bronze/silver/gold reveal tier and value fields. | v0.3 reveal fixture. | blocked |
| special reveals | Payload includes pot/clover candidate fields with confidence. | v0.3 optional reveal fixture. | blocked |
| feature modes | Payload includes mode state and remaining spins/rounds. | v0.3 feature fixture. | blocked |
| bonus buy | Payload separates purchase state, wallet boundary, and feature start state. | featureaction fixture. | blocked |
| max-win cap | Payload includes pre-cap/capped values and cap step. | cap fixture. | blocked |
| win tiers | Payload includes `winRatio` and `winTier`. | win-tier fixtures. | blocked |
| round completion | Payload includes complete/no-pending flags. | final round fixture. | blocked |
| persistence | Payload includes state version/reconnect state. | resume fixture. | blocked |

## Acceptance Gate

All adapter tests remain blocked until Little Gangster runtime owner and v0.3 payload schema are approved.
