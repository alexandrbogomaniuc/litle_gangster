# Checkpoint Push Policy

Status: active fast-lane policy.

## Timing

- Run checkpoint git review/push every 3-4 meaningful local sprints or at a major phase boundary.
- Do not push every sprint.
- Do not combine checkpoint push with implementation unless explicitly approved.

## Required Checks

1. Inspect local changed files.
2. Confirm no forbidden assets, raw secrets, raw donor URLs, HAR, raw logs, private links, or wallet credentials are included.
3. Confirm gates remain accurate.
4. Commit intentionally.
5. Push only if the user approves.
6. Validate pushed raw files or fresh clone state before claiming success.

## Current Status

Checkpoint review/push is due soon. It was not run in this sprint.

