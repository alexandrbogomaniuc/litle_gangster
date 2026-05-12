# Adapter Field Ownership Matrix

Status: BACKEND_OWNERSHIP_DOCUMENTED.

| Field/group | Backend/runtime owns | Client may consume | Client may produce | Evidence label | Notes |
|---|---:|---:|---:|---|---|
| RNG draws and seed state | yes | no | no | PROVEN_BOUNDARY | Production RNG cannot be browser-owned. |
| Initial/final symbols | yes | yes | no | REQUIRED_V0_3 | Browser renders only. |
| Cascades and cluster wins | yes | yes | no | REQUIRED_V0_3 | Includes removed, dropped, and new cells. |
| Golden-square state | yes | yes | no | REQUIRED_V0_3 | Must persist across relevant cascades/features. |
| Rainbow activation | yes | yes | no | REQUIRED_V0_3 | Browser only animates returned events. |
| Coin/special reveals | yes | yes | no | REQUIRED_V0_3 | Values and reveal type are backend-owned. |
| Feature modes | yes | yes | user intent only | PROVEN_GENERIC_PLUS_V0_3 | Browser can request an allowed action only. |
| Bonus buy | yes | yes | confirmation intent only | PROVEN_GENERIC_PLUS_V0_3 | Wallet/accounting remains backend-owned. |
| Max-win cap | yes | yes | no | REQUIRED_V0_3 | Browser cannot decide cap or final win. |
| `winRatio` / `winTier` | yes | yes | no | REQUIRED_V0_3 | Used for presentation only after backend result. |
| Wallet balance/accounting | yes | display only | no | PROVEN_GENERIC | Do not place accounting truth in game payload. |
| Round ID/status/completion | yes | yes | no | PROVEN_GENERIC_PLUS_V0_3 | `round.status` must be canonical. |
| State version/idempotency | yes | yes | request keys only | PROVEN_GENERIC | Browser may send request correlation, not truth. |
| Restore/history/VABS/Lasthand | yes | yes | no | PROVEN_GENERIC_BLOCKED_8001 | Exact Little Gangster payload unproven. |
| Registration metadata | config owner | read config | no | PROVEN_BOUNDARY | Not executable math import. |
| Animation timing hints | backend or renderer policy | yes | no for outcome | OPTIONAL | Timing hints cannot change result. |
