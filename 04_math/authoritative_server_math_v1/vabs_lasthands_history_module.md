# VABS Lasthands History Module

Purpose: define authoritative history storage for player review, VABS/VBA, Lasthands, replay, and lab certification.

Store per round/spin:

- round id.
- spin id.
- session reference.
- bet.
- win.
- total win.
- pre-cap win.
- capped win.
- win ratio and tier.
- starting grid.
- every cascade step.
- removed cells.
- dropped/refilled symbols.
- golden-square state before and after.
- rainbow activation events.
- coin reveals.
- special reveals.
- feature mode state.
- free spins remaining.
- bonus-buy state.
- RNG audit references, not raw RNG secrets.
- state version.
- round completion flag.
- recovery snapshot.
- presentation payload snapshot or compact replay payload.
- compliance metadata.

Needed for player history:

- readable bet, win, feature, and replay summary.

Needed for VABS/Lasthands:

- deterministic replay payload.
- ordered event list.
- final accounting references outside game payload.

Needed for lab certification:

- model version.
- RNG draw references.
- simulation seed batch references.
- cap hit and feature distribution.

Do not store:

- raw player credentials.
- raw RNG seeds or secrets.
- wallet secrets.
- browser-generated result authority.
- donor asset paths.

