#!/usr/bin/env python3
"""Validate a MathProfileCalibrator report JSON has required gate fields."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = {
    "profilesCalibrated",
    "trainGateStatus",
    "validationGateStatus",
    "profilesWithinTolerance",
    "profilesOutsideTolerance",
    "scaleMode",
    "bonusBuyStatus",
    "tailMaxWinStatus",
    "backendAdapterAllowed",
    "registrationGenerationAllowed",
    "exactValuesFinal",
    "certificationStatus",
    "profileResults",
}

REQUIRED_PROFILE_FIELDS = {
    "mathProfileId",
    "rtpLevel",
    "volatilityLevel",
    "targetRtpPercent",
    "observedRtpPercent",
    "deltaFromTarget",
    "passFailAgainstTolerance",
}


def validate_report(data: dict[str, Any]) -> tuple[bool, list[str]]:
    errors: list[str] = []
    missing = sorted(REQUIRED_TOP_LEVEL - set(data))
    if missing:
        errors.append("missing top-level fields: " + ", ".join(missing))

    profiles = data.get("profileResults")
    if not isinstance(profiles, list) or not profiles:
        errors.append("profileResults must be a non-empty list")
        return False, errors

    for index, profile in enumerate(profiles):
        if not isinstance(profile, dict):
            errors.append(f"profileResults[{index}] must be an object")
            continue
        profile_missing = sorted(REQUIRED_PROFILE_FIELDS - set(profile))
        if profile_missing:
            errors.append(f"profileResults[{index}] missing fields: " + ", ".join(profile_missing))

    if data.get("validationSeedsUsedForTuning") is True:
        errors.append("validationSeedsUsedForTuning must not be true")
    if data.get("postSpinPayoutScalingUsedAsReleaseMath") is True:
        errors.append("postSpinPayoutScalingUsedAsReleaseMath must not be true")
    if data.get("certificationStatus") is True and data.get("exactValuesFinal") is not True:
        errors.append("certificationStatus=true requires exactValuesFinal=true")
    return not errors, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    path = Path(args.input)
    data = json.loads(path.read_text(encoding="utf-8"))
    ok, errors = validate_report(data)
    print(json.dumps({"valid": ok, "errors": errors}, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
