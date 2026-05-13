# ExtGame API Advisory Matrix

Generated: 2026-05-11
Corrected: 2026-05-11

## Evidence Boundary

This matrix records advisory checklist items only. It is not a selected Little Gangster architecture and not proof of an ExtGame endpoint.

| Checklist item | If ExtGame is later proven | Current-GS/new-games translation | Current status |
|---|---|---|---|
| ExtGame lane identification | Map external endpoint launch/runtime separately. | Keep ExtGame candidate while proving current lane from GS source/config. | unverified |
| `processTransactions` | Define exact request/response, idempotency, balance, and settlement rules. | Verify reserve/settle/process-equivalent behavior through `/slot/v1/playround`, feature actions, wallet bridge, and history write. |
advisory |
| `gameState` | Define external-side persisted state. | Define restore-safe backend state for cascades, feature modes, cap, pending collect, and history. | advisory |
| `roundFinishedHelper` | Define external or template helper inputs. | Verify current GS `roundFinishedHelper` / `endRoundSignature` need and map math round-complete field. | advisory |
| `restartGame` | Define external restart endpoint. | Verify current GS `restartGame`, FRB restart, and `/slot/v1/resumegame` behavior. | advisory |
| Template parameters | Define ExtGame template fields. | Verify current GS fields before GameServerRegistrar generation. | advisory |
| VBA / VABS / history | External side may need history endpoints. | Verify GS VABS/history/Lasthand support and Little Gangster renderer needs. | advisory |
| FRB / OCB | Implement only if product/current lane requires it. | Treat as product and current-GS support decision. | pending |

## Safety

Missing evidence is a blocker, not a reason to guess. Mock tests must not call production endpoints.

