# v0.3 Result State To Scene Mapping

This mapping links the provisional v0.3 backend/runtime result schema to Little Gangster scene maps and object IDs. It is not a browser outcome-generation design.

|Result state|Result schema field|Scene map|Primary object IDs|Notes|
|---|---|---|---|---|
|Cascade steps|base_game.cascade_steps[]|cascade_sequence, base_game_grid_6x5|cascade_removed/drop_target/new_symbol/cluster_highlight objects|mapped|
|Removed symbol cells|base_game.cascade_steps[].removed_cells|cascade_sequence|scene.base.grid.cell.c*.r*.cascade_removed|mapped|
|Dropped cells|base_game.cascade_steps[].dropped_cells|cascade_sequence|scene.base.grid.cell.c*.r*.drop_target|mapped|
|New/refilled symbols|base_game.cascade_steps[].new_symbols|cascade_sequence|scene.base.grid.cell.c*.r*.new_symbol|mapped|
|Cascade win highlights|base_game.cascade_steps[].clusters/base_game.cascade_win|cascade_sequence|scene.base.grid.cluster.highlight.*|mapped|
|Total cascade win display|base_game.total_cascade_win|cascade_sequence|scene.base.total_cascade_win_display|mapped|
|Golden-square overlays|base_game.golden_squares_before/after/events|golden_square_overlay|scene.base.grid.cell.c*.r*.golden_overlay|mapped|
|Rainbow activation|base_game.rainbow_activation_events|rainbow_activation_scene|scene.base.rainbow.activation|mapped|
|Coin reveals|base_game.coin_reveals|coin_reveal_scene|scene.base.coin_reveal.*|mapped|
|Pot/clover reveal candidates|base_game.special_reveals|coin_reveal_scene|scene.base.special_reveal.*|mapped as candidate|
|Three feature modes|feature_mode_state.mode_key|feature_mode_selection/free_spins_active|scene.feature.mode_*.panel|mapped|
|Bonus-buy selection|bonus_buy_state.selected_mode|bonus_buy_panel/feature_mode_selection|scene.bonus_buy.mode_selection|mapped|
|Max-win cap|max_win_cap|max_win_cap_scene/big_win_scene|scene.max_win.*|mapped|
|Win ratio/tier|winRatio/winTier|big_win_scene|scene.win_tier.big/huge/mega|mapped|
|Round completion|round_completion|round_completion_state|scene.round_completion.ready|mapped|
|State persistence/reconnect|state_persistence|state_recovery_reconnect_scene/reconnect_modal|scene.reconnect.restore_state|mapped|
|Runtime-owned result marker|runtime_result_owner|round_completion_state|scene.developer.runtime_result_owner_marker|mapped as developer note|
|Registration metadata boundary|registration_metadata_boundary|round_completion_state|scene.developer.registration_metadata_boundary|mapped as developer note|

## Renderer Boundary

The client consumes result fields supplied by the proven backend/runtime owner. It must not generate authoritative outcomes, production RNG, wallet/accounting mutations, or registration metadata.
