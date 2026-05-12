# Gap-Based Next Sprint Test Plan

Status: test planning only.

Recommended next sprint tests:

| Gap | Test or validation to define | Owner |
| --- | --- | --- |
| RTP model ids | Validate 96/94/92 model profile shape | MathModelDesigner |
| Cluster bet mapping | Validate min/default/max/coin denominational model | MathModelDesigner |
| Bonus-buy cost/EV | Validate placeholder remains blocked or final values simulate | MathModelDesigner |
| Feature mode rules | Validate mode-specific spin loop and contribution report | MathModelDesigner |
| Max-win cap | Validate 10000x cap handling and cap frequency report | MathModelDesigner |
| VABS replay | Validate deterministic replay payload contents | ProtocolAndSchemaMapper |
| Screenshot requirement | Verify no screenshot binary requirement or record blocker | ProtocolAndSchemaMapper |
| Registration metadata | Validate GL fields remain metadata/config only | GameServerRegistrar |
| Adapter readiness | Validate backend adapter input can receive final math config | ProtocolAndSchemaMapper |

Do not run:

- backend adapter implementation.
- GameClientBuilder implementation.
- registration artifact generation.
- wallet/API tests.
- public export.

