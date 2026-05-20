# Current Game Status - Little Gangster

## 2026-05-15 Update - Lifecycle Wrapper Planning

Lifecycle wrapper and VABS/VBA/Lasthands route planning completed. The current 8001 adapter is still classified as payload mapper only. Lifecycle
wrapper implementation and VABS visual history route implementation are required but not approved.

The wrapper plan covers launch/session ownership, open/resume/close, base spin, cascades, free spins, 100x bonus-buy purchase/result, cap enforcement,
settlement references, reconnect, restart/FRB, pending/stuck recovery, history routes, logging/error hooks, registration dependencies, profile
identity, SD_KEY/KPI, and blocker propagation.

GameClientBuilder remains blocked until the wrapper contract is accepted. GameServerRegistrar generation remains blocked until registration settings
dependencies are resolved. Wallet/launch/history tests remain blocked until wrapper/route implementation is explicitly approved and present. Release
remains blocked.

## 2026-05-15 Update - Legacy GS Lifecycle Audit

Legacy GS lifecycle audit completed. Crazy Rooster 7001 is not authoritative and is only reference evidence.

Current 8001 adapter risk classification: `needs_lifecycle_wrapper`. The adapter can continue as a guarded `presentationPayload.gamePayload` mapper,
but it is not a full launch/session/history/wallet integration. Lifecycle wrapper planning and VABS/VBA/Lasthands runtime route planning are required
before GameClientBuilder, GameServerRegistrar generation, wallet execution, or release.

Registration settings remain blocked for BF_RTP/BF_RTP_MIN/BF_BETS key mapping, SD_KEYS/KPI mapping, GL bet values, possible models, and
CAP_WIN/MAX_WIN policy. No Staging source was modified in this audit sprint.




## 2026-05-15 Update - Backend Adapter Representation Planning

Backend adapter representation planning is complete for base payloads, cascades/features, approved-for-planning 100x bonus-buy payloads, state
persistence, and VABS/Lasthands/history fields. This is planning only. Backend adapter implementation remains not approved.

Active bonus-buy blockers carried forward: `bonus_buy_runtime_validation_pending`, `bonus_buy_wallet_accounting_test_pending`,
`bonus_buy_vabs_lasthands_test_pending`, `bonus_buy_tail_maxwin_confirmation_pending`, `bonus_buy_release_approval_pending`, and
`bonus_buy_certification_false`.

GameClientBuilder, GameServerRegistrar generation, wallet/DB work, final asset approval, certification, and release remain blocked.

## 2026-05-14 Update - Bonus-Buy 100x Product Decision Recorded

Selected option: Option A. The 100x bonus-buy package is approved for implementation planning only. This allows backend adapter representation
planning, runtime payload planning, future registration planning as a candidate, and VABS/Lasthands/history planning.

This does not approve release, certification, backend adapter implementation, active config changes, GS registration generation, DB/Cassandra changes,
wallet tests, or final assets. 125x and 150x remain blocked.

## 2026-05-14 Update - Bonus-Buy 100x Product Approval Package

Status: product_decision_required. The 100x bonus-buy validation gate passed against declared BF_RTP planning targets for 9 / 9 profiles. A product
approval package and decision form now exist. This supersedes older bonus-buy status notes that described v2 simulation as pending.

- Standard candidate: 100x total bet.
- 125x / 150x: blocked as separate premium/super tiers.
- Product approval required: true.
- Release approved: false.
- Certification status: false.
- Active `bonus_buy_rules.json` changed: false.
- Backend adapter remains blocked until product approval and runtime representation are accepted.
- GameServerRegistrar generation remains blocked until product approval and registration values are accepted.
- Anti-loop rule: do not run more bonus-buy math loops unless product rejects the package or requests a specific change.

Generated: 2026-05-14T11:02:16.092089+00:00
Status: consolidation_only_no_new_evidence

## 1. Current Project Status

Little Gangster has a 3x3 RTP/volatility base profile matrix with train and validation gates passed. The project is not release-ready. Backend adapter
implementation, production client generation, GameServerRegistrar generation, wallet tests, VABS/Lasthands runtime tests, final asset approval,
certification, and release approval remain blocked.

## 2. What Is Proven

- LOW/MEDIUM/HIGH RTP labels exist for Little Gangster: LOW 92.00%, MEDIUM 94.00%, HIGH 96.00%.
- The 3x3 RTP/volatility profile matrix exists with 9 `mathProfileId` values.
- Composite train gate passed: 9 / 9 profiles within +/-2 percentage points.
- Validation-seed gate passed: 9 / 9 profiles within +/-2 percentage points.
- Validation seeds were not used for tuning.
- Bonus-buy purchased-feature path was verified in the local non-production simulator.

