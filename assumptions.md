# Assumptions And Blockers

## 2026-05-15 - Lifecycle Wrapper Planning Assumptions

- The current 8001 adapter remains a guarded `presentationPayload.gamePayload` mapper only.
- Lifecycle wrapper implementation is still not approved in this sprint.
- VABS/VBA/Lasthands route implementation is still not approved in this sprint.
- The wrapper must own or coordinate launch/session, open/resume/close, base actions, cascades, feature/free-spin actions, 100x bonus-buy
  purchase/result actions, cap state, settlement references, reconnect, restart/FRB, pending/stuck recovery, logging/error hooks, and blocker
  propagation.
- History route planning must support round replay, session replay, whole-session replay, in-game History, backoffice access, and Lasthands.
- Registration settings remain blocked until model, BF_RTP/BF_RTP_MIN/BF_BETS, SD_KEYS/KPI, cap/max-win, GL bet, language, FRB, round-finished, and
  VABS URL fields are mapped.
- No Staging source, backend adapter code, VABS route code, client code, registration artifacts, DB/Cassandra state, wallet/API endpoints, donor
  assets, or release approvals were changed in this planning sprint.

## 2026-05-15 - Legacy GS Lifecycle Audit Assumptions

- Crazy Rooster 7001 is not authoritative for Little Gangster and is only candidate/reference evidence.
- The current Little Gangster 8001 adapter is a guarded `presentationPayload.gamePayload` mapper, not a complete GS lifecycle integration.
- Legacy GS launch/session, restart/FRB, close/reconnect, wallet/accounting, and VABS/VBA/Lasthands behaviors are outside the adapter and require
  wrapper or route planning.
- The adapter can continue as a mapper, but lifecycle wrapper and VABS visual history route planning are required before GameClientBuilder or
  GameServerRegistrar generation.
- Registration settings remain blocked until `POSSIBLE_MODELS`, BF_RTP/BF_RTP_MIN/BF_BETS naming, SD_KEYS/KPI, GL bet settings, CAP_WIN/MAX_WIN, and
  current GS cache/template fields are mapped.
- No Staging source, backend adapter code, client code, registration artifacts, DB/Cassandra state, wallet/API endpoints, donor assets, or release
  approvals were changed in this audit sprint.

## Assumptions

- The redacted donor URL in `project_manifest.json` is enough for ProjectCreator. Future browser/reference work must request the full URL again or use
  the recorded secret reference.
- The documented stack defaults are acceptable for the manifest because the user explicitly requested them.
- Asset capture is marked allowed because the user explicitly set `asset_capture_allowed: true` and updated the reference mode to
  `authorized_capture_for_internal_scaffold`; real asset body download, hashing, comparison, and classification remain deferred to
  ReferenceAssetInventory.
- Release approval remains false until later workflow gates pass.
- Explicit source/config paths supplied for Sprint 2 were verified by existence/readability only. Their internal contents were not inspected in this
  sprint except where future skills are explicitly authorized.
- Secret-bearing files were not opened for value extraction. PASS_KEY and test token/user data are represented as secret references only.
- Default bank ID `6275`, subCasinoId `507`, and coin denominations were accepted as explicit user input with source-path existence/readability
  verified.

## Open Blockers

- PASS_KEY raw value is intentionally unavailable. Future WalletAndLaunchTester must use a local ignored secret reference or fixture, never raw chat
  text.
- Test user/token raw values are intentionally unavailable. Future launch/wallet tests must use local ignored secret references or fixtures, never raw
  chat text.
- Client/source/config path contents were not verified in this sprint because only AuthorizedReferenceResearcher and SprintReporter were allowed.
- Browser gameplay coverage may remain partial depending on donor URL validity, runtime load behavior, and demo/test-mode safety.
- AuthorizedReferenceResearcher retry on 2026-05-07 initially could not start browser work because the supplied fresh donor/reference URL field was a
  placeholder, not a usable URL.
- User later clarified the earlier donor URL should remain the current in-memory URL for this project, and provided a visible in-app browser
  screenshot showing the playable intro screen.
- Tool discovery did not expose a Google Chrome MCP or the Browser Use Node REPL `js` control tool. With user authorization, Codex used visible
  OS-level clicks/screenshots against the already-open in-app browser instead.
- Safe demo mode was directly observed through `DEMO BALANCE` and `DEMO BET` labels.
- One safe demo spin was attempted and produced an in-game wallet connection error. Completed spin outcome coverage remains blocked.
- Browser DevTools/HAR metadata is not available from the OS-level visible-browser route. Existing sanitized network metadata comes from the earlier
  project-local Playwright retry only.
- ReferenceAssetInventory can proceed only for observed intro/base assets and must still keep scaffold assets gitignored, inventoried, quarantined,
  and blocked from release.
- User then asked Codex to retry Google Chrome MCP. Tool discovery exposed Chrome DevTools MCP on that retry.
- Chrome MCP successfully opened the donor launch, reached demo base game, clicked the spin control, opened menu/game info, and collected
  screenshots/request metadata without saving bodies.
- Chrome MCP network metadata indicates demo `authenticate`, `gameLaunch`, `keepAlive`, and `bet` calls returned HTTP 200.
- The earlier in-app-browser wallet error is treated as a discrepancy between browser/control paths, not as proof the donor demo is unusable.
- Game-info/paytable observations are reference clues only. Final math must still come from internal math templates, user requirements, validated
  config, and simulation.

## Not Done This Sprint

- No ReferenceAssetInventory run.
- No ProtocolAndSchemaMapper run.
- No donor asset body download.
- No request/response body saved from Chrome MCP.
- No math generation.
- No client build.
- No Cassandra registration.
- No wallet/launch tests.

## ReferenceAssetInventory Sprint Updates

- User clarified `authorized_capture_for_internal_scaffold` mode and explicitly authorized asset capture for this sprint.
- Asset capture was limited to static reference asset paths observed from Chrome MCP metadata.
- Wallet/API/auth/balance response bodies were not saved.
- Full donor launch URL and token values were not saved.
- Captured assets are stored only under `02_reference_assets/authorized_raw/chrome_mcp_20260507_1215/`, which is gitignored by project `.gitignore`.
- All 29 captured files are classified as `scaffold_internal_only`, `blocked_from_release`, and `replacement_required=true`.
- Asset inventory approval is a workflow handoff gate only. It does not approve any reference asset for release.
- ProtocolAndSchemaMapper is the next recommended skill.

## ProtocolAndSchemaMapper Sprint Updates

- BSG Common Wallet contract is mapped from uploaded BSG CW summaries and targeted GS constants. No live wallet call was made.
- Browser/client runtime contract is partial: 7001 source proves `slot-browser-v1`, `GS_HTTP_RUNTIME`, request counters, idempotency keys, client
  operation IDs, and `/slot/v1/*` operation names, but the imported `@gamesv1/core-protocol` package root was not inspected.
- Game Server runtime contract is partial: launch actions and routing bridges were inspected, but the server-side `/slot/v1/*` endpoint implementation
  remains a blocker.
- Cassandra/config contract is partial: bank 6275, subCasinoId 507, coin values, new-games route properties, `RCasinoSCKS` summary evidence, and
  generate-only safety are mapped, but no 8001 registration exists and `scn` serialization remains blocked.
- The explicit 7001/new-games source path uses a newer Vite/PIXI v8-style runtime lane, while uploaded docs describe a legacy Webpack/Vue/PIXI
  template. Future GameClientBuilder must choose and verify the approved target path.
- No raw secret values should be required for MathModelDesigner. Later WalletAndLaunchTester must use local ignored secret references or fake
  fixtures.
- Asset release blockers remain unchanged: all captured reference/scaffold assets remain blocked from release.

## ProtocolAndSchemaMapper Open Blockers

- `core_protocol_package_not_inspected`: provide explicit path to `@gamesv1/core-protocol` package or allow targeted inspection of that package root.
- `slot_v1_server_implementation_partial`: provide explicit new-games server/API source path for `/slot/v1/*` endpoint inspection.
- `scn_serializer_missing`: provide a real serializer/tool or approved config-generation pipeline before GameServerRegistrar attempts registration
  artifacts.
- `math_result_ownership_unknown`: resolve through MathModelDesigner and later runtime integration validation.
- `game_8001_registration_missing`: registration must wait until math/client/build inputs exist.

## ProtocolAndSchemaMapper Third-Party GS Integration Extension Updates

