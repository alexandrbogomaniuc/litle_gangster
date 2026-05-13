# Volatility Profile Simulation Design

Created: 2026-05-13

This design defines how Little Gangster can run the existing 3 RTP levels across LOW, MEDIUM, and HIGH volatility profiles. It is planning and smoke-simulation material only. Values are not final, not certified, and not release math.

## Volatility Levers

LOW volatility is intended to increase hit rate while reducing top-win size and tail frequency. It raises low-symbol density, lowers high-symbol density, reduces top-cluster pay scale, slightly increases feature trigger frequency, and
lowers feature, coin, and special reveal values.

MEDIUM volatility keeps the current provisional calibration basis. It applies neutral modifiers and acts as the bridge from the existing `rtp_92`, `rtp_94`, and `rtp_96` smoke models to the new 3x3 profile matrix.

HIGH volatility is intended to reduce hit rate and push more value into the tail. It lowers low-symbol density, raises high-symbol and special-symbol density, reduces small-cluster value, raises top-cluster value, lowers feature trigger
frequency, and increases feature, coin, and special reveal values.

## Expected Effects

- Symbol weights: LOW favors low/mid symbols; HIGH favors high/special symbols.
- Cluster paytable: LOW compresses top-cluster pays; HIGH expands top-cluster pays.
- Feature trigger frequency: LOW is more frequent and smaller; HIGH is less frequent and larger.
- Free-spin and feature-mode value: LOW reduces spins/value; HIGH increases spins/value.
- Coin/special reveal values: LOW lowers reveal value; HIGH raises reveal value.
- Hit rate: LOW should be highest; HIGH should be lowest.
- Max-win frequency: LOW should be lowest; HIGH should be highest.
- Standard deviation: LOW should be lowest; HIGH should be highest.

## Simulator Design

The local non-production simulator now resolves profiles by `mathProfileId`. Each profile maps to:

- legacy RTP model id,
- RTP level,
- volatility level,
- target RTP percent,
- target return multiplier,
- history/runtime/registration profile codes.

At smoke-test time, volatility modifiers are applied in memory only. Source rule JSON files are not rewritten by this sprint.

## Current Limits

- The volatility levers are provisional planning values.
- Bonus-buy EV remains pending and is disabled for this volatility smoke.
- Cap frequency cannot be trusted at certification level from small smoke runs.
- Standard deviation bands need larger deterministic simulations.
- Registration storage for the full 3x3 matrix remains unproven.

