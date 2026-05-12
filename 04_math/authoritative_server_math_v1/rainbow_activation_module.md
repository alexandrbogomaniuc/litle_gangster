# Rainbow Activation Module

Purpose: represent rainbow activation events and their impact on symbol, coin, or special reveal states.

Server-owned behavior:

- Determine activation eligibility.
- Consume RNG only when activation rules require.
- Record affected cells and resulting state changes.
- Emit render event for rainbow animation.

State fields:

- activation id.
- source cell or trigger.
- affected cells.
- created/revealed symbols or values.
- linked golden-square cells.

Open blockers:

- Exact trigger source.
- Exact probability.
- Exact effect in base versus feature modes.

Client boundary:

- Browser renders activation effects only from payload.

