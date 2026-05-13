# Validation Trust Hardening

## Purpose

This document records the validation-trust correction from the Little Gangster pilot. Agent-written reports are no longer enough to prove public export safety or reviewability. A public validation claim must be backed by deterministic
scripts and a post-push validation of the pushed repository state.

## Confirmed Failure Mode

An external reviewer reported that the public GitHub commit appeared to contain collapsed files even after the agent reported a successful formatting fix:

- `README.md` appeared as only a few raw lines.
- `REVIEWER_START_HERE.md` appeared as only a few raw lines.
- `scripts/validate_public_export.py` appeared effectively collapsed.

That contradiction is treated as a validation-trust failure even if the local working tree later appears correct.

## Required Public Export Validation Chain

Public export validation may be reported as passed only when all of these succeed:

1. Local public export validator runs before commit.
2. Commit is created.
3. Local public export validator runs after commit.
4. Push succeeds.
5. A fresh post-push clone or fresh checkout of the pushed commit validates successfully.
6. The exact pushed commit hash is recorded.

If step 5 is skipped or fails, the report must say `public_export_validation_passed=false` and must record `post_push_clone_validation_not_run` or the exact post-push failure.

## Validator Requirements

The public export validator must fail when:

- `README.md` has fewer than 12 non-empty lines.
- `REVIEWER_START_HERE.md` has fewer than 12 non-empty lines.
- `scripts/validate_public_export.py` has fewer than 50 lines.
- Any Markdown line exceeds 300 characters outside code blocks.
- Any Python script appears collapsed or minified.
- Media or binary files are present.
- Donor/scaffold asset folders are present.
- Screenshots, HAR, videos, or event logs are present.
- Tokenized URLs, raw secrets, SIDs, signatures, private links, emails, or local private paths are present.
- `06_resulting_code` contains implementation files before approval.

## Truthfulness Checks

Sprint reports must be cross-checked against actual files and git state. A truthfulness validator must flag contradictions such as:

- Reported line counts do not match public files.
- Report says code was not generated while `package.json`, `src`, `public`, `dist`, or `build` exists.
- Report says assets were not copied while media files or reference asset bodies exist.
- Reported commit hash does not match the working tree or pushed clone.

## Current Result

This sprint creates project-owned validators and a post-push clone validation step. Future public export reports must cite the post-push clone validation result before claiming public validation passed.
