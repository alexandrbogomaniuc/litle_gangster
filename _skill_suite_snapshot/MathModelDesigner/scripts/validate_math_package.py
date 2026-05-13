#!/usr/bin/env python3
"""Validate minimal math_package.json structure."""
import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("math_package")
    args = parser.parse_args()
    path = Path(args.math_package)
    if not path.is_file():
        raise SystemExit(f"ERROR: math package not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in ["game_id", "rtp_variants", "bets", "features", "rng_owner", "result_owner"]:
        if key not in data:
            raise SystemExit(f"ERROR: missing math package key: {key}")
    if not data["rtp_variants"]:
        raise SystemExit("ERROR: rtp_variants must not be empty")
    print("OK: math package structure valid")


if __name__ == "__main__":
    main()

