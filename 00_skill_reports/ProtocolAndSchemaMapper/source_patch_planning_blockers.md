# Source Patch Planning Blockers

| Blocker | Status | Evidence label |
|---|---|---|
| User approval to modify Staging source is required before applying any patch. | Open | USER_SCOPE_BLOCKER |
| Canonical JSON schemas do not support `gamePayload` today. | Open | PROVEN_CANONICAL_SCHEMA_BLOCKER |
| Zod `PresentationPayloadSchema` does not support `gamePayload` today. | Open | PROVEN_ZOD_SCHEMA_BLOCKER |
| UI-kit mapper does not expose `gamePayload` today. | Open | PROVEN_MAPPER_GAP |
| 8001 runtime owner remains unproven. | Open | NOT_FOUND_8001 |
| Backend adapter implementation remains unapproved. | Open | USER_SCOPE_BLOCKER |
| Full GameClientBuilder implementation remains blocked. | Open | USER_SCOPE_BLOCKER |
