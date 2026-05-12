# Scaffold Preview To Release Asset Plan

Status: planning-only art handoff.

## How To Use Scaffold Previews

Artists and developers may use scaffold previews, object IDs, and scene maps as internal reference material. Scaffold previews define placement and interaction intent, not ownership or release approval.

## Replacement Naming

Replacement assets should follow stable object IDs and scene ownership, for example:

- `scene.base.grid.cell.c1.r1.golden_overlay`
- `scene.base.coin_reveal.gold`
- `scene.feature.mode_1.panel`
- `scene.max_win.cap_overlay`

Final file naming may use an approved production convention later, but it must preserve traceability to object IDs.

## Approval Flow

1. Create original/internal-approved/licensed replacements.
2. Add ownership evidence.
3. Update `05_art/approved_assets_manifest.json`.
4. Keep blocked scaffold paths out of production manifests.
5. Run asset packaging validation before any client implementation release bundle.

## While Final Assets Are Missing

GameClientBuilder may only plan against object IDs and placeholders. It must not package scaffold asset bodies or mark the client release-ready.

