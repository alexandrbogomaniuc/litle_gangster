# Coin Reveal Feature Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Required Result Fields

`coin_reveals[]` entries must include:

- `position`
- `tier`: `bronze`, `silver`, or `gold`
- `value_x_bet` or `value_units`
- `source_event`
- `cascade_index`

## Special Reveal Candidates

`special_reveals[]` may include `pot_of_gold` and `four_leaf_clover` as low-confidence candidates until exact donor behavior is proven. Do not treat these as release-certified math.
