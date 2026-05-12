# Current GS Registration Lane Questions

Status: open questions for GameServerRegistrar.

## Current Evidence

- Current Staging GS supports new-games redirect parameters.
- Current Staging Gamesv1 docs and new-games server support `/slot/v1/*`.
- ExtGame external endpoint support for Little Gangster is unverified.
- Legacy template support exists but is not the strongest current planning lane.

## Questions To Answer Before Generation

- Where will game 8001 be registered in current GS: `gametinfocf`, `gameinfocf`, `bankinfocf`, release-registration JSON, or another current pipeline?
- Which path is canonical for new-games registration in Staging: support UI, generated release pack, serializer/import tool, or CQL plus serializer?
- Which current GS fields route game 8001 to a game-specific client URL?
- Which current GS fields route game 8001 to the new-games API URL and GS internal base URL?
- Does game 8001 require `roundFinishedHelper` or `endRoundSignature`?
- Does game 8001 require VABS package references?
- Does game 8001 require FRB/OCB/promo flags?
- Which fields are safe metadata only, and which fields drive runtime behavior?

## Blockers

- `game_8001_registration_missing`
- `scn_serializer_missing`
- `current_gs_registration_schema_unverified`
- `extgame_lane_unverified_for_current_gs`

