#!/usr/bin/env python3
"""Validate a requested LOW/MEDIUM/HIGH RTP and volatility profile request."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

RTP_LEVELS = ("LOW", "MEDIUM", "HIGH")
VOLATILITY_LEVELS = ("LOW", "MEDIUM", "HIGH")
MIN_RTP = 91.0
MAX_RTP = 99.7


def load_request(args: argparse.Namespace) -> dict[str, Any]:
    if args.input:
        return json.loads(Path(args.input).read_text(encoding="utf-8"))
    return {
        "rtpLevels": {
            "LOW": args.low,
            "MEDIUM": args.medium,
            "HIGH": args.high,
        },
        "volatilityLevels": list(VOLATILITY_LEVELS),
    }


def add_error(errors: list[dict[str, Any]], code: str, message: str, level: str | None = None, value: Any = None) -> None:
    error: dict[str, Any] = {"code": code, "message": message}
    if level is not None:
        error["level"] = level
    if value is not None:
        error["value"] = value
    errors.append(error)


def validate_request(data: dict[str, Any]) -> tuple[bool, list[dict[str, Any]], dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    rtp = data.get("rtpLevels")
    if not isinstance(rtp, dict):
        add_error(errors, "missing_required_rtp_level", "rtpLevels must be an object with LOW, MEDIUM, HIGH")
        rtp = {}

    if set(rtp) != set(RTP_LEVELS):
        missing = [level for level in RTP_LEVELS if level not in rtp]
        extra = sorted(set(rtp) - set(RTP_LEVELS))
        for level in missing:
            add_error(errors, "missing_required_rtp_level", f"missing required RTP level {level}", level=level)
        for level in extra:
            add_error(errors, "unexpected_rtp_level", f"unexpected RTP level {level}", level=level)

    parsed: dict[str, float] = {}
    for level in RTP_LEVELS:
        try:
            value = float(rtp.get(level))
        except (TypeError, ValueError):
            add_error(errors, "invalid_rtp_number", f"{level} RTP must be numeric percent", level=level, value=rtp.get(level))
            continue
        normalized = round(value, 2)
        parsed[level] = normalized
        if value < MIN_RTP or value > MAX_RTP:
            if value < MIN_RTP:
                add_error(
                    errors,
                    "below_minimum_allowed_rtp",
                    f"{level} RTP {value:.2f} is below minimum allowed RTP {MIN_RTP:.2f}",
                    level=level,
                    value=round(value, 4),
                )
            if value > MAX_RTP:
                add_error(
                    errors,
                    "above_maximum_allowed_rtp",
                    f"{level} RTP {value:.2f} is above maximum allowed RTP {MAX_RTP:.2f}",
                    level=level,
                    value=round(value, 4),
                )

    if all(level in parsed for level in RTP_LEVELS):
        values = [parsed[level] for level in RTP_LEVELS]
        if len(set(values)) != len(values):
            add_error(errors, "duplicate_rtp_levels", "RTP values must be unique across LOW, MEDIUM, HIGH")
        if not (parsed["LOW"] < parsed["MEDIUM"] < parsed["HIGH"]):
            add_error(errors, "rtp_levels_not_strictly_ascending", "RTP values must satisfy LOW < MEDIUM < HIGH")

    volatility = data.get("volatilityLevels", list(VOLATILITY_LEVELS))
    if isinstance(volatility, dict):
        volatility_set = set(volatility)
    elif isinstance(volatility, list):
        volatility_set = set(str(item) for item in volatility)
    else:
        volatility_set = set()
    if volatility_set != set(VOLATILITY_LEVELS):
        add_error(errors, "invalid_volatility_levels", "volatilityLevels must contain exactly LOW, MEDIUM, HIGH")

    matrix = [
        {
            "rtpLevel": rtp_level,
            "volatilityLevel": volatility_level,
            "targetRtpPercent": parsed.get(rtp_level),
            "targetReturnMultiplier": round(parsed.get(rtp_level, 0.0) / 100.0, 8) if rtp_level in parsed else None,
        }
        for rtp_level in RTP_LEVELS
        for volatility_level in VOLATILITY_LEVELS
    ]
    result = {
        "valid": not errors,
        "errors": errors,
        "errorCodes": [error["code"] for error in errors],
        "allowedRtpRange": {
            "minimum": f"{MIN_RTP:.2f}",
            "maximum": f"{MAX_RTP:.2f}",
            "inclusive": True,
        },
        "rtpLevelsMustBeStrictlyAscending": True,
        "rtpLevels": parsed,
        "volatilityLevels": list(VOLATILITY_LEVELS),
        "expectedProfileCount": 9,
        "matrixPreview": matrix,
    }
    return not errors, errors, result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="Optional JSON request file")
    parser.add_argument("--low", type=float, default=None)
    parser.add_argument("--medium", type=float, default=None)
    parser.add_argument("--high", type=float, default=None)
    args = parser.parse_args()

    if not args.input and (args.low is None or args.medium is None or args.high is None):
        parser.error("provide --input or all of --low --medium --high")

    ok, _errors, result = validate_request(load_request(args))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
