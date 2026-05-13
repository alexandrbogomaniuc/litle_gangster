# Little Gangster Art Direction

Status: original art direction created with release blockers preserved.

## Direction Name

`Little Gangster: Neon Heist`

## Core Idea

Little Gangster should feel like a stylized cartoon city-heist slot: a compact crew, a glowing alley, a casino backroom, and a vault job about to start. The reference/scaffold material may guide layout density, 6x5 readability, feature
hierarchy, and UI scale, but no donor/scaffold art is approved for release.

## Visual Pillars

1. **Readable 6x5 cluster board**: large silhouettes, high contrast, fast symbol recognition, strong cluster highlight overlays.
2. **Original heist identity**: neon city, vault metal, cash/gold accents, cartoon crime caper mood, no direct donor composition copying.
3. **Premium arcade clarity**: saturated highlights, bold outlines, strong button affordances, clear mobile-safe controls.
4. **Feature drama**: Free spins become `Heist Mode`; bonus buy becomes `Start the Job`; big wins become `Vault Break` effects.

## Palette

- Night ink: #151820
- Alley teal: #13b6a6
- Vault gold: #f4c84a
- Signal red: #d94b3d
- Smoke gray: #6f7580
- Cream UI text: #f6edd7

## Shape Language

- Rounded art silhouettes with bold comic outlines.
- UI panels use metal/vault trim and neon tube accents.
- Symbols must read at small mobile size inside 6 columns x 5 rows.
- Cluster highlights should be luminous outlines, not line-pay overlays.

## Scaffold References For Internal Planning Only

- Background layout reference: `02_reference_assets/authorized_raw/playwright_20260510T094437Z/iteration_3/1309_1.23.0_assets_default_common_atlas_background.jpg`
- Symbol/atlas density reference: `02_reference_assets/authorized_raw/playwright_20260510T094437Z/iteration_3/1309_1.23.0_assets_default_common_atlas_symbols.atlas`
- Wild animation reference: `02_reference_assets/authorized_raw/playwright_20260510T094437Z/iteration_3/1309_1.23.0_assets_default_common_spine_wild.json`
- Scatter/bonus trigger reference: `02_reference_assets/authorized_raw/playwright_20260510T094437Z/iteration_3/1309_1.23.0_assets_default_common_spine_special.json`
- UI control/frame reference: `02_reference_assets/authorized_raw/playwright_20260510T094437Z/iteration_3/1309_1.23.0_assets_default_common_atlas_misc.atlas`
- Big win tier reference: `02_reference_assets/authorized_raw/playwright_20260510T094437Z/iteration_3/1309_1.23.0_assets_default_common_spine_win_tiers.json`

All paths above are internal scaffold references only and remain `blocked_from_release`.

## Release Boundary

Final release assets must be original, internally approved, or explicitly licensed. Scaffold assets must not be moved to `06_resulting_code` and must not be shipped.

## Sprint Update: Donor Feature/Settings Parity (2026-05-10 19:52:26 BST)

Target feature policy is now `match_donor_features_and_settings`. Prior successful donor evidence supports a 6x5 cluster game with cascade/removal/refill behavior, golden-square cell states, rainbow activation, coin/reveal mechanics,
bonus-buy entry, separate Sound/Music settings, separate Super Turbo/Turbo settings, Info, Home, demo balance/bet controls, and 10,000x max-win messaging.

The fresh clean Playwright retry in this sprint reached an error shell and RGS/API failures, so this sprint does not claim complete feature coverage. No new asset bodies were saved. No release approvals changed.

Strict parity creates a required MathModelDesigner retry before full GameClientBuilder: the v0.2 math/result contract must be extended for cascade steps, golden-square state, rainbow/coin reveal mechanics, three feature modes, and exact
bonus-buy behavior or explicitly marked as accepted placeholders.
