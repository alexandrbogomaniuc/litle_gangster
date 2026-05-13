# Assumptions And Blockers

## Assumptions

- The redacted donor URL in `project_manifest.json` is enough for ProjectCreator. Future browser/reference work must request the full URL again or use the recorded secret reference.
- The documented stack defaults are acceptable for the manifest because the user explicitly requested them.
- Asset capture is marked allowed because the user explicitly set `asset_capture_allowed: true` and updated the reference mode to `authorized_capture_for_internal_scaffold`; real asset body download, hashing, comparison, and classification
remain deferred to ReferenceAssetInventory.
- Release approval remains false until later workflow gates pass.
- Explicit source/config paths supplied for Sprint 2 were verified by existence/readability only. Their internal contents were not inspected in this sprint except where future skills are explicitly authorized.
- Secret-bearing files were not opened for value extraction. PASS_KEY and test token/user data are represented as secret references only.
- Default bank ID `6275`, subCasinoId `507`, and coin denominations were accepted as explicit user input with source-path existence/readability verified.

## Open Blockers

- PASS_KEY raw value is intentionally unavailable. Future WalletAndLaunchTester must use a local ignored secret reference or fixture, never raw chat text.
- Test user/token raw values are intentionally unavailable. Future launch/wallet tests must use local ignored secret references or fixtures, never raw chat text.
- Client/source/config path contents were not verified in this sprint because only AuthorizedReferenceResearcher and SprintReporter were allowed.
- Browser gameplay coverage may remain partial depending on donor URL validity, runtime load behavior, and demo/test-mode safety.
- AuthorizedReferenceResearcher retry on 2026-05-07 initially could not start browser work because the supplied fresh donor/reference URL field was a placeholder, not a usable URL.
- User later clarified the earlier donor URL should remain the current in-memory URL for this project, and provided a visible in-app browser screenshot showing the playable intro screen.
- Tool discovery did not expose a Google Chrome MCP or the Browser Use Node REPL `js` control tool. With user authorization, Codex used visible OS-level clicks/screenshots against the already-open in-app browser instead.
- Safe demo mode was directly observed through `DEMO BALANCE` and `DEMO BET` labels.
- One safe demo spin was attempted and produced an in-game wallet connection error. Completed spin outcome coverage remains blocked.
- Browser DevTools/HAR metadata is not available from the OS-level visible-browser route. Existing sanitized network metadata comes from the earlier project-local Playwright retry only.
- ReferenceAssetInventory can proceed only for observed intro/base assets and must still keep scaffold assets gitignored, inventoried, quarantined, and blocked from release.
- User then asked Codex to retry Google Chrome MCP. Tool discovery exposed Chrome DevTools MCP on that retry.
- Chrome MCP successfully opened the donor launch, reached demo base game, clicked the spin control, opened menu/game info, and collected screenshots/request metadata without saving bodies.
- Chrome MCP network metadata indicates demo `authenticate`, `gameLaunch`, `keepAlive`, and `bet` calls returned HTTP 200.
- The earlier in-app-browser wallet error is treated as a discrepancy between browser/control paths, not as proof the donor demo is unusable.
- Game-info/paytable observations are reference clues only. Final math must still come from internal math templates, user requirements, validated config, and simulation.

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
- Browser/client runtime contract is partial: 7001 source proves `slot-browser-v1`, `GS_HTTP_RUNTIME`, request counters, idempotency keys, client operation IDs, and `/slot/v1/*` operation names, but the imported `@gamesv1/core-protocol`
package root was not inspected.
- Game Server runtime contract is partial: launch actions and routing bridges were inspected, but the server-side `/slot/v1/*` endpoint implementation remains a blocker.
- Cassandra/config contract is partial: bank 6275, subCasinoId 507, coin values, new-games route properties, `RCasinoSCKS` summary evidence, and generate-only safety are mapped, but no 8001 registration exists and `scn` serialization
remains blocked.
- The explicit 7001/new-games source path uses a newer Vite/PIXI v8-style runtime lane, while uploaded docs describe a legacy Webpack/Vue/PIXI template. Future GameClientBuilder must choose and verify the approved target path.
- No raw secret values should be required for MathModelDesigner. Later WalletAndLaunchTester must use local ignored secret references or fake fixtures.
- Asset release blockers remain unchanged: all captured reference/scaffold assets remain blocked from release.

