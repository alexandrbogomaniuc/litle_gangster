#!/usr/bin/env python3
"""Deterministic simulator for the provisional Little Gangster math package.

This helper is intentionally local and self-contained. It reads only the math
package files passed on the command line, does not use the network, does not
read secrets, and does not call GS, wallet, browser, or donor systems.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Required file does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"Required path is not a file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_variant(package: dict[str, Any], variant_name: str, package_path: Path) -> dict[str, Any]:
    variants = package.get("rtp_variants", {})
    if variant_name not in variants:
        available = ", ".join(sorted(variants))
        raise KeyError(f"Unknown RTP variant {variant_name!r}. Available variants: {available}")
    root = package_path.parent
    variant = dict(variants[variant_name])
    for key in ("model_config", "reel_strips", "paytable", "feature_rules"):
        if key not in variant:
            raise KeyError(f"Variant {variant_name!r} is missing {key!r}")
        variant[key] = root / variant[key]
    return variant


def spin_grid(rng: random.Random, strips: list[list[str]], rows: int) -> list[list[str]]:
    grid: list[list[str]] = []
    for strip in strips:
        if len(strip) < rows:
            raise ValueError("Every reel strip must be at least as long as the visible row count")
        start = rng.randrange(len(strip))
        grid.append([strip[(start + offset) % len(strip)] for offset in range(rows)])
    return grid


def evaluate_grid(
    grid: list[list[str]],
    paylines: list[list[int]],
    paytable: dict[str, Any],
    wild_symbol: str,
    scatter_symbol: str,
) -> dict[str, Any]:
    line_wins = []
    line_total = 0.0
    symbol_pays = paytable["line_pays_x_bet"]
    for line_index, line in enumerate(paylines):
        visible = [grid[reel_index][row_index] for reel_index, row_index in enumerate(line)]
        target_symbol = None
        for symbol in visible:
            if symbol not in (wild_symbol, scatter_symbol):
                target_symbol = symbol
                break
        if target_symbol is None:
            target_symbol = wild_symbol
        if target_symbol == scatter_symbol:
            continue
        match_count = 0
        for symbol in visible:
            if symbol == target_symbol or symbol == wild_symbol:
                match_count += 1
            else:
                break
        pay = float(symbol_pays.get(target_symbol, {}).get(str(match_count), 0.0))
        if match_count >= 3 and pay > 0:
            line_total += pay
            line_wins.append(
                {
                    "line": line_index + 1,
                    "symbol": target_symbol,
                    "count": match_count,
                    "win_x_bet": pay,
                }
            )

    scatter_count = sum(column.count(scatter_symbol) for column in grid)
    scatter_pay = 0.0
    if scatter_count >= 3:
        scatter_pay = float(paytable["scatter_pays_x_bet"].get(str(min(scatter_count, 5)), 0.0))

    return {
        "line_total_x_bet": line_total,
        "scatter_total_x_bet": scatter_pay,
        "total_x_bet": line_total + scatter_pay,
        "scatter_count": scatter_count,
        "line_wins": line_wins,
    }


def simulate_round(
    rng: random.Random,
    model_config: dict[str, Any],
    reel_strips: dict[str, Any],
    paytable: dict[str, Any],
    feature_rules: dict[str, Any],
) -> dict[str, Any]:
    rows = int(model_config["grid"]["rows"])
    paylines = model_config["paylines"]
    wild_symbol = model_config["symbols"]["wild"]
    scatter_symbol = model_config["symbols"]["scatter"]
    payout_scale = float(model_config["rtp_profile"]["payout_scale"])
    max_win_x_bet = float(model_config["max_win_x_bet"])

    base_grid = spin_grid(rng, reel_strips["base_game"], rows)
    base_eval = evaluate_grid(base_grid, paylines, paytable, wild_symbol, scatter_symbol)
    base_win = base_eval["total_x_bet"] * payout_scale
    total_win = base_win
    free_spin_win = 0.0
    free_spins_played = 0
    free_spins_triggered = False
    retriggers = 0

    free_spins_remaining = 0
    scatter_count = int(base_eval["scatter_count"])
    if scatter_count >= 3:
        free_spins_triggered = True
        free_spins_remaining = int(feature_rules["free_spins"]["trigger_spins"].get(str(min(scatter_count, 5)), 0))

    max_free_spins = int(feature_rules["free_spins"]["max_free_spins_in_round"])
    free_spin_multiplier = float(feature_rules["free_spins"]["line_win_multiplier"])
    while free_spins_remaining > 0:
        free_spins_remaining -= 1
        free_spins_played += 1
        free_grid = spin_grid(rng, reel_strips["free_spins"], rows)
        free_eval = evaluate_grid(free_grid, paylines, paytable, wild_symbol, scatter_symbol)
        spin_win = free_eval["total_x_bet"] * free_spin_multiplier * payout_scale
        total_win += spin_win
        free_spin_win += spin_win
        free_scatter_count = int(free_eval["scatter_count"])
        if free_scatter_count >= 3 and free_spins_played < max_free_spins:
            retriggers += 1
            free_spins_remaining += int(
                feature_rules["free_spins"]["retrigger_spins"].get(str(min(free_scatter_count, 5)), 0)
            )
            free_spins_remaining = min(free_spins_remaining, max_free_spins - free_spins_played)
        if total_win >= max_win_x_bet:
            total_win = max_win_x_bet
            break

    return {
        "total_win_x_bet": total_win,
        "base_win_x_bet": base_win,
        "free_spin_win_x_bet": free_spin_win,
        "free_spins_triggered": free_spins_triggered,
        "free_spins_played": free_spins_played,
        "free_spin_retriggers": retriggers,
    }


def run_simulation(args: argparse.Namespace) -> dict[str, Any]:
    package_path = Path(args.math_package).resolve()
    package = load_json(package_path)
    variant_paths = resolve_variant(package, args.rtp_variant, package_path)
    model_config = load_json(variant_paths["model_config"])
    reel_strips = load_json(variant_paths["reel_strips"])
    paytable = load_json(variant_paths["paytable"])
    feature_rules = load_json(variant_paths["feature_rules"])

    rounds = int(args.rounds)
    if rounds <= 0:
        raise ValueError("--rounds must be a positive integer")
    rng = random.Random(int(args.seed))

    total = 0.0
    base_total = 0.0
    free_total = 0.0
    hit_count = 0
    free_trigger_count = 0
    free_spins_played = 0
    retrigger_count = 0
    max_observed = 0.0
    sum_squares = 0.0

    for _ in range(rounds):
        result = simulate_round(rng, model_config, reel_strips, paytable, feature_rules)
        win = float(result["total_win_x_bet"])
        total += win
        sum_squares += win * win
        base_total += float(result["base_win_x_bet"])
        free_total += float(result["free_spin_win_x_bet"])
        if win > 0:
            hit_count += 1
        if result["free_spins_triggered"]:
            free_trigger_count += 1
        free_spins_played += int(result["free_spins_played"])
        retrigger_count += int(result["free_spin_retriggers"])
        if win > max_observed:
            max_observed = win

    mean = total / rounds
    variance = max(0.0, (sum_squares / rounds) - (mean * mean))
    target_rtp = float(model_config["rtp_profile"]["target_rtp_percent"])
    simulated_rtp = mean * 100.0
    tolerance = float(model_config["rtp_profile"]["workflow_test_tolerance_percent"])
    deviation = simulated_rtp - target_rtp
    status = "pass_workflow_tolerance" if abs(deviation) <= tolerance else "outside_workflow_tolerance"

    summary = {
        "project": package["project"],
        "math_version": package["math_version"],
        "rtp_variant": args.rtp_variant,
        "target_rtp_percent": target_rtp,
        "simulated_rtp_percent": round(simulated_rtp, 6),
        "deviation_percent": round(deviation, 6),
        "workflow_test_tolerance_percent": tolerance,
        "status": status,
        "rounds": rounds,
        "seed": int(args.seed),
        "hit_frequency_percent": round((hit_count / rounds) * 100.0, 6),
        "standard_deviation_x_bet": round(math.sqrt(variance), 6),
        "volatility_proxy": "high" if math.sqrt(variance) >= 5.0 else "medium_or_low",
        "max_win_observed_x_bet": round(max_observed, 6),
        "max_win_proposed_x_bet": float(model_config["max_win_x_bet"]),
        "base_game_contribution_percent": round((base_total / rounds) * 100.0, 6),
        "free_spins_contribution_percent": round((free_total / rounds) * 100.0, 6),
        "free_spins_trigger_frequency_percent": round((free_trigger_count / rounds) * 100.0, 6),
        "average_free_spins_played_per_base_round": round(free_spins_played / rounds, 6),
        "free_spin_retrigger_frequency_per_base_round": round(retrigger_count / rounds, 6),
        "bonus_buy_modeled": bool(feature_rules.get("bonus_buy", {}).get("modeled")),
        "bonus_buy_contribution_to_base_rtp": "not included in base-spin RTP; optional feature EV must be tested separately",
        "browser_result_authority_allowed": False,
        "runtime_owner_proven": False,
        "notes": [
            "This is a provisional workflow-test simulation, not release certification.",
            "RNG uses a deterministic local pseudo-random seed for validation only.",
            "Production RNG/result authority must live in backend/new-games runtime, not the browser client.",
        ],
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate provisional Little Gangster math.")
    parser.add_argument("--math-package", required=True, help="Path to math_package.json")
    parser.add_argument("--rtp-variant", required=True, choices=("rtp_96", "rtp_94", "rtp_92"))
    parser.add_argument("--rounds", required=True, type=int, help="Number of base rounds to simulate")
    parser.add_argument("--seed", required=True, type=int, help="Deterministic validation seed")
    parser.add_argument("--output", help="Optional JSON summary output path")
    args = parser.parse_args()

    try:
        summary = run_simulation(args)
    except Exception as exc:
        print(f"simulate_math.py failed: {exc}", file=sys.stderr)
        return 1

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as handle:
            json.dump(summary, handle, indent=2, sort_keys=True)
            handle.write("\n")
    else:
        print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
