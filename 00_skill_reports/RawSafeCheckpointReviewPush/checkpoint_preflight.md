# Raw-Safe Checkpoint Review/Push Preflight

Created: 2026-05-13

## Checkpoint Due

Checkpoint is due: yes.

Checkpoint is due because multiple meaningful local sprints have completed since the last raw-safe checkpoint, including RTP/volatility profile framework work, volatility profile simulation design, and 3x3 calibration harness/results.
External review needs to inspect committed public artifacts rather than local-only reports.

## Recent Sprints Included

- Fast-lane workflow updates.
- MathModelDesigner calibration fast-lane workflow update.
- RTP/volatility profile framework generalization.
- 9-profile RTP x volatility matrix.
- Volatility profile simulation design.
- 3x3 profile calibration harness and first-pass tuning.
- Model-completeness simulator updates.
- Limited and second-pass calibration outputs.
- Authoritative simulation/config refinement package.
- Current MathModelDesigner handoff.
- Current WorkflowOrchestrator handoff.
- Current SprintReporter latest report.

## Export Method

- Use the raw-safe public export repository only.
- Use line-preserving copy for selected safe text/code files.
- Use redaction validation without whitespace collapse.
- Do not use the old public export pipeline.
- Do not minify Markdown or Python.

## Unsafe Exclusions

- Donor asset bodies.
- Scaffold asset bodies.
- Screenshots.
- HAR files.
- Event logs and raw network logs.
- Playwright folders.
- npm caches and `node_modules`.
- Raw secrets, raw tokens, SIDs, signatures, private links, emails, full donor URLs, tokenized URLs.
- Local browser profiles.
- Media/binary donor files.
- Build artifacts and `dist` folders.
- Unapproved release assets.

## Gate State

- Backend adapter implementation remains false.
- GameClientBuilder implementation remains false.
- GameServerRegistrar generation remains false.
- Wallet/API work remains false.
- DB/Cassandra work remains false.
- Release approval remains false.

