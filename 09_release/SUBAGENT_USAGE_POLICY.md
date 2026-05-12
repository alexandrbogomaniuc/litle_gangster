# Subagent Usage Policy

Status: active fast-lane policy.

The main agent decides whether subagents are beneficial. Do not use them automatically.

## Use Subagents When

- Checks are independent.
- Each task is bounded and read-only.
- No subagent writes files.
- No subagent needs secrets, donor assets, Staging source, public GitHub, or broad history.
- The main agent can merge findings quickly.

## Do Not Use Subagents When

- The task is small enough for the main agent.
- The subagent would need broad context.
- The subagent would duplicate analysis.
- The subagent would inspect sensitive assets, secrets, donor bodies, or Staging source.
- Any subagent would need to write or patch files.

## Limits

- Maximum subagents per sprint: 3.
- Output format: compact structured result only.
- Main agent remains responsible for decisions and files.
- Record whether subagent output changed the final decision.

## Current Sprint Decision

Subagents were considered and not used. This sprint is a small operational policy update with bounded reads and file writes owned by the main agent. Subagents would add overhead without improving reliability.

