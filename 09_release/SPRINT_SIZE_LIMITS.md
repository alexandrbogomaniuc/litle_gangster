# Sprint Size Limits

Status: active fast-lane limits.

## Normal Planning Sprint

- Maximum created files: 10.
- Maximum modified files: 5.
- Maximum skill report folders: 1.
- Report format: compact.
- Broad source inspection: no.
- Staging/source inspection: only if explicitly requested.

## Implementation Sprint

- File count follows the approved patch plan.
- Must include preflight, patch, tests, rollback notes, and gate update.
- Full report is allowed.
- Source changes require explicit user approval.

## Checkpoint Sprint

- Purpose: local/public git validation and optional push.
- Full report required.
- Pushed artifact/raw validation required if pushing.
- Do not combine checkpoint push with implementation work.

## Simulation Sprint

- May exceed normal file limits when simulations or generated reports require it.
- Output summarized reports only.
- Exact values remain non-final unless certified evidence exists.

## Compact Report Size

- Target: under 120 lines.
- Include: sprint identity, goal, subagents used yes/no and why, files created, files modified, validations, blockers, gate changes, next prompt.
- Suppress long source-doc lists unless source patch, checkpoint push, release gate, blocker, or explicit user request.

