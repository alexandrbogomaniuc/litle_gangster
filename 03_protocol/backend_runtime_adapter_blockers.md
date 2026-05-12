# Backend Runtime Adapter Blockers

## Blocking Items

| Blocker | Status | Needed to unblock |
|---|---|---|
| `presentation_payload_schema_extension_required` | open | Add/review `presentationPayload.gamePayload` or approved fallback in core protocol schema. |
| `little_gangster_8001_runtime_owner_unproven` | open | Prove or create the backend/runtime component that owns Little Gangster results. |
| `little_gangster_8001_runtime_package_missing` | open | Create/review an 8001 package or server branch after approval. |
| `v0_3_adapter_implementation_not_ready` | open | Implement adapter only after schema and owner are approved. |
| `math_package_consumption_not_found` | open | Prove how runtime consumes v0.3 math/config or define a backend package path. |
| `history_lasthands_vabs_mapping_unproven` | open | Prove or define replay/recovery serialization for 8001. |
| `fixture_strict_schema_mismatch` | open | Align fixture fields if they become protocol validator inputs. |
| `approved_release_assets_missing` | open | Keep production build blocked until approved assets exist. |
| `no_client_code_generation_approval` | open | Explicit future approval required before any client/prototype code. |

## Non-Blocking For Planning

- Generic `/slot/v1` envelope exists.
- Existing 7001 `mathBridge` pattern proves a candidate extension style.
- 24 non-production fixtures are safe planning data.

## Implementation Gates

- `backend_adapter_implementation_allowed=false`
- `gameclientbuilder_implementation_allowed=false`
- `registration_approved=false`
- `wallet_tests_approved=false`
- `release_approved=false`
Evidence label summary: BLOCKED items remain open; PROVEN generic `/slot/v1` support is not enough to unblock implementation.

