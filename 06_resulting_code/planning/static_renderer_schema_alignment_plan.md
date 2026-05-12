# Static Renderer Schema Alignment Plan

Status: PLAN_ONLY_STATIC_RENDERER_REMAINS_VALID

## Decision

The static fixture renderer remains valid as a non-production planning viewer. It should not be changed into production client code.

## After Schema Patch Approval

- Add a strict-runtime fixture mode or fixture set.
- Keep current planning fixtures for coverage of visual states.
- Display whether a fixture is planning-only or strict-runtime-compatible.
- Keep `presentationPayload.gamePayload` as the preferred extension.
- Continue documenting `littleGangsterV03` as fallback only.

## Boundaries

The renderer must not call GS, wallet, backend runtime endpoints, or donor URLs. It must not calculate RNG, payouts, max-win truth, or wallet/accounting values.
