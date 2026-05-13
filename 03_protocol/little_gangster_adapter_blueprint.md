# Little Gangster Adapter Blueprint

Status: BLUEPRINT_ONLY_IMPLEMENTATION_BLOCKED
Future target path: `Gamesv1/games/8001/src/app/runtime/` or an approved backend/runtime adapter package.

## Where Should The Future Adapter Live?

The adapter should live with the future Little Gangster/8001 runtime package or in an approved backend runtime adapter module. No such 8001 source package was found in targeted inspection.

Evidence label: NOT_FOUND_8001.

## Future Source Package/Path To Create Later

Recommended future path after approval:

```text
Gamesv1/games/8001/src/app/runtime/LittleGangsterV03PresentationAdapter.ts
```

Alternative backend-owned path may be selected by the runtime team if 8001 is not a Gamesv1 client package.

## Adapter Input

| Input | Owner | Evidence label |
|---|---|---|
| Authoritative v0.3 outcome/result | Backend/runtime | REQUIRED_NOT_PROVEN_8001 |
| RNG/outcome provenance or result id | Backend/runtime | REQUIRED_BACKEND_AUTHORITY |
| Round id, bet, win, state version | Backend/runtime | PROVEN_GENERIC_RUNTIME_CONCEPT |
| Feature mode, bonus-buy, cap, recovery state | Backend/runtime | REQUIRED_V0_3 |
| History/recovery snapshot | Backend/runtime | REQUIRED_HISTORY_RECOVERY |

## Adapter Output

| Output | Purpose | Evidence label |
|---|---|---|
| Generic presentation fields | Shell/UI-kit compatibility. | PROVEN_GENERIC_MAPPER_NEEDS |
| `gamePayload.gameKey` | `little-gangster`. | RECOMMENDED_EXTENSION |
| `gamePayload.schemaVersion` | `v0.3`. | RECOMMENDED_EXTENSION |
| `gamePayload.payload` | Full v0.3 render payload for cascades, reveals, feature modes, cap, completion, and recovery. | REQUIRED_V0_3_RENDER_STATE |

## Backend-Owned Fields

The browser must never produce or be trusted for RNG draws, authoritative outcome, total win, payout, max-win cap enforcement, feature trigger decisions, bonus-buy entitlement, wallet/accounting mutation, round completion, state
persistence, or history truth.

## Rendering-Only Fields

The browser may render backend-supplied grids, cascade steps, removed/dropped/refilled cells, golden-square overlays, rainbow and coin reveal cues, special reveal cues, feature-mode visual states, bonus-buy visual states, win tier labels,
max-win cap cues, and recovery/completion screens.

## Renderer-Only Tests Later

- Client fixture rendering uses only backend-supplied `gamePayload`.
- Client cannot create production RNG/result payloads.
- Client ignores or rejects wallet/accounting fields if they appear inside `gamePayload`.
- Adapter output can replay reconnect/history render state without browser authority.

## Implementation Status

No adapter implementation was generated. Implementation remains blocked until source patch approval, runtime owner proof, and explicit backend adapter approval.
