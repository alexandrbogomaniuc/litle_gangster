# 8001 VABS/VBA/Lasthands Visual History Route Patch Blueprint

Status: blueprint only. No implementation applied. No Staging source modified.

Crazy Rooster / 7001 is not authoritative. Current adapter history fields are payload planning fields only; a VABS visual history route is required.

## Recommended Source Location

- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/src/games/little-gangster/history/`

## Future Files To Create

- `historyPayload.ts`
- `historyRouteContracts.ts`
- `vabsVisualHistoryRoutes.ts`
- `lasthandsMapper.ts`

## Future Route Host

- `[STAGING_SOURCE_ROOT_REDACTED]/new-games-server/src/index.ts`

## Candidate Routes

- `POST /slot/v1/games/8001/history/round`
- `POST /slot/v1/games/8001/history/session`
- `POST /slot/v1/games/8001/history/whole-session`

These names are planning candidates only. They must be reconciled with GS/backoffice/Casino Manager route expectations before implementation.

## Route Inputs

- `gameId`
- `gameKey`
- `gameSessionId`
- `playerSessionId`
- `roundId`
- `lang`
- `timeZone`
- `wholeSession`
- `hideClose`
- `fromRoundId`
- `limit`

## Route Outputs

- JSON deterministic replay payload.
- VABS display payload.
- Lasthands display payload.
- Visual replay route metadata.
- Optional HTML/URL handoff only after backoffice compatibility is proven.

## Compatibility Blockers

- Backoffice/Casino Manager access requirements are not yet proven for 8001.
- Legacy JSP `vabs/show.jsp` is evidence only, not a first-patch target.
- Screenshot/binary storage is not required unless future evidence proves a hard dependency.
- Round, session, and whole-session replay must be tested before GameClientBuilder.
