#!/usr/bin/env python3
"""Validate the Little Gangster static fixture renderer prototype.

This validator is intentionally local and deterministic. It does not browse,
call runtime services, call wallet services, or inspect donor assets.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROJECT = ROOT.parents[3]

REQUIRED_FILES = [
    "README.md",
    "index.html",
    "renderer.js",
    "styles.css",
    "fixtures_manifest.json",
    "prototype_limitations.md",
    "prototype_validation_report.md",
    "validate_static_fixture_renderer.py",
]

DISALLOWED_DIRS = [
    "node_modules",
    "src",
    "public",
    "dist",
    "build",
]

MEDIA_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".avif",
    ".svg",
    ".gif",
    ".mp3",
    ".ogg",
    ".wav",
    ".mp4",
    ".webm",
    ".mov",
    ".fnt",
    ".atlas",
    ".skel",
    ".bin",
    ".zip",
    ".pdf",
}

TEXT_SCAN_EXCLUDES = {
    "validate_static_fixture_renderer.py",
}

FORBIDDEN_PATH_PATTERNS = [
    "02_reference_assets/",
    "authorized_raw/",
    "authorized_normalized/",
    "quarantine/",
    "scaffold_preview/",
    "donor_asset/",
]

# Built without a literal URL prefix so the validator does not flag itself.
URL_PATTERN = re.compile("h" + r"ttps?://", re.IGNORECASE)
TOKENIZED_URL_PATTERN = re.compile(r"[?&](token|sid|signature|session|auth|key|jwt|pass|password)=", re.IGNORECASE)
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
SECRET_VALUE_PATTERN = re.compile(
    r"\b(PASS_KEY|SID|signature|jwt|bearer|password|private[_-]?key)\b\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{12,}",
    re.IGNORECASE,
)
PRIVATE_LINK_PATTERN = re.compile(r"\b(private|secret|signed|presigned)[-_ ]?link\b", re.IGNORECASE)

RENDERER_FORBIDDEN_CALL_PATTERNS = [
    re.compile(r"fetch\s*\(\s*['\"]\s*h" + r"ttps?://", re.IGNORECASE),
    re.compile(r"XMLHttpRequest", re.IGNORECASE),
    re.compile(r"WebSocket\s*\(", re.IGNORECASE),
    re.compile(r"EventSource\s*\(", re.IGNORECASE),
    re.compile(r"sendBeacon\s*\(", re.IGNORECASE),
    re.compile(r"/slot/v1", re.IGNORECASE),
    re.compile(r"playround", re.IGNORECASE),
    re.compile(r"opengame", re.IGNORECASE),
    re.compile(r"wallet", re.IGNORECASE),
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"non UTF-8 text file: {path}: {exc}")


def required_files_exist() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        assert_true(path.exists(), f"required file missing: {rel}")
        assert_true(path.is_file(), f"required path is not a file: {rel}")
        assert_true(path.stat().st_size > 0, f"required file is empty: {rel}")


def forbidden_project_shape_absent() -> None:
    assert_true(not (ROOT / "package.json").exists(), "package.json exists in prototype folder")
    for rel in DISALLOWED_DIRS:
        assert_true(not (ROOT / rel).exists(), f"disallowed prototype folder exists: {rel}")


def media_files_absent() -> None:
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in MEDIA_EXTENSIONS:
            fail(f"media or binary file exists in prototype folder: {path.relative_to(ROOT)}")


def text_files_to_scan() -> list[Path]:
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name in TEXT_SCAN_EXCLUDES:
            continue
        if path.suffix.lower() in MEDIA_EXTENSIONS:
            continue
        files.append(path)
    return files


def forbidden_paths_absent() -> None:
    for path in text_files_to_scan():
        text = read_text(path)
        for pattern in FORBIDDEN_PATH_PATTERNS:
            assert_true(pattern not in text, f"forbidden asset path pattern {pattern!r} in {path.relative_to(ROOT)}")


def sensitive_values_absent() -> None:
    for path in text_files_to_scan():
        text = read_text(path)
        assert_true(not TOKENIZED_URL_PATTERN.search(text), f"tokenized URL-like value in {path.relative_to(ROOT)}")
        assert_true(not EMAIL_PATTERN.search(text), f"email-like value in {path.relative_to(ROOT)}")
        assert_true(not SECRET_VALUE_PATTERN.search(text), f"secret-like assignment in {path.relative_to(ROOT)}")
        assert_true(not PRIVATE_LINK_PATTERN.search(text), f"private link phrase in {path.relative_to(ROOT)}")
        for match in URL_PATTERN.finditer(text):
            snippet = text[max(0, match.start() - 40): match.start() + 120]
            fail(f"network URL-like text in {path.relative_to(ROOT)}: {snippet!r}")


def renderer_has_no_external_or_endpoint_calls() -> None:
    text = read_text(ROOT / "renderer.js")
    for pattern in RENDERER_FORBIDDEN_CALL_PATTERNS:
        assert_true(not pattern.search(text), f"renderer.js contains forbidden call pattern: {pattern.pattern}")


def non_production_warning_present() -> None:
    text = read_text(ROOT / "index.html")
    assert_true("NON-PRODUCTION" in text, "index.html missing NON-PRODUCTION warning")
    assert_true("NOT A GAME CLIENT" in text, "index.html missing game-client boundary warning")
    assert_true("NOT RELEASE CODE" in text, "index.html missing release-code boundary warning")
    assert_true("NOT AUTHORITATIVE RESULT GENERATION" in text, "index.html missing authority boundary warning")


def parse_json(path: Path) -> object:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"JSON parse failed for {path}: {exc}")


def validate_manifest_and_fixtures() -> None:
    manifest_path = ROOT / "fixtures_manifest.json"
    manifest = parse_json(manifest_path)
    assert_true(isinstance(manifest, dict), "fixtures_manifest.json must be an object")
    fixtures = manifest.get("fixtures")
    assert_true(isinstance(fixtures, list), "fixtures_manifest.json missing fixture list")
    assert_true(len(fixtures) == 24, f"expected 24 fixture entries, found {len(fixtures)}")
    assert_true(manifest.get("nonProductionOnly") is True, "manifest must be nonProductionOnly=true")
    assert_true(manifest.get("productionClientCodeGenerated") is False, "manifest must mark production client code as false")

    seen_ids: set[str] = set()
    for index, entry in enumerate(fixtures, start=1):
        assert_true(isinstance(entry, dict), f"fixture entry {index} must be object")
        fixture_id = entry.get("fixtureId")
        assert_true(isinstance(fixture_id, str) and fixture_id, f"fixture entry {index} missing fixtureId")
        assert_true(fixture_id not in seen_ids, f"duplicate fixtureId {fixture_id}")
        seen_ids.add(fixture_id)
        rel_path = entry.get("path")
        assert_true(isinstance(rel_path, str) and rel_path.endswith(".json"), f"fixture {fixture_id} missing JSON path")
        fixture_path = (ROOT / rel_path).resolve()
        assert_true(fixture_path.exists(), f"fixture path does not exist: {rel_path}")
        assert_true(str(fixture_path).startswith(str(PROJECT)), f"fixture path escapes project: {rel_path}")
        fixture = parse_json(fixture_path)
        validate_fixture(fixture, fixture_id)


def validate_fixture(fixture: object, expected_id: str) -> None:
    assert_true(isinstance(fixture, dict), f"fixture {expected_id} must be object")
    assert_true(fixture.get("fixtureId") == expected_id, f"fixture ID mismatch for {expected_id}")
    assert_true(fixture.get("fixtureType") == "non_production_renderer_fixture", f"fixture {expected_id} wrong fixtureType")
    assert_true(fixture.get("nonProduction") is True, f"fixture {expected_id} must be nonProduction=true")
    assert_true(fixture.get("authoritativeOutcome") is False, f"fixture {expected_id} must be authoritativeOutcome=false")
    assert_true(fixture.get("browserGenerated") is False, f"fixture {expected_id} must be browserGenerated=false")
    assert_true(fixture.get("runtimeEnvelopeStatus") == "candidate_unproven", f"fixture {expected_id} wrong runtimeEnvelopeStatus")
    assert_true(fixture.get("presentationPayloadExtensionStatus") == "pending_schema_review", f"fixture {expected_id} wrong presentation extension status")
    text = json.dumps(fixture, sort_keys=True)
    assert_true("02_reference_assets" not in text, f"fixture {expected_id} contains reference asset path")
    assert_true(not TOKENIZED_URL_PATTERN.search(text), f"fixture {expected_id} contains tokenized URL-like value")
    assert_true(not EMAIL_PATTERN.search(text), f"fixture {expected_id} contains email-like value")


def renderer_sources_non_empty() -> None:
    for rel in ["renderer.js", "styles.css"]:
        text = read_text(ROOT / rel)
        assert_true(len(text.strip()) > 200, f"{rel} is unexpectedly small or empty")


def main() -> None:
    required_files_exist()
    forbidden_project_shape_absent()
    media_files_absent()
    forbidden_paths_absent()
    sensitive_values_absent()
    renderer_has_no_external_or_endpoint_calls()
    non_production_warning_present()
    validate_manifest_and_fixtures()
    renderer_sources_non_empty()
    print("PASS: static fixture renderer validation passed")
    print("fixture_count=24")
    print("prototype_non_production_only=true")
    print("production_client_code_generated=false")


if __name__ == "__main__":
    main()
