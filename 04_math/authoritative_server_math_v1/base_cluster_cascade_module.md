# Base Cluster Cascade Module

Purpose: evaluate the base 6x5 cluster game and cascade sequence.

Input:

- Server bet context.
- Approved paytable.
- Symbol weights.
- Current grid or generated grid request.
- Golden-square state if present.
- Feature context if inside feature spins.

Server-owned steps:

1. Generate or accept persisted starting grid.
2. Evaluate orthogonal clusters.
3. Calculate cluster wins.
4. Remove winning cells.
5. Drop symbols downward.
6. Consume RNG for refill cells.
7. Repeat until no winning cluster or max cascade guard.
8. Emit cascade step records.

Output:

- Starting grid.
- Cascade steps with removed, dropped, refilled, and resulting grid states.
- Cluster win records.
- Cumulative win before cap.
- State updates for downstream modules.

Blockers:

- Exact symbol distribution.
- Final paytable and wild behavior.
- Maximum cascade guard policy.