## ProtocolAndSchemaMapper Open Blockers

- `core_protocol_package_not_inspected`: provide explicit path to `@gamesv1/core-protocol` package or allow targeted inspection of that package root.
- `slot_v1_server_implementation_partial`: provide explicit new-games server/API source path for `/slot/v1/*` endpoint inspection.
- `scn_serializer_missing`: provide a real serializer/tool or approved config-generation pipeline before GameServerRegistrar attempts registration artifacts.
- `math_result_ownership_unknown`: resolve through MathModelDesigner and later runtime integration validation.
- `game_8001_registration_missing`: registration must wait until math/client/build inputs exist.

## ProtocolAndSchemaMapper Third-Party GS Integration Extension Updates

- Little Gangster must not treat Gamesv1, Crazy Rooster, or `slot-browser-v1` as guaranteed truth. They are candidate direction evidence only until current GS source/config/docs prove the lane directly.
- Third-party/new game launch should start through GS launch (`/startgame` wrapper or `/cwstartgamev2.do`) and then redirect to the configured client lane. Direct static-client launch is not sufficient for operator/session/wallet flow.
- `cwstartgamev2.do` authenticates through Common Wallet, creates/resolves a GS session, then redirects to new-games client when route config is enabled; otherwise it can continue to the legacy template route.
- WebGS contains an internal new-games bridge for session validation, wallet reserve/settle, and history read/write. This does not prove WebGS owns slot RNG/result generation.
- `new-games-server` is referenced by 7001 docs as the `/slot/v1/*` slot contract service, but its source root was not explicitly allowed for inspection in this sprint.
- `@gamesv1/core-protocol` remains uninspected and is still a runtime blocker.
- Crazy Rooster 7001 is useful as an integration reference but is not a direct release-ready template for Little Gangster. Its final status docs still require dedicated proof completion for 7001.
- MathModelDesigner can run next only as design/simulation work. It must not claim final runtime ownership, certified RTP, or registration import behavior.
- GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, and release-to-players remain blocked.

## ProtocolAndSchemaMapper Third-Party GS Integration Open Blockers

- `new_games_server_source_path_missing`: provide explicit path to `new-games-server` or authorize targeted inspection.
- `slot_v1_result_owner_unknown`: verify current GS/runtime source directly before trusting any slot-browser-v1 result owner.
- `game_client_builder_blocked_by_inputs`: complete math package, approved art plan, and runtime source proof before building.
- `game_server_registrar_blocked_by_scn_and_8001_inputs`: provide 8001 registration inputs and `scn` serializer/config pipeline before registration generation.

## MathModelDesigner Sprint Updates

- MathModelDesigner created a provisional original Little Gangster math package under `04_math/`.
- The provisional model is a 5x3 fixed-20-line high-volatility slot with wild substitution, scatter pays, free spins, optional bonus buy, and an optional neutral double-up placeholder.
- The model is explicitly not donor-true math. Reference observations are treated only as clues.
- RTP variants were created for 96.0%, 94.0%, and 92.0%.
- Each RTP variant ran a 1,000,000-round deterministic workflow simulation using seed `2026050801`.
- All three variants passed the provisional +/-0.5 percentage-point workflow tolerance.
- The math package is not release-approved and is not certification-grade.
- Browser result authority remains disallowed.
- RNG/result generation must be server/backend-side, not browser-side. Exact final owner remains UNKNOWN/BLOCKED: classic GS, new-games backend, game-specific server package, and GS game processor remain candidates.
- Math is not proven to be imported into GS/Cassandra registration. Registration should treat gameId, name, launch route, bank/casino assignment, client path, RTP display/config values, bet config, feature flags, max-win/cap values, and
template/config records as metadata/config only unless later source proves executable math import.
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
- v0.2 simulator does not scale wins during a run and does not normalize after a run; RTP comes from explicit paytables, symbol weights, connected-cluster evaluation, scatter wins, and free spins.
- v0.2 paytables were calibrated from smoke simulation evidence and remain provisional.
- v0.2 calibration-seed smoke simulations passed provisional workflow tolerance for all three RTP variants.
- v0.2 secondary 100,000-round short seeds drifted outside +/-0.5 percentage-point tolerance, so full multi-seed RTP validation remains open.
- The quality gate result is `PASS_WITH_LIMITATIONS`, not math release approval.
- User stated Staging is now canonical for GS/New Games/Crazy Rooster work. This math sprint did not inspect Staging paths. Future source-inspection skills must update/verify manifest source paths against `[STAGING_ROOT]` and not use old
worktrees as source of truth.

