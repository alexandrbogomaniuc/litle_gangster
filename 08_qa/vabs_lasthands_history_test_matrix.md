# VABS Lasthands History Test Matrix

Status: test plan only.

Required tests:

- completed base round replay.
- no-win round replay.
- single cascade replay.
- multi-cascade replay.
- golden-square replay.
- rainbow activation replay.
- coin reveal replay.
- special reveal replay.
- feature mode replay.
- bonus-buy replay.
- max-win cap replay.
- reconnect recovery replay.
- pending recovery state.

Assertions:

- event order is stable.
- final win matches authoritative result.
- cap state is preserved.
- state version increments are consistent.
- replay does not consume new RNG.
- browser cannot rewrite history.

