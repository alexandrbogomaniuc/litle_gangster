# External Reviewer Copy-Paste Report

## Sprint identity

- Repository/project: `[PROJECT_ROOT]`
- Sprint goal: Run MathModelDesigner and SprintReporter only, creating a provisional internal math package with RTP variants, simulation outputs, integration boundaries, and handoff.
- Date/time: 2026-05-08T17:24:08+01:00
- Skill(s) involved: MathModelDesigner, SprintReporter
- Current status: Provisional math package created and 1,000,000-round workflow simulations passed for 96%, 94%, and 92% RTP variants. Math is not release-approved.

## User instruction received

The user instructed Codex to use `[SKILL_SUITE_ROOT]` and `[PROJECT_ROOT]`, running only MathModelDesigner and SprintReporter. The sprint had to design and simulate a provisional Little Gangster math package without browsing donor URLs,
investigating gameplay, capturing assets, downloading donor files, building client code, generating client runtime code, generating Cassandra registration, executing DB changes, calling wallet endpoints, storing raw secrets, printing full
donor URLs/tokens, approving release, or claiming final runtime integration.

## Source documents inspected

- path/name: `[SKILL_SUITE_ROOT]/AGENTS.md`
  - readable: yes
  - used for: suite safety rules
  - important findings: no broad search, no guessed protocol/schema, no raw secrets, blockers instead of hallucination
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
  - readable: yes
  - used for: skill order and MathModelDesigner boundaries
  - important findings: MathModelDesigner designs internal math packages and validates RTP/volatility with simulation; no screenshot-only math or client-side RNG assumption
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/.agents/skills/MathModelDesigner/SKILL.md`
  - readable: yes
  - used for: required workflow, outputs, and validation expectations
  - important findings: produce paytables, reels, bonus/free-spin/buy-feature rules, simulation config, RTP/volatility/max-win reports
  - unreadable/blocker notes: none

- path/name: `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md`
  - readable: yes
  - used for: report format
  - important findings: report must list exact files changed, validations, blockers, assumptions, risks, and next prompt
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/AGENTS.md`
  - readable: yes
  - used for: project-local safety rules
  - important findings: read manifest before every skill, no broad search, no raw secrets, no full tokenized donor URL, no DB apply
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/project_manifest.json`
  - readable: yes
  - used for: target RTPs, volatility, bet range, features, blockers, and current workflow state
  - important findings: RTP targets 96/94/92, high volatility, bet range 0.20/1.00/100.00, coin denominations verified, runtime owner unknown
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/01_reference_research/reference_research_report.md`
  - readable: yes
  - used for: observed feature clues and evidence boundaries
  - important findings: demo mode, base screen, menu/info, wild/scatter/bonus/free-spin clues observed; final math must not be generated from screenshots alone
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/01_reference_research/scenario_coverage.md`
  - readable: yes
  - used for: gameplay coverage confidence
  - important findings: intro/base/menu/info coverage is medium-high; deep bonus/free-spin/long-run coverage is low
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/01_reference_research/mechanics_observed.md`
  - readable: yes
  - used for: feature clues only
  - important findings: reference observed a 6x5 cluster-style game and max-win/free-spin/buy-feature descriptions, but donor-true math remains unproven
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/02_reference_assets/final_inventory.csv`
  - readable: yes
  - used for: asset release boundary only
  - important findings: 29 captured scaffold assets remain blocked from release
  - unreadable/blocker notes: asset bodies were not inspected for math

- path/name: `[PROJECT_ROOT]/02_reference_assets/asset_ownership_register.csv`
  - readable: yes
  - used for: asset release boundary only
  - important findings: all captured scaffold assets remain replacement-required and blocked
  - unreadable/blocker notes: asset bodies were not inspected for math

- path/name: `[PROJECT_ROOT]/03_protocol/math_rng_ownership_report.md`
  - readable: yes
  - used for: math/runtime ownership boundary
  - important findings: browser must not own real-money RNG/results; final backend/new-games result owner remains UNKNOWN/BLOCKED
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/03_protocol/runtime_lane_decision_matrix.md`
  - readable: yes
  - used for: target runtime lane caveats
  - important findings: new-games `slot-browser-v1` / HTTP runtime is the planning lane, with blockers
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/03_protocol/player_release_integration_blockers.md`
  - readable: yes
  - used for: release blockers and next-skill readiness
  - important findings: MathModelDesigner can run with limits; GameClientBuilder/GameServerRegistrar/WalletAndLaunchTester/release remain blocked
  - unreadable/blocker notes: none

- path/name: `[PROJECT_ROOT]/03_protocol/protocol_contract_summary.json`
  - readable: yes
  - used for: machine-readable protocol state
  - important findings: BSG CW is separate wallet protocol; math lives first in `04_math`; registration import is unknown; runtime owner blocked
  - unreadable/blocker notes: none

## Files created

- `[PROJECT_ROOT]/04_math/math_model_summary.md`
- `[PROJECT_ROOT]/04_math/math_assumptions.md`
- `[PROJECT_ROOT]/04_math/math_blockers.md`
- `[PROJECT_ROOT]/04_math/math_package.json`
- `[PROJECT_ROOT]/04_math/math_runtime_integration_contract.md`
- `[PROJECT_ROOT]/04_math/math_to_gs_registration_boundary.md`
- `[PROJECT_ROOT]/04_math/result_schema.json`
- `[PROJECT_ROOT]/04_math/simulation_config.json`
- `[PROJECT_ROOT]/04_math/rtp_report.md`
- `[PROJECT_ROOT]/04_math/volatility_report.md`
- `[PROJECT_ROOT]/04_math/max_win_report.md`
- `[PROJECT_ROOT]/04_math/feature_contribution_report.md`
- `[PROJECT_ROOT]/04_math/target_models/rtp_96/model_config.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_96/reel_strips.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_96/paytable.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_96/feature_rules.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_96/simulation_summary.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_94/model_config.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_94/reel_strips.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_94/paytable.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_94/feature_rules.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_94/simulation_summary.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_92/model_config.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_92/reel_strips.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_92/paytable.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_92/feature_rules.json`
- `[PROJECT_ROOT]/04_math/target_models/rtp_92/simulation_summary.json`
- `[PROJECT_ROOT]/04_math/paytables/provisional_paytable_v0.1.json`
- `[PROJECT_ROOT]/04_math/reels/provisional_reel_strips_v0.1.json`
- `[PROJECT_ROOT]/04_math/features/provisional_feature_rules_v0.1.json`
- `[PROJECT_ROOT]/04_math/simulations/rtp_96_1000000_seed_2026050801.json`
- `[PROJECT_ROOT]/04_math/simulations/rtp_94_1000000_seed_2026050801.json`
- `[PROJECT_ROOT]/04_math/simulations/rtp_92_1000000_seed_2026050801.json`
- `[PROJECT_ROOT]/04_math/reports/README.md`
- `[PROJECT_ROOT]/04_math/scripts/simulate_math.py`
- `[PROJECT_ROOT]/00_skill_reports/MathModelDesigner/skill_report.md`
- `[PROJECT_ROOT]/00_skill_reports/MathModelDesigner/validation_checklist.md`
- `[PROJECT_ROOT]/00_skill_reports/MathModelDesigner/blockers.md`
- `[PROJECT_ROOT]/00_skill_reports/MathModelDesigner/handoff.json`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_history/20260508_172408_MathModelDesigner.md`

