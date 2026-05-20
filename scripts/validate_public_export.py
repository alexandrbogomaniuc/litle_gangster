#!/usr/bin/env python3
"""Validate this raw-safe public export checkout."""

from __future__ import annotations

import ast
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
FAILURES: list[str] = []

MIN_LINES = {
    "README.md": 30,
    "REVIEWER_START_HERE.md": 30,
    "PUBLIC_EXPORT_NOTICE.md": 15,
    "EXPORT_MANIFEST.md": 20,
    "scripts/validate_public_export.py": 40,
    "_skill_suite_snapshot/ParallelMathValidator/SKILL.md": 40,
    "_skill_suite_snapshot/WalletAndLaunchTester/SKILL.md": 40,
    "_skill_suite_snapshot/GameServerRegistrar/SKILL.md": 40,
    "_skill_suite_snapshot/RTPAndReleaseAuditor/SKILL.md": 40,
    "_skill_suite_snapshot/VisualPrototypeSandboxBuilder/SKILL.md": 40,
    "_skill_suite_snapshot/VisualPrototypeSandboxBuilder/scripts/validate_visual_sandbox_request.py": 40,
    "_skill_suite_snapshot/VisualPrototypeSandboxBuilder/scripts/validate_visual_sandbox_outputs.py": 40,
    "03_protocol/gs_wallet_accounting_responsibility_audit.md": 20,
    "03_protocol/8001_runtime_vs_gs_responsibility_matrix.md": 20,
    "03_protocol/8001_vabs_legacy_alias_apply_summary.md": 15,
    "09_release/WORKFLOW_CONTENT_INTEGRITY_AUDIT.md": 30,
    "09_release/visual_sandbox_builder_skill_adoption.md": 10,
    "09_release/future_game_visual_sandbox_builder_playbook.md": 10,
}

TEXT_SUFFIXES = {".md", ".txt", ".json", ".jsonl", ".csv", ".py", ".js", ".css", ".html", ".toml", ".yaml", ".yml", ".xml"}
UNSAFE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".svg", ".gif", ".har", ".mp4", ".mov", ".webm", ".zip", ".pdf", ".fnt", ".atlas", ".skel", ".bin"}
SAFE_URL_HOSTS = {"github.com", "raw.githubusercontent.com", "api.github.com", "example.com"}

UNSAFE_TEXT_PARTS = [
    "/" + "Users" + "/",
    "Documents/Dev/" + "Staging",
    "docs-" + "internal",
    "default-" + "beta",
    "cgs-" + "beta",
    "discreet" + "gaming.com",
    "local" + "host",
    "drop" + "box.com",
    "google.com/" + "document",
    "SID" + "=",
    "X-" + "Signature",
    "Secret" + "Key",
]

URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
TOKENIZED_URL_RE = re.compile(r"(?i)https?://[^\s)>\]\"']*(?:[?&](?:token|sid|signature|pass|key|auth|jwt|session|hash)=)[^\s)>\]\"']+")
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
SECRET_ASSIGN_RE = re.compile(r"(?i)\b(?:password|secret|token|sid|signature|jwt|auth|session|hash)\b\s*[:=]\s*[\'\"]?(?!\[REDACTED|unknown|null|false|true)[A-Za-z0-9_./+=:-]{12,}")
SCAFFOLD_BODY_RE = re.compile(r"02_reference_assets/(?:authorized_raw|authorized_normalized|quarantine)/(?!\[REDACTED_ASSET_FILE\])[^\s,\"']+")


def fail(message: str) -> None:
    FAILURES.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def iter_files():
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            yield path


def line_count(path: Path) -> int:
    text = read_text(path)
    return len(text.splitlines()) if text else 0


def check_required_depth() -> None:
    for rel, minimum in MIN_LINES.items():
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")
            continue
        count = line_count(path)
        print(f"{rel}: {count} lines")
        if count < minimum:
            fail(f"{rel} has {count} lines, expected at least {minimum}")
        if count <= 1:
            fail(f"one-line placeholder suspected: {rel}")


