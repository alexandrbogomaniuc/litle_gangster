# Future Game VABS Evidence Policy Gate

Generated: 2026-05-15

## Reusable Rule

Every future game must choose a `historyEvidenceMode`, `historyCaptureScope`, and
`historyMediaStoragePolicy` before release.

## Required Gate Outcomes

- deterministic replay payload required: yes;
- visual VABS route required: yes, unless current GS/backoffice evidence proves otherwise;
- screenshot mode policy selected or disabled;
- video mode policy selected or disabled;
- retention policy selected;
- checksum policy selected;
- encryption policy selected;
- PII redaction policy selected;
- storage provider selected or explicitly blocked;
- GameClientBuilder history behavior aligned with the policy;
- GameServerRegistrar config/settings impact recorded;
- WalletAndLaunchTester includes route and evidence-mode tests;
- RTPAndReleaseAuditor blocks release if evidence gates are unresolved.

## Default

Default `historyEvidenceMode` is `deterministic_replay_only`.

That default disables media capture. It does not remove the visual VABS route
requirement.