- Little Gangster must not treat Gamesv1, Crazy Rooster, or `slot-browser-v1` as guaranteed truth. They are candidate direction evidence only until
  current GS source/config/docs prove the lane directly.
- Third-party/new game launch should start through GS launch (`/startgame` wrapper or `/cwstartgamev2.do`) and then redirect to the configured client
  lane. Direct static-client launch is not sufficient for operator/session/wallet flow.
- `cwstartgamev2.do` authenticates through Common Wallet, creates/resolves a GS session, then redirects to new-games client when route config is
  enabled; otherwise it can continue to the legacy template route.
- WebGS contains an internal new-games bridge for session validation, wallet reserve/settle, and history read/write. This does not prove WebGS owns
  slot RNG/result generation.
- `new-games-server` is referenced by 7001 docs as the `/slot/v1/*` slot contract service, but its source root was not explicitly allowed for
  inspection in this sprint.
- `@gamesv1/core-protocol` remains uninspected and is still a runtime blocker.
- Crazy Rooster 7001 is useful as an integration reference but is not a direct release-ready template for Little Gangster. Its final status docs still
  require dedicated proof completion for 7001.
- MathModelDesigner can run next only as design/simulation work. It must not claim final runtime ownership, certified RTP, or registration import
  behavior.
- GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, and release-to-players remain blocked.

## ProtocolAndSchemaMapper Third-Party GS Integration Open Blockers

- `new_games_server_source_path_missing`: provide explicit path to `new-games-server` or authorize targeted inspection.
- `slot_v1_result_owner_unknown`: verify current GS/runtime source directly before trusting any slot-browser-v1 result owner.
- `game_client_builder_blocked_by_inputs`: complete math package, approved art plan, and runtime source proof before building.
- `game_server_registrar_blocked_by_scn_and_8001_inputs`: provide 8001 registration inputs and `scn` serializer/config pipeline before registration
  generation.

## MathModelDesigner Sprint Updates

- MathModelDesigner created a provisional original Little Gangster math package under `04_math/`.
- The provisional model is a 5x3 fixed-20-line high-volatility slot with wild substitution, scatter pays, free spins, optional bonus buy, and an
  optional neutral double-up placeholder.
- The model is explicitly not donor-true math. Reference observations are treated only as clues.
- RTP variants were created for 96.0%, 94.0%, and 92.0%.
- Each RTP variant ran a 1,000,000-round deterministic workflow simulation using seed `2026050801`.
- All three variants passed the provisional +/-0.5 percentage-point workflow tolerance.
- The math package is not release-approved and is not certification-grade.
- Browser result authority remains disallowed.
- RNG/result generation must be server/backend-side, not browser-side. Exact final owner remains UNKNOWN/BLOCKED: classic GS, new-games backend,
  game-specific server package, and GS game processor remain candidates.
- Math is not proven to be imported into GS/Cassandra registration. Registration should treat gameId, name, launch route, bank/casino assignment,
  client path, RTP display/config values, bet config, feature flags, max-win/cap values, and template/config records as metadata/config only unless
  later source proves executable math import.
- Next recommended skill is ArtSceneMapper because a provisional math package now exists, but runtime and release blockers remain.

## MathModelDesigner Open Blockers

- `new_games_server_source_path_missing`: provide explicit path to `new-games-server` or authorize targeted inspection.
- `core_protocol_package_not_inspected`: provide explicit path to `@gamesv1/core-protocol` or authorize targeted inspection.
- `slot_v1_result_owner_unknown`: authoritative RNG/result owner for 8001 is not proven.
- `runtime_math_integration_pending`: math package has not been integrated into the proven server/backend runtime owner.
- `independent_multi_seed_certification_pending`: only one deterministic 1,000,000-round seed per variant was run.
- `bonus_buy_ev_needs_review`: bonus buy price and EV need product/math review.
- `double_up_product_decision_pending`: optional double-up behavior needs product/regulatory confirmation.
- `approved_release_assets_missing`: captured scaffold/reference assets remain blocked from release.
- `wallet_launch_tests_missing`: wallet/launch tests have not run.

## MathModelDesigner Math Quality Gate Updates

- The 5x3 fixed-20-line package from the previous sprint is superseded for downstream planning.
- The selected Little Gangster math layout is now `6x5_cluster_provisional`.
- The selected package is `04_math/alternatives/v0_2_6x5_cluster/math_package.json`.
- ArtSceneMapper may proceed only against the selected 6x5 cluster target scene.
- v0.1 remains preserved for audit history but should not drive ArtSceneMapper.
- v0.1 simulator uses `payout_scale`, so its close RTP results are not true emergent release validation.
- v0.2 simulator does not scale wins during a run and does not normalize after a run; RTP comes from explicit paytables, symbol weights,
  connected-cluster evaluation, scatter wins, and free spins.
- v0.2 paytables were calibrated from smoke simulation evidence and remain provisional.
- v0.2 calibration-seed smoke simulations passed provisional workflow tolerance for all three RTP variants.
- v0.2 secondary 100,000-round short seeds drifted outside +/-0.5 percentage-point tolerance, so full multi-seed RTP validation remains open.
- The quality gate result is `PASS_WITH_LIMITATIONS`, not math release approval.
- User stated Staging is now canonical for GS/New Games/Crazy Rooster work. This math sprint did not inspect Staging paths. Future source-inspection
  skills must update/verify manifest source paths against `[DEV_ROOT_REMOVED]/Staging` and not use old worktrees as source of truth.

## Math Quality Gate Open Blockers

- `full_6x5_multi_seed_validation_pending`: longer independent multi-seed validation is required before release math approval.
- `v0_1_rtp_scaling_blocks_true_math_validation`: v0.1 is superseded and must not be used for release math.
- `staging_source_root_manifest_update_pending`: future source-inspection skills must verify/update source roots to Staging.

## ArtSceneMapper Sprint Updates

- ArtSceneMapper used selected `v0.2_6x5_cluster_provisional` layout.
- The superseded 5x3 v0.1 model was not used for target scene mapping.
- The target scene layout is a 6-column by 5-row cluster-style symbol grid.
- Scene maps are technical planning artifacts only. They are not final art, not client implementation, not runtime integration, and not release
  approval.
- The HTML scene inspector uses placeholders and embedded/local scene-map data only. It does not fetch donor URLs or external resources.
- Existing scaffold/reference assets remain blocked from release and were not copied into `06_resulting_code`.
- No final asset is approved for release.
- ArtDirectionAndReplacementPlanner is required next to create original/approved art direction and replacement plans.

## ArtSceneMapper Open Blockers

- `approved_release_assets_missing`: no mapped visual/audio asset is approved for release.
- `art_direction_required`: every placeholder/scaffold asset needs replacement or explicit approval.
- `runtime_result_owner_unproven`: exact server/backend runtime result owner remains unproven.
- `core_protocol_package_not_inspected`: final result protocol package remains uninspected.
- `new_games_server_source_path_missing`: runtime source inspection remains pending.
- `full_6x5_multi_seed_validation_pending`: math release validation remains pending.
- `bonus_buy_ev_needs_review`: bonus-buy scene is placeholder until product/math review.
- `double_up_product_decision_pending`: double-up/gamble scene is placeholder until product decision.
- `mobile_playable_reference_partial`: mobile target layout is planned but not fully observed in playable reference mode.


## Supplemental Asset Discovery And Scene Preview Assumptions - 2026-05-10 10:28:43 +0100

- Assumption: existing project-local scaffold assets from the prior authorized capture may be used for internal scene preview mapping only.
- Assumption: no fresh donor browsing/capture can occur without a usable fresh donor/demo/test URL in the sprint prompt.
- Assumption: inferred scaffold-to-object matches are planning aids, not evidence of final art ownership or release readiness.
- Blocker remains: `fresh_donor_url_placeholder_not_usable`.
- Blocker remains: `fresh_asset_capture_not_run`.
- Blocker remains: `approved_release_assets_missing`.
- Blocker remains: `art_direction_required`.


## Supplemental Asset Discovery Assumptions - 2026-05-10 10:51:49 +0100

- The provided donor URL is authorized for internal scaffold/reference capture for this project only and remains non-persisted.
- Safe demo/test mode was treated as confirmed by redacted demo/test launch parameters.
- Scaffold-to-object matches are planning references only, not final art ownership evidence.
- No 100% asset coverage is claimed.
- Blocker remains: `approved_release_assets_missing`.
- Blocker remains: `art_direction_required`.
- Blocker remains: `observed_asset_coverage_not_100_percent`.


