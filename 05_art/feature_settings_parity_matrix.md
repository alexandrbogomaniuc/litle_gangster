# Feature Settings Parity Matrix

This is the art/planning view of `01_reference_research/donor_feature_settings_matrix.csv`.

| Donor feature/setting | Parity status | Scene | Object IDs | Required action |
|---|---|---|---|---|
| 6 reel x 5 row grid | matched | base_game_scene | scene.base.grid.root; scene.base.grid.cell.* | Keep 6x5 as target layout. |
| cluster wins | matched | base_game_grid_6x5 | scene.base.grid.root; scene.base.win.cluster_highlight | Keep cluster as target evaluation. |
| super cascade / symbol removal and drop-down refill | mismatch_requires_update | base_game_scene | scene.base.grid.root; scene.base.win.cluster_highlight | Revise math/result contract to include cascade steps and client animation
sequence. |
| golden squares / win-to-win highlighted cells | mismatch_requires_update | base_game_scene | scene.base.grid.cell.*; scene.base.win.cluster_highlight | Add golden-square grid state to math/result schema and scene map animation notes. |
| rainbow special symbol activates golden squares | mismatch_requires_update | base_game_scene | scene.base.symbol.scatter.idle; scene.base.symbol.bonus_trigger.idle | Replace generic scatter assumption with donor-parity rainbow activation
contract or mark exact behavior blocked. |
| bronze/silver/gold coin reveal from activated golden squares | mismatch_requires_update | base_game_scene | scene.base.symbol.coin.idle; scene.base.win.cluster_highlight | Add coin reveal states, values, contribution accounting, and
animation hints. |
| pot-of-gold or clover reveal chance | mismatch_requires_update | base_game_scene | scene.base.symbol.bonus_trigger.idle | Add special reveal candidates and blocked exact probability inputs. |
| wild substitution | matched | base_game_scene | scene.base.symbol.wild.idle | Keep wild in math/art plans; exact substitution limitations still need source/user confirmation. |
| scatter-style generic free-spin trigger | mismatch_requires_update | base_game_scene | scene.base.symbol.scatter.idle | Do not assume classic scatter if donor uses rainbow/golden-square flow; revise terminology and trigger contract. |
| three named bonus/free-spin game modes | mismatch_requires_update | free_spins_active | scene.free_spins.counter.remaining; scene.bonus_buy.panel.root | Model the three donor feature modes as Little Gangster equivalents before full build.
|
| bonus buy / FeatureSpins entry point | mismatch_requires_update | bonus_buy_panel | scene.bonus_buy.panel.buy_button; scene.bonus_buy.panel.root | Document exact donor buy panel flow and revise math EV before full build. |
| maximum win 10,000x | matched | big_win_scene | scene.big_win.counter.amount | Keep max win display/metadata but cap behavior needs implementation proof. |
| max win reachable in base and feature modes | mismatch_requires_update | big_win_scene | scene.big_win.root | Add cap handling to base and feature mode contracts. |
| jackpot | blocked_pending_evidence | none | none | Keep jackpot disabled unless donor evidence appears; do not claim donor has no jackpot with full certainty. |
| double-up / gamble | little_gangster_extra_not_in_donor | double_up_placeholder | scene.double_up.placeholder.root | Product decision required: remove from target scope unless donor evidence appears. |
| normal safe spin in demo mode | matched | base_game_scene | scene.base.panel.spin_button | Keep spin flow; more win/no-win/feature scenario evidence still needed. |
| no-win / regular win / cluster highlight result flows | blocked_pending_evidence | base_game_scene | scene.base.win.cluster_highlight | Need more gameplay observation or source evidence for complete animation/result state machine. |
| free-spins intro, active, retrigger, outro | blocked_pending_evidence | free_spins_active | scene.free_spins.* | Must observe or specify exact donor-parity free-spin flow before final build. |
| big win / win tier sequence | mismatch_requires_update | big_win_scene | scene.big_win.* | Map donor-tier thresholds if observable/source-provided; keep release blocked. |
| main menu panel | matched | settings_modal | scene.settings.modal.root | Keep menu panel in Little Gangster with donor-equivalent settings. |
| sound toggle | matched | settings_modal | scene.settings.sound_toggle | Keep separate sound toggle. |
| music toggle | mismatch_requires_update | settings_modal | scene.settings.music_toggle | Add explicit music toggle to UI plan and client settings contract. |
| super turbo toggle | mismatch_requires_update | settings_modal | scene.settings.super_turbo_toggle | Add Super Turbo as separate donor-parity setting unless product blocks it. |
| turbo toggle | matched | turbo_toggle | scene.base.panel.turbo_toggle | Keep turbo toggle. |
| info/help/rules/paytable | matched | help_rules_paytable_modal | scene.rules.modal.root | Keep info/help/rules modal and populate from final math/rules. |
| home/lobby button | mismatch_requires_update | settings_modal | scene.settings.home_button | Add home/lobby equivalent to settings UI plan; launch behavior must be GS/runtime-owned. |
| bet display and bet up/down controls | matched | bet_panel | scene.base.panel.bet_display; scene.base.panel.bet_up; scene.base.panel.bet_down | Keep bet display and increment/decrement controls. |
| coin denomination controls | blocked_pending_evidence | bet_panel | scene.bet.panel.root | Do not invent separate denomination UI; map only if observed/source-provided. |
| autoplay panel and stop conditions | blocked_pending_evidence | autoplay_panel | scene.autoplay.panel.root | Need donor panel evidence or source docs before exact stop conditions. |
| game history | blocked_pending_evidence | settings_modal | scene.settings.history_button | Keep blocked until donor evidence or product decision. |
| reality check / responsible gaming links | blocked_pending_evidence | settings_modal | scene.settings.responsible_gaming | Confirm regulatory/UI requirement separately; do not guess. |
| about/version screen | blocked_pending_evidence | settings_modal | scene.settings.about | Confirm whether donor has version/about elsewhere. |
| keyboard/accessibility behavior | blocked_pending_evidence | none | none | Requires dedicated accessibility pass; not guessed. |
| mobile layout/settings differences | blocked_pending_evidence | mobile_layout | scene.mobile.* | Need playable mobile donor observation or source evidence. |
| loading / intro / click-to-continue flow | matched | loading_scene | scene.loading.* | Keep intro/continue flow equivalent. |
| base idle flow | matched | base_game_scene | scene.base.* | Keep base idle layout. |
| bonus-buy confirmation/purchase flow | blocked_pending_evidence | bonus_buy_panel | scene.bonus_buy.* | Observe or specify confirmation/payment flow before build. |
| wallet/API error modal behavior | matched | error_modal | scene.error.modal.root | Keep error modal and reconnect handling. |
| reload/reconnect behavior | blocked_pending_evidence | reconnect_modal | scene.reconnect.modal.root | Need live recovery evidence; do not invent retry semantics. |
| audio separation for music, UI clicks, wins, feature sounds | matched | settings_modal | scene.settings.sound_toggle; scene.settings.music_toggle | Keep separate replacement briefs for music/SFX/features. |
| feature-scaffold support for rainbow/coin/clover/wild/win tiers | mismatch_requires_update | base_game_scene | scene.base.symbol.*; scene.big_win.* | Use scaffolds as internal references only and update replacement briefs. |

## Art Direction Rule
Final Little Gangster art remains original Neon Heist. Donor/scaffold assets may be used only as internal reference/previews and remain blocked from release.
