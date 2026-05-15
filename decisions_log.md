# Decisions Log

## 2026-05-15 - Lifecycle Wrapper Planning Decision

Decision: create a planning-only lifecycle wrapper and VABS/VBA/Lasthands route contract around the current 8001 payload mapper.

Rationale:
- The prior legacy GS lifecycle audit classified the adapter as `needs_lifecycle_wrapper`.
- The adapter emits useful `presentationPayload.gamePayload` data, but it is not a launch/session, wallet/accounting, restart/FRB, close/reconnect,
  VABS route, or registration owner.
- GameClientBuilder and GameServerRegistrar must not proceed until the wrapper contract and history route dependencies are accepted.

Outcome:
- Created lifecycle wrapper plan, state machine, action accounting contract, round completion/restart contract, VABS route plan, history payload
  schema, registration dependency doc, lifecycle test matrix, implementation gate, and next implementation sequence.
- Lifecycle wrapper implementation, VABS route implementation, GameClientBuilder, GameServerRegistrar generation, wallet tests, DB/Cassandra, and
  release remain blocked.
- No Staging source or runtime implementation was changed.

## 2026-05-15 - Legacy GS Lifecycle Integration Audit Decision

Decision: classify the current 8001 backend adapter as `needs_lifecycle_wrapper`.

Rationale:
- Current source evidence shows legacy GS lifecycle behavior in launch/session actions, restart/FRB paths, close-session handling, wallet
  transaction/pending-state control, and VABS/VBA/Lasthands routes.
- The current 8001 Staging adapter is a guarded presentation payload mapper for `/slot/v1` responses. It emits the right Little Gangster payload
  fields but does not own full launch, session, history, wallet, or registration lifecycle.
- Crazy Rooster 7001 must not be treated as authoritative proof for Little Gangster.

Outcome:
- Keep the current adapter only as a mapper.
- Require lifecycle wrapper and VABS/history route planning before GameClientBuilder, GameServerRegistrar generation, or wallet/launch testing.
- Keep registration generation blocked pending current GS settings mapping for possible models, BF fields, SD keys/KPI, GL bets, and cap/max-win
  fields.
- No Staging source, backend code, client code, registration artifacts, DB/wallet actions, donor browsing, asset capture, or release approval
  occurred.

Created: 2026-05-07T09:42:35+0100

## User-Provided Decisions

- Project name: `little-gangster`
- Future game name: `Little Gangster`
- Future game ID: `8001`
- Game type: `slot`
- Donor/reference URL: stored only as redacted URL in `project_manifest.json`; full URL not persisted.
- Donor URL secret reference: `provided_in_current_codex_session_not_persisted`
- Reference mode: `licensed_asset_reuse`
- Authorization status: licensed reference game/assets approved for production reuse under company license; reuse allowed for this project.
- Asset capture allowed: `true`
- Observation only allowed: `true`
- Target RTP values: `96.0`, `94.0`, `92.0`
- Volatility target: `high`
- Min bet: `0.20`
- Default bet: `1.00`
- Max bet: `100.00`
- Coin denominations: `unknown`
- Required features: free spins, bonus buy, double up, autoplay, turbo, video capture.
- Not required: jackpot, reality check/history.
- Known client stack: PIXI.js Legacy, Vue.js 2.6, Webpack 4, Babel, Mustache, Node.js v16.20.2.
- Game Server docs source: uploaded docs and generated suite references under `[REDACTED_LOCAL_PATH]

## Safe Defaults Applied

- `db_apply_mode`: `generate_only`
- `production_db_apply_allowed`: `false`
- `raw_secret_storage_allowed`: `false`
- donor/scaffold assets gitignored: `true`
- unknown/protected assets block release: `true`
- no workflow release approval yet: `true`

## Sprint Boundary Decisions

- Only ProjectCreator and SprintReporter may run in this sprint.
- No browser launch.
- No donor/reference investigation.
- No asset capture.
- No downloads.
- No math generation.
- No client build.
- No Cassandra registration generation.
- No Cassandra or DB execution.

## AuthorizedReferenceResearcher Sprint 2 Updates

- Sprint 2 allowed skills: AuthorizedReferenceResearcher and SprintReporter only.
- Reference mode updated to `authorized_capture_for_internal_scaffold`.
- Authorization status updated: owned/internal authorized for temporary technical investigation and internal scaffold capture; all scaffold assets
  must remain gitignored, quarantined, inventoried, and blocked from release until replaced or explicitly approved.
- Donor/reference URL remains stored only as a redacted URL; full tokenized URL was not persisted.
- Asset capture allowed remains `true`, but this AuthorizedReferenceResearcher sprint may record observation evidence and sanitized metadata only.
  Real donor asset body download, hashing, and classification are deferred to ReferenceAssetInventory.
- Client source root candidate verified by path existence/readability: `[REDACTED_LOCAL_PATH]
- Portal/preloader client source root candidate verified by path existence/readability: `[REDACTED_LOCAL_PATH]
- Game Server source root candidate verified by path existence/readability: `[REDACTED_LOCAL_PATH]
- Template game path candidate verified by path existence/readability: `[REDACTED_LOCAL_PATH]
- Launch template/routing path candidates were verified by path existence/readability only; detailed protocol inspection is deferred to
  ProtocolAndSchemaMapper.
- Cassandra/config path candidates were verified by path existence/readability only; no Cassandra execution or DB changes were performed.
- Default bank ID set from explicit user input: `6275`.
- Default subCasinoId set from explicit user input: `507`.
- PASS_KEY handling decision: store only file/property references for `INTEGRATION_PASS_KEY`, `CT_PASS_KEY`, and `BONUS_PASS_KEY`; raw values must not
  be read, printed, stored, or requested.
- Test user/token handling decision: store only file references; literal token or credential values must not be read, printed, stored, or requested.
- Coin denominations set from explicit user input: `1`, `2`, `3`, `4`, `5`, `10`, `15`, `20`, `25`, `50`, `100`.

## AuthorizedReferenceResearcher Retry 2026-05-07T10:56:45+0100

- Retry allowed skills: AuthorizedReferenceResearcher and SprintReporter only.
- Project-local Playwright was available and usable; no reinstall was needed.
- `.gitignore` already covered project-local Playwright/cache folders, sanitized HAR folder, reference asset quarantine/raw folders, and
  sensitive/token logs.
- `project_manifest.json` parsed before browser work.
- Browser retry did not run because the provided fresh donor/reference URL field contained a placeholder, not a usable URL.
- No old donor URL was reused.
- No full donor URL, token, session, auth, key, JWT, signature, or hash query value was persisted.
- No spin, bet change, or gameplay interaction occurred.
- No response bodies or donor asset files were saved.
- Handoff next skill remains AuthorizedReferenceResearcher because a usable fresh donor/demo/test URL is still required.

## AuthorizedReferenceResearcher User-Visible Browser Clarification 2026-05-07T11:22:15+0100

- User clarified that the previously supplied donor URL should be used for this project until moving to the next project.
- User provided a screenshot showing the Codex in-app browser reaches the visible `Le Bandit` intro screen with `CLICK TO CONTINUE`.
- The full tokenized donor URL was not persisted.
- The user-visible screenshot is treated as conversation evidence, not as a saved project asset.
- Tool discovery did not expose a Google Chrome MCP or the Browser Use Node REPL `js` control tool in this session.
- After the user explicitly authorized normal visible-browser use, Codex used OS-level clicks and cropped screenshots against the already-open Codex
  in-app browser.
- Codex did not use headless browser behavior for the visible-browser retry.
- Codex did not bypass wallet, CORS, login, geolocation, paywall, anti-bot, or access controls.
- Codex continued from the intro screen into the base game.
- Safe demo mode was confirmed from visible `DEMO BALANCE` and `DEMO BET` UI labels.
- One normal-user demo spin was attempted only after safe demo mode was visible.
- The spin attempt produced an in-game wallet error modal: `Connection lost to wallet - please try again.`
- No donor asset response bodies, scripts, images, atlases, fonts, binary files, or source responses were saved.
- A later click attempt drifted back onto the Codex UI; that screenshot is retained only as invalid-crop/reorientation evidence, not as gameplay
  evidence.
- Next recommended skill is ReferenceAssetInventory for observed intro/base asset inventory only. Deeper gameplay research remains blocked until a
  working demo/test wallet/RGS path is available.

## AuthorizedReferenceResearcher Chrome MCP Retry 2026-05-07T11:50:00+0100

- User asked Codex to try Google Chrome MCP again after being advised it was fixed.
- Tool discovery exposed `mcp__chrome_devtools__` on retry.
- Chrome MCP opened the donor launch URL in memory only; full URL/token values were not persisted.
- Chrome MCP captured intro, base demo, post-spin, menu, and game-info screenshots.
- Chrome MCP confirmed safe demo mode through accessibility text: `DEMO BALANCE` and `DEMO BET`.
- Chrome MCP clicked the game canvas to continue and clicked the accessible spin control after safe demo mode was confirmed.
- Chrome MCP observed demo balance decreasing from EUR 5,000.00 to EUR 4,996.00 after spin interaction. Network metadata showed demo RGS
  `authenticate`, `gameLaunch`, `keepAlive`, and `bet` requests returning HTTP 200.
- Chrome MCP opened the menu and game-info panel. Game info/paytable content was observed as reference evidence only, not final math.
- No request body or response body was saved.
- No donor asset body was saved.
- No ReferenceAssetInventory, ProtocolAndSchemaMapper, math, client build, Cassandra, DB, wallet test, or release audit skill was run.
- The earlier in-app visible-browser wallet error is now treated as a path-specific discrepancy, not the current blocker for Chrome MCP reference
  research.

## ReferenceAssetInventory Sprint 2026-05-07T14:10:06+0100

- User clarified project reference mode is `authorized_capture_for_internal_scaffold`.
- User authorized asset capture for this sprint under controls: captured files must stay gitignored, saved only under `02_reference_assets/`, no
  wallet/API/auth/balance response bodies, and no full donor URLs/tokens.
- Only ReferenceAssetInventory and SprintReporter were run.
- Captured 29 static reference asset files from observed static asset paths only.
- Captured files were saved under `[REDACTED_LOCAL_PATH]
- No RGS/wallet/API/auth/balance response bodies were saved.
- No full donor launch URL or token value was persisted.
- Every captured asset was classified as `scaffold_internal_only`, `blocked_from_release`, and `replacement_required=true`.
- Asset inventory gate is marked approved only for workflow handoff/completeness, not release approval.
- Next recommended skill is ProtocolAndSchemaMapper.

## ProtocolAndSchemaMapper Sprint 2026-05-08T07:44:03+0100