## Art Direction Assumptions - 2026-05-10 11:23:27 +0100

- Scaffold assets can inform layout, timing, and style density, but cannot ship.
- The 5 unmatched objects are design/implementation helpers, not critical missing donor references.
- Final visual direction should be original cartoon urban heist, not a donor clone.
- GameClientBuilder may proceed only with explicit blocked-release handling for scaffold assets.

## Sprint Update: Donor Feature/Settings Parity (2026-05-10 19:52:26 BST)

- Assumption changed: Little Gangster must match donor settings/features as closely as technically possible while keeping original release-safe art.
- Evidence supports donor 6x5 cluster, cascade/removal/refill, golden-square, rainbow activation, coin/reveal, bonus buy, Super Turbo, Turbo, Sound,
  Music, Info, Home, demo balance/bet, and 10,000x max-win messaging.
- Exact donor autoplay stop conditions, bonus-buy confirmation/cost/EV, natural free-spins flow, mobile playable flow, and full win-tier thresholds
  remain blocked/unobserved.
- v0.2 math remains provisional and now requires donor feature parity revision before full GameClientBuilder.

## Public Git Export Assumptions - 2026-05-10 20:54:42 BST

- The public repository is for external review only and is not a release build.
- Sanitized inventory rows may retain counts, hashes, and release-status metadata but not donor asset bodies or unredacted asset body paths.
- The final public HEAD commit is `a8cfcb2b25f0127a9487a4d41d75e638d20765bd` on branch `main`.
- Public export does not resolve math/runtime/asset/release blockers.


## MathModelDesigner Donor-Parity Retry - 2026-05-11 07:45:26 
- Selected math version moved to `v0.3_donor_feature_parity_provisional` for planning.
- v0.3 models cascades, golden squares, rainbow activation, coin reveals, special reveal candidates, three feature modes, bonus-buy contract, and
  max-win cap.
- Exact donor probabilities, bonus-buy EV/costs, autoplay stop conditions, runtime owner, and certification-grade validation remain blockers.
- ArtSceneMapper update is required before full GameClientBuilder because v0.3 adds explicit animation-state requirements.


## Public Export Update - 2026-05-11 07:49:21 
- Sanitized public export was rebuilt and pushed after v0.3 math retry.
- Public export validation passed.
- Public export intentionally excludes donor asset bodies, screenshots, HAR, raw network logs, raw secrets, and full donor URLs.


## ExtGame External-Collaboration Requirements Patch - 2026-05-11 08:10:35 
- No raw Mantis body was pasted before this report generation; ExtGame requirements were extracted from the user sprint prompt only.
- ExtGame is now tracked as a separate requirement lane for future ProtocolAndSchemaMapper, MathModelDesigner, GameServerRegistrar,
  WalletAndLaunchTester, and RTPAndReleaseAuditor work.
- Exact ExtGame field names, raw endpoints, template values, and VBA/FRB/OCB meanings remain evidence-pending and must use sanitized source excerpts
  only.
- Selected math package was not changed in this sprint.

## Mantis Scope Correction - 2026-05-11

- Corrected assumption: Mantis/ExtGame information is advisory checklist material only and does not select Little Gangster architecture.
- Corrected assumption: ExtGame remains candidate/unverified unless current GS source/config proves it.
- Current Staging evidence provides useful new-games `slot-browser-v1` candidate signals, but that lane is not guaranteed truth and must be verified
  directly before trust or selection.
- Current GS has external game id, VABS/VBA/history, Lasthand, restart, FRB/cash-bonus, RNG, and round-finished helper concepts, but Little
  Gangster-specific contracts remain unverified.
- `processTransactions` from Mantis must be translated to current-GS process-equivalent validation unless ExtGame is later proven.
- The expected Staging new-games paths from the team update were missing, while runtime compose points to `platform-source/platform/...` paths that
  exist; manifest/source roots need cleanup in a future source-inspection sprint.
- New game registration is probably not executable math import; executable math/result logic likely belongs in backend runtime code/config, new-games
  server, a game-specific server package, or a GS game processor, but the owner remains unproven.
- No raw Mantis text, private links, emails, secrets, SIDs, signatures, donor assets, screenshots, HAR, or full donor URLs were stored in this
  correction.

## Current GS Registration/RNG Audit - 2026-05-11

- Corrected assumption: current GS registration appears to configure game/template/bank routing metadata; executable math import during registration
  is not proven.
- Current Staging evidence supports New Games / `slot-browser-v1` as the strongest candidate lane, but not final source of truth for Little Gangster.
- Current Staging evidence proves WebGS New Games session/wallet/history bridge, but does not prove WebGS itself generates Little Gangster results.
- New Games backend source currently shows sample/provisional backend outcome generation, but final 8001 result owner remains unproven.
- Browser result authority remains forbidden.
- v0.3 math package files modified by the previous patch were boundary metadata/docs only, but touching v0.3 package JSON during a
  non-math-implementation sprint is recorded as a scope violation for review.
- GameServerRegistrar remains blocked from generation until 8001 registration records, client/runtime paths, serializer/import tooling, and selected
  runtime lane are proven.

## Public Export Update - 2026-05-11 10:36:00

- Public export commit `17b162ba1dd56d7ee129b154d079be3921280c06` is a sanitized review snapshot only.
- The public export intentionally excludes donor asset bodies, screenshots, HAR, raw network logs, local browser folders, raw secrets, full donor
  URLs, tokenized URLs, SIDs, signatures, private links, and emails.
- The public export does not change delivery approval status; math, client build, registration, wallet tests, and release remain unapproved.

## MathModelDesigner v0.3 Contract Retry - 2026-05-11 11:05:00

- `v0.3_donor_feature_parity_provisional` is now treated as the selected planning math/result contract.
- The sprint completed contract/schema boundaries only; full v0.3 simulation and release-grade validation remain pending.
- Registration remains metadata/config/routing/display only unless future current-GS source proves executable math import.
- Production RNG/result ownership remains unproven and must be server/backend-side.
- Browser/client result generation remains forbidden for production.
- Double-up/gamble remains removed from active scope unless direct donor evidence or explicit user override appears.
- ArtSceneMapper update is required before GameClientBuilder because v0.3 adds explicit cascade, golden-square, rainbow, coin reveal, feature-mode,
  cap, completion, and persistence states.

## Public Export Update - 2026-05-11 11:20:00

- Public export commit `76ee19384aaf6b7c189ca5e80626b5a2682f7fe2` is a sanitized review snapshot only.
- The public export validation passed before push.
- Donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links, emails, and full donor URLs were not intentionally pushed.

## ArtSceneMapper v0.3 Update Assumptions

The v0.3 scene mapping update treats `v0.3_donor_feature_parity_provisional` as a provisional planning result contract. The client is assumed to
  render backend/runtime result payloads only; browser-side production RNG and authoritative win calculation remain forbidden. Current GS result owner
  remains unproven. GameClientBuilder may proceed only to planning/runtime-contract review, not full implementation.

New v0.3 placeholder visual states require original replacement assets and remain pending_replacement or blocked_from_release.
## Public Export After ArtSceneMapper v0.3

Public export was sanitized and pushed to https://github.com/alexandrbogomaniuc/litle_gangster on branch main at commit
  6127bdc2f982038e043d5b2585cbcc46b447a1d8. The export excludes donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links,
  emails, and full donor URLs. `06_resulting_code` remains README-only.
## v0.3 Contract Consistency Audit

Canonical v0.3 result field names now use `result_schema.json` paths in art/scene mapping files. Historical aliases such as
  `feature_mode_state.spins_remaining`, `lastAction`, unprefixed `cascade_steps[]`, and bonus-buy `mode_selection` are patched or documented in
  `result_schema_field_aliases.md`. GameClientBuilder remains planning-only; runtime result owner remains unproven.
## Public Export After v0.3 Contract Consistency Audit

Public export was sanitized and pushed to https://github.com/alexandrbogomaniuc/litle_gangster on branch main at commit
  6b79e4617d9c2faabdb8a2be8ef1da96da830815. The export excludes donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links,
  emails, and full donor URLs. `06_resulting_code` remains README-only.



## Pipeline Lessons Hardening - 2026-05-11 12:32:07 

- Little Gangster pilot lessons were captured as reusable pipeline guidance only.
- The reusable skill suite was patched to ask better early questions, require donor feature/settings parity earlier, require current-GS
  registration/RNG ownership proof earlier, and require contract consistency before builder work.
