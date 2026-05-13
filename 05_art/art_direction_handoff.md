# Art Direction Handoff

## Status

ArtDirectionAndReplacementPlanner completed with release blockers preserved.

## Selected Theme

`Little Gangster: Neon Heist`

## Counts

- Scene objects: 140
- Final approved assets: 0
- Replacement required: 140
- Critical replacements: 108
- Blocked scaffold/reference objects: 135
- Placeholder/technical objects: 5

## Handoff To GameClientBuilder

GameClientBuilder may use this package for planning and interface alignment only. It must not include scaffold assets in release dist. Client build should remain release-blocked until final replacement assets are supplied and approved.

## Required Inputs For Next Stage

- `05_art/approved_assets_manifest.json`
- `05_art/asset_replacement_register.csv`
- `05_art/blocked_assets_register.csv`
- `05_art/art_direction.md`
- `05_art/html_scene_inspector/`
- `04_math/alternatives/v0_2_6x5_cluster/result_schema.json`

## Sprint Update: Donor Feature/Settings Parity (2026-05-10 19:52:26 BST)

Target feature policy is now `match_donor_features_and_settings`. Prior successful donor evidence supports a 6x5 cluster game with cascade/removal/refill behavior, golden-square cell states, rainbow activation, coin/reveal mechanics,
bonus-buy entry, separate Sound/Music settings, separate Super Turbo/Turbo settings, Info, Home, demo balance/bet controls, and 10,000x max-win messaging.

The fresh clean Playwright retry in this sprint reached an error shell and RGS/API failures, so this sprint does not claim complete feature coverage. No new asset bodies were saved. No release approvals changed.

Strict parity creates a required MathModelDesigner retry before full GameClientBuilder: the v0.2 math/result contract must be extended for cascade steps, golden-square state, rainbow/coin reveal mechanics, three feature modes, and exact
bonus-buy behavior or explicitly marked as accepted placeholders.
