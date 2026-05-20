#!/usr/bin/env python3
"""Validate that a visual sandbox request keeps production gates closed."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


FORBIDDEN_TRUE_KEYS = {
    "allow_bo_cm_endpoint_calls",
    "allow_donor_assets_as_production",
    "allow_donor_scripts_as_production_logic",
    "allow_gameclientbuilder_implementation",
    "allow_gs_endpoint_calls",
    "allow_public_export_of_donor_assets",
    "allow_registration_generation",
    "allow_release_approval",
    "allow_wallet_endpoint_calls",
    "bo_cm_calls_enabled",
    "certification_status",
    "donor_assets_as_production_allowed",
    "donor_assets_used_as_production",
    "donor_scripts_as_production_logic_allowed",
    "donor_scripts_used_as_production",
    "external_calls_enabled",
    "gameclientbuilder_implementation_allowed",
    "gs_calls_enabled",
    "production_client_code_allowed",
    "production_client_code_generated",
    "public_export_donor_assets_allowed",
    "registration_generation_allowed",
    "release_allowed",
    "release_approval_allowed",
    "wallet_calls_enabled",
    "wallet_endpoint_tests_allowed",
}

FORBIDDEN_MODE_VALUES = {
    "production",
    "release",
    "certification",
    "registration_generation",
    "gameclientbuilder_implementation",
}


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "allowed", "enabled", "approve", "approved"}
    return False


def load_request(path: Path | None) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8") if path else sys.stdin.read()
    if not raw.strip():
        return {}
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise SystemExit("request JSON must be an object")
    return data


def walk_items(value: Any, prefix: str = "") -> list[tuple[str, Any]]:
    items: list[tuple[str, Any]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_prefix = f"{prefix}.{key}" if prefix else str(key)
            items.extend(walk_items(child, child_prefix))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            items.extend(walk_items(child, f"{prefix}[{index}]"))
    else:
        items.append((prefix, value))
    return items


def validate(data: dict[str, Any]) -> tuple[bool, list[str]]:
    failures: list[str] = []
    for path, value in walk_items(data):
        key = path.split(".")[-1].split("[")[0]
        if key in FORBIDDEN_TRUE_KEYS and truthy(value):
            failures.append(f"{path} must be false for VisualPrototypeSandboxBuilder")
        if key in {"mode", "target", "lane", "requested_work"} and isinstance(value, str):
            if value.strip().lower() in FORBIDDEN_MODE_VALUES:
                failures.append(f"{path}={value!r} is not a visual sandbox request")
    return not failures, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request-json", type=Path)
    args = parser.parse_args()

    data = load_request(args.request_json)
    ok, failures = validate(data)
    result = {
        "accepted": ok,
        "skill": "VisualPrototypeSandboxBuilder",
        "failures": failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
