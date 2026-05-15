---
name: WorkflowOrchestrator
description: Decide the next safe iGaming workflow skill from manifest, handoffs, blockers, and gates; refuse unsafe implementation jumps and produce
the exact next prompt.
---

# WorkflowOrchestrator

## Purpose

WorkflowOrchestrator is the routing and gatekeeping skill. It does not implement game code, generate registration, call wallets, browse donor URLs,
capture assets, or approve release. It reads the current project state and produces one safe next step.

## Required Inputs

- Project root.
- Skill suite root.
- Current user request.
- `project_manifest.json`.
- All available `00_skill_reports/*/handoff.json`.
- Current blockers and latest sprint report, if present.

## Required Reads

1. Nearest `AGENTS.md`.
2. Project `project_manifest.json`.
3. Project `assumptions.md` and `decisions_log.md`.
4. All `00_skill_reports/*/handoff.json` files.
5. `references/WORKFLOW_GATES.md` when gate interpretation is needed.

## Hard Rules

- Planning allowed is not implementation allowed.
- Never infer approval from completed planning reports.
- Use fast-lane mode for routing and optimization work: one primary purpose, compact reports by default, and no broad history re-read unless required.
- Prefer `handoff.json`, `project_manifest.json`, and consolidation gate docs as source of truth for fast-lane decisions.
- Checkpoint git review/push is recommended every 3-4 meaningful local sprints or at a major phase boundary, but never push automatically.
- Subagents are optional. Use them only when the main agent decides they clearly reduce time or improve reliability, and never for writing files or
  source changes.
- Never recommend GameClientBuilder implementation unless runtime owner, result API contract, approved asset strategy, and explicit client-code
  approval are all true.
- Never recommend GameServerRegistrar generation unless registration lane, game ID, bank/source, serializer/workaround, and rollback strategy are
  proven.
- Never recommend WalletAndLaunchTester unless safe test environment and secret references are available.
- Never recommend RTPAndReleaseAuditor release approval unless all prior gates pass.
- Never recommend WalletAndLaunchTester or GameServerRegistrar generation when GS,
  wallet, runtime, storage, and client responsibilities are unresolved. Route to
  ProtocolAndSchemaMapper for a responsibility boundary audit first when wallet
  ownership, session/history ownership, pending/stuck transaction ownership, or
  registration wallet/config ownership is unclear.
- Route to MathProfileCalibrator when a 3x3 math profile matrix exists but
  train/validation gates are not passed, or when requested RTP/volatility
  profiles need calibration.
- Route to ParallelMathValidator when large train/validation/tail simulation is
  needed, bonus-buy EV needs a parallel lane, FRB/promo EV needs validation,
  registration math fields need extracted simulation evidence, certification
  evidence is needed, or the main workflow should continue while math validation
  runs in parallel.
- If the requested next skill is unsafe, refuse the jump and produce the nearest safe prompt.
- Public export validation may be called passed only after local validation, commit, push, and fresh post-push clone validation.

## Workflow

1. Run or inspect `scripts/decide_next_skill.py` with the project root.
2. If the user requested a specific skill, run `scripts/validate_next_skill_allowed.py --skill <SkillName>`.
3. Prefer ParallelMathValidator over implementation or registration work when
   unresolved large-scale math evidence, bonus-buy EV, FRB/promo liability,
   tail/max-win, registration math fields, or certification evidence blocks a
   downstream gate.
4. Prefer MathProfileCalibrator over backend/client/registration work when
   profile calibration gates are open.
5. Prefer ProtocolAndSchemaMapper responsibility-boundary audit before
   WalletAndLaunchTester when prompts imply that the browser/client or game runtime
   owns real wallet state without current GS proof.
6. Report the allowed next skill, blocked unsafe skills, and exact next Codex prompt.
7. Update project reports only when the sprint asks for it.

## Output Shape

Produce:

- `next_allowed_skill`
- `planning_allowed`
- `implementation_allowed`
- `blocked_skills`
- `blocking_gates`
- `exact_next_prompt`

Keep the output short and decision-focused.

## Fast-Lane References

- `references/FAST_LANE_RULES.md`
- `references/SUBAGENT_USAGE_POLICY.md`
