# WorkflowOrchestrator Subagent Usage Policy

The main agent decides whether subagents are useful. Subagents are optional, not automatic.

Use at most 3 subagents, only for bounded read-only tasks. Require compact structured results. The main agent writes all files and owns final
  decisions.

Use subagents when checks are independent and can reduce time or improve reliability.

Do not use subagents when the task is small, broad-context, duplicated, sensitive, or requires writing files, inspecting donor assets, Staging source,
  secrets, or public GitHub.

Record:

- subagents considered: true/false
- subagents used: true/false
- count
- decision reason
- expected benefit
- whether output changed the decision

