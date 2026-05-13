# Sprint Necessity Matrix

Status: consolidation gate audit.

Direct answer: the project is not going in circles. The pilot has been narrowing from broad discovery to specific missing implementation gates. Several future pilot-only sprints can be collapsed into one-click or merged checks, but
implementation gates remain closed.

| Category | Major sprint or sprint group | Why it was necessary | Reusable for future projects | Can be skipped in future | Should become one-click skill | Pilot-only | Artifact proving completion |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project creation | ProjectCreator | Established manifest, assumptions, decisions, roots, game id, safety gates. | Yes | No | Yes | No | `00_skill_reports/ProjectCreator/handoff.json` |
| Donor/reference research | AuthorizedReferenceResearcher | Captured feature/settings parity clues and blockers. | Yes | Only when a clean product spec replaces donor research. | Yes | No |
`01_reference_research/donor_feature_settings_parity_report.md` |
| Asset inventory | ReferenceAssetInventory | Quarantined scaffold/reference assets and blocked release use. | Yes | Only if no scaffold capture is used. | Yes | No | `00_skill_reports/ReferenceAssetInventory/handoff.json` |
| Protocol mapping | Initial ProtocolAndSchemaMapper | Split launch, runtime, wallet, registration, GS, and browser layers. | Yes | No | Yes | No | `03_protocol/protocol_layer_model.md` |
| Math v0.1/v0.2/v0.3 | MathModelDesigner iterations | Moved from provisional math to v0.3 result contract with cascades/features/cap/state. | Yes | Older versions can be skipped once v0.3 template exists. | Yes | Partly |
`04_math/alternatives/v0_3_donor_feature_parity_provisional/result_schema.json` |
| ArtSceneMapper | v0.3 scene/result mapping | Mapped render states and object requirements to v0.3 payload. | Yes | No for visual games. | Yes | No | `05_art/v0_3_result_state_to_scene_mapping.md` |
| ArtDirection | Replacement direction | Created release-safe art direction and kept scaffold assets blocked. | Yes | Only with pre-approved final assets. | Partly | No | `00_skill_reports/ArtDirectionAndReplacementPlanner/handoff.json` |
| Mantis/ExtGame checklist | Mantis scope correction and checklists | Prevented advisory ExtGame notes from becoming guessed architecture. | Yes | Can be merged into ProtocolAndSchemaMapper. | Yes | Partly |
`03_protocol/mantis_lessons_current_gs_checklist.md` |
| Current GS registration/RNG audit | CurrentGSRegistrationRngAudit | Proved registration is config-first and RNG/result owner remains unproven. | Yes | No until lane is stable. | Yes | No |
`00_skill_reports/CurrentGSRegistrationRngAudit/handoff.json` |
| Runtime API inspection | `/slot/v1` runtime review | Proved generic envelope and endpoints, but not Little Gangster runtime owner. | Yes | No unless runtime lane is already fixed. | Yes | No |
`03_protocol/runtime_api_inspection_report.md` |
| Public export validation hardening | Public export reliability sprints | Fixed trust failure between local report and GitHub raw state. | Yes | Skip until checkpoint/export. | Yes | Pilot recovery |
`09_release/checkpoint_git_review_policy.md` |
| gamePayload schema patch | Schema extension review/apply | Added reusable `presentationPayload.gamePayload` support. | Yes | Future projects can reuse if patch remains accepted. | No, source patch is one-time | Pilot/core-platform |
`03_protocol/source_patch_apply_summary.md` |
| Strict fixture update | Strict gamePayload fixtures | Proved 24 v0.3 fixture variants validate through patched schemas. | Yes | Future projects can template it. | Yes | No |
`06_resulting_code/planning/fixtures/strict_schema_validation_report.md` |
| Backend adapter planning | Backend adapter implementation planning | Defined future adapter target/files/contracts without implementation. | Yes | No before backend work. | Yes | No |
`03_protocol/backend_adapter_implementation_planning_report.md` |
| Authoritative server math design | AuthoritativeServerMathDesign | Defined Little Gangster-owned server math/state/history model; excluded 7001 math authority. | Yes | No for real-money games. | Yes | No |
`04_math/authoritative_server_math_v1/authoritative_math_design_summary.md` |

Future compression decision:

- Keep ProjectCreator, reference parity, protocol, math, scene, adapter, registration, wallet, and release gates.
- Merge repeated protocol planning into one current-GS lane audit plus one adapter planning/apply sprint.
- Skip public export except at external review/checkpoint moments.
- Skip separate fixture-only work when a mature strict fixture template already exists.

