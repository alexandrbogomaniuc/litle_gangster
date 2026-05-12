# Max-Win Cap Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Required Fields

- `max_win_cap_x_bet`: 10000
- `possible_max_win_credits`
- `possible_max_win_without_bonus_buy_credits`
- `cap_reached`
- `pre_cap_win`
- `pre_cap_win_x_bet`
- `capped_win`
- `capped_win_x_bet`
- `cap_reached_at_step`
- `cap_applies_to_base`
- `cap_applies_to_feature_modes`
- `cap_applies_to_bonus_buy`

## Important Distinction

`POSSIBLE_MAX_WINS` and `CAP_WIN_MULTIPLIER` are separate concepts. Do not collapse theoretical/observed possible max win and payout cap into one field.
