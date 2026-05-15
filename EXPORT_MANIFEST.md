# Export Manifest

## Export Type

Raw-safe sanitized public review checkpoint.

## Checkpoint Theme

ParallelMathValidator workflow skill creation and Little Gangster lifecycle
wrapper planning.

## Included Groups

- Public metadata files.
- Public-safe project status files.
- ParallelMathValidator skill snapshot.
- ParallelMathValidator references and scripts.
- Skill-suite routing snapshots.
- ParallelMathValidator project adoption and playbook docs.
- Lifecycle wrapper planning docs.
- Lifecycle source-planning docs, curated to remove private local paths.
- Lifecycle planning skill reports.
- ParallelMathValidator skill creation reports.

## Curation Notes

Project documents copied into this export are public-safe copies. Absolute local
paths are replaced with relative or placeholder notation. Donor host references
are removed. Tokenized URLs, private URLs, raw secrets, SIDs, signatures, emails,
and passwords are not included.

Skill snapshots are preserved as review snapshots where possible. If a snapshot
contains a long Markdown line, it may be wrapped for raw-safe validation. If a
snapshot contains unsafe private content, it is curated before export.

## Explicit Exclusions

- Donor and scaffold asset bodies.
- Screenshots, HAR files, videos, browser captures, and raw logs.
- Staging source files.
- Backend adapter source code from Staging.
- Lifecycle wrapper implementation code.
- Production client code.
- Gamesv1/games/8001.
- Registration artifacts.
- DB/Cassandra apply files.
- Wallet endpoint data.
- Release approval or certification claim.

## Blocked Gates

- GameClientBuilder remains blocked.
- GameServerRegistrar generation remains blocked.
- WalletAndLaunchTester remains blocked.
- RTPAndReleaseAuditor release approval remains blocked.
- Release remains blocked.
