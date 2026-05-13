# External Reviewer Copy-Paste Report

## Sprint identity
- Repository/project: [PROJECT_ROOT]
- Sprint goal: Create a strict donor feature/settings parity specification for Little Gangster while keeping art original and all scaffold assets blocked from release.
- Date/time: 2026-05-10 19:55:56 BST
- Skill(s) involved: AuthorizedReferenceResearcher, MathModelDesigner documentation update, ArtDirectionAndReplacementPlanner, SprintReporter. ReferenceAssetInventory and ArtSceneMapper were not run because no new assets were captured and
no scene-map JSON update was required.
- Current status: blocked_requires_math_revision

## User instruction received
Run only the allowed skills to inventory donor settings/features, enforce the policy that Little Gangster must match donor settings/features, update math/art parity contracts if needed, preserve all donor/scaffold assets as internal-only
references, avoid raw URL/token persistence, avoid DB/wallet/release actions, and produce a SprintReporter report.

## Source documents inspected
- path/name: [SKILL_SUITE_ROOT]/AGENTS.md
  - readable: yes
  - used for: suite safety rules and no-broad-search boundaries
  - important findings: no raw secrets, no release approval, no broad search
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/SKILL_INDEX.md
  - readable: yes
  - used for: allowed skill order
  - important findings: confirmed skill suite architecture
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/.agents/skills/AuthorizedReferenceResearcher/SKILL.md
  - readable: yes
  - used for: donor observation and redaction requirements
  - important findings: observation must avoid unredacted URL/token persistence and avoid overclaiming coverage
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/.agents/skills/ReferenceAssetInventory/SKILL.md
  - readable: yes
  - used for: decision not to run asset inventory unless new assets were captured
  - important findings: scaffold assets must remain inventoried, blocked, and not release-approved
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/.agents/skills/MathModelDesigner/SKILL.md
  - readable: yes
  - used for: feature/math contract update boundary
  - important findings: math must remain backend-authoritative and provisional assumptions must be explicit
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/.agents/skills/ArtSceneMapper/SKILL.md
  - readable: yes
  - used for: decision that no scene-map JSON update was needed this sprint
  - important findings: scene maps stay technical planning artifacts and scaffold assets remain blocked
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/.agents/skills/ArtDirectionAndReplacementPlanner/SKILL.md
  - readable: yes
  - used for: original art/theme replacement planning and scaffold-release restrictions
  - important findings: donor/scaffold assets may be reference only; final art must be original/internal-approved/licensed
  - unreadable/blocker notes: none