## 3. What Is Not Proven

- Exact RTP values are not certified.
- Tail/max-win cap frequency is not proven; configured 10,000x cap was not empirically reached.
- POSSIBLE_MAX_WINS values are planning-only.
- Bonus-buy current 100x/125x/150x candidates are not acceptable.
- Bonus-buy v2 premium start-state model is draft-only and untested.
- Backend, client, GS registration, wallet, VABS/Lasthands runtime behavior, final assets, and release are not approved.

## 4. RTP/Volatility Matrix Current State

- RTP levels: LOW, MEDIUM, HIGH.
- Volatility levels: LOW, MEDIUM, HIGH.
- Profile count: 9.
- Little Gangster current RTP targets: LOW 92.00%, MEDIUM 94.00%, HIGH 96.00%.
- Future-game reusable RTP range: 91.00% to 99.70% inclusive. Future games may use different LOW/MEDIUM/HIGH values inside that range; Little Gangster
  values were not changed.

## 5. Train Gate Status

Train gate status: passed.

| Profile | Target | Initial 10M train | Overlay train | Targeted outlier rerun | Composite train | Composite delta |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `LG_8001_RTP_LOW_VOL_LOW` | 92.00% | 94.887745% | 92.892236% | n/a | 92.892236% | 0.892236 pp |
| `LG_8001_RTP_LOW_VOL_MEDIUM` | 92.00% | 85.046533% | 89.871473% | 90.999215% | 90.999215% | -1.000785 pp |
| `LG_8001_RTP_LOW_VOL_HIGH` | 92.00% | 94.971611% | 93.291339% | n/a | 93.291339% | 1.291339 pp |
| `LG_8001_RTP_MEDIUM_VOL_LOW` | 94.00% | 91.096004% | 93.565142% | n/a | 93.565142% | -0.434858 pp |
| `LG_8001_RTP_MEDIUM_VOL_MEDIUM` | 94.00% | 91.529664% | 93.217797% | n/a | 93.217797% | -0.782203 pp |
| `LG_8001_RTP_MEDIUM_VOL_HIGH` | 94.00% | 87.859021% | 91.328486% | 92.836122% | 92.836122% | -1.163878 pp |
| `LG_8001_RTP_HIGH_VOL_LOW` | 96.00% | 102.048750% | 97.562362% | n/a | 97.562362% | 1.562362 pp |
| `LG_8001_RTP_HIGH_VOL_MEDIUM` | 96.00% | 104.337491% | 98.419702% | 97.186493% | 97.186493% | 1.186493 pp |
| `LG_8001_RTP_HIGH_VOL_HIGH` | 96.00% | 100.310665% | 97.375522% | n/a | 97.375522% | 1.375522 pp |

Composite train gate: 9 / 9 within +/-2%. Clean enough for validation. Validation seeds were not used for tuning.

## 6. Validation Gate Status

Validation gate status: `pass_for_profile_matrix_train_validation_stage`.
Actual validation total rounds: 9999990.
Profiles validated: 9 / 9. Profiles within +/-2%: 9. Profiles outside +/-2%: 0.
Overfit risk: low_to_watch_high_high_near_gate. HIGH/HIGH remains watch-listed near the +2% gate at +1.925016 pp.

| Profile | Target | Validation RTP | Delta | Pass ±2% | Overfit risk |
| --- | ---: | ---: | ---: | --- | --- |
| `LG_8001_RTP_LOW_VOL_LOW` | 92.00% | 92.819307% | 0.819307 pp | true | low |
| `LG_8001_RTP_LOW_VOL_MEDIUM` | 92.00% | 91.222383% | -0.777617 pp | true | low |
| `LG_8001_RTP_LOW_VOL_HIGH` | 92.00% | 93.422956% | 1.422956 pp | true | low |
| `LG_8001_RTP_MEDIUM_VOL_LOW` | 94.00% | 93.442742% | -0.557258 pp | true | low |
| `LG_8001_RTP_MEDIUM_VOL_MEDIUM` | 94.00% | 93.655781% | -0.344219 pp | true | low |
| `LG_8001_RTP_MEDIUM_VOL_HIGH` | 94.00% | 93.416788% | -0.583212 pp | true | low |
| `LG_8001_RTP_HIGH_VOL_LOW` | 96.00% | 97.213866% | 1.213866 pp | true | low |
| `LG_8001_RTP_HIGH_VOL_MEDIUM` | 96.00% | 96.876373% | 0.876373 pp | true | low |
| `LG_8001_RTP_HIGH_VOL_HIGH` | 96.00% | 97.925016% | 1.925016 pp | true | watch |

