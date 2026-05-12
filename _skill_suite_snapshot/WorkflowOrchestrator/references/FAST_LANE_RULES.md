# WorkflowOrchestrator Fast-Lane Rules

Use this reference when the user asks for faster workflow, routing, or next-sprint decisions.

1. One sprint has one primary purpose.
2. Normal planning sprint target: 2-4 minutes.
3. Heavy sprint target is allowed only for implementation, simulation, checkpoint, or release work.
4. Do not create more than 10 new docs in a normal planning sprint unless explicitly requested.
5. Use compact SprintReporter by default.
6. Full external-review reports are for checkpoint pushes, source patches, release gates, blockers, or explicit request.
7. Use subagents only when the main agent decides they are beneficial under the subagent policy.
8. Never use subagents for writing files or source changes.
9. Prefer handoff files and consolidation gate docs over full history re-reads.
10. Checkpoint git review/push every 3-4 meaningful local sprints or major phase boundary.
11. Do not push every sprint.
12. Never start implementation unless gate allows it and the user explicitly approves.
13. If validation contradicts a report, fix validation before continuing.
14. If scope expands, stop and record a blocker.