- User authorized only ProtocolAndSchemaMapper and SprintReporter for workflow test stage 4.
- No AuthorizedReferenceResearcher, ReferenceAssetInventory, MathModelDesigner, ArtSceneMapper, ArtDirectionAndReplacementPlanner, GameClientBuilder,
  GameServerRegistrar, WalletAndLaunchTester, or RTPAndReleaseAuditor was run.
- Protocol mapping used only the skill suite, the Little Gangster project, uploaded/generated documentation summaries, project-local prior reports,
  and explicit source paths listed in the prompt or project manifest.
- No browser, Chrome MCP, donor gameplay investigation, asset capture, donor download, wallet endpoint call, Cassandra execution, or DB action
  occurred.
- BSG Common Wallet is recorded as XML wallet/casino protocol only, with `BSGSYSTEM`/`EXTSYSTEM` response roots preserved. It is not treated as
  browser runtime protocol.
- Launch/template layer is recorded separately from browser/client runtime.
- Cassandra/config registration is recorded separately from BSG Common Wallet and remains generate-only.
- Uploaded docs describe a legacy Webpack/Vue/PIXI template stack, while explicit 7001/new-games source paths show a Vite/PIXI v8/new-games slot
  runtime lane. This split is recorded as a GameClientBuilder decision point rather than guessed away.
- PASS_KEY and test-token files were treated as secret-bearing reference files only. Raw values were not persisted in project outputs.
- Protocol mapping is marked `partial_sufficient_for_math_handoff`.
- Next recommended skill is MathModelDesigner because protocol layers, target RTPs, volatility, bet range, and coin denominations are sufficient to
  begin math design, while runtime/registration blockers remain explicit.

## ProtocolAndSchemaMapper Third-Party GS Integration Extension 2026-05-08T15:39:47+0100

- User authorized only ProtocolAndSchemaMapper and SprintReporter for a focused Stage 4 retry/extension.
- No donor URL browsing, browser/Chrome MCP work, asset capture, math generation, client build, Cassandra/DB action, wallet call, or later workflow
  skill was run.
- The extension focused on how a third-party/new game links to GS, which runtime lane should be used, Crazy Rooster 7001 template validity,
  math/RNG/result ownership, Cassandra/config registration blockers, wallet boundary, and player-release readiness.
- Third-party/new game launch is recorded as GS launch first (`/startgame` wrapper or `/cwstartgamev2.do`), then redirect to new-games client or
  legacy template depending on route config.
- Little Gangster runtime lane is no longer treated as selected. New-games `slot-browser-v1` / HTTP runtime is candidate evidence only until current
  GS source/config/docs prove it directly.
- Crazy Rooster 7001 is recorded as a useful integration reference, not a direct release-ready template to copy.
- WebGS internal new-games bridge is mapped for session validation, wallet reserve/settle, and history read/write; this bridge does not prove slot
  RNG/result generation.
- Final RNG/result owner remains UNKNOWN/BLOCKED until current GS runtime ownership is proven directly. The owner could be classic GS, new-games
  backend, a game-specific server package, GS game processor, or another current runtime component.
- Math is expected to live first as a project math package and later as the proven server/backend runtime logic/config. Cassandra/GS registration must
  be treated as metadata/config/routing/display setup unless source proves executable math import.
- MathModelDesigner remains the next recommended skill, with limits: design/simulation only, no claim of final runtime ownership or release readiness.
- GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, and release-to-players remain blocked.

## MathModelDesigner Sprint 2026-05-08T16:25:00+0100

- User authorized only MathModelDesigner and SprintReporter.
- No donor browsing, donor gameplay investigation, asset capture, donor download, client build, client runtime generation, Cassandra/DB action, wallet
  call, release approval, ProtocolAndSchemaMapper, or later workflow skill was run.
- Decision: create an original provisional Little Gangster math package, not donor-true math.
- Decision: use a 5x3 fixed-20-line high-volatility slot model because exact donor math/runtime remains unproven.
- Decision: include wild, scatter, free spins, optional bonus buy, and optional neutral double-up placeholder because project requirements support
  those features.
- Decision: do not include jackpot because project requirements say jackpot is not required.
- Decision: propose a 10,000x max-win cap as a math/product proposal, not final certification.
- Decision: keep browser result authority disallowed.
- Decision: require server/backend-side RNG/result generation, while final owner remains UNKNOWN/BLOCKED and must be proven from current GS/runtime
  source.
- Decision: do not treat GS/Cassandra registration as executable math import.
- Decision: keep `math_approved=false` and `release_approved=false` despite passing workflow simulations.
- Validation: 1,000,000 deterministic base rounds per RTP variant were run with seed `2026050801`.
- Result: `rtp_96` simulated 96.013333%, `rtp_94` simulated 94.013056%, and `rtp_92` simulated 92.012778%.
- Next recommended skill: ArtSceneMapper, with the explicit caveat that math remains provisional and runtime/release blockers remain.

## MathModelDesigner Math Quality Gate 2026-05-09T00:00:00+0100

- User authorized only MathModelDesigner and SprintReporter for a focused math/layout correction sprint.
- No ArtSceneMapper, ArtDirectionAndReplacementPlanner, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, RTPAndReleaseAuditor,
  AuthorizedReferenceResearcher, ReferenceAssetInventory, or ProtocolAndSchemaMapper was run.
- No browser work, donor gameplay investigation, donor download, donor asset body inspection, client build, Cassandra/DB action, wallet call,
  raw-secret handling, donor URL persistence, or release approval occurred.
- External reviewer concern accepted: reference research reported a 6x5 cluster-style reference game, while the prior selected math package was 5x3
  fixed-20-line.
- Decision: the old 5x3 v0.1 package is internally usable as a provisional simulator, but it is no longer acceptable as the selected downstream Little
  Gangster layout.
- Decision: switch selected Little Gangster math to `v0.2_6x5_cluster_provisional`.
- Decision: preserve v0.1 files as superseded, not delete them.
- Decision: ArtSceneMapper should map a 6x5 cluster target scene, not the superseded 5x3 board.
- Simulator audit found v0.1 uses `payout_scale` during win calculation. It does not post-normalize totals, but close RTP results from v0.1 must not
  be treated as true emergent validation.
- Created a new v0.2 6x5 adjacent-cluster provisional package under `04_math/alternatives/v0_2_6x5_cluster/`.
- v0.2 simulator evaluates generated 6x5 grids, connected clusters, scatter wins, and symbol-triggered free spins. It does not scale wins during a
  simulation run and does not normalize results after the run.
- v0.2 paytables were calibrated from smoke simulation evidence. This is acceptable for workflow layout alignment but is not release-grade RTP
  certification.
- Simulation: v0.2 ran 200,000-round calibration-seed smoke simulations for RTP 96/94/92 and two additional 100,000-round secondary seeds per variant.
- Result: calibration seed passed workflow tolerance for all variants; secondary short seeds drifted outside +/-0.5 percentage-point tolerance, so
  full multi-seed validation remains pending.
- Math quality gate result: `PASS_WITH_LIMITATIONS`.
- Next recommended skill remains ArtSceneMapper with limitations: use the 6x5 selected layout, keep math unapproved for release, and preserve
  runtime/source/asset/wallet blockers.
- Durable source-root note: user stated Staging is now canonical for GS/New Games/Crazy Rooster work. This math sprint did not inspect Staging paths;
  future source-inspection skills must update/verify manifest paths against `[REDACTED_LOCAL_PATH] and not use old worktrees as source of truth.

## ArtSceneMapper Sprint 2026-05-09T00:00:00+0100

- User authorized only ArtSceneMapper and SprintReporter.
- No ArtDirectionAndReplacementPlanner, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, RTPAndReleaseAuditor,
  AuthorizedReferenceResearcher, ReferenceAssetInventory, ProtocolAndSchemaMapper, or MathModelDesigner was run.
- No donor URL browsing, donor gameplay investigation, asset capture, donor download, donor asset body inspection, client build, client runtime
  generation, Cassandra/DB action, wallet call, raw-secret handling, full donor URL/token persistence, asset approval, or release approval occurred.
- Decision: use selected `v0.2_6x5_cluster_provisional` layout for target scene mapping.
- Decision: do not use superseded 5x3 v0.1 for target scene mapping.
- Created 18 scene map JSON files under `05_art/scene_maps/`.
- Created 140 stable object IDs, including deterministic 6x5 base-game and free-spins grid cell IDs.
- Created `05_art/object_id_naming.md`, `05_art/object_id_map.json`, `05_art/scene_map_schema.json`, `05_art/asset_audit.csv`, scene mapping summary,
  blockers, and handoff.
- Created a static local HTML scene inspector under `05_art/html_scene_inspector/` with embedded sample data, JSON file loading, search, layer
  toggles, click-to-inspect metadata, and notes export.
- Scaffold/reference assets were not used as inspector previews, not copied into `06_resulting_code`, and remain blocked from release.
- All mapped objects use placeholder references and require replacement or explicit approval by ArtDirectionAndReplacementPlanner.
- ArtSceneMapper completed with limitations.
- Next recommended skill: ArtDirectionAndReplacementPlanner.


## Supplemental Authorized Asset Discovery And Scene Preview - 2026-05-10 10:28:43 +0100

- Decision: run only AuthorizedReferenceResearcher, ReferenceAssetInventory, ArtSceneMapper, and SprintReporter.
- Decision: because the fresh donor URL input was a placeholder, do not launch browser or attempt capture.
- Decision: reconcile the existing 29 project-local scaffold assets and use them only as internal scaffold preview references.
- Decision: update scene/object maps and HTML inspector using selected `v0.2_6x5_cluster_provisional`; do not use the old 5x3 target layout.
- Decision: all scaffold assets remain `scaffold_internal_only`, `replacement_required=true`, and `blocked_from_release`.
- Decision: recommend ArtDirectionAndReplacementPlanner next because scene preview tooling is usable, with the fresh-capture blocker preserved.


## Supplemental Authorized Asset Discovery With Provided URL - 2026-05-10 10:51:49 +0100

- User provided a donor URL for the Little Gangster project and asked to keep using it until a new project starts. The full URL remains in-memory only
  and is not persisted.
- Decision: run AuthorizedReferenceResearcher, ReferenceAssetInventory, ArtSceneMapper, and SprintReporter only.
- Decision: save allowed scaffold asset types under `02_reference_assets/authorized_raw/[REDACTED_ASSET_FILE] only.
- Decision: keep every scaffold/reference asset `scaffold_internal_only`, `replacement_required=true`, and `blocked_from_release`.
- Result: 3 capture iterations ran; 113 new scaffold files were saved; 142 total scaffold files are now inventoried; 135 of 140 scene objects have
  scaffold preview references.
