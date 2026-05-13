#!/usr/bin/env python3
"""Compute simple RTP confidence summary from simulation JSON rows."""
import argparse
import json
import math
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("simulation_json", help="JSON with rounds, total_bet, total_win")
    args = parser.parse_args()
    path = Path(args.simulation_json)
    if not path.is_file():
        raise SystemExit(f"ERROR: simulation file not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    total_bet = float(data.get("total_bet", 0))
    total_win = float(data.get("total_win", 0))
    rounds = int(data.get("rounds", 0))
    if total_bet <= 0 or rounds <= 0:
        raise SystemExit("ERROR: total_bet and rounds must be positive")
    rtp = total_win / total_bet
    stderr_note = "approximation requires per-round variance for real confidence interval"
    print(json.dumps({"rounds": rounds, "rtp": rtp, "stderr_note": stderr_note, "sqrt_rounds": math.sqrt(rounds)}, indent=2))


if __name__ == "__main__":
    main()