## Files modified

- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/10_sprint_reports/sprint_report_latest.md`

## Files deleted

none

## Actions performed

- Read the required suite rules, project rules, manifest, assumptions, decisions, reference reports, asset inventory summaries, and protocol reports.
- Created the `04_math/` structured math package.
- Designed an original provisional slot model for Little Gangster.
- Created RTP variants for 96%, 94%, and 92%.
- Created paytables, reel strips, feature rules, simulation config, result schema, and runtime/registration boundary docs.
- Created `simulate_math.py`, a deterministic local simulator with explicit CLI arguments.
- Ran 1,000,000 base-round simulations for each RTP variant.
- Wrote simulation summaries for each variant.
- Updated manifest math state and preserved runtime/release blockers.
- Wrote MathModelDesigner skill report, checklist, blockers, and handoff.
- Ran SprintReporter and wrote latest/history reports.

## Validations run

- command/check: JSON parse for project manifest, math package, result schema, simulation config, target model JSON files, simulation summaries, and handoff
  - result: pass
  - evidence: Python JSON parse succeeded for all checked files
  - not run reason if skipped: not skipped

- command/check: `python3 -m py_compile [PROJECT_ROOT]/04_math/scripts/simulate_math.py`
  - result: pass
  - evidence: compile command succeeded
  - not run reason if skipped: not skipped

- command/check: 1,000,000-round simulation for `rtp_96`
  - result: pass for workflow tolerance
  - evidence: simulated RTP 96.013333%, deviation +0.013333
  - not run reason if skipped: not skipped

- command/check: 1,000,000-round simulation for `rtp_94`
  - result: pass for workflow tolerance
  - evidence: simulated RTP 94.013056%, deviation +0.013056
  - not run reason if skipped: not skipped

- command/check: 1,000,000-round simulation for `rtp_92`
  - result: pass for workflow tolerance
  - evidence: simulated RTP 92.012778%, deviation +0.012778
  - not run reason if skipped: not skipped

- command/check: required output files exist and are non-empty
  - result: pass
  - evidence: required file existence/non-empty check passed
  - not run reason if skipped: not skipped

- command/check: redaction scan for known raw donor token examples, known raw PASS_KEY example, and sensitive query/value patterns
  - result: pass
  - evidence: sensitive string scan over new/updated math outputs, skill report, manifest, assumptions, and decisions returned no matches
  - not run reason if skipped: not skipped

- command/check: no new donor asset capture
  - result: pass
  - evidence: no files under `02_reference_assets` modified after this sprint start time
  - not run reason if skipped: not skipped

- command/check: no later skill report dirs
  - result: pass
  - evidence: no report directories for ArtSceneMapper, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, or RTPAndReleaseAuditor were created
  - not run reason if skipped: not skipped

- command/check: required boundary statements present
  - result: pass
  - evidence: math runtime contract states backend authority; GS registration boundary states executable math import is unknown/not assumed; RTP report states full-size provisional workflow simulation
  - not run reason if skipped: not skipped

- command/check: release/certification validation
  - result: skipped
  - evidence: user forbade release approval and later runtime/test/audit skills were not run
  - not run reason if skipped: out of sprint scope and blocked by unresolved runtime evidence

## Key findings

- A complete provisional math package now exists under `04_math/`.
- The model is a 5x3, 20-line high-volatility slot with wilds, scatters, free spins, optional bonus buy, and optional neutral double-up.
- RTP variants were created for 96.0%, 94.0%, and 92.0%.
- Each variant ran 1,000,000 deterministic base rounds and passed the provisional workflow tolerance.
- The math package is not donor-true math and does not claim to reconstruct the reference game.
- The model is not release-certified.
- Browser result authority remains forbidden.
- Backend/new-games runtime remains the expected production owner, but exact owner is still UNKNOWN/BLOCKED.
- GS/Cassandra registration is treated as metadata/config/routing only; executable math import is not proven.

## Decisions made

- Decision: use a 5x3 fixed-20-line model rather than a donor-style cluster model.
  - Source: user allowed a preferred provisional model when exact donor mechanics are unproven; reference coverage is incomplete.

- Decision: include free spins and bonus buy.
  - Source: project manifest requires them and reference info observed supporting clues.

- Decision: include double-up only as an optional neutral placeholder.
  - Source: project manifest requires double-up, but gameplay did not prove the actual flow.

- Decision: exclude jackpot.
  - Source: project manifest says jackpot is not required.

- Decision: keep math unapproved for release.
  - Source: runtime ownership, independent validation, wallet/launch testing, asset approval, and release audit are incomplete.

- Decision: recommend ArtSceneMapper next.
  - Source: workflow order and successful provisional math package creation; next step should map scene/object expectations without building client code.

## Assumptions

- The math package is original provisional Little Gangster math, not donor math.
- Backend/new-games runtime will eventually own real-money RNG/result generation.
- `new-games-server` and `@gamesv1/core-protocol` will be provided or authorized later.
- RTP display/config fields in GS registration are metadata unless later source proves executable math import.
- Bonus buy cost and EV need later review.
- Double-up needs later product/regulatory confirmation.
- One deterministic 1,000,000-round seed per variant is sufficient for workflow validation, not release certification.

## Blockers

- `new_games_server_source_path_missing`: backend `/slot/v1/*` source path is still missing.
- `core_protocol_package_not_inspected`: `@gamesv1/core-protocol` package root has not been inspected.
- `slot_v1_result_owner_unknown`: final authoritative RNG/result owner for 8001 is not proven.
- `runtime_math_integration_pending`: math package has not been integrated into backend/new-games runtime.
- `game_8001_registration_missing`: no 8001 GS/Cassandra route/config records exist.
- `scn_serializer_missing`: no safe serializer/config-generation tool verified for binary `scn`.
- `approved_release_assets_missing`: scaffold/reference assets are not release-approved.
- `wallet_launch_tests_missing`: no 8001 wallet/launch tests exist.
- `independent_multi_seed_certification_pending`: only one deterministic 1,000,000-round seed per RTP variant was run.
- `bonus_buy_ev_needs_review`: bonus buy price and EV need product/math review.
- `double_up_product_decision_pending`: optional double-up behavior needs product/regulatory confirmation.

## Risks

- High: If backend runtime result ownership differs from the current expectation, math integration shape may change.
- High: If `@gamesv1/core-protocol` requires a different result schema, `result_schema.json` will need mapping.
- Medium: The provisional 5x3 model intentionally differs from observed reference layout, so product approval may require redesign.
- Medium: Bonus buy and double-up are only placeholders until reviewed.
- Medium: One deterministic seed is not certification-grade.
- Medium: Scaffold assets remain release-blocked.

## Anti-hallucination checks

- Did the agent search outside allowed paths? no
- Did the agent guess missing facts? no; unknowns were recorded as blockers or assumptions
- Did the agent claim 100% coverage? no
- Did the agent ask for raw secrets? no
- Did the agent execute DB changes? no
- Did the agent approve unknown assets? no
- Did the agent separate BSG CW from browser runtime? yes
- Did the agent create handoff files? yes

## Current trust level

partially trustworthy

Why: the math files, simulator, and 1,000,000-round simulation outputs are concrete and reproducible. Trust is partial because the package is provisional, runtime owner remains unproven, independent multi-seed certification has not run, and
no backend/client/wallet/release integration has been tested.

## Next recommended step

Run ArtSceneMapper and SprintReporter only.

## Exact next recommended Codex prompt

```text
Use the reusable skill suite at:
[SKILL_SUITE_ROOT]

Use the existing project at:
[PROJECT_ROOT]

Run only these skills for this sprint:
1. ArtSceneMapper
2. SprintReporter

Do not run ArtDirectionAndReplacementPlanner, GameClientBuilder, GameServerRegistrar, WalletAndLaunchTester, RTPAndReleaseAuditor, AuthorizedReferenceResearcher, ReferenceAssetInventory, ProtocolAndSchemaMapper, or MathModelDesigner.

Read the project manifest, reference research outputs, asset inventory, protocol outputs, and the provisional math package under 04_math/. Create scene maps, object ID rules, and an HTML scene inspector template for artist/developer
planning. Use scaffold/reference assets only as blocked internal reference material; do not approve donor/scaffold assets for release, do not build client code, do not capture more assets, do not browse donor URLs, do not generate
Cassandra, do not call wallet endpoints, and do not claim final runtime integration.
```

## Questions for external reviewer

- Is the provisional 5x3 fixed-line model acceptable as an original Little Gangster starting point, despite the reference clue showing a different layout?
- Are the RTP simulation results reproducible from `simulate_math.py` and the package JSON files?
- Did the sprint preserve the backend-authoritative RNG/result boundary?
- Did the sprint avoid claiming GS registration imports executable math?
- Are bonus buy and double-up correctly marked as provisional placeholders?
- Are runtime and release blockers visible enough for the next agent?
