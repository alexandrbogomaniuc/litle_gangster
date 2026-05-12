# Schema Extension Blockers

Status: BLOCKERS_RECORDED

| Blocker | Status | Evidence label | Resolution needed |
|---|---|---|---|
| Core schema does not support `gamePayload`. | Open | PROVEN_SCHEMA_BLOCKER | Patch `PresentationPayloadSchema` and tests. |
| Core schema does not support `littleGangsterV03`. | Open | PROVEN_SCHEMA_BLOCKER | Use only as fallback if generic extension rejected. |
| Core schema does not support `mathBridge`. | Open for canonical schema | PROVEN_SCHEMA_BLOCKER; CANDIDATE_PATTERN | Decide legacy support or migration policy. |
| UI-kit mapper does not expose `gamePayload`. | Open | PROVEN_MAPPER_GAP | Add pass-through or extension mapping. |
| New-games-server has no 8001 payload branch. | Open | NOT_FOUND_8001 | Add server-side 8001 adapter after approval. |
| Little Gangster/8001 runtime owner remains unproven. | Open | NOT_FOUND_8001 | Prove or create runtime package/path. |
| v0.3 authoritative result source remains unproven in current runtime. | Open | REQUIRED_NOT_PROVEN_8001 | Backend/runtime team must prove result owner. |
| Fixtures are planning-compatible but not strict-runtime-compatible. | Open | STRICT_SCHEMA_CONFLICT | Update strict fixture variants after schema decision. |
| Backend adapter implementation is not approved. | Open | USER_SCOPE_BLOCKER | Requires explicit future approval. |
| GameClientBuilder implementation is not approved. | Open | USER_SCOPE_BLOCKER | Requires runtime/schema/backend proof and explicit approval. |

## Source Patch Apply Update - 2026-05-12

| Blocker | Updated status | Evidence label | Notes |
|---|---|---|---|
| Core schema does not support `gamePayload`. | Resolved for generic schema support | PROVEN_APPLIED | JSON response schemas and Zod helper now accept optional `gamePayload`. |
| UI-kit mapper does not expose `gamePayload`. | Resolved for passthrough | PROVEN_UI_KIT_PASSTHROUGH | Mapper preserves extension untouched. |
| New-games-server has no 8001 payload branch. | Open | NOT_IMPLEMENTED_BY_SCOPE | No backend adapter or 8001 branch was allowed in this sprint. |
| Little Gangster/8001 runtime owner remains unproven. | Open | NOT_FOUND_8001 | Source patch does not prove runtime ownership. |
| v0.3 authoritative result source remains unproven in current runtime. | Open | REQUIRED_NOT_PROVEN_8001 | Backend/runtime proof remains required. |
| Backend adapter implementation is not approved. | Open | USER_SCOPE_BLOCKER | Requires explicit future approval. |
| GameClientBuilder implementation is not approved. | Open | USER_SCOPE_BLOCKER | Remains blocked. |

The schema and UI-kit blockers for reusable generic support are closed. Backend adapter, runtime owner, result
API, registration, wallet, and release blockers remain open.
