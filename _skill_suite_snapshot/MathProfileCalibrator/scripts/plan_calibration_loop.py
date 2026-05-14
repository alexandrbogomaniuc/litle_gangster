#!/usr/bin/env python3
"""Create a 9-profile calibration loop plan from a valid RTP request."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from validate_rtp_request import RTP_LEVELS, VOLATILITY_LEVELS, validate_request  # noqa: E402


def profile_prefix(game_key: str, game_id: str | None, explicit: str | None) -> str:
    if explicit:
        return explicit
    cleaned = re.sub(r"[^A-Za-z0-9]+", "_", game_key).strip("_").upper()
    return f"{cleaned}_{game_id}" if game_id else cleaned


def build_plan(args: argparse.Namespace) -> dict:
    request = {
        "rtpLevels": {"LOW": args.low, "MEDIUM": args.medium, "HIGH": args.high},
        "volatilityLevels": list(VOLATILITY_LEVELS),
    }
    ok, errors, validation = validate_request(request)
    if not ok:
        return {"valid": False, "errors": errors}

    prefix = profile_prefix(args.game_key, args.game_id, args.profile_prefix)
    profiles = []
    for rtp in RTP_LEVELS:
        for vol in VOLATILITY_LEVELS:
            target = float(validation["rtpLevels"][rtp])
            profiles.append(
                {
                    "mathProfileId": f"{prefix}_RTP_{rtp}_VOL_{vol}",
                    "gameKey": args.game_key,
                    "gameId": args.game_id,
                    "rtpLevel": rtp,
                    "volatilityLevel": vol,
                    "targetRtpPercent": target,
                    "targetReturnMultiplier": round(target / 100.0, 8),
                    "trainGateStatus": "pending",
                    "validationGateStatus": "pending",
                    "tailMaxWinStatus": "pending",
                    "bonusBuyStatus": "pending_or_not_in_scope",
                }
            )

    return {
        "valid": True,
        "schemaVersion": "math-profile-calibration-plan-v1",
        "gameKey": args.game_key,
        "gameId": args.game_id,
        "scaleMode": args.scale_mode,
        "maxIterations": args.max_iterations,
        "defaultTrainTolerancePercentagePoints": args.train_tolerance,
        "validationTuningAllowed": False,
        "postSpinPayoutScalingAllowed": False,
        "expectedProfileCount": 9,
        "profiles": profiles,
        "phases": [
            "rtp_request_validation",
            "train_simulation_planning",
            "train_seed_calibration_loop",
            "validation_seed_gate",
            "tail_max_win_and_bonus_buy_gates",
            "handoff",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--game-key", required=True)
    parser.add_argument("--game-id")
    parser.add_argument("--profile-prefix")
    parser.add_argument("--low", type=float, required=True)
    parser.add_argument("--medium", type=float, required=True)
    parser.add_argument("--high", type=float, required=True)
    parser.add_argument("--scale-mode", default="fast_train_matrix")
    parser.add_argument("--max-iterations", type=int, default=3)
    parser.add_argument("--train-tolerance", type=float, default=2.0)
    parser.add_argument("--output")
    args = parser.parse_args()

    plan = build_plan(args)
    text = json.dumps(plan, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if plan.get("valid") else 1


if __name__ == "__main__":
    raise SystemExit(main())
