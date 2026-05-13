# Art Direction Feature Parity Update

## Decision
Little Gangster must preserve the original Neon Heist art direction while matching donor settings/features as closely as technically possible.

## New Required Updates From Donor Parity
- Add Super Turbo as a named setting separate from Turbo.
- Add Music toggle separate from Sound.
- Add Home/Lobby menu action.
- Treat cascade, golden-square, rainbow activation, coin reveal, pot/clover reveal, and three feature modes as required parity targets.
- Treat generic scatter/free-spin v0.2 assumptions as placeholders requiring revision.
- Treat double-up/gamble as out of donor evidence and requiring product decision before it remains in scope.

## Asset Policy
Scaffold assets remain internal-only references. Final art must be original, internally approved, or explicitly licensed. No scaffold asset is release-approved.

## Next Dependency
MathModelDesigner retry is recommended before full GameClientBuilder so the feature/result contract can support the donor-equivalent scene plan.


## v0.3 Math Contract Update
Generated: 2026-05-11 07:45:26 

Art direction remains Little Gangster / Neon Heist, but replacement art now needs explicit support for v0.3 cascade removal/refill, golden-square overlays, rainbow activation, bronze/silver/gold coin reveals, pot/clover special reveal
candidates, and three feature mode treatments. Scaffold assets remain internal reference only and blocked from release.

## v0.3 Contract Completion Update - 2026-05-11 11:05:00 Europe/London

The selected math/result contract is now `v0.3_donor_feature_parity_provisional`. ArtSceneMapper was not run in this sprint, so scene-map JSON remains a planning baseline. A later ArtSceneMapper update is required to map explicit v0.3
states: cascade steps, golden-square overlays, rainbow activation, coin reveal tiers, pot/clover reveal candidates, three feature modes, max-win cap event, round completion, and persistence/reconnect state. GameClientBuilder remains blocked
until that update and runtime-contract review are complete.

## v0.3 ArtSceneMapper Update

Updated for `v0.3_donor_feature_parity_provisional`. Scene maps now include renderer-only mappings for cascade steps, removed/dropped/refilled cells, golden-square state, rainbow activation, bronze/silver/gold coin reveals, pot/clover
reveal candidates, three feature modes, bonus-buy mode selection, max-win cap state, winRatio/winTier effects, round completion, and reconnect/state persistence.

Boundary: the client renders backend/runtime result payload only. It does not generate production RNG, does not calculate authoritative wins, does not perform wallet/accounting, and does not treat registration metadata as the result schema.
Current GS result owner remains unproven; full GameClientBuilder is blocked pending runtime/result API review.
