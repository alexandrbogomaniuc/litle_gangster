# Little Gangster Raw-Safe Review Checkpoint

This repository is a raw-safe sanitized review checkpoint for the Little Gangster
8001 workflow and reusable game-development skill suite.

It is not a release build. Release remains blocked.

Safety posture:

- No donor/scaffold asset bodies are included.
- No screenshots, HAR files, raw logs, or captured media are included.
- No raw secrets, full donor URLs, tokenized URLs, SIDs, signatures, passwords,
  or private local paths are included.
- No Staging source code is included.
- Public copies are curated for review while preserving meaningful workflow and
  planning content.

Current status:

- runtime API inspection completed earlier and is represented by available
  inspection and gap documents in `03_protocol/`.
- Backend adapter payload mapper was applied in Staging, but source code is not
  exported here.
- Lifecycle wrapper was applied in Staging, but source code is not exported here.
- VABS visual history route was applied in Staging, but source code is not
  exported here.
- VABS legacy alias was applied in Staging, but source code is not exported here.
- GS/wallet responsibility boundary was corrected in project planning docs.
- No production client implementation was generated.
- Non-production fixture/prototype work is documented separately where present.
- GameClientBuilder implementation remains blocked.
- GameServerRegistrar generation remains blocked.
- Wallet, launch, and history tests are still missing.
- Certification false.
- release blocked.

Reusable workflow checkpoint:

- ParallelMathValidator was added to support parallel math validation evidence.
- WalletAndLaunchTester guidance now requires responsibility-boundary clarity
  before real endpoint tests.
- GameServerRegistrar guidance requires unresolved wallet/config and math fields
  to block generation.
- RTPAndReleaseAuditor guidance checks math, VABS/Lasthands, wallet/launch, and
  release evidence before approval.

Start with `REVIEWER_START_HERE.md`, then inspect `EXPORT_MANIFEST.md` and
`09_release/WORKFLOW_CONTENT_INTEGRITY_AUDIT.md`.
