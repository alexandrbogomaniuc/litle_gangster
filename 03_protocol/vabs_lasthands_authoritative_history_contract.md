# VABS Lasthands Authoritative History Contract

Status: planning contract only.

VABS / VBA / Lasthands payload must be derived from server-authoritative math state.

Required replay layers:

- summary row for round listing.
- detailed round payload for replay.
- ordered event list for cascades and features.
- compact presentation payload snapshot for renderer replay.
- audit references for certification.

Minimum fields:

- round id.
- state version.
- bet.
- total win.
- pre-cap win.
- capped win.
- win tier.
- grids and cascade steps.
- feature mode state.
- free spins remaining.
- bonus-buy state.
- max-win cap state.
- recovery snapshot.
- completion reason.

Compliance rule:

- Store references needed to verify RNG sequence, not raw secrets.
- Do not store private player identifiers in public or renderer payloads.
- Keep wallet/accounting references outside `gamePayload`.

Implementation remains blocked until an approved history storage target exists.

