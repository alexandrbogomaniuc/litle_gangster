# Next Checkpoint Git Review Plan

Status: due soon, not run in this sprint.

Decision:

- Several local sprints have completed since the last public-export repair work.
- A checkpoint review/push sprint is due soon.
- Do not push in this sprint.
- The next or following sprint should run checkpoint push only if the user explicitly approves it.

Required checkpoint validation:

1. Inspect local changed files.
2. Confirm no forbidden assets, raw secrets, raw donor URLs, screenshots, HAR, raw logs, or private links are exported.
3. Commit only reviewed artifacts.
4. Push only with existing auth.
5. Validate pushed GitHub raw files for critical docs and validators.
6. Do not claim validation passed unless pushed raw validation passes.

Public export needed now: no.

Reason:

- This sprint is a local consolidation gate.
- Public export should be reserved for external review or major checkpoint.

