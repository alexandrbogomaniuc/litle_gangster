# VABS Replay Payload Validation Matrix

| Field | Required | Notes |
| --- | --- | --- |
| startingGrid | yes | 6x5 deterministic replay input |
| cascadeSteps | yes | Includes clusters, removed cells, refills |
| finalGrid | yes | Replay end state |
| winSummary | yes | Pre-cap and capped wins |
| capState | yes | Cap multiplier and hit state |
| featureState | yes | Golden/rainbow/coin/special events when present |
| bonusBuyState | yes | Purchase state, no wallet secret |
| rngDrawReferences | yes | References only, no raw RNG secrets |
| screenshotBinary | no | Requirement unverified |
