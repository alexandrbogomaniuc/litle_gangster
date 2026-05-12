# Little Gangster Adapter Implementation Plan

Status: PLAN_ONLY_IMPLEMENTATION_NOT_APPROVED
Recommended extension: `presentationPayload.gamePayload`

## Adapter Purpose

The future backend adapter must convert authoritative backend game results into a v0.3 renderer payload for Little Gangster. It must not move authority into the browser.

## Future Adapter Input

| Input group | Description | Ownership | Evidence label |
|---|---|---|---|
| Authoritative math/outcome result | Backend-generated spin/cascade/feature result. | Backend/runtime only | REQUIRED_NOT_PROVEN_8001 |
| RNG provenance/reference | Server-side RNG or runtime-owned result evidence. | Backend/runtime only | REQUIRED_NOT_PROVEN_8001 |
| Round state | Round id, status, state version, completion status. | Backend/runtime | PROVEN_GENERIC_RUNTIME_CONCEPT |
| Feature state | Feature mode, bonus-buy state, persistent modifiers. | Backend/runtime | REQUIRED_FOR_V0_3 |
| History/recovery state | Payload snapshot or reconstructable state for reconnect and history. | Backend/runtime | GENERIC_HISTORY_PROVEN_8001_NOT_PROVEN |

## Future Adapter Output

| Output group | Description | Consumer | Evidence label |
|---|---|---|---|
| Generic presentation fields | Shell/UI-kit fields such as symbol grid, cues, counters, labels where useful. | UI shell/shared mapper | PROVEN_GENERIC_MAPPER_NEEDS |
| `presentationPayload.gamePayload.gameKey` | `little-gangster`. | Client renderer | RECOMMENDED_SCHEMA_PATCH |
| `presentationPayload.gamePayload.schemaVersion` | `v0.3`. | Client renderer | RECOMMENDED_SCHEMA_PATCH |
| `presentationPayload.gamePayload.payload` | v0.3 render state covering cascades, golden squares, rainbow, coins, specials, feature mode, bonus buy, max-win, win tiers, completion, and recovery. | Client renderer | REQUIRED_FOR_V0_3 |

## Backend-Owned Fields

The browser must never generate or be trusted for:

- production RNG result
- authoritative outcome and payout
- cascade resolution truth
- coin/special reveal truth
- feature trigger truth
- bonus-buy entitlement and cost validation
- max-win cap enforcement
- round completion authority
- persisted recovery/history truth
- wallet/accounting changes

## Safe Rendering Fields

The client may consume, display, and animate:

- symbol grid and cascade steps
- removed/dropped/refilled cell descriptors
- golden-square overlay state
- rainbow activation cue
- coin/special reveal cue
- feature-mode visual state
- bonus-buy visual state
- win tier labels and non-authoritative animation hints
- recovery/round-completion render state supplied by backend

## Implementation Prerequisites

1. Core schema patch approval and implementation.
2. UI-kit mapper extension/pass-through policy.
3. New-games-server 8001 payload construction path.
4. Little Gangster runtime owner proof or package creation.
5. Authoritative v0.3 result source and server-owned RNG/outcome proof.
6. History/recovery persistence contract for `gamePayload` snapshots.
7. Strict-schema-compatible fixture updates.
8. Explicit user approval for backend adapter implementation.

## Status

Adapter implementation is not allowed in this sprint. This plan defines the future path only.
