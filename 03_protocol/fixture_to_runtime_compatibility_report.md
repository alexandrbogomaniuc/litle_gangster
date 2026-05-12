# Fixture To Runtime Compatibility Report

Status: PLANNING_COMPATIBLE_STRICT_SCHEMA_ADJUSTMENTS_REQUIRED.

## Fixture Inventory

The fixture planning sprint created 24 static JSON examples under `06_resulting_code/planning/fixtures/examples/`.

All fixtures are marked:

- `fixtureType`: `non_production_renderer_fixture`
- `nonProduction`: true
- `authoritativeOutcome`: false
- `browserGenerated`: false
- `runtimeEnvelopeStatus`: `candidate_unproven`
- `presentationPayloadExtensionStatus`: `pending_schema_review`

Evidence label: PROVEN_PROJECT_FIXTURES.

## Compatibility Decision

| Question | Answer | Evidence label |
|---|---|---|
| Are fixtures safe to keep under planning? | Yes. They are static non-production planning data, not runtime or client implementation. | PROVEN_PROJECT_FIXTURES |
| Are fixtures compatible with proposed `gamePayload` adapter concept? | Yes, conceptually. They already include `presentationPayload.gamePayload` and v0.3 render payload. | PLANNING_COMPATIBLE |
| Are fixtures compatible with current strict core schema today? | No. They require schema/fixture alignment before automated protocol validation. | STRICT_SCHEMA_CONFLICT |
| Can fixtures be used for client planning without runtime proof? | Yes, if the next sprint is explicitly fixture-only and non-production. | CONDITIONAL_PLANNING_ONLY |

## Strict Schema Conflicts Found

| Conflict | Current fixture pattern | Current core schema expectation | Evidence label |
|---|---|---|---|
| Presentation extension | `presentationPayload.gamePayload` | strict schema allows only generic fields | PROVEN_SCHEMA_CONFLICT |
| `stateVersion` | fixture string such as `fixture_state_001` | non-negative integer | PROVEN_SCHEMA_CONFLICT |
| `round.status` | lowercase or custom statuses such as `idle`, `final` | `NONE`, `IN_PROGRESS`, or `FINAL` | PROVEN_SCHEMA_CONFLICT |
| `restore` fields | `hasOpenRound`, `roundId` | `hasUnfinishedRound`, `unfinishedRoundId`, `resumeStateVersion`, `opaqueRestorePayload` | PROVEN_SCHEMA_CONFLICT |
| `idempotency` fields | `duplicate` | `isDuplicate`, `duplicateOfRequestId`, `replaySafe` | PROVEN_SCHEMA_CONFLICT |
| `symbolGrid` values | symbolic strings in examples | shared UI mapper expects numeric symbol IDs | PROVEN_MAPPER_CONFLICT |

## Fixture Changes Needed Later

- Keep symbolic fixture payloads for human planning, or add a strict-runtime variant with numeric IDs.
- Add `RuntimeEnvelopeResponseSchema`-compatible casing and field names if fixtures will become automated protocol tests.
- Keep `gamePayload` pending until schema review approves it.
- Do not promote fixtures to production runtime proof.
