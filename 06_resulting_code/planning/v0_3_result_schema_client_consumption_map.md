# v0.3 Result Schema Client Consumption Map

Status: planning-only. Runtime payload must be proven before implementation.

|v0_3_result_field|client_scene_or_object|animation_state|required_for_rendering|source_scene_map|runtime_owner_required|notes|
|---|---|---|---|---|---|---|
|`base_game.cascade_steps`|cascade sequence layer|cascade sequence|yes|`05_art/scene_maps/cascade_sequence.json`|yes|Drives ordered cascade playback.|
|`base_game.cascade_steps[].removed_cells`|`scene.base.grid.cell.c*.r*.cascade_removed`|cascade remove|yes|`cascade_sequence.json`|yes|Cell removal is backend-authored.|
|`base_game.cascade_steps[].dropped_cells`|`scene.base.grid.cell.c*.r*.drop_target`|cascade drop|yes|`cascade_sequence.json`|yes|Drop path is renderer-only.|
|`base_game.cascade_steps[].new_symbols`|`scene.base.grid.cell.c*.r*.new_symbol`|cascade refill|yes|`cascade_sequence.json`|yes|New symbols must come from result payload.|
|`base_game.cascade_steps[].clusters`|`scene.base.grid.cluster.highlight.*`|cluster highlight|yes|`cascade_sequence.json`|yes|No client cluster re-evaluation.|
|`base_game.golden_squares_before`|golden overlay cells|pre-cascade state|yes|`golden_square_overlay.json`|yes|Used to render persisted state.|
|`base_game.golden_square_events`|golden overlay cells|golden square event|yes|`golden_square_overlay.json`|yes|Client only displays events.|
|`base_game.golden_squares_after`|golden overlay cells|post-cascade state|yes|`golden_square_overlay.json`|yes|Backend owns persistence.|
|`base_game.rainbow_activation_events`|`scene.base.rainbow.activation`|rainbow activate|yes|`rainbow_activation_scene.json`|yes|Exact behavior remains provisional.|
|`base_game.coin_reveals`|`scene.base.coin_reveal.*`|coin reveal|yes|`coin_reveal_scene.json`|yes|Bronze, silver, and gold tiers mapped.|
|`base_game.special_reveals`|`scene.base.special_reveal.*`|special reveal|optional|`coin_reveal_scene.json`|yes|Pot/clover candidates only.|
|`feature_mode_state`|`scene.feature.mode_*.panel`|feature mode state|yes|`feature_mode_selection.json`|yes|Three provisional modes mapped.|
|`bonus_buy_state`|`scene.bonus_buy.mode_selection`|bonus buy selection|yes if enabled|`bonus_buy_panel.json`|yes|EV/cost remains pending.|
|`max_win_cap`|`scene.max_win.*`|cap overlay|yes|`max_win_cap_scene.json`|yes|Cap decision must be backend-authored.|
|`winRatio`|win tier counter/effect|win tier classify|yes|`big_win_scene.json`|yes|Candidate thresholds only.|
|`winTier`|`scene.win_tier.big`, `scene.win_tier.huge`, `scene.win_tier.mega`|win tier effect|yes|`big_win_scene.json`|yes|Renderer can select effect from backend tier.|
|`round_completion`|`scene.round_completion.ready`|round ready|yes|`round_completion_state.json`|yes|Round completion authority is backend-owned.|
|`state_persistence`|`scene.reconnect.restore_state`|restore/reconnect|yes|`state_recovery_reconnect_scene.json`|yes|Recovery state must not be browser-authoritative.|
|`animation_hints`|layout/settings/developer hints|timing or labels|optional|multiple scene maps|yes|Hints do not carry outcome authority.|
## RuntimeApiInspection Update

The client consumption map remains valid as a planning map, but it is not yet an implementation contract. The generic runtime envelope is proven; the Little Gangster v0.3 adapter is not.

| v0.3 result field group | Runtime payload status | Client implementation status |
|---|---|---|
| cascade steps/removals/drops/refills | Adapter required | blocked |
| golden-square state | Adapter required | blocked |
| rainbow activation | Adapter required | blocked |
| coin/special reveals | Adapter required | blocked |
| feature mode and bonus-buy state | Adapter required | blocked |
| max-win cap, winRatio, winTier | Adapter required | blocked |
| round completion/state persistence | Adapter required and recovery-reviewed | blocked |
| animation hints | Adapter required | blocked |

Client code may consume these only after the backend/runtime proves where the payload lives, most likely in `presentationPayload` or a reviewed Little Gangster subobject.

## FixturePlanning Update

The 24 static fixture examples under `06_resulting_code/planning/fixtures/examples/` cover the mapped v0.3 render groups:

- base idle and no-win states;
- single and multi-cascade playback;
- golden-square creation and persistence;
- rainbow activation;
- bronze, silver, and gold coin reveals;
- pot-of-gold and four-leaf-clover reveal candidates;
- three feature modes;
- bonus-buy selection and purchased feature start;
- big, huge, and mega win tiers;
- max-win cap display;
- round completion;
- reconnect and recovery-pending states.

These fixtures are non-production planning data. They are not runtime proof and cannot be used as browser-authoritative result generation.