## 7. Tail/Max-Win Status

Tail/max-win pilot status: completed, planning-only, not certified.
Actual tail total rounds: 9999990.
Cap hits observed: no. Profiles with cap hits: 0. Global max observed win: 154.4462x. Configured cap: 10000x.

POSSIBLE_MAX_WINS and max-win values are planning-only. `max_win_tail_frequency_unproven` remains active.

## 8. Bonus-Buy Status

Bonus-buy EV simulation status: completed but runtime-limited, train-only, planning-only.
Purchased-feature simulation path verified: true.
Candidate costs tested: 100x, 125x, 150x.
Formula: `BF_RTP = 100 * totalPurchasedFeatureWinCredits / totalBonusBuyCostCredits`.

Observed BF_RTP planning ranges:

- 100x: 3.95% to 7.45%
- 125x: 3.16% to 5.96%
- 150x: 2.64% to 4.97%

Current candidate costs are unacceptable. Estimated target-matching cost range was about 4.30x to 7.76x, but a 4x-8x cost-only fix is not recommended.
Bonus buy remains in scope and blocked pending v2 premium start/value design simulation.

Draft v2 model: created, draft-only, inactive, product approval required. Active `bonus_buy_rules.json` was not changed.

## 9. Registration Readiness

GS registration generation remains blocked. Base RTP/volatility profiles are train/validation-gate passed, but `BF_RTP`, `BF_RTP_MIN`,
POSSIBLE_MAX_WINS, and cap-frequency evidence are not final.

## 10. Backend Adapter Readiness

Backend adapter implementation remains blocked. Bonus-buy runtime state, wallet boundary, deterministic replay, VABS/Lasthands runtime tests, and
final registration data are not ready.

## 11. Client Readiness

Production client code is not generated and GameClientBuilder implementation remains blocked. Visual planning may continue, but release assets and
backend result contracts are not approved.

## 12. Art Readiness

Final art assets are not approved for release. Scaffold/reference assets remain blocked unless explicitly replaced or approved.

## 13. Release Blockers

- `bonus_buy_v2_simulation_pending`
- `bonus_buy_product_approval_required`
- `current_bonus_buy_candidate_costs_unacceptable`
- `max_win_tail_frequency_unproven`
- `possible_max_win_final_value_pending`
- `backend_adapter_implementation_blocked`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `wallet_launch_tests_missing`
- `VABS/Lasthands_runtime_tests_missing`
- `final_art_assets_not_approved`
- `release_not_approved`
- `certification_false`

## 14. Next Recommended Sprint

Explicitly approve lifecycle wrapper implementation apply for Little Gangster 8001 using the planned
`new-games-server/src/games/little-gangster/lifecycle/` and `new-games-server/src/games/little-gangster/history/` source locations, or run a narrower
VABS/backoffice route compatibility planning sprint before implementation. Keep GameClientBuilder, GameServerRegistrar generation, wallet/API tests,
DB/Cassandra, donor browsing, asset capture, certification, and release blocked unless separately approved.

## Backend Adapter Apply Update - 2026-05-15

Staging source now contains a Little Gangster 8001 backend adapter payload representation under `new-games-server/src/games/little-gangster/`, with
guarded gameId `8001` presentation-payload branches in `new-games-server/src/index.ts`.

Implemented representation coverage:
- base spin payload;
- cascade payload;
- 3x3 RTP/volatility `mathProfileId`;
- 100x bonus-buy purchase/result payload;
- declared BF_RTP target;
- state persistence/reconnect;
- VABS/Lasthands/history fields;
- blocker propagation.

This is not release approval. 100x bonus buy remains not certified and not runtime/wallet/VABS tested. GameClientBuilder, GameServerRegistrar
generation, registration apply, DB/wallet actions, final assets, certification, and release remain blocked.

## Lifecycle Wrapper Source Planning Update - 2026-05-15

Lifecycle wrapper source planning is complete. Staging source was inspected read-only and was not modified.

Current 8001 adapter classification remains: payload mapper only. Lifecycle wrapper remains required. VABS/VBA/Lasthands visual history route remains
required. Crazy Rooster / 7001 is not authoritative.

