#!/usr/bin/env python3
"""Decide the next safe iGaming workflow skill from manifest and handoffs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def boolish(data: dict, key: str) -> bool:
    value = data.get(key)
    if isinstance(value, bool):
        return value
    for container in ("approvals", "approval_gates"):
        nested = data.get(container)
        if isinstance(nested, dict) and isinstance(nested.get(key), bool):
            return nested[key]
    return False


def collect_handoffs(project_root: Path) -> dict[str, dict]:
    reports = project_root / "00_skill_reports"
    handoffs: dict[str, dict] = {}
    if not reports.exists():
        return handoffs
    for path in sorted(reports.glob("*/handoff.json")):
        try:
            handoffs[path.parent.name] = load_json(path)
        except Exception as exc:
            handoffs[path.parent.name] = {"parse_error": str(exc)}
    return handoffs


def checkpoint_due(manifest: dict, handoffs: dict[str, dict]) -> bool:
    if boolish(manifest, "checkpoint_push_due") or boolish(manifest, "checkpoint_git_review_due"):
        return True
    return any(
        boolish(handoff, "checkpoint_push_due") or boolish(handoff, "checkpoint_git_review_due")
        for handoff in handoffs.values()
        if isinstance(handoff, dict)
    )


def decide(manifest: dict, handoffs: dict[str, dict]) -> dict:
    blockers: list[str] = []

    if not boolish(manifest, "project_created"):
        return {
            "next_allowed_skill": "ProjectCreator",
            "planning_allowed": True,
            "implementation_allowed": False,
            "blocking_gates": ["GATE_0_PROJECT_CREATED"],
            "blocked_skills": ["all downstream skills"],
            "exact_next_prompt": "Run ProjectCreator only. Create the project manifest, assumptions, decisions, blockers, and initial handoff. Stop after SprintReporter.",
        }

    if checkpoint_due(manifest, handoffs):
        return {
            "next_allowed_skill": "WorkflowOrchestrator checkpoint git review/push",
            "planning_allowed": True,
            "implementation_allowed": False,
            "fast_lane_mode": True,
            "compact_report_default": True,
            "blocking_gates": ["implementation_gates_remain_closed"],
            "blocked_skills": ["backend adapter implementation", "GameClientBuilder implementation", "GameServerRegistrar generation", "WalletAndLaunchTester", "RTPAndReleaseAuditor"],
            "exact_next_prompt": "Run WorkflowOrchestrator checkpoint git review/push only if the user approves. Validate local artifacts, commit intentionally, push only after raw GitHub validation, and do not start implementation automatically. Stop after compact SprintReporter unless checkpoint/public validation requires full report.",
        }

    if not boolish(manifest, "runtime_owner_proven") or not boolish(manifest, "result_api_contract_proven"):
        blockers.extend(["GATE_3_RUNTIME_LANE_LOCKED", "runtime_owner_or_result_api_unproven"])
        return {
            "next_allowed_skill": "ProtocolAndSchemaMapper runtime adapter planning",
            "planning_allowed": True,
            "implementation_allowed": False,
            "fast_lane_mode": True,
            "compact_report_default": True,
            "blocking_gates": blockers,
            "blocked_skills": ["GameClientBuilder implementation", "GameServerRegistrar generation", "WalletAndLaunchTester", "RTPAndReleaseAuditor"],
            "exact_next_prompt": "Run ProtocolAndSchemaMapper runtime adapter planning only. Prove or define the runtime payload adapter and keep all implementation skills blocked. Stop after SprintReporter.",
        }

    if not boolish(manifest, "gameclientbuilder_implementation_allowed"):
        return {
            "next_allowed_skill": "GameClientBuilder planning/runtime API review",
            "planning_allowed": True,
            "implementation_allowed": False,
            "fast_lane_mode": True,
            "compact_report_default": True,
            "blocking_gates": ["GATE_6_CLIENT_BUILD_ALLOWED"],
            "blocked_skills": ["GameClientBuilder implementation"],
            "exact_next_prompt": "Run GameClientBuilder planning/runtime API review only. Do not generate client code unless explicit implementation approval and all gates are true.",
        }

    return {
        "next_allowed_skill": "GameClientBuilder implementation requires explicit user confirmation",
        "planning_allowed": True,
        "implementation_allowed": False,
        "fast_lane_mode": True,
        "compact_report_default": True,
        "blocking_gates": ["explicit_user_confirmation_required"],
        "blocked_skills": [],
        "exact_next_prompt": "Ask the user for explicit approval before running GameClientBuilder implementation.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    manifest = load_json(project_root / "project_manifest.json")
    handoffs = collect_handoffs(project_root)
    result = decide(manifest, handoffs)
    result["handoffs_read"] = sorted(handoffs)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
