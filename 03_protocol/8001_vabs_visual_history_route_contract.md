# 8001 VABS Visual History Route Contract

Created: 2026-05-15

## Purpose

Define the future Little Gangster 8001 VABS/VBA/Lasthands route contract. This is a
planning artifact only; no route code was created.

## Required Routes

### JSON Round Replay

`POST /slot/v1/8001/history/round/:roundId`

Required inputs:

- `sessionId`
- `requestCounter`
- `currentStateVersion`
- `roundId`
- optional `lang`
- optional `timeZone`
- optional `hideClose`

Output: JSON replay response with deterministic replay payload, wallet/accounting
references, lifecycle state, `presentationPayload.gamePayload`, and visual replay URL.

### JSON Session Replay

`POST /slot/v1/8001/history/session/:gameSessionId`

Required inputs:

- `sessionId`
- `gameSessionId`
- `requestCounter`
- optional `playerSessionId`
- optional `limit`
- optional `cursor`
- optional `lang`
- optional `timeZone`

Output: JSON replay response with session-scoped history records.

### JSON Whole-Session Replay

`POST /slot/v1/8001/history/session/:gameSessionId?wholeSession=true`

Output: JSON replay response with all available session records or paginated whole
session cursor. Must include `wholeSession: true`.

### Visual Round Render

`GET /slot/v1/8001/history/render/round/:roundId`

Required query inputs:

- `sessionId` or an approved opaque server-side access reference
- optional `lang`
- optional `timeZone`
- optional `hideClose`

Output: visual HTML/render response or a render wrapper that loads the deterministic
replay payload. This route supports in-game History and backoffice viewing.

### Visual Session Render

`GET /slot/v1/8001/history/render/session/:gameSessionId`

Output: visual HTML/render response for session replay.

### Visual Whole-Session Render

`GET /slot/v1/8001/history/render/session/:gameSessionId?wholeSession=true`

Output: visual HTML/render response for whole-session replay.

## In-Game History Button

The in-game History button should use `/slot/v1/gethistory` for the list/read view and
then open either:

- JSON round replay for client-native rendering; or
- visual render route if the UI shell expects server-rendered visual history.

The route choice must be explicit in GameClientBuilder before production client work.

## Casino Manager / Backoffice Access

Casino Manager/backoffice must use visual render routes or an approved wrapper URL.
Backoffice compatibility remains blocked until current GS/CM access, authorization, and
URL parameter expectations are proven.

## Error Responses

Use typed error responses for:

- invalid session
- missing round
- missing session
- history storage unavailable
- visual route not implemented
- blocked/missing replay payload

Errors must not expose raw tokens, private URLs, stack traces, or wallet secrets.

## Evidence Storage Policy Addendum

Every route response should be compatible with the evidence policy:

- deterministic replay payload is required and authoritative;
- visual HTML/render route is required for History and CM/backoffice;
- screenshot references are optional supporting evidence;
- video references are optional high-storage supporting evidence;
- media manifest references may be included even when media arrays are empty;
- durable media storage is not implemented by this planning sprint.

Sanitized legacy route-shape evidence requires support for session id equivalent,
game id, language, time zone, and hide-close display controls. Raw URLs and raw
identifiers must not be persisted in planning docs or route logs.
