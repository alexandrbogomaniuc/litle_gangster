#!/usr/bin/env python3
"""Extract or propose registration math fields from validation evidence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: str) -> dict[str, Any]:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def number(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def first(profile: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        if key in profile:
            return profile[key]
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evidence_json", help="Evidence JSON path, or '-' for stdin")
    args = parser.parse_args()

    data = load_json(args.evidence_json)
    profiles = data.get("profiles") or data.get("profileResults")
    if not isinstance(profiles, list) or not profiles:
        print(json.dumps({"ok": False, "errors": ["profiles/profileResults non-empty list is required"]}, indent=2, sort_keys=True))
        return 1

    extracted: list[dict[str, Any]] = []
    blockers: list[str] = []
    hard_errors: list[str] = []

    for index, profile in enumerate(profiles):
        if not isinstance(profile, dict):
            hard_errors.append(f"profile[{index}] must be an object")
            continue
        pid = first(profile, "mathProfileId", "math_profile_id")
        rtp_without_bf = number(first(profile, "RTP_WITHOUT_BF", "rtpWithoutBf", "rtp"))
        rtp_min_without_bf = number(first(profile, "RTP_MIN_WITHOUT_BF", "rtpMinWithoutBf", "rtpMin"))
        bf_rtp = number(first(profile, "BF_RTP", "bfRtp"))
        bf_rtp_min = number(first(profile, "BF_RTP_MIN", "bfRtpMin"))
        possible_models = number(first(profile, "POSSIBLE_MODELS", "possibleModels"))
        other_strategy_rtps = [number(v) for v in profile.get("otherStrategyRtps", [])]
        strategy_values = [v for v in [rtp_without_bf, bf_rtp, *other_strategy_rtps] if v is not None]

        if not pid:
            hard_errors.append(f"profile[{index}] missing mathProfileId")
        if rtp_without_bf is None:
            hard_errors.append(f"profile[{index}] missing RTP_WITHOUT_BF/rtpWithoutBf")
        if possible_models is None and strategy_values:
            possible_models = max(strategy_values)
        if possible_models is None:
            hard_errors.append(f"profile[{index}] cannot determine POSSIBLE_MODELS")
        if bf_rtp is not None and possible_models is not None and bf_rtp > possible_models + 1e-9:
            hard_errors.append(f"profile[{index}] BF_RTP {bf_rtp} exceeds POSSIBLE_MODELS {possible_models}")
        if strategy_values and possible_models is not None and possible_models + 1e-9 < max(strategy_values):
            hard_errors.append(f"profile[{index}] POSSIBLE_MODELS {possible_models} below max supported strategy RTP {max(strategy_values)}")

        cap_win = first(profile, "CAP_WIN_MULTIPLIER", "capWinMultiplier")
        max_win = first(profile, "MAX_WIN", "maxWin")
        possible_max_wins = first(profile, "POSSIBLE_MAX_WINS", "possibleMaxWins")
        if cap_win in (None, "", "unresolved"):
            blockers.append(f"{pid or index}: CAP_WIN_MULTIPLIER unresolved")
        if max_win in (None, "", "unresolved") and possible_max_wins in (None, "", "unresolved"):
            blockers.append(f"{pid or index}: MAX_WIN/POSSIBLE_MAX_WINS unresolved")

        extracted.append({
            "mathProfileId": pid,
            "POSSIBLE_MODELS": possible_models,
            "RTP_WITHOUT_BF": rtp_without_bf,
            "RTP_MIN_WITHOUT_BF": rtp_min_without_bf,
            "BF_RTP": bf_rtp,
            "BF_RTP_MIN": bf_rtp_min,
            "BF_BETS": first(profile, "BF_BETS", "bfBets"),
            "SD_KEYS": first(profile, "SD_KEYS", "sdKeys"),
            "CAP_WIN_MULTIPLIER": cap_win,
            "MAX_WIN": max_win,
            "POSSIBLE_MAX_WINS": possible_max_wins,
            "VOLATILITY": first(profile, "VOLATILITY", "volatilityLevel"),
            "profileDisplay": first(profile, "profileDisplay", "displayName")
        })

    if hard_errors:
        print(json.dumps({"ok": False, "errors": hard_errors, "blockers": blockers}, indent=2, sort_keys=True))
        return 1

    print(json.dumps({
        "ok": True,
        "registrationGenerationAllowed": not blockers,
        "blockers": blockers,
        "registrationMathFields": extracted
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
