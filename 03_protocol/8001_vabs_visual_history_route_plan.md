# 8001 VABS Visual History Route Plan

Date: 2026-05-15
Status: planning only, no route implementation

## Purpose

The VABS/VBA/Lasthands route layer must expose deterministic Little Gangster 8001 replay data to in-game history, backoffice/Casino Manager history,
round
replay, session replay, whole-session replay, and last-hand recovery.

## Route/API Planning

| Route category | Purpose | Required inputs | Required output |
| --- | --- | --- | --- |
| Round replay | Render one round. | `gameSessionId`, `roundId`, `gameId`, `lang`, `timeZone` | deterministic replay payload and visual rendering
payload or URL |
| Whole-session replay | Render full session. | `gameSessionId`, `wholeSession=true`, `gameId`, `lang`, `timeZone` | ordered action/round replay
payloads |
| Session replay | Render bounded session history. | `gameSessionId`, start/end or page params, `gameId`, `lang`, `timeZone` | session history list
and replay route references |
| In-game History button | Player-facing history access. | safe session identity, `hideClose` if required, `lang`, `timeZone` | safe history URL or
embedded replay payload |
| Casino Manager/backoffice | Operator-facing history. | `gameSessionId`, `playerSessionId` if applicable, `roundId`, date range | route to
VABS/VBA-compatible replay |
| Last hand | Recover latest hand for reconnect/review. | player/session identity, game id | latest replayable hand or unfinished state |

## Required Route Fields

- `lang`
- `timeZone`
- `wholeSession`
- `hideClose`
- `gameSessionId`
- `playerSessionId` if applicable
- `roundId`
- `gameId`
- `gameKey`
- `schemaVersion`

## Deterministic Replay Payload

The route must use `8001_history_payload_schema.json` and include:

- action sequence;
- cascade sequence;
- feature state;
- wallet/accounting references;
- replay seed or deterministic references;
- round completion;
- cap state;
- VABS display data;
- Lasthands display data;
- visual replay route references.

## Visual Rendering Payload or URL

The implementation may return a rendered URL or a payload for renderer-side reconstruction. Either approach must keep RNG/result authority server-side
and
must not rely on browser-generated wins.

## Screenshot/Binary Policy

Screenshot or binary storage is not required for this plan. Prefer deterministic replay payloads. Add binary/screenshot storage only if future VABS
evidence
proves it is required.

## Blocker List

- `vabs_visual_history_route_required`
- `vba_backoffice_route_unproven`
- `lasthands_runtime_storage_unproven_for_8001`
- `round_replay_unproven_for_8001`
- `session_replay_unproven_for_8001`
- `whole_session_replay_unproven_for_8001`
- `history_button_route_unproven`
- `wallet_accounting_references_unvalidated`
- `bonus_buy_vabs_lasthands_test_pending`
