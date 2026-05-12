# Future Sprint Go / No-Go

Status: consolidation decision.

## Next Necessary Sprint

Recommended next sprint: MathModelDesigner authoritative simulation/config refinement.

Reason:

- Backend adapter implementation would currently receive incomplete authoritative math/config values.
- Bonus-buy cost/EV is still blocked.
- Free-spin and feature-mode exact rules remain incomplete.
- RTP model flexibility exists as planning, but model ids, contributions, volatility, and cap behavior need strict simulation-ready definitions.
- GL/template settings need final values or explicit placeholders before GameServerRegistrar can generate anything.

## Why Not Backend Adapter Apply Next

Backend adapter implementation remains blocked because:

- authoritative math owner is still unproven;
- exact math/config values are incomplete;
- Little Gangster result API is still not production-proven;
- VABS/Lasthands exact storage format is not proven;
- no 8001 package or backend target has been approved for source modification.

## Why Not GameClientBuilder Next

GameClientBuilder implementation remains blocked because:

- runtime owner and production result API are not proven;
- final release assets are not approved;
- backend adapter is not implemented;
- browser must remain renderer-only.

## Why Not GameServerRegistrar Next

GameServerRegistrar artifact generation remains blocked because:

- registration lane is not final;
- serializer/import path is blocked;
- 8001 client/runtime path is missing;
- math is not release-approved;
- registration must not import executable math.

## What Can Be Skipped Or Merged

- Public export can be skipped until checkpoint review.
- Repeated schema-extension planning can be skipped because `gamePayload` support is already patched.
- Fixture schema planning can be merged into future adapter tests.
- Mantis/ExtGame checklist review can be merged into ProtocolAndSchemaMapper gate checks.

## Checkpoint Push

Checkpoint review/push is due soon because several local sprints have completed, but it is not required in this sprint and must not be run here.

## Public Export Need

Public export is not needed now. It should be run only at a checkpoint or external-review request, with pushed raw validation as source of truth.

## Go / No-Go

| Candidate next sprint | Decision | Reason |
| --- | --- | --- |
| MathModelDesigner authoritative simulation/config refinement | GO | Closes math/RTP/bonus/free-spin/model details before implementation-adjacent source work. |
| ProtocolAndSchemaMapper strict history design | MERGE OR FOLLOW | History is important, but current gap is mostly exact format/storage target after math config is settled. |
| ProtocolAndSchemaMapper backend adapter apply | NO-GO | Implementation approval and complete math/config/history prerequisites missing. |
| Checkpoint push | DUE SOON, NOT THIS SPRINT | Several local sprints have accumulated; run when user explicitly asks. |