Recommended future source shape:
- wrapper option: Option 5, combined small wrapper first, then separate route later;
- wrapper location: `new-games-server/src/games/little-gangster/lifecycle/`;
- VABS/history location: `new-games-server/src/games/little-gangster/history/`;
- route integration host: `new-games-server/src/index.ts`.

Implementation is not approved by this planning sprint. GameClientBuilder, GameServerRegistrar generation, wallet/API tests, DB/Cassandra changes,
registration artifacts, final assets, certification, and release remain blocked.

## Lifecycle Wrapper Apply Update - 2026-05-15

Lifecycle wrapper implementation was applied to Staging source for Little Gangster 8001 under explicit approval.

Implemented Staging scope:
- created `new-games-server/src/games/little-gangster/lifecycle/`;
- added lifecycle state machine, action/accounting representation, round completion, state persistence, reconnect recovery, and blocker propagation;
- updated the guarded gameId `8001` route integration in `new-games-server/src/index.ts`;
- preserved `presentationPayload.gamePayload`, `mathProfileId`, RTP/volatility identity, 100x bonus-buy fields, and VABS/history placeholders.

## VABS Route Resolution Audit Update - 2026-05-15

Legacy GS VBA/VABS/Lasthands route-resolution audit is complete. Staging source was
inspected read-only and was not modified.

Recommended model: `model_e_hybrid_configured_gs_cm_route_new_games_server_visual_replay`.
Legacy GS visual history is proven through `/vabs/show.jsp` style routes and helper
actions. New-games currently proves JSON `/slot/v1/gethistory`, not visual VABS
completion. Little Gangster should implement visual history under
`new-games-server/src/games/little-gangster/history/` with guarded route registration
and legacy-compatible parameter handling.

Registration/config is required but blocked because the exact registration field shape
for visual history route discovery is unproven. GameClientBuilder, GameServerRegistrar
generation, wallet/history tests, VABS route implementation, certification, and release
remain blocked.

## VABS Evidence Policy Update - 2026-05-15

VABS/VBA/Lasthands evidence storage policy and game-level settings planning is complete.
Deterministic replay is required and remains authoritative. Visual HTML/render VABS route
is required for in-game History and Casino Manager/backoffice unless current GS evidence
proves otherwise.

Default `historyEvidenceMode`: `deterministic_replay_only`.

Screenshot and video modes are supported by policy but not implemented. Full video for
every spin is not default because of storage and performance risk. Media capture must be
configured per game with capture scope, retention, byte limits, compression, async
capture, storage provider, checksums, encryption, and PII redaction.

VABS route implementation, screenshot/video capture, durable media storage,
GameClientBuilder, GameServerRegistrar generation, wallet/history tests, certification,
and release remain blocked.

## VABS Visual History Route Apply Update - 2026-05-15

The Little Gangster 8001 VABS/VBA/Lasthands visual history route foundation was applied
to Staging source under explicit approval.

Implemented:
- `new-games-server/src/games/little-gangster/history/`
- deterministic replay JSON payload building;
- safe visual HTML/render shell;
- media manifest support with default `deterministic_replay_only`;
- non-production fixture storage provider and explicit durable-storage blocker;
- guarded 8001 history route registration in `new-games-server/src/index.ts`;
- targeted history route tests.

Targeted history tests passed 6/6.

Still blocked:
- `durable_history_storage_unproven`
- `durable_media_storage_not_implemented`
- `screenshot_capture_not_implemented`
- `video_capture_not_implemented`
- `backoffice_cm_vabs_compatibility_unproven`
- `vabs_runtime_wallet_history_tests_missing`
- `wallet_launch_history_tests_missing`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`

## VisualPrototypeSandboxBuilder Raw-Safe Checkpoint

Status: public-safe curation checkpoint prepared for reusable skill review.

- VisualPrototypeSandboxBuilder included: yes.
- Donor assets included: no.
- Donor scripts included: no.
- Local sandbox prototype files included: no.
- Private paths and donor/private hosts removed: yes.
- Registration generation allowed: false.
- GameClientBuilder implementation allowed: false.
- Wallet endpoint tests allowed: false.
- Release allowed: false.
- Certification status: false.

## VABS Alias Compatibility Audit Update - 2026-05-15

Legacy VABS alias compatibility audit is complete. Staging source was inspected
read-only and was not modified.

Recommended alias decision: `legacy_alias_recommended`.

Finding:
- Legacy GS/source evidence proves `/vabs/show.jsp` style visual history semantics.
- Current 8001 canonical new-games history routes are not enough to claim BO/CM
  compatibility by themselves.
- Future 8001 implementation should support both a guarded legacy-compatible alias or
  redirect and canonical `/slot/v1/8001/history/...` routes.
- Registration/config is required as a concept, but exact field shape remains blocked.

Still blocked:
- `alias_implementation_not_approved`
- `bo_cm_alias_acceptance_untested`
- `view_session_id_equivalence_unproven_for_8001`
- `exact_registration_config_field_shape_unproven`
- `durable_history_storage_unproven`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`