- Release remains blocked; ArtDirectionAndReplacementPlanner is recommended next.


## ArtDirectionAndReplacementPlanner - 2026-05-10 11:23:27 +0100

- Decision: skip targeted donor re-check because the 5 unmatched objects are not critical missing scaffold assets for art direction.
- Decision: select `Little Gangster: Neon Heist` as the original art direction.
- Decision: keep 6x5 cluster provisional layout and v0.2 math model as art/layout target.
- Decision: create an approved assets manifest with zero final approved assets; all scaffold/reference assets remain blocked from release.
- Decision: recommend GameClientBuilder next for planning/build scaffolding only, with release assets still blocked.

## Sprint Decision: Donor Feature/Settings Parity (2026-05-10 19:52:26 BST)

- Decision from user instruction: Little Gangster must match donor settings and features.
- Implementation decision: create parity matrix and update art/math contracts without approving release or moving scaffold assets.
- Safety decision: no new asset bodies were captured in this sprint because the fresh clean browser retry was blocked at an error shell and existing
  scaffold coverage was sufficient for parity documentation.
- Workflow decision: recommend MathModelDesigner next, not full GameClientBuilder, because donor-parity math/result fields are missing from v0.2.

## Public Git Export - 2026-05-10 20:54:42 BST

- Decision: create a sanitized public review snapshot at `[REDACTED_LOCAL_PATH]
- Decision: push the sanitized export to `https://github.com/alexandrbogomaniuc/litle_gangster` on branch `main` using existing local Git
  authentication only.
- Decision: exclude donor asset bodies, screenshots, HAR/network logs, Playwright/browser folders, node modules, binaries/media, PDFs/ZIPs, raw
  secrets, and full donor URLs.
- Decision: keep next recommended workflow skill as MathModelDesigner retry because donor feature/settings parity still requires math/result contract
  revision.
- Result: push succeeded at final HEAD `a8cfcb2b25f0127a9487a4d41d75e638d20765bd`.


## MathModelDesigner Donor-Parity Retry - 2026-05-11 07:45:26 
- Created and selected `v0.3_donor_feature_parity_provisional` as the current planning math/result contract.
- Preserved v0.1 and v0.2 unchanged for traceability.
- Removed double-up/gamble from active math scope because donor evidence did not show it.
- Kept math approval, release approval, client-build approval, and runtime-owner proof set to false.
- Recommended ArtSceneMapper update before GameClientBuilder.

## Mantis Scope Correction - 2026-05-11

- Decision: treat Mantis/ExtGame material as an advisory integration checklist, not selected Little Gangster architecture.
- Decision: do not select `HOSTING_MODE=EXTGAME` and do not claim Little Gangster must implement an external endpoint unless current GS source/config
  later proves it.
- Decision: downgrade new-games `slot-browser-v1` / HTTP runtime to candidate direction only; Gamesv1/Crazy Rooster/slot-browser-v1 is not guaranteed
  truth and must be verified directly against current GS before trust.
- Decision: keep ExtGame as candidate/unverified, with checklist items for process-transaction-equivalent behavior, state persistence, round
  completion, restart/resume, VABS/VBA/history, FRB/OCB, RNG, and certification.
- Decision: update MathModelDesigner next-retry requirements, GameServerRegistrar registration questions, WalletAndLaunchTester QA gates, and
  RTPAndReleaseAuditor gates without running those implementation skills.
- Decision: no public GitHub push in this sprint.
- Decision: next recommended skill remains MathModelDesigner retry/audit using the corrected current-GS checklist.


## Public Export Update - 2026-05-11 07:49:21 
- Pushed sanitized public export commit `f982c7796fac84a5c58c87fd1d741bfca68307a4` to `https://github.com/alexandrbogomaniuc/litle_gangster` on branch
  `main`.
- Kept `06_resulting_code` README-only; no production client code was generated or pushed.
- Next recommended skill remains ArtSceneMapper update for v0.3 animation-state parity.


## ExtGame External-Collaboration Requirements Patch - 2026-05-11 08:10:35 
- Created sanitized ExtGame internal reports under `03_protocol`, `04_math`, and `08_qa`.
- Patched reusable skill-suite requirements for ProtocolAndSchemaMapper, MathModelDesigner, GameServerRegistrar, and WalletAndLaunchTester.
- Added reusable suite reference `references/EXTGAME_EXTERNAL_COLLABORATION_REQUIREMENTS.md`.
- Did not persist raw Mantis text, raw endpoints, emails, private links, SIDs, signatures, tokens, passwords, or secrets.
- Did not change the selected math package and did not run MathModelDesigner implementation.
- Public GitHub export should be updated later only with sanitized summaries, never raw Mantis text.

## Current GS Registration/RNG Audit - 2026-05-11

- Decision: complete the missing current-GS registration/RNG/math-ownership evidence audit before any MathModelDesigner retry, GameServerRegistrar
  generation, or GameClientBuilder work.
- Decision: classify previous v0.3 math package touches as `safe_boundary_doc_update` but still mark `previous_patch_scope_violation=true` because
  package/config files were touched outside the requested implementation scope.
- Decision: do not revert previous v0.3 boundary wording automatically; preserve and recommend manual review if the team wants v0.3 package metadata
  frozen.
- Decision: treat registration as metadata/config/routing/display until direct current GS source proves executable math import.
- Decision: record New Games / `slot-browser-v1` as the strongest candidate lane, not final.
- Decision: next recommended skill remains MathModelDesigner retry for v0.3 contract completion; GameClientBuilder and GameServerRegistrar remain
  blocked.

## Public Export Update - 2026-05-11 10:36:00

- Rebuilt and validated the sanitized public export after the Current GS Registration/RNG audit.
- Pushed public branch `main` to `https://github.com/alexandrbogomaniuc/litle_gangster` at commit `17b162ba1dd56d7ee129b154d079be3921280c06`.
- Confirmed public export validation passed before push.
- Confirmed donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links, emails, and full donor URLs were not intentionally
  pushed.
- Kept next recommended workflow skill as MathModelDesigner retry.

## MathModelDesigner v0.3 Contract Retry - 2026-05-11 11:05:00

- Completed the v0.3 donor-feature-parity contract/schema package without runtime implementation, client code, registration artifacts, DB actions,
  wallet calls, donor browsing, or asset capture.
- Decision: keep `v0.3_donor_feature_parity_provisional` selected for planning only, not release approval.
- Decision: mark v0.3 simulations as `not_run_contract_only`; full multi-seed RTP validation remains pending.
- Decision: separate registration metadata from executable math in `math_to_registration_metadata.md`.
- Decision: keep RNG/result owner unproven and backend/server-side only.
- Decision: keep GameClientBuilder blocked until ArtSceneMapper updates v0.3 animation/state coverage and runtime-contract review is complete.
- Decision: keep GameServerRegistrar blocked until 8001 registration inputs, selected lane, and scn/jcn tooling are proven.

## Public Export Update - 2026-05-11 11:20:00

- Rebuilt and validated the sanitized public export after the v0.3 donor-feature-parity contract sprint.
- Pushed public branch `main` to `https://github.com/alexandrbogomaniuc/litle_gangster` at commit `76ee19384aaf6b7c189ca5e80626b5a2682f7fe2`.
- Confirmed public export validation passed before push.
- Confirmed donor asset bodies, screenshots, HAR, raw secrets, SIDs, signatures, private links, emails, and full donor URLs were not intentionally
  pushed.
- Kept next recommended workflow skill as ArtSceneMapper update.

## ArtSceneMapper v0.3 Update Decision

Decision: ArtSceneMapper v0.3 update completed with object count 140 -> 288. Cascades, golden-square state, rainbow activation, coin/special reveals,
three feature modes, bonus-buy mode selection, max-win cap, win tiers, round completion, and state persistence are mapped for planning.

Full GameClientBuilder remains blocked until runtime result owner and result API contract are reviewed. No release approval, registration approval,
wallet test approval, math approval, client build approval, donor browsing, or asset capture occurred.
## Public Export After ArtSceneMapper v0.3

Decision: push sanitized public review snapshot after ArtSceneMapper v0.3 update. Validation passed and commit
6127bdc2f982038e043d5b2585cbcc46b447a1d8 was pushed to https://github.com/alexandrbogomaniuc/litle_gangster on branch main. No release, client build,
registration, wallet, DB, donor browsing, or asset capture approval was made.
## v0.3 Contract Consistency Audit

Decision: patch only safe documentation/schema naming mismatches before GameClientBuilder planning. Result schema was not changed. Scene/art
references and HTML inspector field labels were canonicalized. Mismatches found: 61; patched: 47; unresolved: 7. Full GameClientBuilder remains
blocked.
## Public Export After v0.3 Contract Consistency Audit

Decision: push sanitized public review snapshot after v0.3 contract consistency audit. Validation passed and commit
6b79e4617d9c2faabdb8a2be8ef1da96da830815 was pushed to https://github.com/alexandrbogomaniuc/litle_gangster on branch main. No release, client build,
registration, wallet, DB, donor browsing, or asset capture approval was made.



## Pipeline Lessons Hardening - 2026-05-11 12:32:07 

- Decision: capture Little Gangster pilot lessons into project release docs and reusable skill-suite reference policies.
- Decision: patch all reusable workflow skills with hardening addenda rather than changing game implementation artifacts.
- Decision: strengthen public export sanitizer and fix public export `.gitignore` folder patterns.
- Decision: preserve all Little Gangster approval blockers and recommend only GameClientBuilder planning/runtime API contract review next.


## Public Export Update - 2026-05-11 12:37:05

- Decision: push the validated sanitized public export snapshot for Pipeline Lessons Hardening.
- Commit: `8744f5b0827ff99775415f62261f9b5fd5721ace` on `main`.
- Decision: next recommended project step remains GameClientBuilder planning/runtime API contract review only.


## Public Export Formatting Fix - 2026-05-11 12:53:34

- Decision: patch the public export in place for Markdown readability, `.gitignore` line breaks, export-manifest placeholder typo, and validator
  enforcement.
- Decision: preserve all Little Gangster delivery blockers and approval gates.


## Public Export Formatting Push - 2026-05-11 12:56:20

- Decision: publish the validated public export formatting/sanitizer correction.
- Commit: `120429e631d6b7de4d4e98af346f8c5e337ccbac` on `main`.
- Decision: next recommended step remains GameClientBuilder planning/runtime API contract review only.

## GameClientBuilder Planning Runtime API Review - 2026-05-11