- No gameplay/build/release approval gates changed.
- Next recommended step remains GameClientBuilder planning/runtime API contract review only.


## Public Export Update - 2026-05-11 12:37:05

- Sanitized public export for Pipeline Lessons Hardening validation passed and was pushed to `main`.
- Public commit hash: `8744f5b0827ff99775415f62261f9b5fd5721ace`.
- Export does not resolve gameplay/build/runtime/registration/wallet/release blockers.


## Public Export Formatting Fix - 2026-05-11 12:53:34

- Public export formatting fixes are review/sanitizer changes only.
- No gameplay/build/runtime/registration/wallet/release approvals changed.
- Next recommended step remains GameClientBuilder planning/runtime API contract review only.


## Public Export Formatting Push - 2026-05-11 12:56:20

- Public export formatting validation passed and was pushed to `main`.
- Public commit hash: `120429e631d6b7de4d4e98af346f8c5e337ccbac`.
- No delivery approval gates changed.

## GameClientBuilder Planning Runtime API Review - 2026-05-11

- GameClientBuilder planning review is planning-only; no client code, runtime implementation, package manifest, production assets, or copied template
  code was generated.
- New Games / `slot-browser-v1` is the strongest current client lane candidate for planning only, not final architecture.
- Current GS runtime/result owner and exact Little Gangster v0.3 result API contract remain unproven.
- The browser/client remains renderer-only and must not generate production RNG or authoritative outcomes.
- Full GameClientBuilder implementation remains blocked until runtime owner, result API, package lane, and asset strategy are proven and explicitly
  approved.

## Public Export After GameClientBuilder Planning Review - 2026-05-11

- Sanitized public export validation passed and was pushed to `main`.
- Public commit hash: `c4af8bc6b4e18fc39cb11b09ee418696f142624d`.
- Public export contains planning-only `06_resulting_code` docs and no generated client implementation.
- No donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links, emails, or full donor URLs were pushed.
## Runtime API Inspection Assumptions - 2026-05-11

- Generic `/slot/v1` endpoints and `RuntimeEnvelopeResponse` are treated as proven current-source contracts for planning only.
- Little Gangster/8001 is not assumed to use `/slot/v1` until a route, runtime package, and payload adapter are proven.
- `presentationPayload` is treated as the likely browser-visible v0.3 render payload container, but the exact Little Gangster schema extension remains
  unproven.
- Browser/client result authority remains forbidden; browser code must render backend/runtime payloads only.
- Direct runtime consumption of the project v0.3 `math_package.json` remains unproven.
- GameClientBuilder implementation remains blocked until runtime owner and result API contract are proven and explicitly approved.

## Public Export Validator Reliability - 2026-05-11

- The external reviewer-observed public GitHub state contradicted the prior validation claim, even though the local public export working tree did not
  reproduce the collapsed README, reviewer guide, or validator at sprint start.
- Future public export validation is trusted only when the validator compiles, runs after the final public export rewrite, and rejects collapsed
  Markdown or minified Python.
- This sprint changed public export formatting and validator/report reliability only; no gameplay, runtime, registration, wallet, client build, or
  release approval changed.

## Validation Trust Hardening - 2026-05-11

- Agent-authored validation reports are not sufficient proof of public export correctness.
- Public export validation may be called passed only after local validation, commit, push, and fresh post-push clone validation of the pushed commit.
- WorkflowOrchestrator is treated as a routing and gatekeeping skill, not an implementation skill.
- The next technical step remains ProtocolAndSchemaMapper runtime adapter planning; GameClientBuilder implementation remains blocked.

## Public Export Validation Emergency Fix - 2026-05-11

- The public GitHub raw files are treated as the source of truth for public export validation.
- The previous public validation report is treated as false because it was contradicted by external raw GitHub review.
- Public validation success now requires working-tree validation, committed git-blob validation, pushed branch update, and GitHub-raw validation.
- The emergency public push is blocked because the available GitHub authentication cannot create/update
  `.github/workflows/public-export-validation.yml`.

## Public Export Validation Push Without Workflow - 2026-05-11

- GitHub Actions workflow publication is deferred because the current GitHub authentication lacks workflow scope.
- Public export validation may still be trusted for this sprint because working-tree validation, committed git-blob validation, and GitHub raw
  validation all passed for pushed commit `829472dab94f2cad01639a23cba83645bc62c920`.
- The deferred workflow remains documented under `09_release/` and is not included under `.github/workflows/` in the pushed public commit.
- No gameplay, math, runtime, registration, wallet, client build, asset, or release approval gate changed.

## Runtime Adapter Planning - 2026-05-11

- Generic `/slot/v1` and `RuntimeEnvelopeResponse` remain proven for current-source planning, not selected production truth for Little Gangster/8001.
- `presentationPayload` is the candidate browser-visible container for v0.3 render state, but the current generic presentation schema is strict and
  requires extension/review before direct v0.3 payload use.
- Little Gangster runtime owner remains unproven.
- Little Gangster result API contract remains unproven.
- Backend/runtime must own RNG, outcome generation, win/cap decisions, wallet/accounting, round completion, persistence, and history/recovery.
- Browser/client remains renderer-only.
- A minimum fixture may be defined later for planning-only renderer work, but it cannot prove runtime ownership, payout correctness, wallet
  accounting, registration, or release readiness.
- No public export, GitHub push, client code, runtime code, registration artifacts, DB/Cassandra action, wallet/API call, donor browsing, asset
  capture, or release approval occurred in this sprint.

## GameClientBuilder Fixture Planning - 2026-05-12

- Static fixture JSON files are planning/test data only, not production client code.
- Fixture payloads use `presentationPayload.gamePayload` as the preferred reusable extension candidate.
- `presentationPayload.littleGangsterV03` remains a fallback option only if the runtime schema team rejects the generic extension.
- The presentation payload extension remains pending schema review.
- Little Gangster runtime owner remains unproven.
- Little Gangster v0.3 result API contract remains unproven.
- GameClientBuilder implementation remains blocked.
- A later static renderer prototype may be considered only if the user explicitly approves prototype generation.


## Backend Runtime Adapter Proof - 2026-05-12

- Generic `/slot/v1` envelope remains proven for planning, but Little Gangster/8001 runtime ownership remains unproven.
- `presentationPayload.gamePayload` is the preferred reusable extension candidate, but current strict core-protocol schema does not allow it today.
- `presentationPayload.littleGangsterV03` remains fallback only if the schema/runtime team rejects generic `gamePayload`.
- Existing 7001 `presentationPayload.mathBridge` is evidence of a candidate custom extension pattern, not Little Gangster proof.
- The 24 non-production fixtures are compatible with the proposed adapter concept but need strict schema adjustments before automated protocol
  validation.
- Backend adapter implementation and full GameClientBuilder implementation remain blocked.
- A later static renderer prototype is allowed only as fixture-only non-production work after explicit user approval.


## Static Fixture Renderer Prototype - 2026-05-12

- The user explicitly approved a fixture-only static renderer prototype for local review.
- The prototype is non-production planning code only and is not the real game client.
- The prototype consumes static non-production fixtures and does not prove runtime owner, result API, wallet/accounting behavior, registration, or
  release readiness.
- Browser/client production authority remains forbidden: no production RNG, no authoritative outcome calculation, and no wallet/accounting mutation.
- Full GameClientBuilder implementation remains blocked.

## Presentation Payload Schema Extension Review

- Assumption status: SOURCE_BACKED_PLANNING_ONLY.
- The reusable extension should prefer `presentationPayload.gamePayload` for Little Gangster and future donor-inspired games.
- Current strict core-protocol schema does not support `gamePayload`, `littleGangsterV03`, or `mathBridge` as canonical fields.
- Transport/server evidence is permissive in places, but that does not replace schema approval.
- `mathBridge` remains a 7001 reference pattern only unless the platform team deliberately generalizes or migrates it.
- Backend adapter implementation and GameClientBuilder implementation remain blocked.

## Source Patch Planning for presentationPayload.gamePayload

- Assumption status: PATCH_PLAN_READY_SOURCE_NOT_MODIFIED.
- `presentationPayload.gamePayload` remains the recommended reusable extension point.
- The first source patch should keep `gamePayload` optional and keep the parent presentation schema strict.
- Core protocol should use an object-shaped `payload` at the reusable boundary; game packages can add typed validation later.
- Existing 7001 `mathBridge` should remain unchanged in the first patch and should be covered by compatibility tests.
- Staging source modification requires explicit future approval.
- Backend adapter implementation and full GameClientBuilder implementation remain blocked.

