# Math Runtime Integration Contract

Generated: 2026-05-11 07:45:26 

## Selected Contract
Runtime integration should target `v0.3_donor_feature_parity_provisional`.

## Proven Server/Backend Runtime Responsibilities
- Own RNG/result generation. The owner is unproven and may be classic GS, new-games backend, a game-specific server package, GS game processor, or another current runtime component.
- Evaluate 6x5 clusters and cascade steps.
- Manage golden-square state.
- Resolve rainbow activation events.
- Resolve coin and special reveal values.
- Run `mode_1`, `mode_2`, and `mode_3` feature modes.
- Apply 10,000x max-win cap.
- Emit the v0.3 result schema to the client.

## Client Boundary
The browser client renders the backend result only. Turbo and Super Turbo change animation timing, not math.

## Blocked
Runtime owner remains unproven until current GS source/config/docs identify which server/backend lane executes math and results. New-games is a candidate, not selected truth.