## Math Quality Gate Open Blockers

- `full_6x5_multi_seed_validation_pending`: longer independent multi-seed validation is required before release math approval.
- `v0_1_rtp_scaling_blocks_true_math_validation`: v0.1 is superseded and must not be used for release math.
- `staging_source_root_manifest_update_pending`: future source-inspection skills must verify/update source roots to Staging.

## ArtSceneMapper Sprint Updates

- ArtSceneMapper used selected `v0.2_6x5_cluster_provisional` layout.
- The superseded 5x3 v0.1 model was not used for target scene mapping.
- The target scene layout is a 6-column by 5-row cluster-style symbol grid.
- Scene maps are technical planning artifacts only. They are not final art, not client implementation, not runtime integration, and not release approval.
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
- Evidence supports donor 6x5 cluster, cascade/removal/refill, golden-square, rainbow activation, coin/reveal, bonus buy, Super Turbo, Turbo, Sound, Music, Info, Home, demo balance/bet, and 10,000x max-win messaging.
- Exact donor autoplay stop conditions, bonus-buy confirmation/cost/EV, natural free-spins flow, mobile playable flow, and full win-tier thresholds remain blocked/unobserved.
- v0.2 math remains provisional and now requires donor feature parity revision before full GameClientBuilder.

## Public Git Export Assumptions - 2026-05-10 20:54:42 BST

- The public repository is for external review only and is not a release build.
- Sanitized inventory rows may retain counts, hashes, and release-status metadata but not donor asset bodies or unredacted asset body paths.
- The final public HEAD commit is `a8cfcb2b25f0127a9487a4d41d75e638d20765bd` on branch `main`.
- Public export does not resolve math/runtime/asset/release blockers.


## MathModelDesigner Donor-Parity Retry - 2026-05-11 07:45:26 
- Selected math version moved to `v0.3_donor_feature_parity_provisional` for planning.
- v0.3 models cascades, golden squares, rainbow activation, coin reveals, special reveal candidates, three feature modes, bonus-buy contract, and max-win cap.
- Exact donor probabilities, bonus-buy EV/costs, autoplay stop conditions, runtime owner, and certification-grade validation remain blockers.
- ArtSceneMapper update is required before full GameClientBuilder because v0.3 adds explicit animation-state requirements.


## Public Export Update - 2026-05-11 07:49:21 
- Sanitized public export was rebuilt and pushed after v0.3 math retry.
- Public export validation passed.
- Public export intentionally excludes donor asset bodies, screenshots, HAR, raw network logs, raw secrets, and full donor URLs.


## ExtGame External-Collaboration Requirements Patch - 2026-05-11 08:10:35 
- No raw Mantis body was pasted before this report generation; ExtGame requirements were extracted from the user sprint prompt only.
- ExtGame is now tracked as a separate requirement lane for future ProtocolAndSchemaMapper, MathModelDesigner, GameServerRegistrar, WalletAndLaunchTester, and RTPAndReleaseAuditor work.
- Exact ExtGame field names, raw endpoints, template values, and VBA/FRB/OCB meanings remain evidence-pending and must use sanitized source excerpts only.
- Selected math package was not changed in this sprint.

## Mantis Scope Correction - 2026-05-11

- Corrected assumption: Mantis/ExtGame information is advisory checklist material only and does not select Little Gangster architecture.
- Corrected assumption: ExtGame remains candidate/unverified unless current GS source/config proves it.
- Current Staging evidence provides useful new-games `slot-browser-v1` candidate signals, but that lane is not guaranteed truth and must be verified directly before trust or selection.
- Current GS has external game id, VABS/VBA/history, Lasthand, restart, FRB/cash-bonus, RNG, and round-finished helper concepts, but Little Gangster-specific contracts remain unverified.
- `processTransactions` from Mantis must be translated to current-GS process-equivalent validation unless ExtGame is later proven.
- The expected Staging new-games paths from the team update were missing, while runtime compose points to `platform-source/platform/...` paths that exist; manifest/source roots need cleanup in a future source-inspection sprint.
- New game registration is probably not executable math import; executable math/result logic likely belongs in backend runtime code/config, new-games server, a game-specific server package, or a GS game processor, but the owner remains
unproven.
- No raw Mantis text, private links, emails, secrets, SIDs, signatures, donor assets, screenshots, HAR, or full donor URLs were stored in this correction.

