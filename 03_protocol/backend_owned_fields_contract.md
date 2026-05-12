# Backend-Owned Fields Contract

Status: REQUIRED_BOUNDARY.

The browser/client must not produce or override authoritative runtime fields.

## Backend-Owned Fields

| Field group | Examples | Evidence label | Client role |
|---|---|---|---|
| RNG and outcome | RNG draws, symbol outcome, grid generation, cascade decisions | PROVEN_BOUNDARY | Render only |
| Win calculation | cluster wins, cascade wins, total win, cap application | REQUIRED_FOR_V0_3 | Render only |
| Wallet/accounting | reserve, settle, balance, currency, net effect | PROVEN_GENERIC | Display returned values only |
| Round authority | round ID, round status, outcome hash, round completion | PROVEN_GENERIC | Render state and send allowed actions |
| Feature authority | mode, remaining actions, buy feature state, next allowed actions | PROVEN_GENERIC_PLUS_EXTENSION | Render and send user choices |
| State persistence | state version, restore payload, unfinished round, history | PROVEN_GENERIC_BLOCKED_FOR_8001 | Restore display only |
| Registration metadata | game ID, route, RTP display, bet limits, flags | PROVEN_BOUNDARY | Read config only |

## Browser Must Never Author

- `base_game.grid_before`
- `base_game.cascade_steps`
- `base_game.final_grid`
- `base_game.golden_squares_after`
- `base_game.rainbow_activation_events`
- `base_game.coin_reveals`
- `feature_mode_state`
- `bonus_buy_state` accounting or purchased start state
- `max_win_cap`
- `winRatio`
- `winTier`
- `round_completion`
- `state_persistence`
- `wallet_accounting_boundary`

## Allowed Browser Inputs

The browser may send user intent only:

- selected bet;
- feature action selection;
- bonus-buy confirmation intent;
- close/resume/history request;
- client operation ID/idempotency key when required.

The backend must validate every input and emit the authoritative result.

