# Little Gangster Pilot Issue Register

| issue_id | sprint_detected | description | root_cause | impact | pipeline_fix | skill_to_patch | status |
|---|---|---|---|---|---|---|---|
| LG-PILOT-001 | ProjectCreator | Initial questions missed donor parity/capture/public export/source lane details. | Initial manifest questions were too narrow for donor-based casino projects. | Repeated correction sprints and late
blockers. | Add fast-start intake questions and blocker recording. | ProjectCreator | patched |
| LG-PILOT-002 | AuthorizedReferenceResearcher | Donor URL handling required repeated correction. | Full tokenized launch URL handling was not strongly templated. | Risk of stale/expired URL reuse or persistence. | In-memory-only donor URL
policy, fresh-token handling, safe demo confirmation. | AuthorizedReferenceResearcher | patched |
| LG-PILOT-003 | DonorFeatureSettingsParity | Feature/settings parity was discovered too late. | Reference research did not force complete settings/features matrix before math selection. | v0.2 needed rework after math and art planning. |
Require donor feature/settings parity before final math selection. | AuthorizedReferenceResearcher, MathModelDesigner | patched |
| LG-PILOT-004 | ReferenceAssetInventory | Scaffold asset use was constrained by prompt wording and not planned early enough. | Workflow did not clearly separate observation-only, scaffold capture, and licensed release reuse. | Scene/art
planning missed available preview scaffolds at first. | Add explicit capture mode and inventory/hash/map before art direction. | ReferenceAssetInventory, ArtSceneMapper | patched |
| LG-PILOT-005 | MathQualityGate | Initial math layout did not match donor 6x5 cluster direction. | MathModelDesigner did not require layout alignment report before model generation. | 5x3 v0.1 became superseded and caused extra correction
sprint. | Require layout alignment before writing selected model. | MathModelDesigner | patched |
| LG-PILOT-006 | MathQualityGate | Simulator payout scaling appeared in v0.1. | Simulator trust audit was not a mandatory first-class gate. | RTP appeared closer than true emergent validation supported. | Require
scaling/post-normalization/forced-RTP audit. | MathModelDesigner | patched |
| LG-PILOT-007 | ProtocolAudit | Gamesv1/Crazy Rooster/slot-browser-v1 was over-trusted. | Prior-agent direction was treated too close to source truth. | Registration/runtime/RNG assumptions needed correction. | Require current-GS
lane/registration/RNG/math ownership audit before builder/registrar. | ProtocolAndSchemaMapper | patched |
| LG-PILOT-008 | MantisScopeCorrection | ExtGame/Mantis information was over-framed. | Advisory collaboration notes were not clearly separated from selected architecture. | Risk of selecting wrong runtime lane. | Require advisory-only label
unless current GS source proves lane. | ProtocolAndSchemaMapper | patched |
| LG-PILOT-009 | CurrentGSAudit | Registration/RNG/math ownership audit was needed earlier. | Pipeline allowed downstream planning before ownership was documented. | GameServerRegistrar and builder remained blocked. | Add required early
audit questions and evidence labels. | ProtocolAndSchemaMapper, GameServerRegistrar | patched |
| LG-PILOT-010 | MathModelDesignerV03 | Complex donor features required v0.3 result contract before builder. | Earlier package did not expose full cascade/golden/rainbow/coin/state fields. | Scene maps and builder readiness lagged. |
Require v0.3-style result contract for complex donor parity. | MathModelDesigner | patched |
| LG-PILOT-011 | ArtSceneMapperV03 | Scene maps needed update after result schema changed. | Pipeline did not automatically gate scene maps on schema changes. | Animation/object mapping drifted from math contract. | Require scene-map update
whenever result schema changes. | ArtSceneMapper | patched |
| LG-PILOT-012 | V03ContractConsistencyAudit | Field drift appeared between math schema and art maps. | No mandatory contract consistency audit before builder planning. | Potential implementation mismatch. | Require Math/Art/Runtime
Contract Consistency Audit with zero unresolved mismatches. | ArtSceneMapper, GameClientBuilder | patched |
| LG-PILOT-013 | PublicGitExport | Public export needed stronger sanitizer/gitignore rules. | Validator initially depended on narrower patterns and .gitignore was over-redacted. | Public review risk and confusing export metadata. |
Strengthen validator and use folder ignore patterns. | PublicGitExport, SprintReporter | patched |
| LG-PILOT-014 | All Sprints | External reviewer reports were essential for continuity. | Long multi-sprint work needs durable copy-paste review packs. | Without reports, corrective sprints lose evidence context. | SprintReporter after
every sprint, with exact files/validations/blockers/next prompt. | SprintReporter | patched |
