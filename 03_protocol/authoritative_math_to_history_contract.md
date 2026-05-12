# Authoritative Math To History Contract

Status: planning contract only.

Evidence labels:

- PROVEN: v0.3 contracts already require state persistence and round completion concepts.
- PROVEN: strict fixtures include recovery and round completion states.
- CANDIDATE: `/slot/v1/gethistory` and platform history can carry or reference replay data.
- NOT_PROVEN: Little Gangster-specific history implementation.

History must be created by the authoritative server owner after each committed state transition.

Stored history payload:

- round id.
- spin id.
- session reference.
- bet and win values.
- total win, pre-cap win, capped win.
- win ratio and tier.
- starting grid.
- ordered cascade steps.
- removed, dropped, and refilled cells.
- golden-square state before and after.
- rainbow activations.
- coin reveals.
- special reveals.
- feature mode and free spin state.
- bonus-buy state.
- max-win cap event.
- round completion flag.
- state version.
- recovery snapshot.
- presentation payload snapshot or compact replay payload.

Forbidden in history:

- raw credentials.
- raw RNG secrets.
- browser-generated result authority.
- donor asset paths.

History output is required for player history, VABS/VBA, Lasthands, bot replay, and lab certification.

