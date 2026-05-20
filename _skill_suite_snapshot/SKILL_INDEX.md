# Skill Index Snapshot

This is a public-safe, line-wrapped snapshot of the reusable iGaming skill order.

## Future Donor Project Workflow Order

- 00 WorkflowOrchestrator: route and gatekeep the next safe skill.
- 01 ProjectCreator: create the project workspace and manifest.
- 02 AuthorizedReferenceResearcher: observe authorized donor/reference gameplay.
- 03 ReferenceAssetInventory: inventory and quarantine authorized reference assets.
- 04 ProtocolAndSchemaMapper: map launch, wallet, runtime, and config contracts.
- 05 MathModelDesigner: design and validate internal math packages.
- 06 MathProfileCalibrator: calibrate RTP/volatility profile matrices.
- 07 ParallelMathValidator: coordinate large-scale validation evidence.
- 08 ArtSceneMapper: map scenes, object ids, layers, and inspector data.
- 09 ArtDirectionAndReplacementPlanner: plan original replacement art.
- 10 ContractConsistencyAudit: compare math, art, object maps, and runtime boundaries.
- 10A VisualPrototypeSandboxBuilder: create and validate a local non-production visual
  sandbox using quarantined donor/reference placeholders and scripted visual outcomes
  while keeping production client, registration, wallet, DB, and release gates blocked.
- 11 GameClientBuilder planning/runtime API review: review client consumption plans.
- 12 GameClientBuilder implementation: build client only after all gates pass.
- 13 GameServerRegistrar: generate safe registration/config artifacts only after proof.
- 14 WalletAndLaunchTester: test launch, wallet, history, and runtime flows safely.
- 15 RTPAndReleaseAuditor: audit final release gates.
- 16 SprintReporter: generate the sprint report.
- 17 Sanitized public/private export: create review-safe exports when needed.

VisualPrototypeSandboxBuilder must not generate production client code, run
GameClientBuilder implementation, generate registration, call endpoints, public-export
donor/reference assets, approve donor production assets, approve release, or claim
certification.