## Current GS Registration/RNG Audit - 2026-05-11

- Corrected assumption: current GS registration appears to configure game/template/bank routing metadata; executable math import during registration is not proven.
- Current Staging evidence supports New Games / `slot-browser-v1` as the strongest candidate lane, but not final source of truth for Little Gangster.
- Current Staging evidence proves WebGS New Games session/wallet/history bridge, but does not prove WebGS itself generates Little Gangster results.
- New Games backend source currently shows sample/provisional backend outcome generation, but final 8001 result owner remains unproven.
- Browser result authority remains forbidden.
- v0.3 math package files modified by the previous patch were boundary metadata/docs only, but touching v0.3 package JSON during a non-math-implementation sprint is recorded as a scope violation for review.
- GameServerRegistrar remains blocked from generation until 8001 registration records, client/runtime paths, serializer/import tooling, and selected runtime lane are proven.

## Public Export Update - 2026-05-11 10:36:00

- Public export commit `17b162ba1dd56d7ee129b154d079be3921280c06` is a sanitized review snapshot only.
- The public export intentionally excludes donor asset bodies, screenshots, HAR, raw network logs, local browser folders, raw secrets, full donor URLs, tokenized URLs, SIDs, signatures, private links, and emails.
- The public export does not change delivery approval status; math, client build, registration, wallet tests, and release remain unapproved.

## MathModelDesigner v0.3 Contract Retry - 2026-05-11 11:05:00

- `v0.3_donor_feature_parity_provisional` is now treated as the selected planning math/result contract.
- The sprint completed contract/schema boundaries only; full v0.3 simulation and release-grade validation remain pending.
- Registration remains metadata/config/routing/display only unless future current-GS source proves executable math import.
- Production RNG/result ownership remains unproven and must be server/backend-side.
- Browser/client result generation remains forbidden for production.
- Double-up/gamble remains removed from active scope unless direct donor evidence or explicit user override appears.
- ArtSceneMapper update is required before GameClientBuilder because v0.3 adds explicit cascade, golden-square, rainbow, coin reveal, feature-mode, cap, completion, and persistence states.

## Public Export Update - 2026-05-11 11:20:00

- Public export commit `76ee19384aaf6b7c189ca5e80626b5a2682f7fe2` is a sanitized review snapshot only.
- The public export validation passed before push.
- Donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links, emails, and full donor URLs were not intentionally pushed.

## ArtSceneMapper v0.3 Update Assumptions

The v0.3 scene mapping update treats `v0.3_donor_feature_parity_provisional` as a provisional planning result contract. The client is assumed to render backend/runtime result payloads only; browser-side production RNG and authoritative win
calculation remain forbidden. Current GS result owner remains unproven. GameClientBuilder may proceed only to planning/runtime-contract review, not full implementation.

New v0.3 placeholder visual states require original replacement assets and remain pending_replacement or blocked_from_release.
## Public Export After ArtSceneMapper v0.3

Public export was sanitized and pushed to https://github.com/alexandrbogomaniuc/litle_gangster on branch main at commit 6127bdc2f982038e043d5b2585cbcc46b447a1d8. The export excludes donor asset bodies, screenshots, HAR, raw secrets, SIDs,
signatures, private links, emails, and full donor URLs. `06_resulting_code` remains README-only.
## v0.3 Contract Consistency Audit

Canonical v0.3 result field names now use `result_schema.json` paths in art/scene mapping files. Historical aliases such as `feature_mode_state.spins_remaining`, `lastAction`, unprefixed `cascade_steps[]`, and bonus-buy `mode_selection` are
patched or documented in `result_schema_field_aliases.md`. GameClientBuilder remains planning-only; runtime result owner remains unproven.
## Public Export After v0.3 Contract Consistency Audit

