# Operator Profile Selection Contract

Created: 2026-05-13T08:55:01Z

Operators select from approved `rtpLevel` and `volatilityLevel` values only. The selection must resolve to a pretested `mathProfileId` before a round is executed.

## Input

- `rtpLevel`: one of `LOW`, `MEDIUM`, `HIGH`.
- `volatilityLevel`: one of `LOW`, `MEDIUM`, `HIGH`.
- Optional operator/casino profile reference if the current GS lane supports it.

## Resolution

The backend or configuration layer resolves `(rtpLevel, volatilityLevel)` to `mathProfileId`. The resolved profile includes registration, runtime, and history profile codes.

## Restrictions

- No arbitrary RTP percentages.
- No arbitrary volatility values.
- No profile mutation by client/browser.
- No executable math import from registration.
- Any value outside 92.00%-99.00% is blocked unless explicitly approved.

## Little Gangster Blockers

- `gs_profile_matrix_storage_unproven`
- `volatility_profile_specific_simulation_pending`
- `bonus_buy_ev_pending`
