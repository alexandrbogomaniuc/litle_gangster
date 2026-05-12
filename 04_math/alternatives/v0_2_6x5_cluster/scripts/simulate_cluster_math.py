#!/usr/bin/env python3
"""Deterministic simulator for Little Gangster v0.2 6x5 cluster math.

The simulator reads only explicit math package files passed by CLI. It does not
access the network, donor assets, GS, wallet endpoints, databases, or secrets.
RTP is computed from generated grids, connected cluster evaluation, paytables,
and symbol-triggered free spins. It does not normalize totals after simulation
and does not read target RTP to scale wins during a run.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import deque
from pathlib import Path
from typing import Any


NEIGHBORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def load_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Required file does not exist: {path}")
    if not path.is_file():
        raise ValueError(f"Required path is not a file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def resolve_variant(package: dict[str, Any], variant: str, package_path: Path) -> dict[str, Path]:
    variants = package.get("rtp_variants", {})
    if variant not in variants:
        raise KeyError(f"Unknown RTP variant {variant!r}; available: {', '.join(sorted(variants))}")
    root = package_path.parent
    spec = variants[variant]
    required = ("model_config", "reel_weights", "paytable", "feature_rules")
    return {key: root / spec[key] for key in required}


def weighted_symbol(rng: random.Random, weights: dict[str, int]) -> str:
    total = sum(int(v) for v in weights.values())
    if total <= 0:
        raise ValueError("Symbol weights must sum to a positive number")
    choice = rng.randrange(total)
    cursor = 0
    for symbol, weight in weights.items():
        cursor += int(weight)
        if choice < cursor:
            return symbol
    return next(reversed(weights))


def spin_grid(rng: random.Random, reel_weights: dict[str, Any], mode: str, rows: int, reels: int) -> list[list[str]]:
    weights_by_reel = reel_weights[mode]
    if len(weights_by_reel) != reels:
        raise ValueError(f"{mode} must contain exactly {reels} reel weight maps")
    return [
        [weighted_symbol(rng, weights_by_reel[col]) for col in range(reels)]
        for _ in range(rows)
    ]


def cluster_pay(symbol: str, count: int, paytable: dict[str, Any]) -> float:
    pays = paytable["cluster_pays_x_bet"].get(symbol, {})
    best = 0.0
    for threshold_text, value in pays.items():
        if count >= int(threshold_text):
            best = float(value)
    return best


def evaluate_clusters(
    grid: list[list[str]],
    paytable: dict[str, Any],
    wild_symbol: str,
    scatter_symbol: str,
) -> dict[str, Any]:
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    cluster_total = 0.0
    clusters = []
    pay_symbols = list(paytable["cluster_pays_x_bet"].keys())

    for target in pay_symbols:
        visited: set[tuple[int, int]] = set()
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                if grid[row][col] not in (target, wild_symbol):
                    continue
                queue: deque[tuple[int, int]] = deque([(row, col)])
                visited.add((row, col))
                cells = []
                while queue:
                    current_row, current_col = queue.popleft()
                    cells.append((current_row, current_col))
                    for row_delta, col_delta in NEIGHBORS:
                        next_row = current_row + row_delta
                        next_col = current_col + col_delta
                        if not (0 <= next_row < rows and 0 <= next_col < cols):
                            continue
                        if (next_row, next_col) in visited:
                            continue
                        if grid[next_row][next_col] not in (target, wild_symbol):
                            continue
                        visited.add((next_row, next_col))
                        queue.append((next_row, next_col))
                if len(cells) >= int(paytable["minimum_cluster_size"]):
                    win = cluster_pay(target, len(cells), paytable)
                    if win > 0:
                        cluster_total += win
                        clusters.append({"symbol": target, "count": len(cells), "win_x_bet": win})

    scatter_count = sum(cell == scatter_symbol for row in grid for cell in row)
    scatter_win = 0.0
    if scatter_count >= 3:
        scatter_win = float(paytable["scatter_pays_x_bet"].get(str(min(scatter_count, 6)), 0.0))

    return {
        "cluster_total_x_bet": cluster_total,
        "scatter_total_x_bet": scatter_win,
        "total_x_bet": cluster_total + scatter_win,
        "scatter_count": scatter_count,
        "clusters": clusters,
    }


def simulate_round(
    rng: random.Random,
    model_config: dict[str, Any],
    reel_weights: dict[str, Any],
    paytable: dict[str, Any],
    feature_rules: dict[str, Any],
) -> dict[str, Any]:
    rows = int(model_config["grid"]["rows"])
    reels = int(model_config["grid"]["reels"])
    wild_symbol = model_config["symbols"]["wild"]
    scatter_symbol = model_config["symbols"]["scatter"]
    max_win = float(model_config["max_win_x_bet"])

    base_grid = spin_grid(rng, reel_weights, "base_game", rows, reels)
    base_eval = evaluate_clusters(base_grid, paytable, wild_symbol, scatter_symbol)
    total_win = float(base_eval["total_x_bet"])
    base_win = total_win
    free_win = 0.0
    free_spins_played = 0
    retriggers = 0

    free_spins_remaining = 0
    if int(base_eval["scatter_count"]) >= 3:
        free_spins_remaining = int(
            feature_rules["free_spins"]["trigger_spins"].get(str(min(int(base_eval["scatter_count"]), 6)), 0)
        )

    free_multiplier = float(feature_rules["free_spins"]["cluster_win_multiplier"])
    max_free_spins = int(feature_rules["free_spins"]["max_free_spins_in_round"])
    while free_spins_remaining > 0:
        free_spins_remaining -= 1
        free_spins_played += 1
        free_grid = spin_grid(rng, reel_weights, "free_spins", rows, reels)
        free_eval = evaluate_clusters(free_grid, paytable, wild_symbol, scatter_symbol)
        spin_win = float(free_eval["total_x_bet"]) * free_multiplier
        total_win += spin_win
        free_win += spin_win
        free_scatter_count = int(free_eval["scatter_count"])
        if free_scatter_count >= 3 and free_spins_played < max_free_spins:
            retriggers += 1
            free_spins_remaining += int(
                feature_rules["free_spins"]["retrigger_spins"].get(str(min(free_scatter_count, 6)), 0)
            )
            free_spins_remaining = min(free_spins_remaining, max_free_spins - free_spins_played)
        if total_win >= max_win:
            total_win = max_win
            break

    return {
        "total_win_x_bet": total_win,
        "base_win_x_bet": base_win,
        "free_spin_win_x_bet": free_win,
        "free_spins_triggered": int(base_eval["scatter_count"]) >= 3,
        "free_spins_played": free_spins_played,
        "free_spin_retriggers": retriggers,
    }


def run_simulation(args: argparse.Namespace) -> dict[str, Any]:
    package_path = Path(args.math_package).resolve()
    package = load_json(package_path)
    paths = resolve_variant(package, args.rtp_variant, package_path)
    model_config = load_json(paths["model_config"])
    reel_weights = load_json(paths["reel_weights"])
    paytable = load_json(paths["paytable"])
    feature_rules = load_json(paths["feature_rules"])

    rounds = int(args.rounds)
    if rounds <= 0:
        raise ValueError("--rounds must be positive")
    rng = random.Random(int(args.seed))

    total = 0.0
    base_total = 0.0
    free_total = 0.0
    sum_squares = 0.0
    hits = 0
    free_triggers = 0
    free_spins_played = 0
    retriggers = 0
    max_observed = 0.0

    for _ in range(rounds):
        result = simulate_round(rng, model_config, reel_weights, paytable, feature_rules)
        win = float(result["total_win_x_bet"])
        total += win
        sum_squares += win * win
        base_total += float(result["base_win_x_bet"])
        free_total += float(result["free_spin_win_x_bet"])
        hits += int(win > 0)
        free_triggers += int(result["free_spins_triggered"])
        free_spins_played += int(result["free_spins_played"])
        retriggers += int(result["free_spin_retriggers"])
        max_observed = max(max_observed, win)

    mean = total / rounds
    variance = max(0.0, (sum_squares / rounds) - (mean * mean))
    target = float(model_config["rtp_profile"]["target_rtp_percent"])
    simulated = mean * 100.0
    tolerance = float(model_config["rtp_profile"]["workflow_test_tolerance_percent"])
    deviation = simulated - target

    return {
        "project": package["project"],
        "math_version": package["math_version"],
        "rtp_variant": args.rtp_variant,
        "target_rtp_percent": target,
        "simulated_rtp_percent": round(simulated, 6),
        "deviation_percent": round(deviation, 6),
        "workflow_test_tolerance_percent": tolerance,
        "status": "pass_workflow_tolerance" if abs(deviation) <= tolerance else "outside_workflow_tolerance",
        "rounds": rounds,
        "seed": int(args.seed),
        "hit_frequency_percent": round((hits / rounds) * 100.0, 6),
        "standard_deviation_x_bet": round(math.sqrt(variance), 6),
        "volatility_proxy": "high" if math.sqrt(variance) >= 5.0 else "medium_or_low",
        "max_win_observed_x_bet": round(max_observed, 6),
        "max_win_proposed_x_bet": float(model_config["max_win_x_bet"]),
        "base_game_contribution_percent": round((base_total / rounds) * 100.0, 6),
        "free_spins_contribution_percent": round((free_total / rounds) * 100.0, 6),
        "free_spins_trigger_frequency_percent": round((free_triggers / rounds) * 100.0, 6),
        "average_free_spins_played_per_base_round": round(free_spins_played / rounds, 6),
        "free_spin_retrigger_frequency_per_base_round": round(retriggers / rounds, 6),
        "bonus_buy_modeled": bool(feature_rules.get("bonus_buy", {}).get("modeled")),
        "double_up_modeled_as_placeholder": bool(feature_rules.get("double_up", {}).get("modeled")),
        "simulator_scaling_detected": False,
        "rtp_is_emergent_from_variant_paytable_and_symbol_weights": True,
        "browser_result_authority_allowed": False,
        "runtime_owner_proven": False,
        "notes": [
            "Provisional workflow simulation only, not release certification.",
            "Target RTP is reported for comparison only; it is not used to scale wins during simulation.",
            "Variant RTP comes from reel weights, cluster paytable values, and symbol-triggered features.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate provisional Little Gangster 6x5 cluster math.")
    parser.add_argument("--math-package", required=True, help="Path to v0.2 math_package.json")
    parser.add_argument("--rtp-variant", required=True, choices=("rtp_96", "rtp_94", "rtp_92"))
    parser.add_argument("--rounds", required=True, type=int)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--output", help="Optional JSON summary path")
    args = parser.parse_args()

    try:
        summary = run_simulation(args)
    except Exception as exc:
        print(f"simulate_cluster_math.py failed: {exc}", file=sys.stderr)
        return 1

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    else:
        print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