- path/name: [SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md
  - readable: yes
  - used for: report structure
  - important findings: report must include files, validations, blockers, assumptions, anti-hallucination checks, and next prompt
  - unreadable/blocker notes: none
- path/name: [PROJECT_ROOT]/project_manifest.json
  - readable: yes
  - used for: current project state and manifest updates
  - important findings: selected layout is 6x5_cluster_provisional; all release approvals remain false
  - unreadable/blocker notes: none
- path/name: [PROJECT_ROOT]/01_reference_research/* prior reports and screenshots
  - readable: yes
  - used for: donor parity evidence
  - important findings: prior playable evidence shows 6x5 grid, demo balance/bet, buy bonus, settings menu, game info/rules, and safe demo spin evidence
  - unreadable/blocker notes: fresh clean Playwright retry reached error shell
- path/name: [PROJECT_ROOT]/02_reference_assets/final_inventory.csv and related asset reports
  - readable: yes
  - used for: scaffold support for feature/audio/art parity
  - important findings: 142 scaffold assets remain blocked_from_release
  - unreadable/blocker notes: no new assets captured this sprint
- path/name: [PROJECT_ROOT]/04_math/alternatives/v0_2_6x5_cluster/*
  - readable: yes
  - used for: math feature parity audit
  - important findings: v0.2 covers broad 6x5 cluster direction but not donor-specific cascade/golden-square/rainbow/coin/three-mode behavior
  - unreadable/blocker notes: runtime owner and full validation remain blocked
- path/name: [PROJECT_ROOT]/05_art/* art/scene outputs
  - readable: yes
  - used for: art direction and feature/settings parity mapping
  - important findings: original Little Gangster / Neon Heist theme exists; no final assets approved
  - unreadable/blocker notes: none

## Files created
- [PROJECT_ROOT]/00_skill_reports/ArtDirectionAndReplacementPlanner/feature_settings_parity_blockers.md
- [PROJECT_ROOT]/00_skill_reports/ArtDirectionAndReplacementPlanner/feature_settings_parity_file_changes.json
- [PROJECT_ROOT]/00_skill_reports/ArtDirectionAndReplacementPlanner/feature_settings_parity_update_report.md
- [PROJECT_ROOT]/00_skill_reports/ArtDirectionAndReplacementPlanner/feature_settings_parity_validation_checklist.md
- [PROJECT_ROOT]/00_skill_reports/AuthorizedReferenceResearcher/feature_settings_parity_blockers.md
- [PROJECT_ROOT]/00_skill_reports/AuthorizedReferenceResearcher/feature_settings_parity_skill_report.md
- [PROJECT_ROOT]/00_skill_reports/AuthorizedReferenceResearcher/feature_settings_parity_validation_checklist.md
- [PROJECT_ROOT]/00_skill_reports/MathModelDesigner/feature_parity_blockers.md
- [PROJECT_ROOT]/00_skill_reports/MathModelDesigner/feature_parity_update_report.md
- [PROJECT_ROOT]/00_skill_reports/MathModelDesigner/feature_parity_validation_checklist.md
- [PROJECT_ROOT]/01_reference_research/donor_feature_parity_blockers.md
- [PROJECT_ROOT]/01_reference_research/donor_feature_settings_evidence.json
- [PROJECT_ROOT]/01_reference_research/donor_feature_settings_matrix.csv
- [PROJECT_ROOT]/01_reference_research/donor_feature_settings_parity_report.md
- [PROJECT_ROOT]/01_reference_research/donor_settings_screenshots_index.md
- [PROJECT_ROOT]/01_reference_research/feature_parity_run_feature_parity_20260510T183859Z.json
- [PROJECT_ROOT]/01_reference_research/har/sanitized_network_metadata_feature_parity_20260510T183859Z.jsonl
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/01_initial_intro.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/02_after_continue.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/03_base_idle_after_continue.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/04_menu_or_settings_click_top_right.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/05_menu_item_top.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/06_menu_item_second.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/07_menu_item_third.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/08_menu_item_fourth.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/09_after_escape_from_menu.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/10_bottom_left_buy_or_feature.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/11_bottom_left_bet_or_menu.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/12_bottom_center_menu_or_bet.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/13_bottom_right_autoplay_or_aux.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/14_bottom_right_spin_area_pre_spin.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/15_safe_demo_spin_1.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/16_safe_demo_spin_5.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/17_safe_demo_spin_10.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/18_safe_demo_spin_20.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/19_safe_demo_spin_30.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/20_after_reload.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/21_mobile_initial.png
- [PROJECT_ROOT]/01_reference_research/screenshots/feature_parity_20260510T183859Z/22_mobile_after_tap.png
- [PROJECT_ROOT]/04_math/donor_feature_math_alignment.md
- [PROJECT_ROOT]/04_math/feature_parity_impact_report.md
- [PROJECT_ROOT]/05_art/art_direction_feature_parity_update.md
- [PROJECT_ROOT]/05_art/donor_feature_scene_mapping.md
- [PROJECT_ROOT]/05_art/feature_flow_replacement_plan.md
- [PROJECT_ROOT]/05_art/feature_settings_parity_matrix.md
- [PROJECT_ROOT]/05_art/settings_ui_replacement_plan.md
- [PROJECT_ROOT]/10_sprint_reports/sprint_report_history/20260510T195556+0100_DonorFeatureSettingsParity.md

## Files modified
- [PROJECT_ROOT]/00_skill_reports/ArtDirectionAndReplacementPlanner/handoff.json
- [PROJECT_ROOT]/00_skill_reports/AuthorizedReferenceResearcher/handoff.json
- [PROJECT_ROOT]/00_skill_reports/MathModelDesigner/handoff.json
- [PROJECT_ROOT]/01_reference_research/blockers.md
- [PROJECT_ROOT]/01_reference_research/event_timeline.jsonl
- [PROJECT_ROOT]/01_reference_research/mechanics_observed.md
- [PROJECT_ROOT]/01_reference_research/network_observations.md
- [PROJECT_ROOT]/01_reference_research/reference_research_report.md
- [PROJECT_ROOT]/01_reference_research/scenario_coverage.md
- [PROJECT_ROOT]/01_reference_research/visual_style_observations.md
- [PROJECT_ROOT]/05_art/approved_assets_manifest.json
- [PROJECT_ROOT]/05_art/art_direction.md
- [PROJECT_ROOT]/05_art/art_direction_blockers.md
- [PROJECT_ROOT]/05_art/art_direction_handoff.md
- [PROJECT_ROOT]/10_sprint_reports/sprint_report_latest.md
- [PROJECT_ROOT]/assumptions.md
- [PROJECT_ROOT]/decisions_log.md
- [PROJECT_ROOT]/project_manifest.json

## Files deleted
none

## Actions performed
- Used the donor URL in memory only; no full donor URL or raw token was persisted.
- Ran a focused project-local Playwright donor retry for feature/settings parity.
- Captured screenshots and sanitized network metadata only; no donor asset response bodies were saved.
- Checked Chrome DevTools MCP availability; it exposed only about:blank, so it was not used as parity evidence.
- Built a 41-row donor feature/settings parity matrix covering game mechanics, settings/menu items, feature flows, and visual/audio scaffolding.
- Used prior successful demo-mode evidence to identify donor features/settings, and used the fresh retry as blocker evidence.
- Created math parity impact reports showing that v0.2 is directionally aligned but insufficient for strict donor feature parity.
- Created art-direction parity updates preserving original Little Gangster / Neon Heist art while matching donor settings/features.
- Updated project manifest, assumptions, decisions, and skill handoffs.
- Did not run ReferenceAssetInventory because no new assets were captured.
- Did not run ArtSceneMapper because no scene-map JSON update was required.
- Did not build client code, generate Cassandra registration, execute DB changes, call wallet endpoints intentionally, or approve release.

## Validations run
- command/check: JSON parse for project_manifest.json, donor_feature_settings_evidence.json, feature parity run JSON, skill handoffs, approved_assets_manifest.json, and file-change manifest.
  - result: pass
  - evidence: 8 JSON files parsed successfully.
  - not run reason if skipped: not skipped
- command/check: Required parity output existence/non-empty check.
  - result: pass
  - evidence: all required research, math, art, and skill-report outputs exist and are non-empty.
  - not run reason if skipped: not skipped
- command/check: donor_feature_settings_matrix.csv required columns and row consistency.
  - result: pass
  - evidence: 41 rows, every observed row has parity status, every mismatch has required_action, unobserved rows are not marked matched.
  - not run reason if skipped: not skipped
- command/check: redaction scan for the known raw donor token and full donor query URL in persisted text outputs.
  - result: pass
  - evidence: no raw token or full query URL found; only redacted donor URL remains in manifest.
  - not run reason if skipped: not skipped
- command/check: asset release status scan.
  - result: pass
  - evidence: no donor/scaffold asset row has release_status=approved_for_release.
  - not run reason if skipped: not skipped
- command/check: 06_resulting_code inspection.
  - result: pass
  - evidence: 0 files found; no donor/scaffold asset moved into release code.
  - not run reason if skipped: not skipped
- command/check: DB/Cassandra/wallet/release action review.
  - result: pass by action log
  - evidence: no such commands or integrations were run.
  - not run reason if skipped: no DB/wallet actions were permitted or needed

## Key findings
- Donor feature/settings coverage confidence: medium.
- Donor URL browsing succeeded only partially: the fresh clean Playwright retry reached the donor error shell, but prior successful in-app/Chrome evidence remains usable.
- Safe demo/test mode was confirmed from prior demo balance/spin evidence and redacted launch context; the fresh clean retry did not reach playable UI.
- Matrix rows: 41.
- Observed or partially observed donor feature/settings rows: 31.
- Donor feature rows observed/partial: 22.
- Donor settings rows observed/partial: 9.
- Matched Little Gangster rows: 14.
- Mismatch rows requiring update: 14.
- Blocked/unobserved/product-decision rows: 13.
- Strict donor parity requires MathModelDesigner retry before full GameClientBuilder.
- Art direction update completed and remains original/release-safe.
- All scaffold assets remain blocked_from_release.

## Decisions made
- Decision: target_feature_policy is `match_donor_features_and_settings`.
  - source: user instruction
- Decision: recommend MathModelDesigner next, not GameClientBuilder.
  - source: evidence-based mismatch between donor feature rules and v0.2 math/result contract
- Decision: do not run ReferenceAssetInventory.
  - source: no new scaffold assets captured this sprint
- Decision: do not run ArtSceneMapper.
  - source: no scene-map JSON update required; parity update was documentation/contract level
- Decision: keep art/theme original Little Gangster / Neon Heist.
  - source: user requirement and prior art direction
- Decision: keep all scaffold assets blocked_from_release.
  - source: user instruction and suite safety rules

## Assumptions
- Prior successful donor screenshots and reports are valid evidence for feature/settings parity.
- Fresh clean Playwright error shell reflects a browser/runtime context blocker, not proof that the donor game is unplayable generally.
- Exact donor autoplay stop conditions, feature probabilities, bonus-buy EV, mobile playable layout, and full win-tier thresholds remain unknown until observed or sourced.
- v0.2 math can be revised rather than discarded, because its 6x5 cluster layout remains directionally aligned.
- No final asset approval evidence was supplied in this sprint.

## Blockers
- `fresh_clean_context_rgs_api_error`: fresh clean browser retry reached donor error shell and RGS/API failures.
- `cascade_result_contract_missing`: donor super cascade/removal/refill is not modeled in v0.2 result contract.
- `golden_square_state_missing`: donor golden-square cell state is not modeled.
- `rainbow_activation_math_missing`: donor rainbow activation is not represented by v0.2 generic scatter assumption.
- `coin_reveal_values_missing`: bronze/silver/gold coin reveal values are not modeled.
- `three_feature_modes_missing`: donor’s three feature modes are not modeled separately.
- `bonus_buy_confirmation_unobserved`: button visible, but confirmation/cost/EV/purchased flow not captured.
- `autoplay_stop_conditions_unobserved`: autoplay panel and stop conditions not directly captured.
- `mobile_playable_layout_unobserved`: fresh mobile retry stayed in error shell.
- `final_assets_not_approved`: all scaffold assets remain blocked and replacement-required.

## Risks
- High: GameClientBuilder could build the wrong result/animation state machine if started before math/result parity revision.
- High: Release would be unsafe if scaffold assets were treated as final assets.
- Medium: Some donor settings/features remain partially observed or blocked, so parity confidence is medium, not high.
- Medium: Bonus-buy and feature-mode math may require significant revision once exact donor rules are fully proven.
- Low: Redacted URL appears in manifest by design; raw donor token/full URL was not found in persisted text outputs.

## Anti-hallucination checks
- Did the agent search outside allowed paths? No.
- Did the agent guess missing facts? No; unknown or unobserved items were marked blocked/pending evidence.
- Did the agent claim 100% coverage? No.
- Did the agent ask for raw secrets? No.
- Did the agent execute DB changes? No.
- Did the agent approve unknown assets? No.
- Did the agent separate donor/scaffold references from release assets? Yes.
- Did the agent preserve original Little Gangster art direction while matching donor features/settings? Yes.
- Did the agent create handoff files? Yes.

## Current trust level
partially trustworthy

Reason: the reports are grounded in prior successful demo evidence, current project outputs, and a fresh retry blocker, with redaction and validation checks passing. Trust is partial because the fresh clean browser retry did not reach
playable UI and several donor feature/settings details remain unobserved.

## Next recommended step
Run MathModelDesigner to revise the v0.2 6x5 math/result contract for strict donor feature/settings parity before full GameClientBuilder.

## Exact next recommended Codex prompt
Use the reusable skill suite at `[SKILL_SUITE_ROOT]` and the project at `[PROJECT_ROOT]`. Run only MathModelDesigner and SprintReporter. Goal: revise the selected `v0.2_6x5_cluster_provisional` math/result contract to match donor
feature/settings parity from `01_reference_research/donor_feature_settings_matrix.csv`, especially super cascade, golden-square state, rainbow activation, coin reveal values, pot/clover reveal, three feature modes, max-win cap behavior, and
bonus-buy flow. Do not browse donor URLs, do not capture assets, do not build client code, do not generate or execute Cassandra/DB changes, do not call wallet endpoints, do not store raw secrets, and do not approve release. Produce updated
math package/result schema reports, validation, handoff, and SprintReporter report.

## Questions for external reviewer
- Does the parity matrix correctly distinguish directly observed features from blocked/unobserved ones?
- Should GameClientBuilder remain blocked until MathModelDesigner revises cascade/golden-square/rainbow/coin feature contracts?
- Should double-up/gamble be removed from Little Gangster scope unless donor evidence appears?
- Are any donor settings missing from the matrix based on the prior screenshots or captured scaffold inventory?
- Are the scaffold asset restrictions strong enough for release safety?
