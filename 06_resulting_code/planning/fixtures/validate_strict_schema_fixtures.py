#!/usr/bin/env python3
"""Validate Little Gangster strict-schema non-production fixture variants."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_DIR = Path(__file__).resolve().parent
STRICT_DIR = FIXTURE_DIR / "strict_schema_examples"
RESULT_SCHEMA = (
    PROJECT_ROOT
    / "04_math/alternatives/v0_3_donor_feature_parity_provisional/result_schema.json"
)
GAMESV1_ROOT = Path(
    "[STAGING_ROOT]/platform-source/platform/Gamesv1"
)
STAGING_SCHEMA_DIR = GAMESV1_ROOT / "docs/gs/schemas"
EXPECTED_COUNT = 24


TARGET_SCHEMA_BY_FILE = {
    "01_base_idle.json": "opengame.response.schema.json",
    "13_feature_mode_1_entry.json": "featureaction.response.schema.json",
    "14_feature_mode_2_entry.json": "featureaction.response.schema.json",
    "15_feature_mode_3_entry.json": "featureaction.response.schema.json",
    "16_bonus_buy_mode_selection.json": "featureaction.response.schema.json",
    "17_bonus_buy_purchased_feature_start.json": "featureaction.response.schema.json",
    "22_round_completion_ready.json": "closegame.response.schema.json",
    "23_reconnect_state_restore.json": "resumegame.response.schema.json",
    "24_error_or_recovery_pending_state.json": "gethistory.response.schema.json",
}


FORBIDDEN_VALUE_PATTERNS = [
    re.compile(r"https?://", re.IGNORECASE),
    re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"),
    re.compile(r"[USER_HOME]/(?!Documents/CodexGameDev/little-gangster)"),
    re.compile(r"PASS_KEY", re.IGNORECASE),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]+", re.IGNORECASE),
    re.compile(r"eyJ[A-Za-z0-9_-]{12,}"),
    re.compile(r"SID=[A-Za-z0-9._-]+", re.IGNORECASE),
    re.compile(r"signature=[A-Za-z0-9._-]+", re.IGNORECASE),
    re.compile(r"token=[A-Za-z0-9._-]+", re.IGNORECASE),
    re.compile(r"02_reference_assets/"),
    re.compile(r"authorized_raw|authorized_normalized|quarantine"),
    re.compile(r"\.(png|jpg|jpeg|webp|avif|svg|gif|mp3|ogg|wav|mp4|webm|mov|fnt|atlas|skel|bin|zip|pdf)\b", re.IGNORECASE),
]


def target_schema_name(path: Path) -> str:
    return TARGET_SCHEMA_BY_FILE.get(path.name, "playround.response.schema.json")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_string_values(value: Any) -> list[str]:
    out: list[str] = []
    if isinstance(value, str):
        out.append(value)
    elif isinstance(value, list):
        for item in value:
            out.extend(iter_string_values(item))
    elif isinstance(value, dict):
        for item in value.values():
            out.extend(iter_string_values(item))
    return out


def assert_no_forbidden_values(path: Path, data: Any) -> list[str]:
    findings: list[str] = []
    for value in iter_string_values(data):
        for pattern in FORBIDDEN_VALUE_PATTERNS:
            if pattern.search(value):
                findings.append(f"{path.name}: forbidden value matched {pattern.pattern!r}")
    return findings


def validate_with_ajv(schema_path: Path, instance_path: Path) -> tuple[bool | None, str]:
    """Return (ok, detail). ok=None means AJV could not run."""

    node_code = r"""
import fs from 'node:fs';
import Ajv2020 from 'ajv/dist/2020.js';

const [schemaPath, instancePath] = process.argv.slice(1);
const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
const instance = JSON.parse(fs.readFileSync(instancePath, 'utf8'));
const ajv = new Ajv2020({ strict: false, allErrors: true });
const validate = ajv.compile(schema);
const ok = validate(instance);
const detail = ok
  ? 'valid'
  : (validate.errors || [])
      .slice(0, 8)
      .map((error) => `${error.instancePath || '/'} ${error.message}`)
      .join('; ');