## Source Patch Apply for presentationPayload.gamePayload

- Assumption status: SOURCE_PATCH_APPLIED_WITH_TOOLCHAIN_CAVEATS.
- The approved reusable `presentationPayload.gamePayload` extension is now applied to canonical JSON schemas,
  core-protocol runtime validation, core transport types, and UI-kit passthrough mapping.
- Parent `presentationPayload` strictness remains required; arbitrary top-level presentation fields are still not
  approved.
- Existing 7001 `mathBridge` behavior remains unchanged.
- `new-games-server` was not modified because no 8001 emission branch or backend adapter implementation was
  approved.
- Runtime owner 8001 remains unproven.
- Little Gangster v0.3 result API remains unproven.
- Backend adapter implementation and full GameClientBuilder implementation remain blocked.

## Strict Fixture Update for presentationPayload.gamePayload

- Assumption status: STRICT_FIXTURES_VALIDATED_NON_PRODUCTION.
- All 24 original renderer-planning fixtures now have strict response-envelope variants under
  `06_resulting_code/planning/fixtures/strict_schema_examples/`.
- The strict variants validate against the patched `/slot/v1` response schemas and v0.3 result schema.
- Non-production markers are preserved inside `gamePayload.payload.state_persistence.fixture_metadata`.
- Staging source was not modified in this sprint.
- The strict fixtures can be used as planning/test examples for a future backend adapter, but they do not approve
  backend adapter implementation.
- GameClientBuilder implementation remains blocked.

## Backend Adapter Implementation Planning

- Assumption status: PATCH_READY_PLAN_ONLY_IMPLEMENTATION_BLOCKED.
- The recommended future target is `new-games-server/src/games/little-gangster/` plus a guarded 8001 branch in
  `new-games-server/src/index.ts`.
- The 7001 runtime files are reference-only and do not prove Little Gangster runtime ownership.
- The adapter input must be backend-owned authoritative v0.3 result data plus runtime, wallet, persistence, and
  history context.
- The adapter output must be a valid `/slot/v1` envelope with v0.3 render data under
  `presentationPayload.gamePayload`.
- The 24 strict fixtures are the future non-production test contract, not production runtime proof.
- No Staging source was modified in this sprint.
- Backend adapter implementation and full GameClientBuilder implementation remain blocked until explicit approval.

## Authoritative Server Math Design

- Assumption status: AUTHORITATIVE_DESIGN_COMPLETE_IMPLEMENTATION_BLOCKED.
- Little Gangster must define its own server-authoritative math, state, recovery, and history model.
- 7001 / Crazy Rooster is not an authoritative math source for Little Gangster; it may only be a structural
  reference for package layout, runtime mapper style, test style, envelope usage, and presentation payload pattern.
- Recommended authoritative owner is a future Little Gangster server-side math/runtime module integrated through
  the backend adapter and `presentationPayload.gamePayload`.
- Authoritative owner remains unproven until the source target is approved, implemented, tested, and certified.
- Bonus buy is designed with blocker `bonus_buy_cost_ev_pending`.
- Jackpot support is designed as hooks only; `jp_enabled=false` until product approval.
- VABS/Lasthands history is required to store server-owned replay, recovery, cap, feature, and audit references.
- Browser/client remains renderer-only and must not generate production RNG or authoritative wins.
- Registration remains metadata/config/routing only and must not import executable math.
- Backend adapter implementation, GameClientBuilder implementation, registration, wallet tests, and release remain
  blocked.

## Consolidation Gate: Math Config History

- Assumption status: CONSOLIDATION_COMPLETE_IMPLEMENTATION_BLOCKED.
- The project is not going in circles; previous sprints resolved distinct gates and narrowed unknowns.
- Future delivery can merge repeated protocol/schema/fixture planning, but must not skip runtime owner, result API,
  math simulation, registration serializer, VABS/history, wallet, asset, and release gates.
- GL/template settings are mapped to math/runtime/registration dependencies, but values remain incomplete.
- RTP 96/94/92 flexibility is covered as planning, but model-specific simulation outputs remain pending.
- VABS/VBA/Lasthands/history coverage is design-complete for planning, but exact 8001 storage/serialization is not
  proven.
- Deterministic replay payload is preferred over screenshot binaries unless product/current-GS evidence proves
  screenshot storage is required.
- Checkpoint git review is due soon, but public export/push was not run in this sprint.
- Recommended next sprint is MathModelDesigner authoritative simulation/config refinement.

## 2026-05-12 14:05:14 - Authoritative Simulation Config Refinement

- RTP 96/94/92 profiles created with provisional candidate values for smoke simulation only; exact values are not final or certified.
- Cluster-equivalent bet metadata is preferred over fixed-line formulas; fixed-line fields remain compatibility placeholders only.
- Bonus-buy cost multipliers are candidates and EV remains blocked pending simulation.
- Jackpot is disabled by default; hooks are present for future extension only.
- Deterministic replay remains preferred for VABS/VBA/Lasthands; screenshot requirement remains unverified.

## 2026-05-12 14:33:04 - Fast-Lane Optimization

- Compact SprintReporter is the default for normal planning sprints.
- Subagents are considered but not automatic; main agent decides based on bounded read-only benefit.
- Checkpoint review/push remains due, but no push was run in this sprint.
- Implementation gates remain closed unless explicit user approval and manifest gates allow them.

## 2026-05-12 15:26:48 - Checkpoint Git Review Push

- Public export validation is trustworthy for commit `ca854797d2d67def46f17dd989164b71ce49cc44` because working-tree, staged/index, committed blob,
  and GitHub raw checks passed.
- Checkpoint push is no longer due after this sprint.
- Public export remains sanitized; donor assets, screenshots/HAR/raw logs, raw secrets, full donor URLs, and tokenized URLs are excluded.
- Implementation and release gates remain closed.

## 2026-05-12 16:59:34 - Public Export Corruption Contradiction

- External raw-content evidence contradicted the previous checkpoint validation claim for commit `ca854797d2d67def46f17dd989164b71ce49cc44`.
- The previous `public_export_validation_passed` and `github_raw_validation_passed` claims are reset to false until a project-local validator outside
  the public export validates GitHub raw content.
- Root cause is not proven from current local files; the proven failure is the validation trust boundary.
- Public export success must not be claimed from a validator stored only inside the export.

## 2026-05-12 17:04:16 - Public Export Corruption Fix Completed

- Replacement public export commit `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` passed the project-local GitHub raw validator.
- Raw line counts: README 49, reviewer 44, validator 193, WorkflowOrchestrator skill 67.
- Exact collapse root cause remains not proven, but the previous trust boundary has been fixed.

## 2026-05-12 17:24:01 - Raw-Safe Public Export

- The previous public export at `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` was treated as still corrupted based on external raw line counts.
- A new raw-safe export was built from scratch at `.` using selected safe files only.
- The new public commit `e0e5a2e04b1c793bf06a586601a3778154e6be2c` passed project-local working-tree, git blob, and GitHub raw validation.
- Future public export success should prefer raw-safe export mechanics over the abandoned old pipeline.

## 2026-05-12 17:42:40 - Math Calibration Smoke Sprint

- The authoritative smoke simulator ran for `rtp_96`, `rtp_94`, and `rtp_92` with 75 deterministic rounds per model.
- The simulator output is structural smoke evidence only, not certification-grade RTP calibration.
- Bonus-buy EV, free-spin/feature-mode probabilities, symbol weights, cluster paytable, and GL registration values remain provisional or blocked.

## 2026-05-13T03:56:32Z - Calibration Diagnostics Assumptions

- The current simulator is non-production and diagnostic-only.
- Observed return multipliers near 0.20x are not treated as certified RTP evidence.
- Bonus-buy EV, free-spin loops, and feature-mode contribution remain blocked until modeled explicitly.
- Jackpot remains disabled by default unless product confirms otherwise.

## 2026-05-13T04:39:10Z - Model Completeness Fix Assumptions

- The simulator remains non-production and calibration-smoke only.
- `defaultTotalBet` is the current cluster-equivalent bet denominator for local reporting.
- Feature/free-spin and bonus-buy paths are smoke implementations, not certified EV.
- Bonus-buy cost candidates exist, but EV remains pending.
- Jackpot remains disabled pending product decision.

