# Server Result Owner Decision

Recommended owner: future Little Gangster server-side math/runtime module.

Preferred placement:

- CANDIDATE: `new-games-server/src/games/little-gangster/` for first backend adapter and math ownership integration.
- CANDIDATE: future `Gamesv1/games/8001` package only if platform ownership chooses a per-game package model.
- BLOCKED: browser/client result generation.
- BLOCKED: registration metadata as executable math.

Acceptance requirements before owner is proven:

- Approved source target for Little Gangster runtime owner.
- Implemented and tested authoritative result generator.
- Server-side RNG draw audit model.
- State persistence and recovery contract implemented.
- History / Lasthands / VABS storage implemented.
- Runtime adapter maps server result to `presentationPayload.gamePayload`.
- Certification simulation outputs generated.
- Wallet/accounting remains outside game payload.

Why browser ownership is forbidden:

- Browser output is player-controlled and cannot own production RNG, win evaluation, cap logic, feature mode outcomes, or history truth.
- Browser may render cascades, overlays, win tiers, and replay states only from server-provided payloads.

Why registration cannot import math:

- Registration config describes routing, IDs, enabled features, RTP metadata, and launch wiring.
- It must not instantiate RNG, evaluate wins, select features, or produce authoritative outcomes.

7001 caveat:

- 7001 may inform code structure and mapper style only.
- 7001 must not be copied as Little Gangster math truth.