## VABS Legacy Alias Apply Update - 2026-05-15

The Little Gangster 8001 VABS legacy alias foundation was applied to Staging source
under explicit approval.

Implemented:
- guarded root alias support for `/vabs/show.jsp`;
- guarded scoped alias support for `/slot/v1/8001/legacy/vabs/show.jsp`;
- sanitized mapping of `VIEWSESSID`, `GAMEID`, `LANG`, `TIMEZONE`, `hideClose`, optional
  `ROUNDID`, and optional whole-session flags;
- wrong `GAMEID` blocked for non-8001 requests;
- alias rendering through the existing 8001 visual history foundation;
- blocker propagation for BO/CM acceptance, durable storage, view-session equivalence,
  release, and certification;
- targeted alias/canonical history tests.

Targeted tests passed 9/9.

Still blocked:
- `bo_cm_alias_acceptance_untested`
- `durable_history_storage_unproven`
- `view_session_id_equivalence_unproven_for_8001`
- `exact_registration_config_field_shape_unproven`
- `vabs_runtime_wallet_history_tests_missing`
- `wallet_launch_history_tests_missing`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`

Targeted Little Gangster tests passed 13/13. Isolated lifecycle TypeScript checking passed. Broader `src/index.ts` typecheck remains blocked by
existing checkout dependency/strictness issues.

VABS/VBA/Lasthands visual history route implementation was not created. GameClientBuilder, GameServerRegistrar generation, registration artifacts,
wallet/launch/history tests, DB/Cassandra changes, final assets, certification, and release remain blocked.

## VABS Visual History Source Planning Update - 2026-05-15

VABS/VBA/Lasthands visual history route source planning is complete. Staging source was inspected read-only and was not modified.

Recommended route source location:
- `new-games-server/src/games/little-gangster/history/`

Recommended route shapes:
- `POST /slot/v1/8001/history/round/:roundId`
- `POST /slot/v1/8001/history/session/:gameSessionId`
- `POST /slot/v1/8001/history/session/:gameSessionId?wholeSession=true`
- `GET /slot/v1/8001/history/render/round/:roundId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId`
- `GET /slot/v1/8001/history/render/session/:gameSessionId?wholeSession=true`

JSON replay and visual HTML/render responses are both planned. In-game History button and Casino Manager/backoffice access are planned. Stored JSON
alone is not treated as sufficient for release unless current GS/backoffice evidence proves JSON-only replay is acceptable.

Implementation remains blocked until explicit approval. GameClientBuilder, GameServerRegistrar generation, wallet/history tests, DB/Cassandra changes,
registration artifacts, final assets, certification, and release remain blocked.

## GS Responsibility Boundary Audit Update - 2026-05-15

GS/wallet/runtime responsibility boundary audit is complete. Staging source was
inspected read-only and was not modified.

Findings:
- browser/client is not the real wallet owner;
- Little Gangster runtime/lifecycle owns action/accounting intent, idempotency, state,
  result/history payload references, and blocker propagation;
- current GS/WebGS/common-wallet plus wallet/casino provider own real balance settlement
  and wallet operation state;
- GS/Cassandra own durable session, round, bet, wallet-operation, last-hand, and history
  storage unless a future approved source plan proves another owner;
- pending/stuck transaction ownership belongs to current GS wallet-operation tracking
  and persistence, while 8001 carries pending markers and recovery references.

WalletAndLaunchTester scope is corrected: future tests must verify accounting boundary
and approved GS/wallet/provider settlement behavior, not assume the client/runtime owns
the wallet.

Still blocked:
- `wallet_launch_history_tests_missing`
- `real_wallet_tests_not_approved`
- `real_gs_tests_not_approved`
- `bo_cm_alias_acceptance_untested`
- `durable_history_storage_unproven`
- `view_session_id_equivalence_unproven_for_8001`
- `exact_registration_config_field_shape_unproven`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
- `certification_false`