- Decision: create only planning/runtime API contract review docs under `06_resulting_code`.
- Decision: do not create `package.json`, `src/`, `public/`, production assets, runtime implementation, or copied template code.
- Decision: treat New Games / `slot-browser-v1` as the current planning candidate only.
- Decision: keep GameClientBuilder implementation blocked because runtime result owner and exact result API payload are not proven for Little
  Gangster.
- Decision: recommend targeted ProtocolAndSchemaMapper runtime API inspection next.

## Public Export After GameClientBuilder Planning Review - 2026-05-11

- Decision: push the validated sanitized public export after GameClientBuilder planning/runtime API contract review.
- Commit: `c4af8bc6b4e18fc39cb11b09ee418696f142624d` on `main`.
- Decision: keep full GameClientBuilder implementation blocked and recommend ProtocolAndSchemaMapper runtime API inspection next.
## 2026-05-11 - Runtime API Inspection

- Decision: Generic `/slot/v1` endpoint names and `RuntimeEnvelopeResponse` are now proven for current-source planning.
- Decision: `/slot/v1` is not selected as final Little Gangster runtime; it remains candidate until 8001 runtime owner and adapter proof exists.
- Decision: v0.3 payload adapter is documented as requirements only, not implemented or proven.
- Decision: GameClientBuilder implementation remains blocked; planning-only may continue.
- Decision: Next recommended work is ProtocolAndSchemaMapper runtime adapter planning/proof before client code generation.

## 2026-05-11 - Public Export Validator Reliability

- Decision: Treat the prior public formatting validation claim as contradicted by the external reviewer-observed public GitHub state.
- Decision: Rewrite public export README, reviewer guide, notice, manifest, and validator as readable multiline files before final validation and
  push.
- Decision: Strengthen the public validator to fail collapsed Markdown, minified Python, missing runtime status text, excluded asset folders, media
  files, sensitive URLs, token/session/signature patterns, private links, emails, absolute local paths, and unexpected `06_resulting_code` contents.
- Decision: Push only after the stricter validator compiled, ran, and passed against the final public working tree.

## 2026-05-11 - Validation Trust Hardening

- Decision: Treat external-review contradiction as a validation-trust failure even when local raw GitHub checks show readable files.
- Decision: Create project-owned validation scripts for public export, post-push clone verification, workflow gates, and sprint truthfulness.
- Decision: Create WorkflowOrchestrator to choose the next safe skill and refuse unsafe implementation jumps.
- Decision: Require fresh post-push clone validation before future reports may claim public export validation passed.
- Decision: Keep all client build, registration, wallet, and release approval gates false.

## 2026-05-11 - Public Export Validation Emergency Fix

- Decision: Treat the prior public validation claim as false because external raw GitHub review contradicted it.
- Decision: Add committed git-blob and GitHub-raw validators in addition to the working-tree validator.
- Decision: Add a GitHub Actions workflow locally as required, but do not claim public success because GitHub rejected the push without `workflow`
  scope.
- Decision: Keep public_export_validation_passed=false until a push to `main` succeeds and GitHub raw validation passes for that pushed commit.

## 2026-05-11 - Public Export Validation Push Without Workflow

- Decision: Defer `.github/workflows/public-export-validation.yml` because the current GitHub authentication lacks workflow scope.
- Decision: Preserve the workflow plan under `09_release/deferred_github_actions_public_export_validation.yml` and document the deferral in
  `09_release/GITHUB_ACTIONS_VALIDATION_DEFERRED.md`.
- Decision: Publish public export validation fixes only after working-tree validation, committed git-blob validation, and GitHub raw validation
  passed.
- Decision: Mark public export validation passed for pushed commit `829472dab94f2cad01639a23cba83645bc62c920`; README raw lines: 35, reviewer raw
  lines: 41, validator raw lines: 410.
- Decision: Keep all gameplay, client build, runtime, registration, wallet, asset, and release approval gates unchanged.

## 2026-05-11 - Runtime Adapter Planning

- Decision: Define Little Gangster v0.3 adapter as a planning contract only, not implementation.
- Decision: Keep `/slot/v1` as the strongest generic candidate lane but not selected production runtime for 8001.
- Decision: Require presentation payload extension/review before v0.3 fields can be consumed by a client.
- Decision: Keep `runtime_owner_proven=false` and `result_api_contract_proven=false`.
- Decision: Allow only a future non-production minimum client fixture for planning; full GameClientBuilder implementation remains blocked.
- Decision: Do not run public export or GitHub push in this sprint.
- Decision: Keep all client build, registration, wallet test, final asset, math, and release approvals false.

## 2026-05-12 - GameClientBuilder Fixture Planning

- Decision: create only static non-production renderer fixture planning files under `06_resulting_code/planning/fixtures/`.
- Decision: create 24 fixture JSON examples covering v0.3 cascade, golden-square, rainbow, coin, special reveal, feature mode, bonus buy, win tier,
  cap, round completion, and reconnect states.
- Decision: prefer `presentationPayload.gamePayload` as the reusable presentation extension candidate.
- Decision: document `presentationPayload.littleGangsterV03` as fallback only if schema review rejects the generic extension.
- Decision: keep the presentation extension pending schema review.
- Decision: keep `runtime_owner_proven=false` and `result_api_contract_proven=false`.
- Decision: do not create production client code, package scaffolding, runtime implementation, registration artifacts, wallet calls, donor assets, or
  public export output.
- Decision: keep GameClientBuilder implementation blocked.


## 2026-05-12 - Backend Runtime Adapter Proof

- Decision: recommend `presentationPayload.gamePayload` as the future reusable extension point for Little Gangster v0.3 render payloads.
- Decision: keep `presentationPayload.littleGangsterV03` as fallback only if generic extension is rejected.
- Decision: current strict core-protocol schema does not support either extension today, so schema review/change is required before implementation.
- Decision: existing 7001 `mathBridge` proves a candidate extension pattern but does not prove Little Gangster/8001 runtime ownership.
- Decision: keep `runtime_owner_8001_proven=false` and `v0_3_adapter_implementation_ready=false`.
- Decision: allow only future fixture-only static renderer prototype after explicit user approval; full GameClientBuilder implementation remains
  blocked.
- Decision: no public export, GitHub push, client code, runtime code, backend adapter code, registration artifact, DB/Cassandra action, wallet/API
  call, donor browsing, asset capture, or release approval occurred.


## 2026-05-12 - Static Fixture Renderer Prototype

- Decision: create only a fixture-only, non-production static renderer prototype under `06_resulting_code/prototypes/static_fixture_renderer_v0_1/`
  after explicit user approval.
- Decision: use plain static HTML/CSS/JS with no package manifest, npm dependencies, production client scaffold, runtime implementation, registration
  artifact, wallet/API call, donor browsing, asset capture, or public export.
- Decision: render placeholder shapes, colors, labels, and state summaries for all 24 non-production v0.3 fixture examples.
- Decision: keep `client_code_generated=false` for production client code while recording `prototype_code_generated=true` for the local non-production
  renderer prototype.
- Decision: keep `runtime_owner_proven=false`, `result_api_contract_proven=false`, `client_build_approved=false`, `registration_approved=false`,
  `wallet_tests_approved=false`, and `release_approved=false`.
- Decision: recommend ProtocolAndSchemaMapper schema extension review or backend/runtime adapter implementation planning next, not full
  GameClientBuilder implementation.

## Presentation Payload Schema Extension Review

Decision: Recommend `presentationPayload.gamePayload` as the future reusable extension point for Little Gangster v0.3 renderer payloads.

Evidence:
- Strict core-protocol `PresentationPayloadSchema` rejects unknown keys today.
- 7001 `mathBridge` proves an adapter-style extension pattern exists, but it is not canonical schema support and is not reusable enough as the final
  Little Gangster contract.
- No Little Gangster/8001 runtime owner or payload branch was found in targeted Staging inspection.

Outcome:
- Schema patch required: true.
- UI-kit patch required: true.
- New-games-server patch required: true.
- Backend adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- Next recommended skill: ProtocolAndSchemaMapper source patch planning.

## Source Patch Planning for presentationPayload.gamePayload

Decision: Create patch-ready proposal documents only; do not modify Staging source in this sprint.

Evidence:
- Canonical JSON response schemas and Zod helpers both reject `gamePayload` today.
- Transport parser is already record-permissive and likely needs tests more than functional change.
- UI-kit mapper does not expose extension payloads today.
- New-games-server has 7001 `mathBridge` reference behavior but no 8001 branch.

Outcome:
- Source patches applied: false.
- Staging source modified: false.
- Schema patch approval required: true.
- Adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- Next recommended skill: ProtocolAndSchemaMapper source patch apply only if the user explicitly approves Staging source modification.

## Source Patch Apply for presentationPayload.gamePayload

Decision: Apply only the approved reusable `presentationPayload.gamePayload` schema/type/mapper patch set.

Evidence:
- Canonical response schemas now accept optional `gamePayload` and keep `presentationPayload` strict.
- Core-protocol Zod runtime schema now accepts optional `gamePayload`.
- Core transport types now expose `GamePayloadExtension` and `PresentationPayload`.
- UI-kit mapper now preserves `gamePayload` untouched.

Outcome:
- Source patches applied: true.
- Staging source modified: true.
- New-games-server patch applied: false.
- Backend adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- Next recommended skill: ProtocolAndSchemaMapper strict fixture update.

## Strict Fixture Update for presentationPayload.gamePayload

Decision: Create strict-schema-compatible non-production fixture variants as candidate `/slot/v1` response envelopes.

Evidence:
- 24 strict fixture JSON files were created.
- 24 / 24 strict fixtures validate against patched response schemas.
- 24 / 24 embedded `gamePayload.payload` objects validate against the v0.3 result schema.
- Applied source patch evidence was recorded through hashes and safe metadata only.
- Staging source hashes were unchanged during this sprint.

Outcome:
- Strict fixture update completed: true.
- Backend adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- Next recommended skill: ProtocolAndSchemaMapper backend adapter implementation planning.

## Backend Adapter Implementation Planning

Decision: Create a patch-ready implementation plan only; do not modify Staging source or create backend adapter files.

Evidence:
- `new-games-server/src/index.ts` owns `/slot/v1` routes and the generic `runtimeEnvelope(...)` helper.
- `new-games-server/src/index.ts` has a 7001 presentation payload branch that is reference-only.
- No `Gamesv1/games/8001` package was found in the targeted Staging paths.
- No `new-games-server/src/games/little-gangster/adapter.ts` file was found.
- 24 / 24 strict fixtures validate against patched response schemas and v0.3 result schema.

Outcome:
- Backend adapter implementation planning completed: true.
- Recommended target: `new-games-server/src/games/little-gangster/` plus guarded 8001 branch in
  `new-games-server/src/index.ts`.
