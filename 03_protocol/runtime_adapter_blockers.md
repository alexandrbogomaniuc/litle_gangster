# Runtime Adapter Blockers

## Open Blockers

| Blocker | Status | Needed to unblock |
|---|---|---|
| `little_gangster_8001_runtime_owner_unproven` | open | Prove the backend/runtime component that owns Little Gangster results. |
| `little_gangster_result_api_contract_unproven` | open | Approve exact `/slot/v1` or equivalent payload shape for game 8001. |
| `presentation_payload_extension_unreviewed` | open | Review and approve how v0.3 fields enter `presentationPayload`. |
| `v0_3_to_slot_v1_adapter_not_implemented` | open | Implement or formally fixture-approve the backend adapter in a later sprint. |
| `history_lasthands_mapping_unproven_for_8001` | open | Prove history/VABS/Lasthands replay payload shape. |
| `math_package_consumption_not_found` | open | Prove where runtime consumes v0.3 math/config or define backend package path. |
| `gameclientbuilder_implementation_blocked` | open | Requires runtime owner, result API, presentation extension, assets, and explicit user approval. |
| `gameserverregistrar_generation_blocked` | open | Registration route, serializer/import tooling, and 8001 records remain unproven. |

## Not Blockers For Planning

- generic `/slot/v1` endpoints are proven;
- generic `RuntimeEnvelopeResponse` is proven;
- generic `presentationPayload` exists;
- a safe minimum fixture can be defined later for planning only.

