# Schema Patch Approval Gate

Status: APPROVAL_REQUIRED_SOURCE_PATCH_NOT_APPLIED

## Gate Decision

Source patch has not been applied yet.

Approval is required before modifying any file under `[STAGING_ROOT]`.

## Required Before Patch Apply

- User explicitly approves Staging source modification.
- Patch scope is limited to the approved files.
- Rollback plan is accepted.
- Test plan is accepted.
- No backend adapter implementation is included unless separately approved.
- No GameClientBuilder implementation is included.

## Required Tests Before Patch Is Accepted

- Browser runtime contract tests.
- Presentation mapper tests.
- Gamesv1 contract/template tests where available.
- 7001 compatibility check.
- new-games-server build/test only after server patch approval.

## Rollback Requirement

Patch groups must be revertible separately: canonical JSON schemas, Zod/type helpers, UI-kit mapper, new-games-server emission, and future 8001 adapter.

## Implementation Status

Backend adapter implementation remains blocked.
Full GameClientBuilder implementation remains blocked.
Client build, registration, wallet tests, final assets, and release approvals remain false.