Public export was sanitized and pushed to https://github.com/alexandrbogomaniuc/litle_gangster on branch main at commit 6b79e4617d9c2faabdb8a2be8ef1da96da830815. The export excludes donor asset bodies, screenshots, HAR, raw secrets, SIDs,
signatures, private links, emails, and full donor URLs. `06_resulting_code` remains README-only.



## Pipeline Lessons Hardening - 2026-05-11 12:32:07 

- Little Gangster pilot lessons were captured as reusable pipeline guidance only.
- The reusable skill suite was patched to ask better early questions, require donor feature/settings parity earlier, require current-GS registration/RNG ownership proof earlier, and require contract consistency before builder work.
- No gameplay/build/release approval gates changed.
- Next recommended step remains GameClientBuilder planning/runtime API contract review only.


## Public Export Update - 2026-05-11 12:37:05

- Sanitized public export for Pipeline Lessons Hardening validation passed and was pushed to `main`.
- Public commit hash : [REDACTED_FIXTURE]
- Export does not resolve gameplay/build/runtime/registration/wallet/release blockers.


## Public Export Formatting Fix - 2026-05-11 12:53:34

- Public export formatting fixes are review/sanitizer changes only.
- No gameplay/build/runtime/registration/wallet/release approvals changed.
- Next recommended step remains GameClientBuilder planning/runtime API contract review only.


## Public Export Formatting Push - 2026-05-11 12:56:20

- Public export formatting validation passed and was pushed to `main`.
- Public commit hash : [REDACTED_FIXTURE]
- No delivery approval gates changed.

## GameClientBuilder Planning Runtime API Review - 2026-05-11

- GameClientBuilder planning review is planning-only; no client code, runtime implementation, package manifest, production assets, or copied template code was generated.
- New Games / `slot-browser-v1` is the strongest current client lane candidate for planning only, not final architecture.
- Current GS runtime/result owner and exact Little Gangster v0.3 result API contract remain unproven.
- The browser/client remains renderer-only and must not generate production RNG or authoritative outcomes.
- Full GameClientBuilder implementation remains blocked until runtime owner, result API, package lane, and asset strategy are proven and explicitly approved.

## Public Export After GameClientBuilder Planning Review - 2026-05-11

- Sanitized public export validation passed and was pushed to `main`.
- Public commit hash : [REDACTED_FIXTURE]
- Public export contains planning-only `06_resulting_code` docs and no generated client implementation.
- No donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links, emails, or full donor URLs were pushed.
## Runtime API Inspection Assumptions - 2026-05-11

- Generic `/slot/v1` endpoints and `RuntimeEnvelopeResponse` are treated as proven current-source contracts for planning only.
- Little Gangster/8001 is not assumed to use `/slot/v1` until a route, runtime package, and payload adapter are proven.
- `presentationPayload` is treated as the likely browser-visible v0.3 render payload container, but the exact Little Gangster schema extension remains unproven.
- Browser/client result authority remains forbidden; browser code must render backend/runtime payloads only.
- Direct runtime consumption of the project v0.3 `math_package.json` remains unproven.
- GameClientBuilder implementation remains blocked until runtime owner and result API contract are proven and explicitly approved.

## Public Export Validator Reliability - 2026-05-11

- The external reviewer-observed public GitHub state contradicted the prior validation claim, even though the local public export working tree did not reproduce the collapsed README, reviewer guide, or validator at sprint start.
- Future public export validation is trusted only when the validator compiles, runs after the final public export rewrite, and rejects collapsed Markdown or minified Python.
- This sprint changed public export formatting and validator/report reliability only; no gameplay, runtime, registration, wallet, client build, or release approval changed.

## Validation Trust Hardening - 2026-05-11

- Agent-authored validation reports are not sufficient proof of public export correctness.
- Public export validation may be called passed only after local validation, commit, push, and fresh post-push clone validation of the pushed commit.
- WorkflowOrchestrator is treated as a routing and gatekeeping skill, not an implementation skill.
- The next technical step remains ProtocolAndSchemaMapper runtime adapter planning; GameClientBuilder implementation remains blocked.

## Public Export Validation Emergency Fix - 2026-05-11

- The public GitHub raw files are treated as the source of truth for public export validation.
- The previous public validation report is treated as false because it was contradicted by external raw GitHub review.
- Public validation success now requires working-tree validation, committed git-blob validation, pushed branch update, and GitHub-raw validation.
- The emergency public push is blocked because the available GitHub authentication cannot create/update `.github/workflows/public-export-validation.yml`.

