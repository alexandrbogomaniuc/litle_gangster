#!/usr/bin/env python3
"""Tiny deterministic RTP simulation template for placeholder math packages."""
import argparse
import json
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, required=True)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--bet", type=int, default=100)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.rounds <= 0 or args.bet <= 0:
        raise SystemExit("ERROR: rounds and bet must be positive")
    rng = random.Random(args.seed)
    total_win = 0
    for _ in range(args.rounds):
        total_win += args.bet * rng.choice([0, 0, 0, 1, 2, 5])
    data = {"rounds": args.rounds, "seed": args.seed, "total_bet": args.rounds * args.bet, "total_win": total_win}
    Path(args.output).write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(f"OK: wrote simulation {args.output}")


if __name__ == "__main__":
    main()

