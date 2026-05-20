#!/usr/bin/env python3
"""Validate required non-production visual sandbox outputs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_FILES = [
    "README.md",
    "PROTOTYPE_STATUS.md",
    "asset_inventory.json",
    "placeholder_binding.json",
    "scripted_outcomes.json",
    "screen_states.json",
]

CODE_EXTENSIONS = {".html", ".js", ".css", ".mjs", ".cjs"}
NETWORK_PATTERNS = [
    re.compile(r"\bfetch\s*\(", re.IGNORECASE),
    re.compile(r"\bXMLHttpRequest\b", re.IGNORECASE),
    re.compile(r"\bWebSocket\b", re.IGNORECASE),
    re.compile(r"\bsendBeacon\s*\(", re.IGNORECASE),
    re.compile(r"\baxios\s*[\.(]", re.IGNORECASE),
    re.compile(r"https?://", re.IGNORECASE),
]
SENSITIVE_PATTERNS = [
    re.compile(r"https?://", re.IGNORECASE),
    re.compile(r"(?i)(token|sid|signature|secret|password|pass_key)=[^\\s\"'<>]+"),
    re.compile(r"(?i)realmoneyenv="),
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "allowed", "enabled", "approved"}
    return False


def collect_assets(inventory: Any) -> list[dict[str, Any]]:
    if isinstance(inventory, list):
        return [item for item in inventory if isinstance(item, dict)]
    if isinstance(inventory, dict):
        for key in ("assets", "items", "files", "inventory"):
            value = inventory.get(key)
            if isinstance(value, list):
                return [item for item in value if isinstance(item, dict)]
    return []


def donorish(item: dict[str, Any]) -> bool:
    text = json.dumps(item, sort_keys=True).lower()
    return "donor" in text or "reference" in text


def item_false(item: dict[str, Any], *keys: str) -> bool:
    return any(key in item and not truthy(item.get(key)) for key in keys)


def item_true(item: dict[str, Any], *keys: str) -> bool:
    return any(key in item and truthy(item.get(key)) for key in keys)


def validate_inventory(inventory: Any) -> list[str]:
    failures: list[str] = []
    for index, item in enumerate(collect_assets(inventory)):
        if not donorish(item):
            continue
        if not item_true(item, "placeholderOnly", "placeholder_only"):
            failures.append(f"asset_inventory item {index} is donor/reference but not marked placeholder-only")
        if not item_true(item, "nonProduction", "non_production"):
            failures.append(f"asset_inventory item {index} is donor/reference but not marked non-production")
        if not item_false(item, "productionReady", "production_ready", "approvedForRelease", "approved_for_release"):
            failures.append(f"asset_inventory item {index} is donor/reference but not blocked from production/release")
    return failures


def scan_files(sandbox: Path) -> list[str]:
    failures: list[str] = []
    for path in sandbox.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = path.relative_to(sandbox)
        if path.suffix.lower() in CODE_EXTENSIONS:
            for pattern in NETWORK_PATTERNS:
                if pattern.search(text):
                    failures.append(f"{rel} contains forbidden network/API call pattern: {pattern.pattern}")
        for pattern in SENSITIVE_PATTERNS:
            if pattern.search(text):
                failures.append(f"{rel} contains forbidden private URL or secret-like pattern: {pattern.pattern}")
    return failures


def validate_manifest_flags(project_root: Path) -> list[str]:
    manifest_path = project_root / "project_manifest.json"
    if not manifest_path.exists():
        return []
    data = load_json(manifest_path)
    failures: list[str] = []
    for key in (
        "gameclientbuilder_implementation_allowed",
        "registration_generation_allowed",
        "release_allowed",
    ):
        if truthy(data.get(key)):
            failures.append(f"project_manifest.json has {key}=true")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--sandbox-path", type=Path, required=True)
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    sandbox = args.sandbox_path.resolve()
    expected_root = (project_root / "11_prototypes").resolve()
    failures: list[str] = []
    parsed: dict[str, bool] = {}

    if expected_root not in sandbox.parents:
        failures.append("sandbox path must be under project 11_prototypes")
    if not sandbox.exists():
        failures.append("sandbox path does not exist")

    if sandbox.exists():
        for name in REQUIRED_FILES:
            path = sandbox / name
            if not path.exists():
                failures.append(f"missing required file: {name}")
            elif path.suffix == ".json":
                try:
                    load_json(path)
                    parsed[name] = True
                except Exception as exc:  # noqa: BLE001
                    failures.append(f"{name} does not parse: {exc}")
                    parsed[name] = False

        inventory_path = sandbox / "asset_inventory.json"
        if inventory_path.exists():
            try:
                failures.extend(validate_inventory(load_json(inventory_path)))
            except Exception:
                pass
        failures.extend(scan_files(sandbox))

    failures.extend(validate_manifest_flags(project_root))
    result = {
        "accepted": not failures,
        "sandboxPath": str(sandbox),
        "jsonParsed": parsed,
        "failures": failures,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
