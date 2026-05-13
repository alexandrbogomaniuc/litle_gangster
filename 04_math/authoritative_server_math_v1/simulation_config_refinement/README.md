# Authoritative Simulation Config Refinement

This artifact is planning and local simulation material only. It is not production math, not backend adapter code, not registration output, not wallet integration, not client code, and not release approval. Exact values are not final or
certified.


Created: 2026-05-12 14:05:14

This package turns the prior authoritative math design into concrete, simulation-ready structures for local smoke testing. It connects 6x5 cluster math, RTP model profiles, GL game settings, bonus buy, free spins, feature modes, max-win
cap, jackpot hooks, VABS/VBA/Lasthands replay payloads, backend adapter input expectations, and registration metadata mapping.

## Scope

- RTP models represented: `rtp_96`, `rtp_94`, `rtp_92`.
- Jackpot hooks are represented but `jackpotEnabled` is false by default.
- Bonus buy is represented with candidate cost multipliers, while EV remains blocked pending simulation.
- Deterministic replay payload is preferred over screenshot binaries. Screenshot requirement remains unverified.
- The local simulator is non-production and uses deterministic pseudo-rounds for smoke checks only.

## Not In Scope

- Production backend adapter implementation.
- Gamesv1/games/8001 package creation.
- Registration artifact generation.
- Wallet, DB, GS, or browser execution.
- Certification claims or final RTP values.