- Backend adapter implemented: false.
- Staging source modified in this sprint: false.
- Backend adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- Next recommended skill: ProtocolAndSchemaMapper backend adapter apply only if the user explicitly approves
  Staging source modification.

## Authoritative Server Math Design

Decision: Define a Little Gangster owned server-authoritative math/state/history design before any backend adapter
implementation.

Evidence:
- v0.3 result contract, strict `gamePayload` fixtures, backend adapter planning docs, and history/runtime checklists
  exist in the project.
- 7001 runtime files were treated only as structural reference and not as math authority.
- Existing project gates require browser renderer-only behavior and registration metadata separation.

Outcome:
- Authoritative server math design completed as planning documentation.
- Recommended math owner: future Little Gangster server-side math/runtime module integrated through backend adapter.
- 7001 authoritative math source: false.
- Base, cascade, golden-square, rainbow, coin, special reveal, feature modes, bonus buy, jackpot hook, max-win, VABS,
  history, simulation, and certification design areas are covered.
- Bonus-buy cost/EV remains blocked.
- Jackpot hooks are disabled by default pending product decision.
- Backend adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- Release approved: false.
- Next recommended skill: MathModelDesigner authoritative simulation design refinement, or backend adapter apply only
  if the user explicitly approves implementation.

## Consolidation Gate: Math Config History

Decision: Create a strict consolidation gate before the next implementation-adjacent sprint.

Evidence:
- Prior sprints produced feature parity, protocol, schema patch, strict fixtures, backend adapter planning, and
  authoritative server math design artifacts.
- Current blockers are specific: math/config values, RTP model simulations, VABS/history storage, registration
  serializer/lane, runtime owner, assets, wallet tests, and release approval.
- Checkpoint policy says public push should occur every 3-4 local sprints or major checkpoint, with pushed raw
  validation as truth.

Outcome:
- Consolidation gate completed: true.
- Going in circles risk: low.
- Math/config/GL dependency matrix created: true.
- RTP model flexibility matrix created: true.
- VABS/Lasthands/history matrix created: true.
- Game settings profile planning schema and sample profiles created: true.
- Checkpoint git review due soon: true.
- Public export/push run: false.
- Backend adapter implementation allowed: false.
- GameClientBuilder implementation allowed: false.
- GameServerRegistrar generation allowed: false.
- Next recommended skill: MathModelDesigner authoritative simulation/config refinement.

## 2026-05-12 14:05:14 - Authoritative Simulation Config Refinement

- Created a non-production simulation/config refinement package under `04_math/authoritative_server_math_v1/simulation_config_refinement/`.
- Created a local deterministic smoke simulator under `04_math/authoritative_server_math_v1/simulation/`.
- Kept exact values non-final, jackpot disabled by default, bonus-buy EV pending, and all implementation gates closed.
- Recommended next step is checkpoint git review/push if the user approves, not implementation.

## 2026-05-12 14:33:04 - Fast-Lane Optimization

- Adopted fast-lane operating mode for future Little Gangster and donor-to-release projects.
- Set normal planning sprint limits: max 10 created files, max 5 modified files, compact report only.
- Updated WorkflowOrchestrator skill and scripts to recognize checkpoint due and fast-lane defaults.
- Chose not to use subagents for this sprint because the work was small and write-owned by the main agent.

## 2026-05-12 15:26:48 - Checkpoint Git Review Push

- Rebuilt sanitized public export and included recent safe artifacts plus WorkflowOrchestrator fast-lane snapshot.
- Committed public export as `ca854797d2d67def46f17dd989164b71ce49cc44` with message `Checkpoint Little Gangster fast-lane and math config artifacts`.
- Pushed to public GitHub `main` and validated raw GitHub content at the pushed commit.
- Set checkpoint push due to false and kept implementation/release gates false.

## 2026-05-12 16:59:34 - Public Export Corruption Fix Policy

- Treat commit `ca854797d2d67def46f17dd989164b71ce49cc44` as invalidated by external raw validation contradiction.
- Rebuild public export using newline-preserving copy/redaction only.
- Add `scripts/validate_github_raw_public_export.py` under the private project tree as the required raw GitHub validator.
- Claim public export success only if the project-local raw validator passes against the pushed commit.

## 2026-05-12 17:04:16 - Public Export Raw Validation Is Required

- Public export success may only be claimed after `scripts/validate_github_raw_public_export.py` validates GitHub raw content for the pushed commit.
- Commit `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` is the replacement validated checkpoint.
- Checkpoint push due is false after this validated replacement.

## 2026-05-12 17:24:01 - RawSafeCheckpointExport Completed

- Use raw-safe selected-file export for public checkpoints when raw GitHub line preservation is critical.
- Do not trust public-export-internal validators as the sole proof source.
- Public validation for `e0e5a2e04b1c793bf06a586601a3778154e6be2c` passed through `validate_rawsafe_github_raw.py` and curl line counts.
- Next recommended sprint remains MathModelDesigner calibration; implementation gates stay closed.

## 2026-05-12 17:42:40 - Math Calibration Gate Decision

- Do not unlock backend adapter implementation from this smoke sprint.
- Do not unlock GameServerRegistrar generation from this smoke sprint.
- Next required sprint is compact MathModelDesigner calibration continuation or product/math decisioning for final RTP, bonus-buy, free-spin, and GL
  values.

## 2026-05-13T03:56:32Z - Calibration Diagnostics Decision

- Decision: do not tune symbol weights or paytables yet.
- Reason: simulator sanity checks found RTP unit/denominator gaps and missing free-spin/feature/bonus-buy contribution paths.
- Gate: backend adapter implementation and registration generation remain blocked.
- Next: repair the non-production simulator model completeness before another calibration pass.

## 2026-05-13T04:39:10Z - Model Completeness Fix Decision

- Decision: patch only the non-production simulator to make RTP units, denominators, feature/free-spin smoke paths, and bonus-buy smoke paths
  explicit.
- Decision: do not tune symbol weights or paytables in this sprint.
- Decision: keep backend adapter implementation and GameServerRegistrar generation blocked.
- Next: limited calibration tuning may proceed only against the local simulator outputs.

## 2026-05-13T04:57:31Z - Limited Calibration Tuning Decision

- Decision: apply exactly one provisional tuning set: cluster paytable x6.5, feature trigger 0.08, free spins 12/15/18.
- Decision: do not use post-spin payout scaling as release math.
- Decision: do not move to backend adapter or registration generation yet.
- Decision: update reusable MathModelDesigner calibration fast-lane workflow for future games.

## 2026-05-13T08:12:26Z - Second-Pass Calibration Decision

- Decision: apply one `rtp_92`-only cluster pay multiplier of `1.026`.
- Decision: do not tune bonus buy because the purchased feature path is incomplete for product EV.
- Decision: keep backend adapter implementation and registration generation blocked.

## 2026-05-13T08:55:01Z - RTP / Volatility Profile Framework Decision

- Decision: generalize RTP models to LOW/MEDIUM/HIGH labels instead of hardcoding `rtp_92/94/96` as the reusable model.
- Decision: require a 3x3 RTP/volatility profile matrix for future games.
- Decision: store profile identity in runtime and VABS/history payloads.
- Decision: keep registration metadata separate from executable math.
## Volatility Profile Simulation Design 2026-05-13

- Decision: keep the 3x3 RTP x volatility matrix as the operator-facing profile framework.
- Decision: simulator profile selection should resolve by `mathProfileId`, with legacy `rtp_92`, `rtp_94`, and `rtp_96` retained only as provisional
  backing model IDs.
- Decision: LOW volatility should prioritize hit rate and smaller wins; HIGH volatility should prioritize tail value and larger but less frequent
  outcomes; MEDIUM remains the neutral provisional basis.
- Decision: bonus-buy EV remains excluded from volatility smoke until its denominator and feature path are finalized.
- Decision: backend adapter implementation, GameClientBuilder implementation, GameServerRegistrar generation, wallet work, DB work, and release
  approval remain blocked.

## 3x3 Profile Calibration First Pass 2026-05-13

- Decision: use profile-specific overlays for calibration rather than editing global rule JSON.
- Decision: allow at most two local smoke calibration iterations in this sprint.
- Decision: treat +/-2.0 percentage points as first-pass smoke tolerance only, not certification tolerance.
- Decision: do not tune bonus buy in this sprint.
- Decision: keep backend adapter implementation, GameClientBuilder implementation, GameServerRegistrar generation, wallet work, DB work, and release
  approval blocked.

## Raw-Safe Checkpoint Review/Push 2026-05-13

- Decision: use the raw-safe export repository and avoid the old export pipeline.
- Decision: commit and push checkpoint `b7b420ba0916af6f6073f5e714ab73e1d36d4f93` after local validation passed.
- Decision: trust the checkpoint only after GitHub raw validation and direct raw line counts passed.
- Decision: set checkpoint push due to false.
- Decision: keep all implementation, registration, wallet, DB, asset, and release gates blocked.

## Large-Sample Stability and Bonus-Buy EV Decision 2026-05-13

- Decision: treat the larger 3x3 profile run as smoke stability evidence only, not certification.
- Decision: keep 8 of 9 profiles in calibration-pending status because they fell outside +/-2.0 percentage points at 10,000 rounds per seed.
- Decision: preserve volatility framework because hit-rate and standard-deviation ordering still passed.
- Decision: keep `max_win_tail_frequency_unproven` because cap frequency remained zero.
- Decision: keep bonus buy blocked and move it to a separate bonus-buy EV design sprint; do not tune or implement it yet.
- Decision: keep backend adapter implementation and GameServerRegistrar generation blocked.

## 3x3 Profile Stability Triage 2026-05-13

- Decision: do not proceed to bonus-buy EV design yet; base 3x3 RTP/profile instability is the higher-priority blocker.
- Decision: no simulator or harness bug was proven, so no simulator code patch was made.
- Decision: no tuning values were changed in this triage sprint.
- Decision: classify the likely root cause as small-sample calibration overfit plus profile-specific tuning weakness.
- Decision: require a larger train/validation seed split recalibration sprint before backend adapter planning or registration generation.

## RTP Confidence Scale Correction 2026-05-13

- Decision: reclassify the 10,000-round-per-seed 3x3 results as smoke/inconclusive, not true RTP failures.
- Decision: replace "failed profile" language with "outside small-sample smoke tolerance" unless a statistical confidence threshold is met.
- Decision: define simulation scale tiers from wiring smoke through certification/lab scale.
- Decision: do not tune aggressively from smoke variance.
- Decision: never approve backend adapter implementation, GameServerRegistrar generation, or release from smoke-only RTP evidence.

