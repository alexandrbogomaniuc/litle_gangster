# Golden Workflow

## Fixed Order

1. ProjectCreator.
2. AuthorizedReferenceResearcher.
3. ReferenceAssetInventory.
4. ProtocolAndSchemaMapper.
5. MathModelDesigner.
6. ArtSceneMapper.
7. ArtDirectionAndReplacementPlanner.
8. ContractConsistencyAudit.
9. GameClientBuilder planning/runtime API review.
10. GameClientBuilder implementation.
11. GameServerRegistrar generate-only.
12. WalletAndLaunchTester.
13. RTPAndReleaseAuditor.
14. SprintReporter.
15. Sanitized public/private export when needed.

## Hard Gates

- Planning allowed is not implementation allowed.
- Implementation skills must read `project_manifest.json` and all relevant `handoff.json` files.
- Runtime owner and result API must be proven before client implementation.
- Registration lane and serializer must be proven before registration generation.
- Wallet testing requires a safe test environment and secret references.
- Release audit requires all prior gates and validators to pass.

## Public Export Rule

Public export validation requires local validation, commit, push, and fresh post-push clone validation. Without the clone validation, the sprint may report local validation only.

## Fast-Lane Rule

Future projects may move quickly only when the reusable playbook already contains:

- Known runtime lane.
- Registration template.
- RNG/result owner policy.
- Asset exclusion policy.
- Math simulator trust policy.
- Contract consistency validator.
- Public export validation and post-push clone check.
