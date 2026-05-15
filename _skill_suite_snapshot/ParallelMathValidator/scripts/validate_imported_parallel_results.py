#!/usr/bin/env python3
"""Validate imported ParallelMathValidator result packages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

PROFILE_FIELDS = [
    "mathProfileId",
    "rtpLevel",
    "volatilityLevel",
    "roundCount",
    "rtp",
    "standardDeviation",
    "hitRate",
    "capFrequency",
    "maxObservedWin",
]


def load_json(path: str) -> dict[str, Any]:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def fail(errors: list[str]) -> int:
    print(json.dumps({"ok": False, "errors": errors}, indent=2, sort_keys=True))
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results_json", help="Results JSON path, or '-' for stdin")
    args = parser.parse_args()

    data = load_json(args.results_json)
    errors: list[str] = []

    seed_policy = data.get("seedPolicy") or data.get("seed_policy")
    if not isinstance(seed_policy, dict):
        errors.append("seedPolicy object is required")
    else:
        train_seed = seed_policy.get("trainSeedFamily")
        validation_seed = seed_policy.get("validationSeedFamily")
        if not train_seed:
            errors.append("seedPolicy.trainSeedFamily is required")
        if not validation_seed:
            errors.append("seedPolicy.validationSeedFamily is required")
        if train_seed and validation_seed and train_seed == validation_seed:
            errors.append("train and validation seed families must be separate")
        if seed_policy.get("validationSeedsUsedForTuning") is not False:
            errors.append("validationSeedsUsedForTuning must be false")

    profiles = data.get("profileResults") or data.get("profiles")
    if not isinstance(profiles, list) or not profiles:
        errors.append("profileResults non-empty list is required")
    else:
        expected_count = int(data.get("expectedProfilesCount") or 9)
        if len(profiles) != expected_count:
            errors.append(f"profileResults count {len(profiles)} does not match expected {expected_count}")
        for index, profile in enumerate(profiles):
            if not isinstance(profile, dict):
                errors.append(f"profileResults[{index}] must be an object")
                continue
            for field in PROFILE_FIELDS:
                if field not in profile:
                    errors.append(f"profileResults[{index}] missing {field}")
            if data.get("bonusBuyApplicable") is True and "bonusBuyEv" not in profile:
                errors.append(f"profileResults[{index}] missing bonusBuyEv")
            if data.get("frbApplicable") is True and "frbPromoEv" not in profile:
                errors.append(f"profileResults[{index}] missing frbPromoEv")

    if "machineReadableStatus" not in data:
        errors.append("machineReadableStatus is required")

    cert_status = data.get("certificationStatus")
    cert_claim = data.get("certificationClaim")
    cert_approved = data.get("certificationApproved") is True
    if (cert_status is True or cert_claim) and not cert_approved:
        errors.append("certification claim/status requires certificationApproved=true")

    if errors:
        return fail(errors)

    print(json.dumps({"ok": True, "importedResultsValid": True, "profilesTestedCount": len(profiles)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