## Confidence-Scale Raw-Safe Checkpoint 2026-05-13

- Decision: update the raw-safe public export using line-preserving copy/generation only, not the old sanitizer pipeline.
- Decision: push checkpoint `30d7dc4855bffd2eb5f5fec83bb9f562974fa8ac` after local validation and git-blob line-count checks passed.
- Decision: trust the checkpoint only after project-local GitHub raw validation and direct curl line counts passed.
- Decision: keep backend adapter, client, registration, wallet, DB, donor, asset, and release gates blocked.

## Train / Validation Simulation Design 2026-05-13

- Decision: create a design-only train/validation workflow before any further tuning.
- Decision: define distinct seed families for smoke, diagnostic, training, validation, pre-certification, tail/max-win discovery, and lab scale.
- Decision: allow tuning only from training runs; validation runs cannot tune values.
- Decision: require every future report to preserve `mathProfileId`, RTP level, volatility level, seed set, confidence interval, volatility ordering,
  cap/tail status, and bonus-buy EV status.
- Decision: keep backend adapter implementation, GameServerRegistrar generation, client work, wallet/DB actions, donor work, and release approval
  blocked.

## External Simulation Job Export 2026-05-13

- Decision: create external train, validation, and tail/max-win job definitions for all 9 profiles.
- Decision: use 1,000,000 rounds per seed as the default train job size and 5,000,000 rounds per seed as the default validation job size.
- Decision: use 10,000,000 rounds per seed as the first tail/max-win discovery pass, with future 100M/1B tiers documented.
- Decision: run only the 9-profile 100-round dry-run inside Codex.
- Decision: keep validation seeds unavailable for tuning and keep backend, client, registration, wallet, DB, donor, asset, and release gates blocked.

## Train Results Import Attempt 2026-05-13

- Decision: stop the import sprint because `external_train_results_missing` blocked the required input.
- Decision: do not infer tuning needs from missing results.
- Decision: do not use validation seeds or tail-discovery outputs.
- Decision: keep exact values non-final and keep backend, client, registration, wallet, DB, donor, asset, and release gates blocked.

## Local Simulation Runner 2026-05-13

- Decision: create a local, self-service runner for future train jobs instead of waiting on external infrastructure.
- Decision: run only a benchmark and 9-profile x 100-round proof smoke in this sprint.
- Decision: keep 1M train jobs as the next manual Terminal action, not as part of this sprint.
- Decision: keep validation seeds forbidden for tuning.
- Decision: keep exact values non-final and keep backend, client, registration, wallet, DB, donor, asset, and release gates blocked.

## Local 10M Total Train Run 2026-05-13

- Decision: use the existing train manifest with `--rounds-override 222222` because the runner applies the override per train seed.
- Decision: keep the total run budget at 9,999,990 rounds across all 9 profiles, not 10M per profile or seed.
- Decision: run train phase only and exclude validation, tail-discovery, and bonus-buy jobs.
- Decision: do not tune values during the run.
- Decision: use these outputs as inputs to a later train-results import and tuning-decision sprint.
- Decision: keep exact values non-final and keep backend, client, registration, wallet, DB, donor, asset, and release gates blocked.

## 10M Train Tuning Decision 2026-05-14

- Decision: update only `profile_calibration_adjustments.json` using local 10M train data.
- Decision: apply profile-specific adjustments instead of a single global multiplier.
- Decision: use cluster/free-spin/feature and symbol-weight overlay levers only; do not edit base rule JSON.
- Decision: do not use validation seeds, tail jobs, bonus-buy tuning, jackpot tuning, or post-spin payout scaling.
- Decision: skip optional verification in this sprint to stay within the fast-lane file cap.
- Decision: require a validation-seed overlay check next, with validation output used only for pass/fail evidence, not tuning.
- Decision: keep exact values non-final and keep backend, client, registration, wallet, DB, donor, asset, and release gates blocked.

## 10M Overlay Train Rerun 2026-05-14

- Decision: complete the updated-overlay rerun as train-only evidence using 9,999,990 total rounds.
- Decision: do not run validation seeds yet because 3 profiles remain outside +/-2 percentage points: LG_8001_RTP_LOW_VOL_MEDIUM,
  LG_8001_RTP_MEDIUM_VOL_HIGH, LG_8001_RTP_HIGH_VOL_MEDIUM.
- Decision: preserve the volatility framework because LOW/MEDIUM/HIGH hit-rate and standard-deviation ordering still passed.
- Decision: keep cap/tail, bonus-buy EV, exact-value certification, backend adapter, client, registration, DB, wallet, donor, asset, and release gates
  blocked.
- Decision: next safest step is a targeted train-only outlier adjustment pass, not validation.

## Targeted Outlier Adjustment 2026-05-14

- Decision: adjust only `LG_8001_RTP_LOW_VOL_MEDIUM`, `LG_8001_RTP_MEDIUM_VOL_HIGH`, and `LG_8001_RTP_HIGH_VOL_MEDIUM` in
  `profile_calibration_adjustments.json`.
- Decision: leave the six passing profile overlay entries unchanged.
- Decision: run a targeted train-only rerun for 3,333,330 rounds total using train seeds only.
- Decision: build a composite 9-profile train gate from six previous passing results plus three targeted rerun results.
- Decision: the composite train gate is clean enough to proceed to validation-seed overlay check, but validation results must not tune values.
- Decision: keep bonus buy, jackpot, tail discovery, backend adapter, client, registration, DB, wallet, donor, asset, and release gates blocked.

## Validation Seed Check 2026-05-14

- Decision: run a local 10M-total validation-seed check across all 9 RTP/volatility profiles.
- Decision: do not tune from validation seeds and do not modify `profile_calibration_adjustments.json`.
- Decision: mark the 3x3 matrix as `pass_for_profile_matrix_train_validation_stage` because 9 of 9 profiles are within +/-2 percentage points.
- Decision: do not open backend adapter, GameServerRegistrar, or release gates because cap/tail, bonus-buy EV, and certification-scale validation
  remain blocked.
- Decision: recommend tail/max-win validation planning next, with bonus-buy EV design remaining a separate blocker.

## Tail / Max-Win Pilot 2026-05-14

- Decision: run a bounded 10M-total tail discovery pilot across all 9 RTP/volatility profiles, not 10M per profile.
- Decision: use tail seed family only; do not use train or validation seeds.
- Decision: keep possible max win planning-only because the bounded pilot did not prove cap/tail behavior at certification scale.
- Decision: keep bonus-buy EV, larger tail confirmation, backend adapter, registration generation, and release gates blocked.

## MathProfileCalibrator Skill Creation 2026-05-14

- Decision: create MathProfileCalibrator as the reusable skill for 3x3 RTP/volatility calibration.
- Decision: patch MathModelDesigner to hand off calibration loops instead of owning endless tuning.
- Decision: patch WorkflowOrchestrator to route open profile-calibration gates to MathProfileCalibrator before backend/client/registration work.
- Decision: keep Little Gangster math values unchanged and run no simulations in this sprint.

## MathProfileCalibrator RTP Range Update 2026-05-14

- Decision: update reusable MathProfileCalibrator RTP validation range to 91.00%-99.70% inclusive.
- Decision: require strict RTP ordering LOW < MEDIUM < HIGH and reject duplicate RTP levels.
- Decision: keep operators restricted to approved pretested mathProfileIds, not arbitrary runtime RTP values.
- Decision: do not change Little Gangster RTP profiles in this sprint.

## RTP Range Raw-Safe Checkpoint 2026-05-14

- Decision: push raw-safe checkpoint `6fc02b341be2e2432b79b810b75b726794d1db7a` for the reusable MathProfileCalibrator RTP range update.
- Decision: include line-preserving MathProfileCalibrator skill snapshots and safe project docs only.
- Decision: keep Little Gangster RTP profiles unchanged and keep all implementation/release gates blocked.

## 2026-05-14 - Bonus-Buy EV Decision And Design

Decision: keep bonus buy in scope as a design requirement, but keep it blocked for implementation, registration generation, and release.

Rationale:
- Existing planning artifacts include bonus-buy metadata and BF registration fields.
- Removing bonus buy requires explicit product approval.
- Bonus-buy EV must be calculated independently from base RTP using buy cost as denominator.
- Cost candidates are defined as 100x, 125x, and 150x total bet, but product approval and simulation evidence are still pending.

Outcome:
- Created bonus-buy EV, profile matrix, registration field, history, simulation plan, and blocker documents.
- Backend adapter, GameClientBuilder, GameServerRegistrar generation, wallet/DB work, and release remain blocked.

## 2026-05-14 - Bonus-Buy EV Simulation And Cost Recommendation

Decision: do not proceed to backend adapter or registration generation after the bonus-buy EV sample.

Rationale:
- Purchased-feature simulation path was verified for all 9 profiles using train seed family only.
- Candidate costs 100x, 125x, and 150x produce BF_RTP values far below the provisional desired BF targets in the runtime-limited sample.
- No candidate cost is acceptable as-is; a lower cost, stronger purchased-feature start/value model, volatility-specific cost model, or explicit scope
  removal decision is needed.
- Exact values remain non-final and certification status remains false.

Outcome:
- Created bonus-buy EV simulation results, cost recommendation, registration planning values, and blockers.
- Backend adapter, GameClientBuilder, GameServerRegistrar generation, wallet/DB work, and release remain blocked.

## 2026-05-14 - Bonus-Buy Model Redesign Decision

Decision: keep bonus buy in scope, reject current candidate costs as acceptable, and do not approve a 4x-8x cost-only fix.

Rationale:
- Current BF_RTP at 100x/125x/150x is far below desired BF RTP.
- Denominator logic is correct by design, so the likely issue is the purchased-feature value/start-state model.
- The direct purchased-feature path does not sufficiently model guaranteed premium state, golden-square/rainbow progress, enhanced coin/special
  reveals, or retriggers.

Outcome:
- Created required feature-value analysis, redesign options, redesign decision, inactive v2 draft model, v2 simulation plan, and blockers.
- Active `bonus_buy_rules.json` remains unchanged.
- Backend adapter, GameClientBuilder, GameServerRegistrar generation, wallet/DB work, and release remain blocked.

## 2026-05-14 - Latest Simulation Results Documentation Consolidation

Decision: consolidate current Little Gangster math/simulation evidence into central docs for future sprints and review.

Outcome:
- Created/updated `GAME_STATUS_CURRENT.md`, `LATEST_SIMULATION_RESULTS_SUMMARY.md`, `latest_simulation_results_summary.json`,
  `current_registration_readiness.md`, and `current_release_blockers.md`.
