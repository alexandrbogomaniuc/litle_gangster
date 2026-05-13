# Public Export Collapse Root Cause

root_cause_status: not_proven

## Questions

1. Which step collapsed the files?
   - Not proven from the allowed roots. The current public export working tree does not contain an active, obvious newline-collapse writer for the target files.

2. Was it the sanitizer?
   - Not proven. The current `scripts/validate_public_export.py` validates and scans; it does not rewrite files.

3. Was it the export copy step?
   - Not proven. No current export-copy script in the allowed inspection set was found rewriting the target files with newline collapse.

4. Was it a Markdown wrapping step?
   - Not proven. Prior emergency fixes used wrapping logic, but no current committed path was found that calls `" ".join(text.split())` or directly replaces all newlines with spaces for the target files.

5. Was it a post-validation rewrite?
   - Not proven. The failure pattern is consistent with a post-validation rewrite or a mismatch between validated local state and published raw state, but this sprint did not prove the exact writer.

6. Was the validator run before or after the collapse?
   - The prior report cannot be trusted. This sprint treats the previous validation claim as false because public GitHub raw review contradicted it.

7. Why did fresh clone validation claim pass while GitHub raw failed?
   - Not proven. The emergency fix removes reliance on agent reports by adding committed-blob and GitHub-raw validators. Future success cannot be claimed unless the pushed raw GitHub files pass directly.

8. What exact fix was applied?
   - Public metadata and validator files were manually rewritten as multiline files.
   - `scripts/validate_public_export.py` now enforces physical line counts and key Markdown line lengths.
   - `scripts/validate_git_blob_content.py` checks `git show HEAD:<path>` blobs.
   - `scripts/validate_github_raw_commit.py` checks raw GitHub files for a specific commit.
   - `.github/workflows/public-export-validation.yml` was created locally to run validation on push and pull request.

## Blocker

The public push failed because existing GitHub authentication lacks `workflow` scope for creating/updating `.github/workflows/public-export-validation.yml`. Therefore the emergency fix is committed locally but is not pushed to public
`main`, and public validation is not claimed as passed.
