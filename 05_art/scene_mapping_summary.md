# Art Scene Mapping Summary

Status: completed with limitations.

## Scope

ArtSceneMapper created technical scene/object mapping artifacts for Little Gangster. These are planning artifacts only. They are not final art, not client code, not runtime integration, not asset release approval, and not release approval.

## Selected Layout

- Selected math/layout: `6x5_cluster_provisional`.
- Selected math model: `v0.2_6x5_cluster_provisional`.
- Target grid: 6 columns by 5 rows, 30 symbol cells.
- Cluster evaluation: provisional.
- The superseded 5x3 v0.1 model was not used for target scene mapping.

## Outputs

- Scene maps created: 18.
- Unique objects mapped: 140.
- Static HTML inspector created under `05_art/html_scene_inspector/`.
- Asset audit created at `05_art/asset_audit.csv`.

## Asset Policy

- Scaffold/reference assets remain blocked from release.
- No scaffold/reference asset was copied into `06_resulting_code`.
- No final art was created or approved.
- All mapped visual/audio/UI objects use placeholder references and require replacement or approval by ArtDirectionAndReplacementPlanner.

## Runtime/Math Boundaries

- Historical v0.2 scene maps originally referenced camelCase planning fields. For current v0.3 planning, canonical fields use `base_game.*`, `feature_mode_state`, `bonus_buy_state`, `totalWin`, `winRatio`, `winTier`, and `animationHints`;
see `05_art/v0_3_field_mapping_matrix.csv` and `result_schema_field_aliases.md`.
- Scene maps do not treat BSG Common Wallet payloads as client result schema.
- Wallet/accounting remains separate from result animation data.
- Backend/new-games runtime owner remains unproven.

## Next Skill

Recommended next skill: ArtDirectionAndReplacementPlanner.

## v0.3 ArtSceneMapper Update

Updated for `v0.3_donor_feature_parity_provisional`. Scene maps now include renderer-only mappings for cascade steps, removed/dropped/refilled cells, golden-square state, rainbow activation, bronze/silver/gold coin reveals, pot/clover
reveal candidates, three feature modes, bonus-buy mode selection, max-win cap state, winRatio/winTier effects, round completion, and reconnect/state persistence.

Boundary: the client renders backend/runtime result payload only. It does not generate production RNG, does not calculate authoritative wins, does not perform wallet/accounting, and does not treat registration metadata as the result schema.
Current GS result owner remains unproven; full GameClientBuilder is blocked pending runtime/result API review.
