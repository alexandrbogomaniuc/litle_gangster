#!/usr/bin/env python3
"""Validate a ParallelMathValidator request JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

RTP_LABELS = ["LOW", "MEDIUM", "HIGH"]
VOL_LABELS = ["LOW", "MEDIUM", "HIGH"]


def load_json(path: str) -> dict[str, Any]:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def bool_value(data: dict[str, Any], *keys: str) -> bool | None:
    for key in keys:
        if key in data:
            return bool(data[key])
    return None


def fail(errors: list[str]) -> int:
    print(json.dumps({"ok": False, "errors": errors}, indent=2, sort_keys=True))
    return 1


def normalize_rtp_levels(raw: Any) -> dict[str, float] | None:
    if not isinstance(raw, dict):
        return None
    try:
        return {str(k).upper(): float(v) for k, v in raw.items()}
    except (TypeError, ValueError):
        return None


def normalize_volatility(raw: Any) -> list[str] | None:
    if isinstance(raw, dict):
        return [str(k).upper() for k in raw.keys()]
    if isinstance(raw, list):
        return [str(v).upper() for v in raw]
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request_json", help="Request JSON path, or '-' for stdin")
    args = parser.parse_args()

    data = load_json(args.request_json)
    errors: list[str] = []

    rtp = normalize_rtp_levels(data.get("rtpLevels") or data.get("rtp_levels"))
    if rtp is None:
        errors.append("rtpLevels must be an object with LOW, MEDIUM, HIGH")
    elif set(rtp) != set(RTP_LABELS):
        errors.append("rtpLevels must contain exactly LOW, MEDIUM, HIGH")
    else:
        values = [rtp[label] for label in RTP_LABELS]
        for label, value in zip(RTP_LABELS, values):
            if value < 91.00 or value > 99.70:
                errors.append(f"{label} RTP {value:.2f} outside 91.00-99.70")
        if not (values[0] < values[1] < values[2]):
            errors.append("RTP values must be strictly ascending: LOW < MEDIUM < HIGH")

    vol = normalize_volatility(data.get("volatilityLevels") or data.get("volatility_levels"))
    if vol is None:
        errors.append("volatilityLevels must contain LOW, MEDIUM, HIGH")
    elif set(vol) != set(VOL_LABELS):
        errors.append("volatilityLevels must contain exactly LOW, MEDIUM, HIGH")

    profiles = data.get("profiles") or data.get("profileMatrix") or data.get("profile_matrix")
    profiles_planned = bool_value(data, "profileMatrixPlanned", "profile_matrix_planned")
    if isinstance(profiles, list):
        if len(profiles) != 9:
            errors.append("profiles must contain 9 entries")
        combos = set()
        for index, profile in enumerate(profiles):
            if not isinstance(profile, dict):
                errors.append(f"profile[{index}] must be an object")
                continue
            pid = profile.get("mathProfileId") or profile.get("math_profile_id")
            rtp_level = str(profile.get("rtpLevel") or profile.get("rtp_level") or "").upper()
            vol_level = str(profile.get("volatilityLevel") or profile.get("volatility_level") or "").upper()
            if not pid:
                errors.append(f"profile[{index}] missing mathProfileId")
            if rtp_level not in RTP_LABELS:
                errors.append(f"profile[{index}] invalid rtpLevel")
            if vol_level not in VOL_LABELS:
                errors.append(f"profile[{index}] invalid volatilityLevel")
            combos.add((rtp_level, vol_level))
        expected = {(r, v) for r in RTP_LABELS for v in VOL_LABELS}
        if combos != expected:
            errors.append("profiles must cover every LOW/MEDIUM/HIGH RTP x LOW/MEDIUM/HIGH volatility combination")
    elif not profiles_planned:
        errors.append("profiles must exist, or profileMatrixPlanned must be true")

    if not data.get("simulationScope") and not data.get("simulation_scope"):
        errors.append("simulationScope must be declared")

    for canonical, snake in (
        ("bonusBuyExists", "bonus_buy_exists"),
        ("frbExists", "frb_exists"),
        ("jackpotExists", "jackpot_exists"),
    ):
        if bool_value(data, canonical, snake) is None:
            errors.append(f"{canonical} must be declared true/false")

    if errors:
        return fail(errors)

    print(json.dumps({"ok": True, "profilesExpectedCount": 9, "requestValid": True}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
