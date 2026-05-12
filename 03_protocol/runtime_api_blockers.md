# Runtime API Blockers

## Open Blockers

| Blocker | Status | Needed to unblock |
|---|---|---|
| `little_gangster_8001_runtime_not_found` | open | Locate or create a reviewed backend/runtime package and route for Little Gangster. |
| `runtime_result_owner_unproven` | open | Prove whether New Games backend, classic GS, game-specific backend, or GS processor owns results. |
| `result_api_contract_unproven_for_8001` | open | Approve exact Little Gangster envelope and presentation payload shape. |
| `v0_3_runtime_payload_adapter_unproven` | open | Implement or fixture-approve backend adapter from v0.3 result schema to runtime payload. |
| `presentation_payload_schema_extension_unreviewed` | open | Verify compatibility with strict core-protocol schema before client implementation. |
| `math_package_consumption_not_found` | open | Prove where v0.3 math package/config is consumed by backend runtime. |
| `history_recovery_contract_unverified_for_8001` | open | Prove resumegame/gethistory/VABS/Lasthand/replay shape for Little Gangster. |
| `gameclientbuilder_implementation_blocked` | open | Requires runtime owner and result API proof plus explicit user approval. |

## Non-Blockers For Planning

- Generic `/slot/v1` endpoint names are proven.
- Generic `RuntimeEnvelopeResponse` is proven.
- Generic browser transport and presentation mapper pattern exist.

These are enough for planning-only continuation, not implementation.
