# Little Gangster v0.3 Adapter Input / Output Contract

Status: DEFINED_AS_CONTRACT_NOT_IMPLEMENTED_NOT_READY.

## Adapter Owner

The adapter must be backend/runtime-owned. It must not run in the production browser client.

## Input Contract

| Input group | Required contents | Owner | Evidence label |
|---|---|---|---|
| Authoritative result | symbols, clusters, cascades, reveals, feature state, cap state, total win | backend/runtime | REQUIRED_NOT_PROVEN_8001 |
| Wallet/accounting result | balance, previous balance, currency, reserve/settle result | backend/runtime / wallet bridge | PROVEN_GENERIC_BRIDGE |
| Round state | round ID, status, bet, win, outcome hash, completion | backend/runtime | PROVEN_GENERIC_PLUS_REQUIRED_V0_3 |
| Feature state | mode, remaining actions, next allowed actions, selected buy mode | backend/runtime | PROVEN_GENERIC_PLUS_REQUIRED_V0_3 |
| Restore/history state | state version, idempotency, unfinished round, replay snapshot | backend/runtime | PROVEN_GENERIC_BLOCKED_8001 |

## Output Contract

The adapter output should be a `/slot/v1` `RuntimeEnvelopeResponse` with:

- `wallet`: backend/accounting values only;
- `round`: canonical round ID, status, bet/win, outcome hash;
- `feature`: backend-approved action/mode state;
- `presentationPayload`: generic fields plus reviewed `gamePayload` or fallback;
- `restore`: unfinished-round state and opaque restore payload;
- `idempotency` and `retry`: backend duplicate/retry policy;
- `history`: optional replay/history payload for `gethistory` responses.

## v0.3 Render Payload Fields

| v0.3 field | Output location | Evidence label |
|---|---|---|
| `base_game.cascade_steps` | `presentationPayload.gamePayload.payload.base_game.cascade_steps` | REQUIRED_EXTENSION |
| `base_game.removed_cells`, `dropped_cells`, `new_symbols` | same payload under each cascade step | REQUIRED_EXTENSION |
| `base_game.golden_square_events` | game payload | REQUIRED_EXTENSION |
| `base_game.rainbow_activation_events` | game payload | REQUIRED_EXTENSION |
| `base_game.coin_reveals`, `special_reveals` | game payload | REQUIRED_EXTENSION |
| `feature_mode_state` | game payload plus envelope `feature` summary | REQUIRED_EXTENSION |
| `bonus_buy_state` | game payload plus envelope `feature` summary | REQUIRED_EXTENSION |
| `max_win_cap` | game payload; monetary cap reflected in `round.winMinor` | REQUIRED_EXTENSION |
| `winRatio`, `winTier` | game payload and optional generic labels/cues | REQUIRED_EXTENSION |
| `round_completion` | game payload plus envelope `round.status` | REQUIRED_EXTENSION |
| `state_persistence` | game payload plus envelope `restore`/`stateVersion` | REQUIRED_EXTENSION |
| `animationHints` | game payload or generic `animationCues` when safe | OPTIONAL |

## Non-Ready Conditions

- No Little Gangster/8001 backend package was found.
- No current source consumes the project v0.3 `math_package.json` directly.
- No schema approval exists for `gamePayload`.
- No production adapter implementation exists.
