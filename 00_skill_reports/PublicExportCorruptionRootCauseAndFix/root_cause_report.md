# Public Export Corruption Root Cause Report

Sprint: PublicExportCorruptionRootCauseAndFix

## External Contradiction Recorded

The checkpoint commit `ca854797d2d67def46f17dd989164b71ce49cc44` was reported externally as corrupted on GitHub raw:

- `README.md`: 3 physical raw lines.
- `REVIEWER_START_HERE.md`: 4 physical raw lines.
- `scripts/validate_public_export.py`: 1 physical raw line.
- `_skill_suite_snapshot/WorkflowOrchestrator/SKILL.md`: 7 physical raw lines.

The prior checkpoint report claimed much higher line counts and therefore must be treated as contradicted. The prior `public_export_validation_passed` and `github_raw_validation_passed` claims are invalid until a project-local validator
outside the public export validates GitHub raw content.

## Root Cause Status

`root_cause_status: not_proven`

The exact newline-collapse mechanism was not proven from the current local files inspected inside the allowed roots. Current local working-tree files and local git blobs for the same commit are multiline, and a fresh GitHub raw fetch during
this sprint returned multiline content. That makes the collapse mechanism non-reproducible from the present checkout state.

## Questions

1. Which script or step collapsed files?

Not proven. No currently inspected export validator or project-local public export validator contains a direct newline-collapsing operation such as `" ".join(text.split())` or `replace("\n", " ")` in the active validation scripts.

2. Was it a sanitizer?

Not proven. A sanitizer remains a candidate class of failure, but no active sanitizer was proven to have collapsed newlines.

3. Was it a Markdown wrapper?

Not proven. No inspected current Markdown wrapper was proven to collapse files.

4. Was it a report sanitizer?

Not proven. The observed failure could be consistent with report/export post-processing, but no specific report sanitizer was proven.

5. Was it a public export copy step?

Not proven. The public export copy step is still the most relevant failure boundary because the corrupted files were public-export artifacts, but the current local copy output is multiline.

6. Was validation run before collapse?

Likely yes, or validation was run against a different artifact than GitHub raw. The prior checkpoint claim cannot be trusted because the final pushed raw content was not independently validated by a project-local validator outside the
public export.

7. Why did local validation report false success?

The proven process failure is validation trust-boundary collapse. The exported validator was treated as a trusted source of truth even though, if exported as a single physical line beginning with `#`, Python can compile and run it as a
comment-only no-op. A validator stored only inside the artifact it validates cannot prove the pushed artifact is sound after export, commit, and GitHub raw publication.

8. What exact fix is applied?

This sprint applies a process and tooling fix:

- add a project-local GitHub raw validator outside the public export,
- rebuild the public export using newline-preserving copy/redaction,
- keep internal public-export validation for working-tree checks only,
- validate staged/committed git blobs with line counts,
- validate the pushed commit through the project-local raw validator,
- set public export success only if GitHub raw validation passes.

## Safety Result

Until the new external raw validator passes against the pushed replacement commit:

- `public_export_validation_passed=false`
- `github_raw_validation_passed=false`
- `checkpoint_git_review_status=invalidated_by_external_raw_contradiction`
