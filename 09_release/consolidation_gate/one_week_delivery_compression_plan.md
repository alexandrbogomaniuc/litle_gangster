# One-Week Delivery Compression Plan

Status: future-process plan.

Goal: turn the Little Gangster pilot into a reusable delivery path without skipping hard gates.

## What Is Now Reusable

- Project manifest and gate structure.
- Donor feature/settings parity matrix pattern.
- Asset quarantine and release-blocking policy.
- `presentationPayload.gamePayload` schema extension.
- Strict fixture format and validation script pattern.
- Authoritative server math design template.
- Runtime adapter planning template.
- Public export checkpoint policy.

## What Can Be Automated

- Handoff and manifest gate checks.
- Required file presence checks.
- JSON schema parsing.
- GL/template/RTP matrix generation from a profile file.
- Strict fixture validation.
- SprintReporter report skeleton.
- Public raw validation during checkpoint sprint.

## What Still Needs Manual Approval

- Donor/reference access and asset capture.
- Final art release approval.
- Exact math/RTP/bonus-buy EV signoff.
- Jackpot product decision.
- Backend adapter source modification.
- GameServerRegistrar artifact generation.
- DB/Cassandra apply.
- Wallet endpoint testing.
- Release approval.

## What Cannot Be Skipped

- Runtime owner proof.
- Result API contract proof.
- Registration lane and serializer proof.
- Math simulation/certification evidence.
- VABS/Lasthands/history replay proof.
- Wallet/accounting boundary proof.
- Post-push raw validation for public export.

## Checkpoint Git Timing

- Run checkpoint review/push every 3-4 local sprints or at major external-review checkpoints.
- Do not push in every sprint.
- When pushing, validate working tree, git blob, pushed raw files, and fresh clone/raw state.

## Avoiding Public Export Validation Problems

- Treat pushed raw files as source of truth.
- Do not rely only on agent line counts or local reports.
- Include raw validation output in checkpoint sprint report.
- Keep GitHub Actions workflow deferred unless auth scope supports it.

## Proposed One-Week Plan

| Day | Work | Gate |
| --- | --- | --- |
| Day 0 | Confirm roots, product decisions, secrets policy, target lane, checkpoint status. | Project and safety gate |
| Day 1 | Donor/reference feature parity and asset inventory if needed. | Feature and asset gate |
| Day 2 | Protocol lane, math config, RTP models, and authoritative state contract. | Runtime/math gate |
| Day 3 | Strict fixtures, schema validation, and scene mapping. | Contract consistency gate |
| Day 4 | Backend adapter apply only if approved; otherwise stay planning. | Source modification gate |
| Day 5 | Client prototype or implementation only if runtime/result/assets are proven; GameServerRegistrar generate-only only if registration lane/serializer proven. | Build/registration gate |
| Buffer | Wallet/history/reconnect tests, simulation reports, release audit, checkpoint push. | QA/release gate |

Compression conclusion:

- The pilot can be shortened, but not by jumping to implementation.
- The next implementation-adjacent sprint should occur only after simulation/config and history gaps are closed.

