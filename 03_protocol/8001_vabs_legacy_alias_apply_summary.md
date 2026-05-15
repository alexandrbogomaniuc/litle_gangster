# 8001 VABS Legacy Alias Apply Summary

Date: 2026-05-15

## Result

The Little Gangster 8001 VABS legacy alias foundation was applied to Staging source
under explicit approval.

## Implemented

- `legacyAliasTypes.ts` defines alias request/query/mapping/display/blocker types.
- `legacyAliasSecurity.ts` rejects or strips unsafe alias input and sanitizes display
  controls.
- `legacyAliasMapper.ts` maps sanitized `VIEWSESSID`, `GAMEID`, `LANG`, `TIMEZONE`,
  `hideClose`, `WHOLE_SESSION`, and `ROUNDID` style parameters.
- `legacyAliasRoutes.ts` defines guarded root and scoped alias route registration.
- History module exports were updated.
- `new-games-server/src/index.ts` now registers the guarded legacy alias routes.

## Supported Alias Routes

- root alias: `GET /vabs/show.jsp`
- scoped alias: `GET /slot/v1/8001/legacy/vabs/show.jsp`

Both require `GAMEID=8001`. Wrong game ids return blocked/not-supported responses.

## Preserved Canonical Routes

The canonical routes remain preserved:

- `POST /slot/v1/8001/history/round/:roundId`
- `POST /slot/v1/8001/history/session/:gameSessionId`
- `POST /slot/v1/8001/history/session/:gameSessionId?wholeSession=true`
- `GET /slot/v1/8001/history/render/round/:roundId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId`

## Boundaries Preserved

- Durable history storage was not implemented.
- Durable media storage was not implemented.
- Screenshot/video capture was not implemented.
- BO/CM acceptance was not tested.
- Wallet endpoints were not called.
- DB/Cassandra was not touched.
- GameClientBuilder and GameServerRegistrar were not run.
- Release/certification remain false.

## Active Blockers

- `bo_cm_alias_acceptance_untested`
- `durable_history_storage_unproven`
- `view_session_id_equivalence_unproven_for_8001`
- `exact_registration_config_field_shape_unproven`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`
