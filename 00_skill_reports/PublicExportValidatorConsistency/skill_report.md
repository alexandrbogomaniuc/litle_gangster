# Public Export Validator Consistency Skill Report

Sprint: Runtime API Inspection preflight  
Date: 2026-05-11

## Summary

The public export working copy and its committed HEAD were inspected before runtime API inspection. The public README and reviewer guide are multiline and readable in the local export at commit `c4af8bc6b4e18fc39cb11b09ee418696f142624d`.

## Findings

|File|Working tree non-empty lines|Working tree longest line|HEAD non-empty lines|HEAD longest line|
|---|---:|---:|---:|---:|
|`README.md`|18|90|18|90|
|`REVIEWER_START_HERE.md`|28|116|28|116|

`PUBLIC_EXPORT_NOTICE.md` has 8 non-empty lines and longest line length 90. `EXPORT_MANIFEST.md` has 43 non-empty lines and longest line length 84.

## Validator Enforcement

`scripts/validate_public_export.py` enforces:

- `README.md` has at least 8 non-empty lines.
- `REVIEWER_START_HERE.md` has at least 8 non-empty lines.
- Markdown lines must not exceed 500 characters outside code blocks.
- Latest workflow checkpoint text must be present.
- Next-step text must be present.
- No-client-code statement must be present.

## Validation Run

`python3 scripts/validate_public_export.py` was run against the public export working tree before runtime API inspection and passed.

## Why The Prior Sprint Could Report Pass While Reviewer Saw Collapsed Markdown

The local export working tree and local committed HEAD both contain multiline readable Markdown. The most likely explanation is that the reviewer saw a stale/cached GitHub view, a different branch/commit, or a rendered wrapping/display
artifact rather than the local `main` HEAD content inspected here. No local evidence was found that the current README or reviewer guide are collapsed.

## Corrective Action

- The preflight is now documented in project reports.
- The validator was confirmed to enforce line-count and line-length checks.
- The validator was run before continuing this sprint.
- Public metadata will be updated again after runtime API inspection and revalidated before any push.

