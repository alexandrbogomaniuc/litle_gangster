#!/usr/bin/env python3
"""Validate whether a requested next skill is allowed by workflow gates."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


IMPLEMENTATION_SKILLS = {
    "GameClientBuilder": [
        "runtime_owner_proven",
        "result_api_contract_proven",
        "approved_assets_strategy_exists",
        "explicit_user_approval_for_client_code",
    ],
    "GameServerRegistrar": [
        "registration_lane_proven",
        "game_id_selected",
        "bank_source_selected",
        "rollback_strategy_exists",
    ],
    "WalletAndLaunchTester": [
        "launch_url_or_test_environment_available",
        "safe_test_user_secret_reference_exists",
        "wallet_mock_or_stage_mode_selected",
    ],
    "RTPAndReleaseAuditor": [
        "math_approved",
        "client_build_approved",
        "registration_approved",
        "wallet_tests_approved",
        "final_assets_approved",
    ],
}

CHECKPOINT_SKILLS = {
    "WorkflowOrchestrator checkpoint git review/push",
    "checkpoint git review/push",
}


def load_manifest(project_root: Path) -> dict:
    return json.loads((project_root / "project_manifest.json").read_text(encoding="utf-8"))


def boolish(data: dict, key: str) -> bool:
    value = data.get(key)
    if isinstance(value, bool):
        return value
    for container in ("approvals", "approval_gates"):
        nested = data.get(container)
        if isinstance(nested, dict) and isinstance(nested.get(key), bool):
            return nested[key]
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--skill", required=True)
    args = parser.parse_args()

    data = load_manifest(args.project_root.resolve())
    requested = args.skill
    failures: list[str] = []

    if requested in CHECKPOINT_SKILLS or "checkpoint" in requested.lower():
        print("NEXT SKILL ALLOWED")
        print(f"skill={requested}")
        print("fast_lane_mode=true")
        print("implementation_allowed=false")
        return 0

    for skill, required_flags in IMPLEMENTATION_SKILLS.items():
        if requested == skill or requested.startswith(skill):
            for flag in required_flags:
                if not boolish(data, flag):
                    failures.append(f"{requested} blocked because {flag}=false")
            if skill == "GameServerRegistrar":
                status = data.get("scn_serializer_status")
                if status not in {"proven", "workaround_defined"}:
                    failures.append("GameServerRegistrar blocked because scn_serializer_status is not proven/workaround_defined")

    if "backend adapter" in requested.lower() and "implementation" in requested.lower():
        if not boolish(data, "backend_adapter_implementation_allowed"):
            failures.append("backend adapter implementation blocked because backend_adapter_implementation_allowed=false")
    if "gameclientbuilder" in requested.lower() and "implementation" in requested.lower():
        if not boolish(data, "gameclientbuilder_implementation_allowed"):
            failures.append("GameClientBuilder implementation blocked because gameclientbuilder_implementation_allowed=false")

    if failures:
        print("NEXT SKILL BLOCKED")
        for item in failures:
            print(f"- {item}")
        return 1

    print("NEXT SKILL ALLOWED")
    print(f"skill={requested}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
