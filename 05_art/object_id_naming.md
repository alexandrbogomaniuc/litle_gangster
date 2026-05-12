# Object ID Naming System

## Rule

Use stable, searchable IDs in this pattern:

`scene.<scene_or_mode>.<category>.<detail>[.c{column}.r{row}|.<state>]`

## Grid Coordinates

- Columns are 1-based: `c1` through `c6`.
- Rows are 1-based: `r1` through `r5`.
- Base game cell example: `scene.base.grid.cell.c1.r1`.
- Free-spins cell example: `scene.free_spins.grid.cell.c6.r5`.

## Symbol State IDs

- Idle state example: `scene.base.symbol.lg_wild.idle`.
- Win state example: `scene.base.symbol.lg_scatter.win`.
- Symbol IDs are math/planning IDs only; they are not final release asset names.

## UI Examples

- `scene.base.panel.spin_button`
- `scene.base.panel.bet_display`
- `scene.base.panel.balance_display`
- `scene.base.panel.menu_button`
- `scene.bonus_buy.panel.buy_button`
- `scene.big_win.counter.amount`
- `scene.settings.modal.root`
- `scene.rules.modal.root`

## Safety Rules

- Do not reuse donor/scaffold filenames as release IDs.
- Do not mark any placeholder or scaffold object as approved for release.
- ArtDirectionAndReplacementPlanner must replace or explicitly approve every asset before release.