## 2026-05-13T04:57:31Z - Limited Calibration Tuning Assumptions

- The 6.5x cluster paytable boost is a provisional diagnostic tuning set, not release math.
- Feature trigger probability `0.08` and free-spin counts `12/15/18` are provisional.
- Bonus-buy cost candidates remain unresolved for EV; current bonus-buy smoke RTP is not acceptable for release.
- Exact values remain non-final and certification is not claimed.

## 2026-05-13T08:12:26Z - Second-Pass Calibration Assumptions

- `rtp_92` model-specific clusterPayMultiplier `1.026` is provisional and not certified.
- rtp_96 and rtp_94 are treated as regression baselines for this pass.
- Bonus-buy EV is formula-correct but product-incomplete; purchased feature behavior needs design before tuning.

## 2026-05-13T08:55:01Z - RTP / Volatility Profile Framework Assumptions

- Little Gangster LOW/MEDIUM/HIGH RTP values are provisionally 92.00/94.00/96.00.
- Future games may use different LOW/MEDIUM/HIGH RTP values within 92.00%-99.00%.
- Volatility LOW/MEDIUM/HIGH profiles are placeholders pending simulation.
- Operator selection must resolve to a pretested `mathProfileId`; arbitrary values are blocked.
## Volatility Profile Simulation Design Updates

- LOW / MEDIUM / HIGH volatility levers are provisional planning values only.
- The local simulator can select profiles by `mathProfileId` for smoke simulation, but this is not production runtime behavior.
- Bonus-buy EV remains pending and was disabled for the 9-profile volatility smoke.
- Observed RTP drift across volatility profiles means profile-specific calibration is still required before backend adapter or registration
  generation.
- Exact values remain non-final and uncertified.

## 3x3 Profile Calibration First-Pass Updates

- The profile-specific calibration overlay is a local simulation artifact, not release math.
- All 9 profiles reached +/-2.0 percentage-point smoke tolerance in the bounded first pass, but this does not prove large-sample stability.
- Bonus-buy EV remains excluded from calibration and must be handled before profile approval.
- Cap/max-win tail behavior remains unproven because cap frequency stayed at zero in smoke runs.
- Exact values remain non-final and uncertified.

## Raw-Safe Checkpoint Review/Push 2026-05-13

- Raw-safe checkpoint commit `b7b420ba0916af6f6073f5e714ab73e1d36d4f93` passed GitHub raw validation.
- Public checkpoint includes recent safe workflow, RTP/volatility, simulator, and calibration artifacts.
- Public checkpoint excludes donor assets, screenshots/HAR, raw logs, raw secrets, full donor URLs, tokenized URLs, implementation code, registration
  artifacts, DB actions, wallet calls, and release approval.
- Checkpoint push is no longer due after this sprint.
- Implementation and release gates remain closed.

## Large-Sample Stability 2026-05-13

- The 20,000-round-per-seed target was attempted but exceeded fast-lane runtime, so the completed stability run used 10,000 rounds per seed and
  records `large_sample_limited_by_runtime`.
- The 3x3 profile matrix is not stable enough for backend adapter implementation: 8 of 9 profiles were outside +/-2.0 percentage points in the larger
  smoke sample.
- Volatility ordering remained preserved in the larger smoke sample, but exact RTP/volatility values remain non-final and uncertified.
- Cap/max-win tail frequency remains unproven because no cap hits were observed.
- Bonus-buy EV remains blocked and should move to a separate design sprint before tuning or implementation.

## 3x3 Profile Stability Triage 2026-05-13

- The 8-profile failure is assumed to be caused primarily by small-sample calibration overfit and profile-specific tuning weakness, not by a proven
  harness bug.
- `mathProfileId` resolution and profile-adjustment coverage matched all 9 profiles in the matrix.
- The previous 2 seeds x 1,000 rounds calibration pass is not sufficient evidence for backend adapter or registration work.
- The next math step should recalibrate the 3x3 overlay with larger train/validation seed splits before bonus-buy EV design.

## RTP Confidence Scale Correction 2026-05-13

- The prior 10,000-round-per-seed profile results are now classified as `small_sample_profile_stability_inconclusive`.
- Profiles outside +/-2 percentage points in smoke are not true RTP failures and profiles inside smoke tolerance are not RTP approved.
- Small samples prove wiring, denominator, profile routing, and obvious logic sanity only.
- Meaningful RTP confidence for high-volatility/tail-heavy games may require millions, tens of millions, hundreds of millions, or one billion rounds
  depending on feature rarity and cap/tail behavior.
- Backend adapter, registration, and release gates must not open from smoke-only RTP evidence.

## Confidence-Scale Raw-Safe Checkpoint 2026-05-13

- The public checkpoint is assumed trustworthy only because GitHub raw validation passed after push.
- The raw-safe checkpoint includes the RTP confidence-scale correction artifacts and safe skill snapshots.
- The checkpoint does not make RTP/volatility values final or certified.
- Bonus-buy EV, backend adapter implementation, registration generation, wallet, DB, and release work remain blocked.

## Train / Validation Simulation Design 2026-05-13

- Training and validation seed families must remain distinct.
- Tuning may use training runs only; validation runs can pass, fail, or send a profile back to training, but cannot tune values.
- No new simulations were run in this sprint.
- No math values were tuned or frozen in this sprint.
- Backend adapter, registration generation, and release gates remain blocked until future train/validation evidence and explicit approval exist.

## External Simulation Job Export 2026-05-13

- External train, validation, and tail job definitions are planning artifacts until run on approved dedicated infrastructure.
- The Codex dry-run covered all 9 profiles with 100 rounds each for package validation only.
- Train results may inform future tuning; validation results must not tune values.
- Tail/max-win jobs are for rare event discovery and are not certification by themselves.
- Backend adapter, registration generation, and release gates remain blocked.

## Train Results Import Attempt 2026-05-13

- The expected external train result directory was missing.
- No train results were imported, parsed, or summarized.
- No validation seeds were used for tuning.
- No tuning values were changed.
- Backend adapter, registration generation, and release gates remain blocked.

## Local Simulation Runner 2026-05-13

- A local, non-production simulation runner can now run benchmark, smoke, and future train jobs from Terminal.
- The benchmark completed 900 proof rounds across all 9 profiles at 932.15 rounds per second on this machine.
- ETA estimates from the tiny benchmark are 17.9m for 1M rounds, 3.0h for 10M rounds, 29.8h for 100M rounds, and 12.4d for 1B rounds.
- The local proof smoke covered all 9 profiles with 100 rounds per profile.
- Large train, validation, and tail-discovery simulations were not run in this sprint.
- Validation seeds must not be used for tuning.
- Exact values remain non-final and uncertified.
- Backend adapter, client, registration, DB, wallet, donor, asset, and release gates remain blocked.

## Local 10M Total Train Run 2026-05-13

- A local train-only simulation ran across all 9 RTP/volatility profiles.
- The run used 5 train seeds per profile and 222,222 rounds per seed.
- Planned total rounds were 9,999,990 and actual total rounds were 9,999,990.
- Validation seeds were not used.
- Tail-discovery jobs were not run.
- Bonus-buy jobs were not run.
- No tuning values were changed during the run.
- Results are training evidence only; exact values remain non-final and uncertified.
- Backend adapter, client, registration, DB, wallet, donor, asset, and release gates remain blocked.

## 10M Train Tuning Decision 2026-05-14

- The 10M train outputs were imported as training evidence only.
- Validation seeds were not used and validation jobs were not run.
- Four profiles need upward RTP adjustment: LOW/MEDIUM, MEDIUM/LOW, MEDIUM/MEDIUM, and MEDIUM/HIGH.
- Five profiles need downward RTP adjustment: LOW/LOW, LOW/HIGH, HIGH/LOW, HIGH/MEDIUM, and HIGH/HIGH.
- The profile-specific adjustment overlay was updated for all 9 profiles.
- No base rule JSON, bonus-buy rules, jackpot rules, or post-spin payout scaling were used.
- Optional verification was skipped to keep this fast-lane sprint within the requested file cap.
- Exact values remain non-final and uncertified; validation, tail-discovery, bonus-buy EV, backend, client, registration, DB, wallet, donor, asset,
  and release gates remain blocked.

## 10M Overlay Train Rerun 2026-05-14

