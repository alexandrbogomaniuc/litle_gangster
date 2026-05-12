# Free Spins And Feature Modes Module

Purpose: define server-owned feature spin and three-mode flow.

Feature modes:

- `mode_1`
- `mode_2`
- `mode_3`

Mode names are neutral placeholders until product copy is approved.

Server-owned behavior:

1. Validate feature trigger or bonus-buy entry.
2. Select or validate feature mode.
3. Initialize feature spin count.
4. Run feature-spin loop.
5. Apply cluster/cascade, golden-square, rainbow, coin, and special reveal modules.
6. Track free spins remaining.
7. Track retriggers if approved.
8. Complete feature and merge with round result.

Open blockers:

- Entry symbol/count trigger.
- Number of spins per mode.
- Retrigger rules.
- Mode-specific weights or modifiers.
- Whether player can choose mode.

History:

- Each feature spin must have its own replay snapshot and state version.