- Documented base train gate and validation gate as passed.
- Documented tail/max-win and bonus-buy evidence as planning-only/non-certified.
- Documented bonus-buy v2 as draft-only and inactive.
- Confirmed backend adapter, client, registration generation, wallet/DB, donor/asset, certification, and release gates remain blocked.

## 2026-05-14 - Bonus-Buy V2 Draft Diagnostic Simulation

Decision: keep bonus buy blocked after the inactive v2 draft diagnostic.

Rationale:
- The v2 draft diagnostic was run with train seed family only and did not modify active `bonus_buy_rules.json`.
- The diagnostic verified the non-production purchased-feature v2 path for all 9 profiles.
- The 100x denominator is closest for every profile, but 3 of 9 profiles remain outside the +/-2 percentage-point planning band.
- 125x and 150x remain too low versus target BF_RTP in this diagnostic.
- The 25,000-per-profile fallback attempt exceeded fast-lane runtime and was stopped; retained evidence is a bounded 1,000-per-profile diagnostic
  sample.

Outcome:
- Created bonus-buy v2 diagnostic results, report, cost recommendation, and blockers.
- Do not move bonus buy to train/validation EV yet.
- Refine the inactive v2 purchased-feature value model for outlier profiles before rerunning a bounded diagnostic.
- Backend adapter, GameServerRegistrar generation, wallet/DB work, and release remain blocked.

## 2026-05-14 - Bonus-Buy V2 Outlier Refinement

Decision: keep bonus buy blocked after one draft-only outlier refinement pass.

Rationale:
- The refined draft model adjusted only the three prior 100x outliers and remained inactive.
- Active `bonus_buy_rules.json`, the original `bonus_buy_v2_draft_model.json`, and base profile tuning overlays were unchanged.
- The refined diagnostic used train seed family only and tested all 9 profiles at 10,000 purchased-feature samples per profile.
- The 100x gate remained not clean: 6 of 9 profiles were within +/-2 percentage points and 3 remained outside.
- 125x and 150x remain too low for standard-buy use and should stay blocked as separate premium/super tiers pending separate design.

Outcome:
- Created `bonus_buy_v2_refined_draft_model.json`, refined diagnostic results, cost recommendation, and blocker reports.
- Bonus buy is not ready for train/validation EV yet.
- Backend adapter, GameServerRegistrar generation, wallet/DB work, and release remain blocked.

## 2026-05-14 - Bonus-Buy V2 Pass2 Final Draft Refinement

Decision: move 100x bonus-buy v2 to train/validation EV planning, but keep backend adapter and registration generation blocked.

Rationale:
- This was the second and final draft-only refinement pass.
- The pass2 draft adjusted only the latest source outliers: LOW/HIGH, MEDIUM/HIGH, and HIGH/HIGH.
- Active `bonus_buy_rules.json`, original `bonus_buy_v2_draft_model.json`, first refined `bonus_buy_v2_refined_draft_model.json`, and base profile
  tuning overlays were unchanged.
- The pass2 diagnostic used train seed family only and tested all 9 profiles at 10,000 purchased-feature samples per profile.
- The 100x gate is clean at diagnostic scale: 9 of 9 profiles within +/-2 percentage points.
- 125x and 150x remain blocked as separate premium/super tiers pending separate design.

Outcome:
- Created `bonus_buy_v2_refined_pass2_draft_model.json`, pass2 diagnostic results, cost recommendation, and blocker reports.
- Bonus buy is ready for a focused train/validation EV sprint using 100x as the standard candidate.
- Exact values remain non-final and certification status remains false.
- Backend adapter, GameServerRegistrar generation, wallet/DB work, and release remain blocked until train/validation EV and product approval pass.

## 2026-05-14 - Bonus-Buy V2 100x Train EV Gate

Decision: keep bonus buy blocked and do not run validation because the train EV gate failed.

Rationale:
- The train EV gate used the inactive pass2 draft and train seed family only.
- The train phase tested all 9 profiles at 25,000 purchased-feature simulations per profile.
- The train gate required all 9 profiles within +/-2 percentage points at 100x.
- Train result was 8 of 9 within tolerance; `LG_8001_RTP_HIGH_VOL_HIGH` was outside at +2.235423 pp.
- Validation seeds must not be used for tuning, and validation was not run because train did not pass.
- Active `bonus_buy_rules.json`, pass2 draft, and base profile tuning overlays were unchanged.

Outcome:
- Created train EV results, gate summary, provisional registration planning values, and blocker reports.
- BF_RTP and BF_RTP_MIN values are train-only provisional planning values, not final registration values.
- 125x and 150x remain blocked as separate premium/super tiers.
- Recommend product decision or explicitly approved deeper redesign for the HIGH/HIGH 100x train outlier.
- Backend adapter, GameServerRegistrar generation, wallet/DB work, and release remain blocked.

## 2026-05-14 - Bonus-Buy BF_RTP Policy Decision

Decision: allow Little Gangster bonus-buy BF_RTP to differ from base RTP as a planning policy, provided the separate BF_RTP values are
product-approved, disclosed, validated, and registered separately.

Rationale:
- Bonus-buy RTP is a separate product/math value from base-game RTP in many slot models.
- The prior 100x train result had 8 of 9 profiles within +/-2 pp of base RTP, with only HIGH/HIGH above base target by 2.235423 pp.
- Treating HIGH/HIGH as a declared BF_RTP planning value is safer than tuning from validation seeds or forcing BF_RTP to equal base RTP without a
  product requirement.

Outcome:
- Created BF_RTP policy, declared BF_RTP targets, validation target decision, registration policy update, and blocker docs.
- `LG_8001_RTP_HIGH_VOL_HIGH` is reclassified as `BF_RTP_above_base_target` and requires product approval plus validation-seed evidence.
- Bonus-buy validation is ready to proceed against declared BF_RTP planning targets.
- Active `bonus_buy_rules.json`, base profile tuning, backend adapter, client code, registration artifacts, DB/wallet flows, donor assets, and release
  approval were not touched.

## 2026-05-14 - Bonus-Buy 100x Declared BF_RTP Validation Decision

Decision: mark bonus-buy 100x validation as passed against declared BF_RTP planning targets and move bonus buy to product approval review, while
keeping backend adapter and registration generation blocked.

Rationale:
- The validation-seed run tested all 9 profiles at 25000 purchased-feature simulations per profile.
- Validation compared against declared BF_RTP planning targets, not base RTP, following the separated BF_RTP policy.
- Result: 9 of 9 profiles within +/-2 percentage points; 0 outside.
- Validation seeds were not used for tuning, and no active math/config files were modified.
- Overfit risk remains `moderate_watch_all_profiles_within_tolerance` and exact values are non-final/certification false.

Outcome:
- Created validation result, gate summary, registration planning values, blocker report, and skill reports.
- 100x remains the standard candidate; 125x and 150x remain blocked as separate premium/super tiers.
- Product approval is required before any active config, backend adapter, or registration generation work proceeds.

## 2026-05-14 - Bonus-Buy Product Approval Package Decision

Decision: stop the default bonus-buy math/refinement loop and move the 100x bonus-buy model to product decision.

Rationale:
- Bonus-buy 100x validation passed against declared BF_RTP planning targets for 9 of 9 profiles.
- The evidence is sufficient for a product approval review package, not release approval or certification.
- Further math loops without a product decision risk churn and do not resolve approval, runtime representation, or registration gating.

Outcome:
- Created product approval package, machine-readable package, registration impact summary, runtime/VABS impact summary, product decision form, and
  no-more-loop note.
- Backend adapter implementation and GameServerRegistrar generation remain blocked until product approval and downstream runtime/registration gates
  are accepted.
- 125x and 150x remain blocked as separate premium/super tiers.

## 2026-05-14 - Bonus-Buy Option A Product Decision

Decision: record Option A approval for the 100x bonus-buy package for implementation planning only.

Outcome:
- Backend adapter representation planning is allowed for approved 100x bonus-buy payload and VABS/history fields.
- Backend adapter implementation remains blocked until separately approved.
- GameClientBuilder implementation, GameServerRegistrar generation/apply, wallet/DB work, final assets, release, and certification remain blocked.
- Active `bonus_buy_rules.json` was not changed.

## 2026-05-15 - Backend Adapter Representation Planning Decision

Decision: create backend adapter representation planning for Little Gangster, including base results, cascades/features, the approved-for-planning
100x bonus-buy payload, and VABS/Lasthands/history fields.

Outcome:
- Created backend adapter representation plan, payload field map, 100x bonus-buy payload plan, VABS/Lasthands/history plan, blocker doc, and
  implementation gate doc.
- Planning allowed remains true, but backend adapter implementation, GameClientBuilder, GameServerRegistrar generation, wallet/DB work, certification,
  and release remain blocked.

## 2026-05-15 - Backend Adapter Apply Decision

Decision: apply the Little Gangster 8001 backend adapter payload representation in Staging source under the explicitly approved scope.

Outcome:
- Created the isolated `new-games-server/src/games/little-gangster/` adapter module and targeted tests.
- Added guarded gameId `8001` presentation-payload branches for base spin and 100x bonus-buy representation.
- The adapter emits `presentationPayload.gamePayload` with math profile, RTP/volatility, declared BF_RTP, 100x bonus-buy, cascade, state persistence,
  and VABS/Lasthands/history fields.
- 100x bonus buy remains planning-only and carries runtime, wallet/accounting, VABS/Lasthands, tail/max-win, release, and certification blockers.
- 125x and 150x remain blocked.
- GameClientBuilder, GameServerRegistrar generation, registration artifacts, DB/wallet work, certification, and release remain blocked.

## 2026-05-15 - Lifecycle Wrapper Source Planning Decision

Decision: select Option 5 for future lifecycle wrapper source shape: a small Little Gangster-specific lifecycle wrapper under
`new-games-server/src/games/little-gangster/lifecycle/`, plus a separate visual history module under
`new-games-server/src/games/little-gangster/history/`, integrated through guarded gameId `8001` route calls in `new-games-server/src/index.ts`.

Rationale:
- Current 8001 adapter is a payload mapper only and should not become the full runtime owner.
- `new-games-server/src/index.ts` is the proven route host for slot lifecycle, wallet bridge, history, resume, and close behavior.
- Core protocol already supports runtime envelopes and `presentationPayload.gamePayload`.
- VABS/VBA/Lasthands visual history is not proven by the current adapter and needs its own route planning/implementation lane.
- Crazy Rooster / 7001 is not authoritative.

Outcome:
- Created source target map, source planning report, patch blueprints, source test plan, implementation approval gate, blockers, and skill reports.
- No Staging source, backend adapter code, VABS route code, client code, registration artifact, DB/Cassandra, wallet/API call, donor browsing, asset
  capture, or release approval occurred.