def check_file_shapes() -> None:
    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in UNSAFE_SUFFIXES:
            fail(f"unsafe media/raw-capture file included: {rel}")
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name != ".gitignore":
            fail(f"unexpected non-text file included: {rel}")
        if any(part in {"screenshots", "har", "event_logs", "videos", "node_modules", "dist", "build"} for part in path.parts):
            fail(f"unsafe generated/raw-capture directory included: {rel}")
        if any(part in {"assets_placeholder", "scripts_reference"} for part in path.parts):
            fail(f"visual sandbox placeholder body directory included: {rel}")
        if "11_prototypes" in path.parts:
            fail(f"local visual sandbox prototype file included: {rel}")
        if path.name == "package.json" and "06_resulting_code" in path.parts:
            fail(f"package manifest under resulting code is not allowed: {rel}")


def check_markdown_lines() -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for number, line in enumerate(read_text(path).splitlines(), 1):
            if len(line) > 250:
                fail(f"Markdown line exceeds 250 characters: {rel}:{number}")


def check_text_safety() -> None:
    for path in iter_files():
        rel = path.relative_to(ROOT).as_posix()
        text = read_text(path)
        lower_text = text.lower()
        for unsafe in UNSAFE_TEXT_PARTS:
            if unsafe.lower() in lower_text:
                fail(f"unsafe term present in {rel}")
        if TOKENIZED_URL_RE.search(text):
            fail(f"tokenized URL present: {rel}")
        if EMAIL_RE.search(text):
            fail(f"email-like value present: {rel}")
        if SECRET_ASSIGN_RE.search(text):
            fail(f"secret-like assignment present: {rel}")
        if SCAFFOLD_BODY_RE.search(text):
            fail(f"unredacted scaffold asset body path present: {rel}")
        for url in URL_RE.findall(text):
            host = (urlparse(url).hostname or "").lower()
            if host and host not in SAFE_URL_HOSTS:
                fail(f"non-allowlisted URL host {host} present: {rel}")


def check_status_wording() -> None:
    readme = read_text(ROOT / "README.md") if (ROOT / "README.md").exists() else ""
    reviewer = read_text(ROOT / "REVIEWER_START_HERE.md") if (ROOT / "REVIEWER_START_HERE.md").exists() else ""
    for phrase in [
        "raw-safe sanitized review checkpoint",
        "runtime API inspection",
        "No production client implementation was generated",
        "GameClientBuilder implementation remains blocked",
        "GameServerRegistrar generation remains blocked",
        "release blocked",
    ]:
        if phrase not in readme:
            fail(f"README.md missing truthful status phrase: {phrase}")
    for phrase in [
        "runtime_api_inspection_report.md",
        "runtime_payload_adapter_gap_analysis.md",
        "ProtocolAndSchemaMapper/handoff.json",
        "GsResponsibilityBoundaryAudit/handoff.json",
        "WalletAndLaunchTester/SKILL.md",
        "GameServerRegistrar/SKILL.md",
    ]:
        if phrase not in reviewer:
            fail(f"REVIEWER_START_HERE.md missing reference: {phrase}")


def check_json_csv_python() -> None:
    json_count = 0
    csv_count = 0
    py_count = 0
    for path in iter_files():
        if path.suffix.lower() == ".json":
            json.loads(read_text(path))
            json_count += 1
        if path.suffix.lower() == ".csv":
            with path.open("r", encoding="utf-8", newline="") as handle:
                list(csv.reader(handle))
            csv_count += 1
        if path.suffix.lower() == ".py":
            ast.parse(read_text(path), filename=str(path))
            py_count += 1
    print(f"json_ok={json_count} csv_ok={csv_count} python_ok={py_count}")


def main() -> int:
    check_required_depth()
    check_file_shapes()
    check_markdown_lines()
    check_text_safety()
    check_status_wording()
    check_json_csv_python()
    if FAILURES:
        print("PUBLIC EXPORT VALIDATION FAILED")
        for failure in FAILURES:
            print(f"- {failure}")
        return 1
    print("PUBLIC EXPORT VALIDATION PASSED")
    print(f"files_checked={sum(1 for _ in iter_files())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