- The updated profile-specific overlay was used for a train-only rerun across all 9 RTP/volatility profiles.
- Validation seeds were not used and validation jobs were not run.
- The train rerun produced 6 of 9 profiles within +/-2 percentage points and 3 outside the gate.
- Volatility ordering remains preserved, but the train set is not assumed good enough for validation until the outliers are addressed or explicitly
  accepted.
- Exact values remain non-final and uncertified; backend adapter, client, registration, DB, wallet, donor, asset, and release gates remain blocked.

## Targeted Outlier Adjustment 2026-05-14

- Only the three outlier profile overlay entries were adjusted: LOW/MEDIUM, MEDIUM/HIGH, and HIGH/MEDIUM.
- The six previously passing profile overlay entries are assumed unchanged in this targeted pass.
- The targeted rerun used train seeds only and produced 3 of 3 targeted profiles within +/-2 percentage points.
- The composite train gate now has 9 of 9 profiles within +/-2 percentage points and 0 outside.
- Validation seeds remain unused; exact values remain non-final and uncertified.

## Validation Seed Check 2026-05-14

- Validation seeds were used only for pass/fail evidence, not tuning.
- The validation run covered all 9 RTP/volatility profiles with 9,999,990 total rounds.
- The validation gate passed for the train/validation stage with 9 of 9 profiles within +/-2 percentage points.
- This is not certification and does not make exact values final.
- Tail/max-win discovery and bonus-buy EV remain unresolved, so backend adapter, registration, and release gates remain blocked.

## Tail / Max-Win Pilot 2026-05-14

- The bounded tail pilot used 9,999,990 total tail-phase rounds across all 9 profiles.
- No train or validation seeds were used in the tail pilot.
- Bonus-buy and jackpot were disabled and no tuning values were changed.
- Cap hits observed: false; possible max win remains planning-only and not final.
- Backend adapter, registration generation, and release gates remain blocked.

## MathProfileCalibrator Skill Creation 2026-05-14

- Future games require exactly LOW/MEDIUM/HIGH RTP levels and LOW/MEDIUM/HIGH volatility levels.
- RTP requests outside 92.00% to 99.00% must be blocked unless explicit approval exists.
- MathProfileCalibrator owns train-only calibration loops after MathModelDesigner creates the initial profile matrix and simulator/runner.
- Validation seeds must not be used for tuning, and backend/registration/release gates remain blocked by default.

## MathProfileCalibrator RTP Range Update 2026-05-14

- Reusable future-game requested average RTP range is now 91.00% to 99.70%, inclusive.
- Future-game RTP levels must be strictly ascending: LOW < MEDIUM < HIGH.
- Decimal RTP values are allowed and should be normalized/reported to two decimals where practical.
- This supersedes the earlier reusable 92.00% to 99.00% assumption.
- Little Gangster remains 92.00% / 94.00% / 96.00% unless explicitly changed later.

## RTP Range Raw-Safe Checkpoint 2026-05-14

- Raw-safe public checkpoint `6fc02b341be2e2432b79b810b75b726794d1db7a` includes the MathProfileCalibrator RTP range update.
- GitHub raw validation passed for the pushed checkpoint.
- Little Gangster RTP values were not changed.
- No donor assets, screenshots, HAR, secrets, client/runtime/registration, DB, wallet, or release artifacts were pushed.

## 2026-05-14 - Bonus-Buy EV Design Assumptions

- Bonus buy remains in Little Gangster scope unless an explicit product decision removes it.
- Current cost candidates are 100x, 125x, and 150x total bet, but product approval is still pending.
- BF_RTP must be calculated separately from base RTP using bonus-buy cost as denominator.
- Base train and validation gates do not approve bonus-buy EV.
- BF_RTP, BF_RTP_MIN, and BF_BETS remain blocked for registration until focused bonus-buy simulations pass.
- Backend adapter implementation and GameServerRegistrar generation remain blocked.
- Exact values remain non-final and certification status remains false.

## 2026-05-14 - Bonus-Buy EV Simulation Assumptions

- Bonus-buy EV simulation used train seed family only; validation seeds were not used.
- The 100,000 and 25,000 purchased bonus rounds per profile targets exceeded fast-lane runtime, so the completed result is a runtime-limited
  1,000-per-profile path verification sample.
- Candidate costs 100x, 125x, and 150x were evaluated as denominators against the same purchased-feature win sample.
- Current purchased-feature value path is far below desired BF RTP when divided by 100x/125x/150x; current candidates are not acceptable as-is.
- Estimated target-matching costs are planning-only and imply a bonus-buy cost/model redesign decision before backend or registration work.

## 2026-05-14 - Bonus-Buy Redesign Decision Assumptions

- Current bonus-buy candidate costs 100x, 125x, and 150x are not acceptable from the runtime-limited EV sample.
- The 4x-8x target-matching cost range is treated as suspicious diagnostic evidence, not an approved product cost.
- The bonus-buy denominator appears correct; the purchased-feature start/value model is likely incomplete or too weak.
- Purchased bonus should be redesigned as a premium feature entry with explicit golden-square, rainbow, coin/special, retrigger, and
  volatility-specific behavior before any active config change.
- `bonus_buy_v2_draft_model.json` is draft-only and not active config.
- Backend adapter, registration generation, and release remain blocked.

## 2026-05-14 - Latest Results Documentation Consolidation Assumptions

- Central status documents now summarize existing Little Gangster math evidence without creating new simulation evidence.
- Base 3x3 train and validation gates are documented as passed, but exact values remain non-final and certification status remains false.
- Tail/max-win pilot values are planning-only because no cap hits were observed and the configured 10,000x cap was not empirically reached.
- Bonus-buy current 100x/125x/150x candidates are documented as unacceptable; bonus-buy v2 remains draft-only and inactive.
- Backend adapter, GameClientBuilder, GameServerRegistrar generation, wallet/VABS/Lasthands tests, final art approval, and release remain blocked.

## 2026-05-14 - Bonus-Buy V2 Draft Diagnostic Assumptions

- The bonus-buy v2 diagnostic used the inactive draft model only; active `bonus_buy_rules.json` was not changed.
- The diagnostic used train seed family only and did not use validation seeds for tuning or evidence.
- A 25,000-per-profile fallback run was attempted but stopped due fast-lane runtime; the retained result is a 1,000-per-profile diagnostic
  path-verification sample.
- The v2 draft materially improves BF_RTP versus v1, but 3 of 9 profiles remain outside the +/-2 percentage-point planning band at 100x.
- 100x is closest among 100x/125x/150x for every profile, but the candidate set is not acceptable for all profiles yet.
- Bonus buy remains blocked until v2 feature-value refinement, product approval, and train/validation EV evidence are completed.

## 2026-05-14 - Bonus-Buy V2 Outlier Refinement Assumptions

- The refinement created `bonus_buy_v2_refined_draft_model.json` as draft-only and inactive.
- Only draft-only feature-value entries were adjusted; active `bonus_buy_rules.json` and the original `bonus_buy_v2_draft_model.json` were not
  modified.
- Initial 100x outliers refined were LOW/HIGH, MEDIUM/HIGH, and HIGH/HIGH.
- The refined 10,000-per-profile train-seed diagnostic tested all 9 profiles and kept validation seeds unused.
- Refined 100x result is still not clean: 6 of 9 profiles are within +/-2 percentage points and 3 remain outside.
- 125x and 150x remain blocked as separate premium/super tiers unless separately designed and approved.
- Bonus buy remains blocked for backend adapter and registration generation.

## 2026-05-14 - Bonus-Buy V2 Pass2 Final Refinement Assumptions

- The pass2 refinement created `bonus_buy_v2_refined_pass2_draft_model.json` as draft-only and inactive.
- Active `bonus_buy_rules.json`, original `bonus_buy_v2_draft_model.json`, and first refined `bonus_buy_v2_refined_draft_model.json` were not
  modified.
- Latest source outliers refined were LOW/HIGH, MEDIUM/HIGH, and HIGH/HIGH; all were over target at 100x in the latest refined diagnostic.
- The pass2 10,000-per-profile train-seed diagnostic tested all 9 profiles and kept validation seeds unused.
- Pass2 100x result is clean at diagnostic scale: 9 of 9 profiles are within +/-2 percentage points.
- 100x can move to bonus-buy train/validation EV planning as the standard candidate, but exact values remain non-final and certification status
  remains false.
- 125x and 150x remain blocked as separate premium/super tiers unless separately designed and approved.
- Bonus buy still blocks backend adapter and registration generation until train/validation EV and product approval pass.

