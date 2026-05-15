# Future Project ExtGame / GS Lessons Checklist

Created: 2026-05-15

## Visual History Route Resolution

- Run a VABS/VBA/Lasthands route-resolution audit before implementation.
- Check legacy GS/global routes, new-games routes, Gamesv1/client History behavior,
  Casino Manager/backoffice access, and registration/bootstrap settings.
- Use evidence labels: `PROVEN_SOURCE`, `LIKELY_SOURCE`, `CANDIDATE_SOURCE`,
  `NOT_FOUND`, and `BLOCKED`.
- Stored JSON replay does not prove visual history completion unless current
  GS/backoffice evidence explicitly accepts JSON-only replay.
- Client History buttons must use bootstrap/configured or backend-generated route data,
  not guessed hardcoded paths.
- GameServerRegistrar must block generation if visual history URL/config fields are
  unresolved.

## Runtime / Accounting Checklist

- process-transaction-equivalent behavior must be proven for every action/spin.
- Balance must come from settlement/process responses, not repeated balance polling.
- Runtime must persist state for reconnect, restart, pending action, and recovery.
- `roundFinished` and end-round signatures must be derived from game state.
- FRB/restart flows must be implemented only against proven current GS behavior.

## Registration / Release Checklist

- SD_KEYS must identify math profile/RTP/SD, not feature names.
- FeatureKPI names must match platform-approved categories.
- CAP_WIN_MULTIPLIER must be enforced server-side and apply to bonus buy by base bet.
- POSSIBLE_MODELS must cover max supported strategy RTP, including BF_RTP where present.
- GL bet calculation and cluster base-bet compatibility must be explicit.
- LQA, licensee acceptance, wallet tests, visual history tests, and release audit remain
  gates before release.
