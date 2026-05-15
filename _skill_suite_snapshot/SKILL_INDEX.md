# Skill Index

## Future Donor Project Workflow Order

| Order | Skill / Gate | Does | Must not do | Required previous output | Next skill / gate | Parallel? | Core refs |
|---|---|---|---|---|---|---|---|
| 00 | WorkflowOrchestrator | Reads manifest, handoffs, blockers, and gate status; decides the next safe skill; refuses unsafe jumps; produces an
exact next prompt. | No implementation, donor browsing, asset capture, DB/wallet calls, registration generation, release approval, or inferred
approval. | Existing project state or new-project request. | Next allowed skill | No |
`.agents/skills/WorkflowOrchestrator/references/WORKFLOW_GATES.md` |
| 01 | ProjectCreator | Creates project workspace, manifest, decisions, assumptions, local rules, initial blockers, and review/export intent. Asks
donor parity, capture mode, GS roots, game ID, RTP, volatility, layout, and secret-reference questions. | No browser, donor investigation, asset
capture, math, build, or DB/Cassandra execution. | User inputs and suite references. | AuthorizedReferenceResearcher | No |
`project_manifest.schema.json`, `MASTER_WORKFLOW_CONTRACT.md`, `references/FUTURE_PROJECT_FAST_START_CHECKLIST.md` |
| 02 | AuthorizedReferenceResearcher | Observes authorized donor/reference gameplay and creates donor feature/settings parity matrix with evidence. |
No access bypass, raw secrets, full donor URL persistence, asset copying unless authorized mode allows, or 100% coverage claims without direct
evidence. | Project manifest and authorization mode. | ReferenceAssetInventory | No | `references/DONOR_FEATURE_SETTINGS_PARITY_POLICY.md` |
| 03 | ReferenceAssetInventory | Captures/inventories/hashes/classifies authorized scaffold assets and maps gaps. | No release approval for
donor/scaffold assets; no movement into resulting code. | Reference research outputs and capture authorization. | ProtocolAndSchemaMapper | Can run
after research evidence exists. | `references/PUBLIC_EXPORT_SANITIZATION_RULES.md` |
| 04 | ProtocolAndSchemaMapper | Audits current GS lane, registration process, math import boundary, RNG/result ownership, wallet/runtime layers, and
advisory checklists. | No donor investigation, guessed architecture, selected-lane claims from prior-agent/advisory notes, raw external-collaboration
text persistence, or DB changes. | Manifest, docs, explicit source roots if available. | MathModelDesigner | Yes after ProjectCreator; should precede
builder/registrar. | `references/CURRENT_GS_REGISTRATION_RNG_AUDIT_POLICY.md`, `references/MANTIS_EXTERNAL_COLLABORATION_CHECKLIST.md` |
| 05 | MathModelDesigner | Performs layout alignment, simulator trust audit, initial math package design, 3x3 RTP/volatility framework, and
backend-oriented result contract. | No endless calibration loops, no math from screenshots alone, no release RTP claims from scaled simulators, no
browser RNG authority, no registration math-import assumption. | Donor parity, protocol audit, math targets. | MathProfileCalibrator when profile
calibration is needed; otherwise ArtSceneMapper | Yes after protocol facts known. | `references/MATH_SIMULATOR_TRUST_POLICY.md` |
| 06 | MathProfileCalibrator | Validates requested LOW/MEDIUM/HIGH RTP values, calibrates the 3x3 RTP/volatility profile matrix with train-only
overlay loops, runs/imports validation evidence, and reports tail/bonus-buy blockers. | No backend/client/registration implementation, no
validation-seed tuning, no post-spin payout scaling, no DB/wallet/donor/release actions, no certification claim from smoke or fast-train evidence. |
Initial math package, 3x3 profile matrix, simulator/local or external runner. | ArtSceneMapper or blocker-specific math sprint | No |
`.agents/skills/MathProfileCalibrator/references/RTP_REQUEST_VALIDATION.md` |
| 07 | ParallelMathValidator | Coordinates local/server/subagent/parallel-thread math validation at larger scale; validates/imports train, validation,
tail, bonus-buy, FRB/promo, confidence, registration math fields, and certification evidence packages. | No active config changes, validation-seed
tuning, backend/client/registration/release actions, DB/wallet calls, donor browsing, asset capture, or certification claims. | Initial math package
or calibrated profile matrix plus declared simulation scope. | Main workflow may continue; downstream implementation/registration/release gates
consume evidence when needed. | Yes | `.agents/skills/ParallelMathValidator/SKILL.md` |
| 08 | ArtSceneMapper | Maps scenes, object IDs, layers, result-state mappings, scaffold previews, and inspector metadata. | No donor asset approval,
no unsupported client assumptions, no outcome-authority claims. | Math/result contract, asset inventory, reference evidence. |
ArtDirectionAndReplacementPlanner | Yes after asset inventory and result contract. | `references/CONTRACT_CONSISTENCY_AUDIT_POLICY.md` |
| 09 | ArtDirectionAndReplacementPlanner | Creates original art direction and replacement plan while preserving donor feature/settings parity when
required. | No scaffold/unknown asset release, silent donor reuse, or removal of donor-required parity. | Asset inventory and scene maps. |
ContractConsistencyAudit | No | `references/DONOR_FEATURE_SETTINGS_PARITY_POLICY.md` |
| 10 | ContractConsistencyAudit | Compares math result schema, art scene maps, object maps, handoffs, and runtime boundaries before builder planning.
| No feature redesign, payout logic changes, client implementation, or runtime ownership decisions. | Math and art scene contracts. |
GameClientBuilder planning | No | `references/CONTRACT_CONSISTENCY_AUDIT_POLICY.md` |
| 11 | GameClientBuilder planning/runtime API review | Reviews runtime result API contract and client consumption plan. | No client build
implementation, browser-authoritative outcomes, or runtime code generation. | Zero unresolved contract mismatches or explicit blockers. |
GameClientBuilder implementation | No | `references/REQUIRED_PIPELINE_GATES.md` |
| 12 | GameClientBuilder implementation | Builds client only after planning approval, runtime owner/API proof, and asset approval. | No generic stack
migration, donor asset release, DB changes, or unproven runtime assumptions. | Approved planning review, approved assets, proven runtime contract. |
GameServerRegistrar | No | `references/CLIENT_BUILD_AND_ARCHITECTURE_SUMMARY.md` |
| 13 | GameServerRegistrar | Generates safe registration/config and rollback artifacts. | No production DB apply, no Cassandra execution by default,
no guessed scn/jcn serializer, no math-import assumption. | Client/runtime contract, protocol audit, manifest, and ParallelMathValidator evidence when
registration math fields depend on simulations. | WalletAndLaunchTester | No | `references/CASSANDRA_REGISTRATION_SUMMARY.md` |
| 14 | WalletAndLaunchTester | Tests launch, wallet, history/reconnect, VABS/Lasthands, and runtime API flows with safe fixtures/endpoints. | No
production wallet calls, raw secret logging, fake pass results, or hardcoded paths without proof. | Protocol contract, registration artifacts, secret
references. | RTPAndReleaseAuditor | No | `references/BSG_COMMON_WALLET_SUMMARY.md` |
| 15 | RTPAndReleaseAuditor | Audits final release gates, including ParallelMathValidator evidence when present. | No code creation, DB changes, or
approval with unresolved blockers. | All prior reports. | SprintReporter | No | `references/REQUIRED_PIPELINE_GATES.md` |
| 16 | SprintReporter | Generates copy-paste external review report after every sprint. | No hiding blockers, vague done reports, raw secrets, or
unexplained changes. | Current project context and latest reports. | User/reviewer | Yes | `references/SPRINT_REPORTING_STANDARD.md` |
| 17 | Sanitized public/private export | Creates review-safe export when needed. | No donor assets, screenshots, HAR, logs, secrets, tokenized URLs,
private links, or local private paths. | Latest sprint outputs and validator. | User/reviewer | No | `references/PUBLIC_EXPORT_SANITIZATION_RULES.md`
|
