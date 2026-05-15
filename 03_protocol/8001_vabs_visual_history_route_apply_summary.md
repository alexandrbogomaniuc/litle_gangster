# 8001 VABS Visual History Route Apply Summary

Date: 2026-05-15

## Result

The Little Gangster 8001 VABS/VBA/Lasthands visual history route foundation was
implemented in Staging source under the approved limited scope.

Implemented source location:

- `new-games-server/src/games/little-gangster/history/`

Guarded route registration:

- `new-games-server/src/index.ts`

## Implemented Foundation

- Deterministic replay/history payload builder.
- JSON round replay response foundation.
- JSON session replay response foundation.
- Whole-session replay flag representation.
- Safe visual HTML replay shell.
- Media manifest support with default `deterministic_replay_only` mode.
- Storage provider interface and non-production in-memory fixture provider.
- Durable storage blocked provider.
- History security helpers for language, timezone, hide-close, unsafe text, and HTML
  escaping.
- Route registration for guarded 8001 history routes.
- Safe non-production fixtures only.

## Route Shapes

- `POST /slot/v1/8001/history/round/:roundId`
- `POST /slot/v1/8001/history/session/:gameSessionId`
- `POST /slot/v1/8001/history/session/:gameSessionId?wholeSession=true`
- `GET /slot/v1/8001/history/render/round/:roundId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId`

The route foundation supports legacy-style parameters conceptually:

- `lang`
- `timeZone`
- `hideClose`
- `wholeSession`
- `gameId`
- `gameSessionId` / view-session equivalent
- `roundId`

## Preserved Boundaries

- No durable DB/object storage was implemented.
- No screenshot capture was implemented.
- No video capture was implemented.
- No wallet endpoint was called.
- No registration artifact was generated.
- No GameClientBuilder work was performed.
- No GameServerRegistrar generation was performed.
- No release or certification approval occurred.

## Active Blockers

- `durable_history_storage_unproven`
- `durable_media_storage_not_implemented`
- `screenshot_capture_not_implemented`
- `video_capture_not_implemented`
- `backoffice_cm_vabs_compatibility_unproven`
- `vabs_runtime_wallet_history_tests_missing`
- `wallet_launch_history_tests_missing`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`
