# VABS History Screenshot Replay Decision

Status: planning decision.

Decision:

- Prefer deterministic replay payload over screenshot binary storage unless current GS/product evidence proves screenshot or thumbnail storage is required.

Reason:

- Current project evidence proves VABS/VBA/Lasthands/history concepts and `/slot/v1/gethistory` planning, but does not prove a Little Gangster-specific screenshot storage requirement.
- v0.3 strict fixtures and `presentationPayload.gamePayload` can carry enough render state for deterministic replay planning.
- Screenshot binaries would add storage, privacy, and export-sanitization risk without proof they are required.

Required replay payload:

- starting grid.
- cascade steps.
- final grid.
- golden/rainbow/coin/special reveal state.
- feature mode state.
- bonus-buy state.
- free-spins state.
- jackpot state only if enabled.
- cap and win tier.
- recovery snapshot.
- audit references.

Blocker retained:

- `vabs_screenshot_requirement_unverified`.

Implementation status:

- No history implementation created.
- No screenshot assets captured.
- No binary replay storage created.

## Simulation Config Refinement Update

The simulation package includes a deterministic replay snapshot template and sample replay output. Replay remains preferred over screenshot binary storage. Screenshot requirement status remains `unverified`; do not store screenshots unless
direct GS/product/compliance evidence requires it.
