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


def int_value(data: dict, key: str, default: int | None = None) -> int | None:
    value = data.get(key)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return default
    return default


def math_profile_matrix_exists(manifest: dict, handoffs: dict[str, dict]) -> bool:
    math = manifest.get("math")
    if isinstance(math, dict):
        if boolish(math, "profile_matrix_created") or boolish(math, "rtp_volatility_profile_framework_completed"):
            return True
        if boolish(math, "simulator_mathProfileId_support") or math.get("tail_maxwin_pilot_profiles_tested_count") == 9:
            return True
    for handoff in handoffs.values():
        if not isinstance(handoff, dict):
            continue
        if boolish(handoff, "profile_matrix_created") or boolish(handoff, "simulator_supports_mathProfileId"):
            return True
        if int_value(handoff, "expected_profiles_count") == 9 and (
            boolish(handoff, "profile_calibration_completed")
            or boolish(handoff, "validation_seed_check_completed")
            or boolish(handoff, "tail_maxwin_pilot_completed")
        ):
            return True
    return False


def train_validation_gates_passed(handoffs: dict[str, dict]) -> bool:
    for handoff in handoffs.values():
        if not isinstance(handoff, dict):
            continue
        train_passed = boolish(handoff, "train_gate_clean_enough_for_validation")
        if int_value(handoff, "composite_profiles_outside_tolerance_count") == 0 and int_value(handoff, "composite_profiles_within_tolerance_count") == 9:
            train_passed = True
        validation_passed = boolish(handoff, "validation_seed_check_completed")
        if int_value(handoff, "validation_profiles_outside_tolerance_count") == 0 and int_value(handoff, "validation_profiles_within_tolerance_count") == 9:
            validation_passed = True
        status = handoff.get("validation_gate_status")
        if status == "pass_for_profile_matrix_train_validation_stage":
            validation_passed = True
        if train_passed and validation_passed:
            return True
    return False


def math_profile_calibration_requested(manifest: dict, handoffs: dict[str, dict]) -> bool:
    if boolish(manifest, "math_profile_calibration_requested") or boolish(manifest, "rtp_volatility_profiles_need_calibration"):
        return True
    for handoff in handoffs.values():
        if isinstance(handoff, dict) and (
            boolish(handoff, "math_profile_calibration_requested")
            or boolish(handoff, "rtp_request_validation_required")
            or boolish(handoff, "profile_calibration_requested")
        ):
            return True
    return False


def parallel_math_validation_needed(manifest: dict, handoffs: dict[str, dict]) -> bool:
    trigger_flags = [
        "parallel_math_validation_requested",
        "parallel_math_validation_needed",
        "large_math_validation_needed",
        "large_train_validation_tail_needed",
        "large_train_validation_needed",
        "tail_maxwin_large_validation_needed",
        "bonus_buy_ev_validation_parallel_needed",
        "bonus_buy_ev_validation_needed",
        "frb_promo_ev_validation_needed",
        "registration_math_fields_need_simulation_evidence",
        "certification_evidence_package_needed",
        "main_workflow_should_continue_while_math_validates",
    ]
    if any(boolish(manifest, flag) for flag in trigger_flags):
        return True
    blockers = manifest.get("blockers") or manifest.get("active_backend_adapter_apply_blockers") or []
    if isinstance(blockers, list):
        blocker_text = json.dumps(blockers).lower()
        if any(
            token in blocker_text
            for token in (
                "large_math_validation",
                "tail_maxwin",
                "bonus_buy_ev_validation",
                "frb_promo",
                "registration_math_fields",
                "certification_evidence",
            )
        ):
            return True
    for handoff in handoffs.values():
        if not isinstance(handoff, dict):
            continue
        if any(boolish(handoff, flag) for flag in trigger_flags):
            return True
        if boolish(handoff, "bonus_buy_ready_for_train_validation") or boolish(handoff, "bonus_buy_validation_ready"):
            return True
        if handoff.get("suggested_next_skill") == "ParallelMathValidator":
            return True
    return False


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

    if parallel_math_validation_needed(manifest, handoffs):
        return {
            "next_allowed_skill": "ParallelMathValidator",
            "planning_allowed": True,
            "implementation_allowed": False,
            "parallel_allowed": True,
            "fast_lane_mode": True,
            "compact_report_default": True,
            "blocking_gates": ["parallel_math_validation_evidence_needed"],
            "blocked_skills": ["backend adapter implementation", "GameClientBuilder implementation", "GameServerRegistrar generation", "WalletAndLaunchTester", "RTPAndReleaseAuditor"],
            "exact_next_prompt": "Run ParallelMathValidator only. Create or import large-scale train/validation/tail, bonus-buy, FRB/promo, registration math field, or certification evidence in a parallel output folder; do not change active configs, do not tune from validation seeds, and keep backend/client/registration/wallet/DB/donor/release work blocked. Stop after SprintReporter.",
        }

    if math_profile_calibration_requested(manifest, handoffs) or (
        math_profile_matrix_exists(manifest, handoffs) and not train_validation_gates_passed(handoffs)
    ):
        return {
            "next_allowed_skill": "MathProfileCalibrator",
            "planning_allowed": True,
            "implementation_allowed": False,
            "fast_lane_mode": True,
            "compact_report_default": True,
            "blocking_gates": ["math_profile_train_validation_gate_open"],
            "blocked_skills": ["backend adapter implementation", "GameClientBuilder implementation", "GameServerRegistrar generation", "WalletAndLaunchTester", "RTPAndReleaseAuditor"],
            "exact_next_prompt": "Run MathProfileCalibrator only. Validate requested LOW/MEDIUM/HIGH RTP values, calibrate the 3x3 RTP/volatility profile matrix with train seeds only, run validation only after the train gate passes, and keep backend/client/registration/wallet/DB/donor/release work blocked. Stop after SprintReporter.",
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
