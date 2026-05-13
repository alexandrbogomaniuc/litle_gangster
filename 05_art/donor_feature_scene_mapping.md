# Donor Feature Scene Mapping

## Mapping Policy
All donor-observed settings/features must have a Little Gangster scene/object equivalent, or be explicitly blocked.

## Critical Scene Requirements
- Base scene must remain 6x5 cluster layout.
- Add/retain cascade visual states for symbol removal/drop-down/refill.
- Add golden-square cell-highlight states to grid-cell objects.
- Treat rainbow-equivalent special symbol as a Little Gangster original heist-themed trigger, not donor art reuse.
- Add coin/reveal visual states for bronze/silver/gold/pot/clover-equivalent feature outcomes using original Little Gangster assets.
- Keep Bonus Buy visible and map confirmation/purchase flow once math/flow evidence is available.
- Keep Sound and Music as separate settings controls.
- Add Super Turbo as a distinct donor-parity setting from Turbo.
- Keep Home/Lobby action in settings, with runtime behavior owned by launch/GS flow.

## Scene Map Update Decision
No scene-map JSON files were changed in this sprint because the current maps already contain the core 6x5 grid, settings, bonus-buy, free-spins, big-win, error, reconnect, desktop, and mobile scaffolds. However, their notes and future
implementation contracts must be updated by the next MathModelDesigner/GameClientBuilder work to include cascade/golden-square/rainbow/coin feature states.

Scene map update required now: false. Runtime/result schema update required before full build: true.

## v0.3 Contract Completion Update - 2026-05-11 11:05:00 Europe/London

The selected math/result contract is now `v0.3_donor_feature_parity_provisional`. ArtSceneMapper was not run in this sprint, so scene-map JSON remains a planning baseline. A later ArtSceneMapper update is required to map explicit v0.3
states: cascade steps, golden-square overlays, rainbow activation, coin reveal tiers, pot/clover reveal candidates, three feature modes, max-win cap event, round completion, and persistence/reconnect state. GameClientBuilder remains blocked
until that update and runtime-contract review are complete.

## v0.3 ArtSceneMapper Update

Updated for `v0.3_donor_feature_parity_provisional`. Scene maps now include renderer-only mappings for cascade steps, removed/dropped/refilled cells, golden-square state, rainbow activation, bronze/silver/gold coin reveals, pot/clover
reveal candidates, three feature modes, bonus-buy mode selection, max-win cap state, winRatio/winTier effects, round completion, and reconnect/state persistence.

Boundary: the client renders backend/runtime result payload only. It does not generate production RNG, does not calculate authoritative wins, does not perform wallet/accounting, and does not treat registration metadata as the result schema.
Current GS result owner remains unproven; full GameClientBuilder is blocked pending runtime/result API review.
