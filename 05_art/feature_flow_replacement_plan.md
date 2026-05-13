# Feature Flow Replacement Plan

## Required Donor-Parity Flows
- Loading / click-to-continue.
- Base idle 6x5 cluster scene.
- Safe demo spin flow and backend-authoritative result display.
- Super cascade: winning cluster removal and drop-down refill.
- Golden-square / win-to-win cell state.
- Rainbow-equivalent special symbol activation.
- Coin/reveal feature with bronze/silver/gold/pot/clover-equivalent outcomes.
- Three feature/free-spin modes.
- Bonus-buy button, confirmation, and purchased feature start.
- Big-win / win-tier presentation.
- Error and reconnect modal flows.

## Flows Still Blocked
- Exact donor bonus-buy confirmation/cost/EV flow.
- Natural free-spins intro/active/outro/retrigger flow.
- Autoplay panel and stop conditions.
- Mobile playable flow.
- Full win/no-win/cluster animation sequence.

## Release-Safe Replacement Direction
Every donor visual/audio cue must be replaced with original Little Gangster assets: vault lights, marked cash, neon alley signage, safe-dial effects, original symbol art, original SFX/music, and original win-tier animations.


## v0.3 Math Handoff Update
Generated: 2026-05-11 07:45:26 

The selected math/result contract is now `v0.3_donor_feature_parity_provisional`. ArtSceneMapper should update scene/object maps for explicit cascade-step, golden-square, rainbow-activation, coin-reveal, pot/clover-candidate, feature-mode,
and max-win-cap animation states before GameClientBuilder.

## v0.3 Contract Completion Update - 2026-05-11 11:05:00 Europe/London

The selected math/result contract is now `v0.3_donor_feature_parity_provisional`. ArtSceneMapper was not run in this sprint, so scene-map JSON remains a planning baseline. A later ArtSceneMapper update is required to map explicit v0.3
states: cascade steps, golden-square overlays, rainbow activation, coin reveal tiers, pot/clover reveal candidates, three feature modes, max-win cap event, round completion, and persistence/reconnect state. GameClientBuilder remains blocked
until that update and runtime-contract review are complete.

## v0.3 ArtSceneMapper Update

Updated for `v0.3_donor_feature_parity_provisional`. Scene maps now include renderer-only mappings for cascade steps, removed/dropped/refilled cells, golden-square state, rainbow activation, bronze/silver/gold coin reveals, pot/clover
reveal candidates, three feature modes, bonus-buy mode selection, max-win cap state, winRatio/winTier effects, round completion, and reconnect/state persistence.

Boundary: the client renders backend/runtime result payload only. It does not generate production RNG, does not calculate authoritative wins, does not perform wallet/accounting, and does not treat registration metadata as the result schema.
Current GS result owner remains unproven; full GameClientBuilder is blocked pending runtime/result API review.
