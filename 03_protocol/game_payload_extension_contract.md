# `presentationPayload.gamePayload` Extension Contract

Status: PROPOSED_NOT_APPROVED.

## Purpose

Provide a reusable game-specific render payload slot inside the existing generic `/slot/v1` presentation payload.

## Recommended Contract

| Field | Type | Owner | Evidence label | Notes |
|---|---|---|---|---|
| `gameKey` | string | backend/runtime | REQUIRED | Must be `little-gangster` for this game. |
| `schemaVersion` | string | backend/runtime | REQUIRED | Use `v0.3` or a reviewed exact version label. |
| `payload` | object | backend/runtime | REQUIRED | Contains v0.3 render payload. |
| `payload.base_game` | object | backend/runtime | REQUIRED_V0_3 | Cascades, golden-square, rainbow, coin, special reveals. |
| `payload.feature_mode_state` | object | backend/runtime | REQUIRED_V0_3 | Three feature modes and remaining rounds/actions. |
| `payload.bonus_buy_state` | object | backend/runtime | REQUIRED_V0_3 | Renderable buy-mode state only; wallet accounting remains outside. |
| `payload.max_win_cap` | object | backend/runtime | REQUIRED_V0_3 | Render cap state after backend cap decision. |
| `payload.round_completion` | object | backend/runtime | REQUIRED_V0_3 | Render and restore; browser cannot decide completion. |
| `payload.state_persistence` | object | backend/runtime | REQUIRED_V0_3 | Render/recovery correlation, not browser persistence truth. |
| `payload.animationHints` | array | backend/runtime or renderer hints | OPTIONAL_RENDER_HINTS | Hints may guide timing but not outcome. |

## Compatibility Rules

- Keep wallet/accounting in envelope `wallet` and `round` fields.
- Keep backend-approved feature actions in envelope `feature` fields.
- Keep restore and replay correlation in `restore`, `history`, and `state_persistence`.
- Do not let browser generate or modify `gamePayload` for production.
- Do not include donor/scaffold asset paths in payloads.

## Fallback

If `gamePayload` is rejected, use `presentationPayload.littleGangsterV03` with the same payload shape and the same backend ownership boundary.

## Current Status

Current core-protocol strict schema does not support this field today. This contract is proposed for review only.