console.log(JSON.stringify({ ok, detail }));
"""
    try:
        completed = subprocess.run(
            ["node", "--input-type=module", "-e", node_code, str(schema_path), str(instance_path)],
            cwd=str(GAMESV1_ROOT),
            text=True,
            capture_output=True,
            check=False,
        )
    except FileNotFoundError:
        return None, "node_not_available"

    if completed.returncode != 0:
        detail = (completed.stderr or completed.stdout).strip().splitlines()[:4]
        return None, "ajv_unavailable_or_failed: " + " | ".join(detail)

    try:
        result = json.loads(completed.stdout)
    except json.JSONDecodeError:
        return None, "ajv_output_not_json"

    return bool(result.get("ok")), str(result.get("detail") or "")


def validate_fixture(path: Path) -> dict[str, Any]:
    data = load_json(path)
    presentation = data.get("presentationPayload")
    game_payload = presentation.get("gamePayload") if isinstance(presentation, dict) else None
    payload = game_payload.get("payload") if isinstance(game_payload, dict) else None
    metadata = None
    if isinstance(payload, dict):
        metadata = (
            payload.get("state_persistence", {})
            if isinstance(payload.get("state_persistence"), dict)
            else {}
        ).get("fixture_metadata")

    errors: list[str] = []
    if not isinstance(game_payload, dict):
        errors.append("missing presentationPayload.gamePayload")
    else:
        if game_payload.get("gameKey") != "little-gangster":
            errors.append("gamePayload.gameKey is not little-gangster")
        if game_payload.get("schemaVersion") != "v0.3":
            errors.append("gamePayload.schemaVersion is not v0.3")
        if not isinstance(payload, dict):
            errors.append("gamePayload.payload is not an object")

    if not isinstance(metadata, dict):
        errors.append("missing gamePayload.payload.state_persistence.fixture_metadata")
    else:
        expected = {
            "fixtureType": "non_production_renderer_fixture",
            "nonProduction": True,
            "authoritativeOutcome": False,
            "browserGenerated": False,
        }
        for key, expected_value in expected.items():
            if metadata.get(key) != expected_value:
                errors.append(f"fixture_metadata.{key} expected {expected_value!r}")

    errors.extend(assert_no_forbidden_values(path, data))

    schema_name = target_schema_name(path)
    response_schema_path = STAGING_SCHEMA_DIR / schema_name
    response_ok, response_detail = validate_with_ajv(response_schema_path, path)
    if response_ok is False:
        errors.append(f"response_schema_validation_failed: {response_detail}")
    elif response_ok is None:
        errors.append(f"response_schema_validation_not_run: {response_detail}")

    result_ok: bool | None = None
    result_detail = "not_run"
    if isinstance(payload, dict):
        temp_payload_path = path.with_suffix(".gamePayloadPayload.tmp.json")
        temp_payload_path.write_text(json.dumps(payload), encoding="utf-8")
        try:
            result_ok, result_detail = validate_with_ajv(RESULT_SCHEMA, temp_payload_path)
        finally:
            temp_payload_path.unlink(missing_ok=True)
        if result_ok is False:
            errors.append(f"v0_3_result_schema_validation_failed: {result_detail}")
        elif result_ok is None:
            errors.append(f"v0_3_result_schema_validation_not_run: {result_detail}")

    return {
        "fixture": path.name,
        "target_schema": schema_name,
        "json_valid": True,
        "response_schema_valid": response_ok is True,
        "response_schema_detail": response_detail,
        "v0_3_result_schema_valid": result_ok is True,
        "v0_3_result_schema_detail": result_detail,
        "gamePayload_present": isinstance(game_payload, dict),
        "nonProduction_flags_present": isinstance(metadata, dict)
        and metadata.get("fixtureType") == "non_production_renderer_fixture"
        and metadata.get("nonProduction") is True
        and metadata.get("authoritativeOutcome") is False
        and metadata.get("browserGenerated") is False,
        "errors": errors,
    }


def main() -> int:
    if not STRICT_DIR.exists():
        print(f"ERROR strict fixture dir missing: {STRICT_DIR}", file=sys.stderr)
        return 1

    files = sorted(STRICT_DIR.glob("*.json"))
    if len(files) != EXPECTED_COUNT:
        print(f"ERROR expected {EXPECTED_COUNT} strict fixtures, found {len(files)}", file=sys.stderr)
        return 1

    results: list[dict[str, Any]] = []
    for path in files:
        try:
            results.append(validate_fixture(path))
        except Exception as exc:  # noqa: BLE001 - loud validation failure.
            results.append(
                {
                    "fixture": path.name,
                    "target_schema": target_schema_name(path),
                    "json_valid": False,
                    "response_schema_valid": False,
                    "response_schema_detail": "not_run",
                    "v0_3_result_schema_valid": False,
                    "v0_3_result_schema_detail": "not_run",
                    "gamePayload_present": False,
                    "nonProduction_flags_present": False,
                    "errors": [f"{type(exc).__name__}: {exc}"],
                }
            )

    result_csv = FIXTURE_DIR / "strict_schema_validation_results.csv"
    with result_csv.open("w", newline="", encoding="utf-8") as handle:
        fields = [
            "fixture",
            "target_schema",
            "json_valid",
            "response_schema_valid",
            "v0_3_result_schema_valid",
            "gamePayload_present",
            "nonProduction_flags_present",
            "errors",
        ]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for result in results:
            writer.writerow(
                {
                    key: "; ".join(result[key]) if key == "errors" else result[key]
                    for key in fields
                }
            )

    failed = [result for result in results if result["errors"]]
    response_valid = sum(1 for result in results if result["response_schema_valid"])
    result_valid = sum(1 for result in results if result["v0_3_result_schema_valid"])
    print(f"strict_fixture_count={len(results)}")
    print(f"response_schema_valid_count={response_valid}")
    print(f"v0_3_result_schema_valid_count={result_valid}")
    print(f"validation_results_csv={result_csv}")
    if failed:
        print("STRICT_FIXTURE_VALIDATION_FAILED", file=sys.stderr)
        for result in failed:
            print(f"{result['fixture']}: {'; '.join(result['errors'])}", file=sys.stderr)
        return 1

    print("STRICT_FIXTURE_VALIDATION_PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