- Lifecycle wrapper implementation, VABS route implementation, GameClientBuilder, GameServerRegistrar generation, wallet tests, and release remain
  blocked until explicit approval.

## 2026-05-15 - ParallelMathValidator Skill Creation Decision

Decision: create a reusable `ParallelMathValidator` skill and patch workflow routing/downstream awareness so large-scale math validation can run in a
parallel lane while the main workflow continues where safe.

Rationale:
- MathProfileCalibrator should remain bounded and train-focused rather than becoming an endless large simulation loop.
- Future projects need a generic way to validate 3x3 RTP/volatility matrices, bonus-buy EV, FRB/promo liability, tail/max-win evidence, registration
  math fields, and certification evidence packages.
- Downstream skills need explicit blockers when registration/release fields depend on unresolved simulation evidence.

Outcome:
- Created `ParallelMathValidator` skill docs, references, and scripts.
- Updated `SKILL_INDEX.md`, MathProfileCalibrator, WorkflowOrchestrator routing scripts, GameServerRegistrar, and RTPAndReleaseAuditor.
- Created Little Gangster adoption/playbook docs and gate matrix.
- Script compile and sample validations passed.
- No simulations, active math changes, Staging source changes, backend/client/registration implementation, DB/wallet actions, donor browsing, asset
  capture, certification, or release approval occurred.

## 2026-05-15 - Raw-Safe Checkpoint Review Decision

Decision: stop the ParallelMathValidator/lifecycle raw-safe checkpoint before commit and push.

Rationale:
- Local raw-safe validation failed before staging.
- Prepared export content included long Markdown lines that violate the raw-safe validator.
- Prepared export content included private local path strings and one non-allowlisted redacted donor host.

Outcome:
- No commit was created.
- No push was attempted.
- GitHub raw validation was not run.
- A follow-up raw-safe export curation sprint is required before publishing this checkpoint.

## 2026-05-15 - Raw-Safe Curation Checkpoint Push Decision

Decision: curate and push the ParallelMathValidator/lifecycle raw-safe public checkpoint.

Rationale:
- The previous checkpoint failed before commit because prepared public files still contained long Markdown lines, private local paths, and a donor
  host reference.
- Public review needs a checkpoint for the reusable ParallelMathValidator workflow and lifecycle wrapper planning, but only after raw-safe validation
  passes.

Outcome:
- Created public-safe metadata and a slim public-safe `project_manifest.json`.
- Curated copied project docs to remove private paths and donor host values.
- Wrapped long Markdown lines without weakening the validator.
- Local raw-safe validation passed.
- Git blob validation passed.
- Pushed commit `cdf0606603c6b576989de6210e160f8f2f8a559a` to public `main`.
- GitHub raw validation passed.
- Release, certification, GameClientBuilder, GameServerRegistrar generation, wallet/DB work, lifecycle wrapper implementation, and VABS route
  implementation remain blocked.

## 2026-05-15 - Lifecycle Wrapper Apply Decision

Decision: apply the Little Gangster 8001 lifecycle wrapper in Staging source under the explicitly approved implementation scope.

Outcome:
- Created the `new-games-server/src/games/little-gangster/lifecycle/` wrapper module.
- Added lifecycle state, action/accounting representation, round completion, state persistence, reconnect recovery, and active blocker propagation
  around the existing `presentationPayload.gamePayload` mapper.
- Updated only the guarded gameId `8001` branch in `new-games-server/src/index.ts` to call the lifecycle wrapper for base spin and
  approved-for-planning 100x bonus-buy representation.
- VABS/VBA/Lasthands visual history route implementation remains blocked and was not created.
- Targeted Little Gangster tests passed 13/13, and isolated Little Gangster lifecycle TypeScript passed.
- GameClientBuilder, GameServerRegistrar generation, registration artifacts, DB/Cassandra, wallet/API calls, donor browsing, asset capture,
  certification, and release remain blocked.

## 2026-05-15 - VABS Visual History Source Planning Decision

Decision: plan Little Gangster 8001 VABS/VBA/Lasthands visual history routes and patch reusable workflow guidance for future games.

Outcome:
- Recommended `new-games-server/src/games/little-gangster/history/` as the 8001 visual history source module location.
- Recommended guarded route registration in `new-games-server/src/index.ts`.
- Planned JSON round/session/whole-session replay routes and visual round/session/whole-session render routes.
- Planned in-game History button and Casino Manager/backoffice access paths.
- Created response schema, storage contract, security/privacy contract, test plan, implementation gate, source target map, and blockers.
- Patched ProtocolAndSchemaMapper, WalletAndLaunchTester, GameClientBuilder, and RTPAndReleaseAuditor guidance so future games must implement or
  explicitly block visual history before release.
- No Staging source, VABS route code, backend adapter code, client code, registration artifacts, DB/Cassandra, wallet/API calls, donor browsing, asset
  capture, certification, or release approval occurred.

## 2026-05-15 - VABS Route Resolution Audit Decision

Decision: select a hybrid VABS/VBA/Lasthands route-resolution model before implementing
Little Gangster 8001 visual history.

Rationale:
- Legacy GS proves visual VABS access through `/vabs/show.jsp` style routes, helper
  actions, history list URLs, and CM/backoffice-facing visual links.
- New-games proves JSON `/slot/v1/gethistory` and 8001 replay payloads, but not a visual
  render route.
- Gamesv1/client evidence does not prove a generic visual VABS renderer or completed
  History button route.
- Registration/bootstrap config must carry or derive the visual route, but exact
  GameServerRegistrar field shape remains unproven.

Outcome:
- Recommended model: `model_e_hybrid_configured_gs_cm_route_new_games_server_visual_replay`.
- Recommended VABS source location: `new-games-server/src/games/little-gangster/history/`.
- GameClientBuilder, GameServerRegistrar generation, wallet/history tests, VABS route
  implementation, certification, and release remain blocked.

## 2026-05-15 - VABS Evidence Policy Decision

Decision: define a reusable VABS/VBA/Lasthands evidence policy with three layers:
deterministic replay, required visual HTML/render route, and optional screenshot/video
media controlled by game-level settings.

Rationale:
- Deterministic replay is the only acceptable authoritative source for round/session
  reconstruction.
- Visual VABS route is still required for History and CM/backoffice workflows unless
  current GS evidence proves otherwise.
- Screenshots and videos can support audit/dispute workflows, but full video for every
  spin is storage-heavy and not a safe default.

Outcome:
- Default `historyEvidenceMode`: `deterministic_replay_only`.
- Screenshot and video modes are supported by policy but not implemented.
- Media manifest schema, game-level settings plan, QA matrix, and release gate were
  created.
- Durable media storage, screenshot capture, video capture, route implementation,
  registration generation, wallet/API calls, certification, and release remain blocked.

## 2026-05-15 - VABS Visual History Route Apply Decision

Decision: apply the Little Gangster 8001 VABS/VBA/Lasthands visual history route
foundation in Staging source under the explicitly approved limited implementation
scope.

Outcome:
- Created `new-games-server/src/games/little-gangster/history/`.
- Added deterministic replay payload building, safe visual HTML rendering, media
  manifest support, history security helpers, non-production fixture storage, and
  guarded 8001 history route registration.
- Added targeted tests for history routes, visual rendering, payload building, media
  manifest defaults, security, and storage provider behavior.
- Targeted history route tests passed 6/6.
- Durable storage, screenshot capture, video capture, wallet/API calls, registration
  generation, client code, certification, and release remain blocked.

## 2026-05-15 - VABS Alias Compatibility Audit Decision

Decision: recommend `legacy_alias_recommended` for Little Gangster 8001.

Rationale:
- Legacy GS/source evidence proves `/vabs/show.jsp` style VBA/VABS visual history
  semantics for round/session and BO/support history flows.
- Current 8001 canonical `/slot/v1/8001/history/...` routes provide JSON/render
  foundation but do not prove BO/CM compatibility alone.
- Registration/bootstrap route configuration is required as a concept, but exact field
  shape remains blocked.

Outcome:
- Created alias compatibility audit, evidence, route decision, route contract,
  registration config audit, History button plan, QA plan, implementation gate, blockers,
  and skill reports.
- No Staging source, alias implementation, client code, registration artifact,
  DB/Cassandra action, wallet/API call, donor browsing, asset capture, certification, or
  release approval occurred.

## 2026-05-15 - VABS Legacy Alias Apply Decision

Decision: apply the Little Gangster 8001 VABS legacy alias foundation in Staging source.

Outcome:
- Created `legacyAliasTypes.ts`, `legacyAliasMapper.ts`, `legacyAliasRoutes.ts`, and
  `legacyAliasSecurity.ts`.
- Registered guarded root and scoped alias routes:
  `/vabs/show.jsp` and `/slot/v1/8001/legacy/vabs/show.jsp`.
- Preserved canonical 8001 new-games history routes.
- Added targeted mapper, security, alias route foundation, and canonical preservation
  tests.
- Targeted tests passed 9/9.
- Durable storage, media storage, screenshot/video capture, BO/CM acceptance,
  GameClientBuilder, GameServerRegistrar generation, wallet/API calls, DB/Cassandra,
  registration artifacts, certification, and release remain blocked.

## 2026-05-15 - GS Responsibility Boundary Audit Decision

Decision: treat wallet/accounting/session/history responsibility as GS/platform-owned
unless current source proves runtime ownership. The browser/client is display/request
orchestration only; Little Gangster runtime/lifecycle is representation and coordination
only for wallet references, state, idempotency, result/history payload, and blockers.

Rationale:
- BankInfo/common-wallet source proves wallet manager/config ownership in GS.
- GS internal new-games bridge proves wallet reserve/settle and history write/read
  belong behind GS session/account context.
- Cassandra persisters prove durable session, bet, round, wallet-operation, and pending
  operation storage surfaces.
- Gamesv1 client transport proves the client calls GS runtime endpoints and displays
  envelope state rather than owning provider settlement.

Outcome:
- Created GS responsibility audit, responsibility matrix, wallet boundary contract,
  pending/stuck ownership doc, WalletAndLaunchTester scope correction, test matrix,
  registration dependency doc, future-game boundary gate, and prompt correction.
- Patched reusable ProtocolAndSchemaMapper, WalletAndLaunchTester,
  WorkflowOrchestrator, GameServerRegistrar, and RTPAndReleaseAuditor guidance.
- Wallet/GS/BO endpoint calls, DB/Cassandra actions, implementation, registration
  generation, GameClientBuilder, certification, and release remain blocked.
