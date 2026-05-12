# Restart / FRB / OCB / Promo Checklist

Status: advisory checklist; no feature/promo support selected by this file.

## Current Source Signals

| Topic | Evidence | Current interpretation |
|---|---|---|
| Restart | `IGameServer.java:28` exposes `restartGame`; `StartGameSessionHelper.java:87-99` exposes `restartGame4FRB`. | Restart exists in GS, but Little Gangster's current-lane restart behavior is not proven. |
| Resume | `/slot/v1/resumegame` exists in `new-games-server/src/index.ts:1829-1877`. | New-games lane has a resume endpoint. |
| FRB configs | Staging bank/config exports and source include FRB manager class/property signals. | FRB exists as GS concept; 8001 requirement/support is unverified. |
| OCB / cash bonus | Source search found Cash Bonus and OCB-adjacent signals in GS/promo code. | Treat as promo checklist only until current GS/product scope confirms it. |

## Future Validation Items

- Determine whether Little Gangster supports FRB.
- Determine whether Little Gangster supports OCB/cash bonus.
- Determine whether buy feature is distinct from FRB/OCB.
- Verify restart behavior after FRB finished, canceled, expired, or capped states if those states apply.
- Verify `/slot/v1/resumegame` restores pending collect, feature mode, cap state, and animation state without duplicate settlement.
- Verify `closegame` or `closeSession` equivalent for session exit/accounting.

## Product Decisions Pending

- `frb_ocb_promo_support_decision_pending`
- `restart_game_required_for_current_lane_unverified`
- `bonus_buy_vs_promo_boundary_unverified`

