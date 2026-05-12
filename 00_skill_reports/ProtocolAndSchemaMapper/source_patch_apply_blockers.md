# Source Patch Apply Blockers

## Remaining Blockers

| Blocker | Status | Evidence label | Required next step |
|---|---|---|---|
| Full TypeScript typecheck fails on existing config | Open | PRE_EXISTING_CONFIG_FAILURE | Fix repo `allowImportingTsExtensions` and package `rootDir` setup separately. |
| `new-games-server` has no 8001 emission branch | Open | NOT_IMPLEMENTED_BY_SCOPE | Approve backend/runtime adapter implementation planning or implementation later. |
| Little Gangster/8001 runtime owner remains unproven | Open | NOT_FOUND_8001 | Prove or create the runtime owner path before production client work. |
| Little Gangster v0.3 result API remains unproven | Open | NOT_PROVEN_FOR_8001 | Implement/prove backend authoritative adapter contract later. |
| Backend adapter implementation not approved | Open | USER_SCOPE_BLOCKER | Requires explicit future approval. |
| GameClientBuilder implementation not approved | Open | USER_SCOPE_BLOCKER | Remains blocked until backend/runtime contract is proven. |
| Staging git baseline is untracked from parent repo | Open | GIT_TOPOLOGY_CAVEAT | Establish clean tracked source baseline before release-grade patch review. |

## Resolved In This Sprint

- Generic `presentationPayload.gamePayload` schema support is applied.
- UI-kit passthrough for `gamePayload` is applied.
- Parent presentation schema remains strict.
