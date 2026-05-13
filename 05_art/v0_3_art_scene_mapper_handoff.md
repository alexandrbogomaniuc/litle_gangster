# v0.3 ArtSceneMapper Handoff

## Completed

- Added v0.3 object/state IDs for cascades, golden squares, rainbow activation, coin reveals, special reveal candidates, feature modes, bonus-buy selection, max-win cap, win tiers, round completion, and reconnect/state persistence.
- Updated required scene maps to reference `v0.3_donor_feature_parity_provisional` and the v0.3 result schema.
- Added dedicated v0.3 scene maps for cascade, golden-square, rainbow, coin/special reveal, feature modes, max-win cap, round completion, and state recovery.
- Updated the HTML scene inspector as a static local planning tool with v0.3 layers and renderer-only boundary notes.

## Counts

- Object count before: 140
- Object count after: 288
- New v0.3 objects added: 148

## Boundaries

Client rendering is not outcome authority. Browser-side RNG/result generation remains forbidden. Wallet/accounting and registration metadata remain separate from animation rendering. Full GameClientBuilder is still blocked until the
current-GS runtime result API contract is reviewed.