## 2026-05-14 - Bonus-Buy V2 100x Train EV Gate Assumptions

- The 100x train EV gate used the inactive pass2 draft model and train seed family only.
- Active `bonus_buy_rules.json`, the pass2 draft model, and base profile tuning overlays were not modified.
- The train phase ran 25,000 purchased-feature simulations per profile, 225,000 total.
- Train gate did not pass: 8 of 9 profiles were within +/-2 percentage points.
- The train outlier was `LG_8001_RTP_HIGH_VOL_HIGH` at 98.235423% BF_RTP versus a 96.00% target, delta +2.235423 pp.
- Validation was correctly not run because the train gate failed.
- Validation seeds were not used for tuning.
- Bonus buy remains blocked for product review, backend adapter, and registration generation.

## 2026-05-14 - Bonus-Buy BF_RTP Policy Assumptions

- Bonus-buy BF_RTP may differ from base RTP if product-approved, disclosed, modeled, validated, and registered separately.
- Base RTP remains `RTP_WITHOUT_BF`; bonus-buy RTP remains `BF_RTP`; bonus-buy minimum/planning floor remains `BF_RTP_MIN`.
- Bonus-buy validation should compare against declared BF_RTP planning targets, not automatically against base RTP targets.
- `LG_8001_RTP_HIGH_VOL_HIGH` is reclassified as `BF_RTP_above_base_target`, not a model failure, under the separated BF_RTP policy.
- Declared BF_RTP targets are train-only planning values; product approval, validation evidence, certification, backend adapter, and registration
  generation remain blocked.
- No simulations were run and no validation seeds were used in this sprint.

## 2026-05-14 - Bonus-Buy 100x Declared BF_RTP Validation Assumptions

- Bonus-buy 100x validation used validation seed family only and did not use validation seeds for tuning.
- Validation compared against declared BF_RTP planning targets, not base RTP targets.
- The validation run tested all 9 profiles at 25000 purchased-feature simulations per profile, 225000 total.
- Validation passed for 9 of 9 profiles within +/-2 percentage points against declared BF_RTP targets.
- Overfit risk is `moderate_watch_all_profiles_within_tolerance` because all profiles passed, but the largest declared-target delta remains above 1
  percentage point.
- Active `bonus_buy_rules.json`, declared BF_RTP targets, pass2 draft model, and base profile tuning overlays were not modified.
- Bonus buy is ready for product approval review, but backend adapter implementation and registration generation remain blocked until product approval
  and runtime/registration representation are accepted.

## 2026-05-14 - Bonus-Buy Product Approval Package Assumptions

- The 100x bonus-buy model is ready for product approval review because validation passed against declared BF_RTP planning targets for 9 of 9
  profiles.
- The approval package is decision-ready only; it does not approve release, certification, active config, backend adapter implementation, or
  GameServerRegistrar generation.
- 125x and 150x remain blocked as separate premium/super tiers and are not part of the current approval request.
- No more bonus-buy math loops should run by default unless product rejects the package or requests a specific change.
- No simulations, tuning, active config changes, backend/client/registration generation, wallet/DB actions, donor work, asset capture, or release
  approval occurred in this sprint.

## 2026-05-14 - Bonus-Buy Option A Product Decision Assumptions

- Product selected Option A for 100x bonus buy: implementation planning only.
- 100x may be represented in backend adapter planning, runtime payload planning, future registration planning as a candidate, and
  VABS/Lasthands/history planning.
- This does not approve release, certification, backend adapter implementation, active config changes, GameServerRegistrar generation/apply,
  DB/Cassandra changes, wallet calls/tests, or final assets.
- 125x and 150x premium/super tiers remain blocked.
- No simulations, tuning, implementation, registration artifacts, DB/wallet actions, donor browsing, asset capture, or release approval occurred in
  this sprint.

## 2026-05-15 - Backend Adapter Representation Planning Assumptions

- Backend adapter planning may represent the approved-for-planning 100x bonus-buy payload, but backend adapter implementation is not approved.
- 100x bonus buy is not release-approved, not certified, not runtime-tested, not wallet-tested, not VABS/Lasthands-tested, and not registration-ready.
- Adapter representation must carry `bonus_buy_runtime_validation_pending`, `bonus_buy_wallet_accounting_test_pending`,
  `bonus_buy_vabs_lasthands_test_pending`, `bonus_buy_tail_maxwin_confirmation_pending`, `bonus_buy_release_approval_pending`, and
  `bonus_buy_certification_false`.
- Registration generation remains blocked until runtime, wallet/accounting, VABS/Lasthands/history, and product/release gates are complete.
- No backend code, Staging source, client code, registration artifacts, DB/Cassandra changes, wallet calls, donor browsing, asset capture, or release
  approval occurred in this sprint.

## 2026-05-15 - Backend Adapter Apply Assumptions

- Backend adapter implementation apply was explicitly approved for Staging source only and limited to Little Gangster 8001 payload representation.
- The implementation creates an isolated `new-games-server/src/games/little-gangster/` adapter module and guarded gameId `8001` presentation-payload
  branches.
- The adapter supports planning/testing representation for base spin, cascades, 3x3 `mathProfileId`, 100x bonus-buy purchase/result, declared BF_RTP,
  state persistence, reconnect, and VABS/Lasthands/history fields.
- 100x bonus buy remains implementation-planning-only: not release-approved, not certified, not runtime-tested, not wallet-tested, not
  VABS/Lasthands-tested, and not registration-ready.
- 125x and 150x remain blocked as separate premium/super tiers.
- No active math values, active `bonus_buy_rules.json`, RTP/volatility profiles, BF_RTP targets, registration configs, GameClientBuilder code,
  Gamesv1/games/8001 package, registration artifacts, DB/Cassandra changes, wallet/API calls, donor browsing, asset capture, or release approval
  occurred.
- Targeted Little Gangster adapter tests passed; full repository typecheck remains blocked by missing local checkout dependencies.

## 2026-05-15 - Lifecycle Wrapper Source Planning Assumptions

- Lifecycle wrapper source planning was read-only against Staging source and did not modify Staging.
- Crazy Rooster / 7001 is not authoritative; it remains weak candidate/reference evidence only.
- Current Little Gangster 8001 adapter remains a guarded `presentationPayload.gamePayload` mapper only, not the full GS lifecycle owner.
- Recommended wrapper option is Option 5: create a small 8001 lifecycle wrapper first, then add a separate VABS/VBA/Lasthands visual history route.
- Recommended wrapper source location is `new-games-server/src/games/little-gangster/lifecycle/`.
- Recommended VABS visual history route source location is `new-games-server/src/games/little-gangster/history/`.
- `new-games-server/src/index.ts` is the proven route integration host, but implementation is not approved in this sprint.
- GameClientBuilder, GameServerRegistrar generation, wallet/API tests, DB/Cassandra work, donor browsing, asset capture, certification, and release
  remain blocked.

## 2026-05-15 - ParallelMathValidator Skill Creation Assumptions

- `ParallelMathValidator` is a reusable generic skill for future projects, not a Little Gangster-specific math change.
- Future games may define LOW/MEDIUM/HIGH RTP values anywhere inside 91.00% to 99.70%, strictly ascending, with LOW/MEDIUM/HIGH volatility and nine
  pretested `mathProfileId` profiles unless product explicitly approves a smaller matrix.
- Large train/validation/tail, bonus-buy EV, FRB/promo liability, registration math field extraction, and certification evidence should be routed to
  ParallelMathValidator instead of endless main-thread calibration loops.
- Parallel workers must write only to a declared output folder and must not change active configs, tune from validation seeds, perform
  backend/client/registration/release work, call wallets, browse donors, capture assets, or claim certification.
- Little Gangster active math values, active `bonus_buy_rules.json`, profile calibration adjustments, and Staging source were not changed in this
  sprint.

## 2026-05-15 - Raw-Safe Checkpoint Review Assumptions

- The ParallelMathValidator/lifecycle checkpoint was prepared in the raw-safe export working tree but was not committed or pushed.
- Content-depth checks passed for the critical checkpoint files.
- The existing raw-safe public export validator failed before commit on long Markdown lines.
- Focused safety scanning found private local paths and one non-allowlisted redacted donor host in prepared export content.
- No donor assets, screenshots, HAR captures, Staging source files, runtime source, client code, registration artifacts, DB/Cassandra changes,
  wallet/API calls, or release approvals were pushed.
