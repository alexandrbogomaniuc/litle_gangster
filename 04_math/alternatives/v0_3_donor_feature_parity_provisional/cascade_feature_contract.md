# Cascade Feature Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Required Result Fields

- `grid_before`
- `cascade_steps[]`
- `cascade_index`
- `clusters` / `winning_clusters`
- `removed_cells`
- `dropped_cells`
- `new_symbols`
- `grid_after`
- `cascade_win`
- `total_cascade_win`
- `final_grid`

## Rules

1. Evaluate connected clusters on the 6x5 board.
2. Remove winning cells.
3. Drop symbols down within each column.
4. Fill replacement symbols from the server/backend RNG source.
5. Re-evaluate until no winning clusters or max-cascade guard.

Exact donor cluster thresholds and special interactions remain provisional unless source evidence is later supplied.
