# Source Patch Risks And Blockers

Status: BLOCKERS_RECORDED

| Risk or blocker | Status | Evidence label | Mitigation |
|---|---|---|---|
| Canonical JSON schemas and Zod helper both need updates. | Open | PROVEN_CANONICAL_SCHEMA_BLOCKER | Patch both in same source patch set. |
| UI-kit mapper currently does not expose extension data. | Open | PROVEN_MAPPER_GAP | Add passthrough and tests. |
| Transport parser is permissive, which can hide canonical schema drift. | Open risk | CONFLICTING_EVIDENCE | Use contract tests against JSON schemas. |
| `mathBridge` exists as 7001 pattern but is not canonical. | Open risk | CANDIDATE_PATTERN | Keep unchanged; do not reuse as Little Gangster contract. |
| New-games-server 8001 branch missing. | Open | NOT_FOUND_8001 | Do not add until runtime owner proof/approval. |
| Little Gangster runtime owner not proven. | Open | NOT_FOUND_8001 | Block adapter implementation. |
| Fixture strict-schema variants missing. | Open | STRICT_SCHEMA_CONFLICT | Create after schema patch approval. |
| Source patch not approved. | Open | USER_SCOPE_BLOCKER | Require explicit user approval before Staging modification. |
