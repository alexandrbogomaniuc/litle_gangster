# Client Prototype Next Step Decision

Status: PLANNING_DECISION_RECORDED

## Decision

The next technical step should be ProtocolAndSchemaMapper source patch planning for the schema extension, not full GameClientBuilder implementation.

A future static prototype iteration may be allowed only if the user explicitly requests fixture-only work, but it must remain non-production and must not connect to GS, wallet, or backend runtime endpoints.

## Decision Matrix

| Next step | Status | Reason | Evidence label |
|---|---|---|---|
| ProtocolAndSchemaMapper source patch planning | Recommended | Schema patch is required before backend adapter implementation. | PROVEN_SCHEMA_BLOCKER |
| GameClientBuilder static prototype iteration | Conditional | Useful for fixture visualization only if explicitly requested. | PLANNING_ONLY_ALLOWED |
| Backend adapter implementation | Blocked | Requires schema patch approval and 8001 runtime owner proof. | BLOCKED_RUNTIME_OWNER |
| Full GameClientBuilder implementation | Blocked | Runtime owner/result API/schema/backend path not proven. | BLOCKED_IMPLEMENTATION |
| Release/client build approval | Blocked | Assets, runtime, wallet, registration, and release gates remain false. | RELEASE_BLOCKED |