## Public Export Validation Push Without Workflow - 2026-05-11

- GitHub Actions workflow publication is deferred because the current GitHub authentication lacks workflow scope.
- Public export validation may still be trusted for this sprint because working-tree validation, committed git-blob validation, and GitHub raw validation all passed for pushed commit `829472dab94f2cad01639a23cba83645bc62c920`.
- The deferred workflow remains documented under `09_release/` and is not included under `.github/workflows/` in the pushed public commit.
- No gameplay, math, runtime, registration, wallet, client build, asset, or release approval gate changed.

## Runtime Adapter Planning - 2026-05-11

- Generic `/slot/v1` and `RuntimeEnvelopeResponse` remain proven for current-source planning, not selected production truth for Little Gangster/8001.
- `presentationPayload` is the candidate browser-visible container for v0.3 render state, but the current generic presentation schema is strict and requires extension/review before direct v0.3 payload use.
- Little Gangster runtime owner remains unproven.
- Little Gangster result API contract remains unproven.
- Backend/runtime must own RNG, outcome generation, win/cap decisions, wallet/accounting, round completion, persistence, and history/recovery.
- Browser/client remains renderer-only.
- A minimum fixture may be defined later for planning-only renderer work, but it cannot prove runtime ownership, payout correctness, wallet accounting, registration, or release readiness.
- No public export, GitHub push, client code, runtime code, registration artifacts, DB/Cassandra action, wallet/API call, donor browsing, asset capture, or release approval occurred in this sprint.

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
- The 24 non-production fixtures are compatible with the proposed adapter concept but need strict schema adjustments before automated protocol validation.
- Backend adapter implementation and full GameClientBuilder implementation remain blocked.
- A later static renderer prototype is allowed only as fixture-only non-production work after explicit user approval.


## Static Fixture Renderer Prototype - 2026-05-12

- The user explicitly approved a fixture-only static renderer prototype for local review.
- The prototype is non-production planning code only and is not the real game client.
- The prototype consumes static non-production fixtures and does not prove runtime owner, result API, wallet/accounting behavior, registration, or release readiness.
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

- Public export validation is trustworthy for commit `ca854797d2d67def46f17dd989164b71ce49cc44` because working-tree, staged/index, committed blob, and GitHub raw checks passed.
- Checkpoint push is no longer due after this sprint.
- Public export remains sanitized; donor assets, screenshots/HAR/raw logs, raw secrets, full donor URLs, and tokenized URLs are excluded.
- Implementation and release gates remain closed.

## 2026-05-12 16:59:34 - Public Export Corruption Contradiction

- External raw-content evidence contradicted the previous checkpoint validation claim for commit `ca854797d2d67def46f17dd989164b71ce49cc44`.
- The previous `public_export_validation_passed` and `github_raw_validation_passed` claims are reset to false until a project-local validator outside the public export validates GitHub raw content.
- Root cause is not proven from current local files; the proven failure is the validation trust boundary.
- Public export success must not be claimed from a validator stored only inside the export.

## 2026-05-12 17:04:16 - Public Export Corruption Fix Completed

- Replacement public export commit `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` passed the project-local GitHub raw validator.
- Raw line counts: README 49, reviewer 44, validator 193, WorkflowOrchestrator skill 67.
- Exact collapse root cause remains not proven, but the previous trust boundary has been fixed.

## 2026-05-12 17:24:01 - Raw-Safe Public Export

- The previous public export at `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` was treated as still corrupted based on external raw line counts.
- A new raw-safe export was built from scratch at `[PUBLIC_EXPORT_ROOT]` using selected safe files only.
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
- Observed RTP drift across volatility profiles means profile-specific calibration is still required before backend adapter or registration generation.
- Exact values remain non-final and uncertified.

## 3x3 Profile Calibration First-Pass Updates

- The profile-specific calibration overlay is a local simulation artifact, not release math.
- All 9 profiles reached +/-2.0 percentage-point smoke tolerance in the bounded first pass, but this does not prove large-sample stability.
- Bonus-buy EV remains excluded from calibration and must be handled before profile approval.
- Cap/max-win tail behavior remains unproven because cap frequency stayed at zero in smoke runs.
- Exact values remain non-final and uncertified.
