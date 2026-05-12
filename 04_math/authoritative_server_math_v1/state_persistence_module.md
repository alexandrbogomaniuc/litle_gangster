# State Persistence Module

Purpose: persist enough server state to recover without re-running RNG.

Persisted state:

- session id reference.
- round id.
- spin id when applicable.
- state version.
- request counter and idempotency references.
- bet context.
- total win and pre-cap win.
- current grid.
- cascade cursor.
- golden-square state.
- feature mode state.
- feature spins remaining.
- bonus-buy state.
- max-win cap state.
- round completion status.
- recovery snapshot.
- history snapshot reference.

Rules:

- State version increments after every authoritative transition.
- Recovery returns the last committed state.
- Duplicate requests must return idempotent result or conflict safely.
- No raw RNG secrets are stored in game payload.

