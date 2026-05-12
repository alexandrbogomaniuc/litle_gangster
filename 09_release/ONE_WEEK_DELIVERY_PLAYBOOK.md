# One Week Delivery Playbook

## Goal

Future donor-based projects should stop rediscovering Little Gangster pilot rules. A one-week delivery is realistic only when runtime, registration, result ownership, asset, validation, and reporting gates are already encoded.

## Day 0: Prework

- Runtime lane selected or known blockers listed.
- Registration template and rollback model available.
- Public/private export validator available.
- Math simulator and trust policy available.
- Asset replacement policy available.
- WorkflowOrchestrator available.

## Day 1: Project And Donor Capture

- Run ProjectCreator.
- Run AuthorizedReferenceResearcher for donor feature/settings parity.
- Run ReferenceAssetInventory only when authorized scaffold capture is selected.
- Stop if donor mode, settings, capture authorization, or secret references are unclear.

## Day 2: Math And Scene Contracts

- Run ProtocolAndSchemaMapper if runtime lane is not already locked.
- Run MathModelDesigner with layout alignment and simulator trust audit.
- Run ArtSceneMapper when the math result schema changes.
- Stop if payout scaling, browser result authority, or unresolved feature parity appears.

## Day 3: Builder Planning

- Run ContractConsistencyAudit.
- Run GameClientBuilder planning/runtime API review only.
- Do not implement client code until implementation gates pass.

## Day 4: Client And Registration

- Run GameClientBuilder implementation only after runtime owner, result API, asset strategy, and explicit approval are true.
- Run GameServerRegistrar generate-only only after registration lane, serializer, game ID, bank/source, and rollback gates pass.

## Day 5: QA And Release Audit

- Run WalletAndLaunchTester only with safe test environment and secret references.
- Run RTPAndReleaseAuditor only after all prior gates pass.
- Do not approve release with unresolved runtime, wallet, asset, math, or validation blockers.

## Buffer Days

- Retest fixes.
- Re-run deterministic validators.
- Run public/private export only at major checkpoints or when external review is needed.

## Required Stop Rules

- Any validator failure stops the sprint.
- Any missing gate blocks implementation.
- Any public export push must be followed by fresh post-push clone validation.
