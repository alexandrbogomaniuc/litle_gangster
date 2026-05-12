# v0.3 To `/slot/v1` Adapter Contract

Status: REQUIRED_NOT_IMPLEMENTED_NOT_PROVEN.

## Purpose

Define the boundary between the Little Gangster v0.3 backend result contract and the generic `/slot/v1` runtime envelope.

This is a contract document only. It is not runtime implementation, client code, registration generation, wallet testing, or release approval.

## Adapter Direction

| Adapter step | Input | Output | Owner | Evidence label |
|---|---|---|---|---|
| Authoritative outcome generation | Server/backend runtime RNG and math execution | Backend result object compatible with v0.3 concepts | Backend/runtime only | REQUIRED_NOT_PROVEN_FOR_8001 |
| v0.3 contract normalization | Backend result object | `result_schema.json` compatible structure | Backend/runtime only | REQUIRED |
| `/slot/v1` envelope projection | v0.3 result plus wallet/round/session state | `RuntimeEnvelopeResponse` | Backend/runtime only | REQUIRED |
| Client render mapping | Reviewed presentation payload | Scene/object animation state | Browser renderer only | PLANNING_ALLOWED |

## Generic Envelope Mapping

| v0.3 concept | `/slot/v1` location | Evidence label | Notes |
|---|---|---|---|
| `gameId` | bootstrap/context or round metadata | PROVEN_GENERIC_NEEDS_8001_ROUTE | 8001 route remains unproven. |
| `roundId` | `round.roundId` and v0.3 payload | PROVEN_GENERIC | Must match history/recovery records. |
| `spinId` | v0.3 payload and/or `round` extension | REQUIRED_REVIEW | Generic schema does not define spin ID. |
| `stateVersion` | envelope `stateVersion` and `state_persistence.stateVersion` | PROVEN_GENERIC | Must advance under runtime rules. |
| `clientOperationId` | request/body/header and `state_persistence.clientOperationId` | PROVEN_GENERIC | Correlation only; not outcome authority. |
| bet and total win | `round.betMinor`, `round.winMinor`, v0.3 payload | PROVEN_GENERIC | Minor-unit conversion needs final currency/bet review. |
| `winRatio`, `winTier` | v0.3 presentation extension | REQUIRED_EXTENSION | Generic envelope has no dedicated fields. |
| cascade/golden/rainbow/coin fields | v0.3 presentation extension | REQUIRED_EXTENSION | Cannot be browser-generated. |
| feature mode and bonus buy state | `feature` plus v0.3 presentation extension | PROVEN_GENERIC_PLUS_EXTENSION | `feature` owns action availability; presentation owns render detail. |
| max-win cap state | `round`, `feature`, and v0.3 presentation extension | REQUIRED_EXTENSION | Backend must cap before render. |
| round completion | `round.status`, `feature.nextAllowedActions`, v0.3 `round_completion` | PROVEN_GENERIC_PLUS_EXTENSION | Browser cannot declare completion. |
| state persistence/reconnect | `restore`, `history`, and v0.3 `state_persistence` | PROVEN_GENERIC_PLUS_EXTENSION | Needs 8001-specific proof. |

## Proposed Presentation Extension

Do not treat this as implemented. It is a reviewed-contract candidate:

```json
{
  "featureMode": "BASE",
  "reelStops": [],
  "symbolGrid": [],
  "uiMessages": [],
  "animationCues": [],
  "audioCues": [],
  "counters": [],
  "labels": {},
  "littleGangsterV03": {
    "schemaVersion": "v0.3_donor_feature_parity_provisional",
    "renderState": "subset or full v0.3 result schema fields for rendering"
  }
}
```

Because the current generic schema is strict, `littleGangsterV03` requires schema review or a different approved extension point before implementation.

## Acceptance Criteria

- Runtime owner is proven.
- `/slot/v1` or equivalent is selected for Little Gangster.
- Core protocol accepts the chosen presentation extension.
- History and restore store enough state to replay/reconnect v0.3 rounds.
- Browser remains renderer-only.
- Client implementation receives explicit user approval.

