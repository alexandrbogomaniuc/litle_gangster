# Win-Tier Module

Purpose: classify display win tiers from authoritative win ratio.

Server-owned or adapter-owned display output:

- `winRatio`
- `winTier`
- optional threshold metadata.

Suggested tiers:

- `none`
- `small`
- `big`
- `huge`
- `mega`
- `max_win`

Rules:

- Tier classification must not change payout.
- Thresholds must come from approved product configuration.
- History stores ratio and tier for replay.

Open blocker:

- Final tier thresholds.

