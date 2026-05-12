# Fast-Lane Operating Mode

Status: active operating policy.

Purpose: keep Little Gangster and future donor-to-release projects moving quickly without weakening safety gates.

## Rules

1. One sprint has one primary purpose.
2. Normal planning sprint target: 2-4 minutes.
3. Heavy sprints are allowed only for implementation patches, simulation runs, checkpoint pushes, or release gates.
4. A normal planning sprint may create at most 10 files and modify at most 5 files unless the user explicitly expands scope.
5. SprintReporter uses compact mode by default.
6. Full external-review reports are reserved for checkpoint pushes, source patches, release gates, blockers, or explicit user request.
7. Subagents are optional and used only when the main agent decides they reduce time or improve reliability.
8. Subagents never write files or make source changes.
9. Do not re-read full project history unless the task requires it.
10. Prefer `handoff.json`, `project_manifest.json`, and consolidation gate docs as source of truth.
11. Run checkpoint git review/push every 3-4 meaningful local sprints or major phase boundary.
12. Do not push every sprint.
13. Never start implementation unless the gate says implementation is allowed and the user explicitly approves.
14. If validation contradicts a report, stop and fix validation before continuing.
15. If a sprint expands beyond scope, stop and record a blocker instead of doing extra work.

## Default Source Set

For routing decisions, read only:

- `project_manifest.json`
- nearest `AGENTS.md`
- relevant `00_skill_reports/*/handoff.json`
- current consolidation gate docs
- current skill docs

Broader source inspection requires an implementation, patch, release, or explicit audit sprint.

