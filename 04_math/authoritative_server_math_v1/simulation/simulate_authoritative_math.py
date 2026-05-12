#!/usr/bin/env python3
"""Non-production deterministic smoke simulator for Little Gangster planning.

This script is not production math, not a backend adapter, not a wallet flow,
and not certification evidence. It only exercises local planning configs.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROWS = 5
COLS = 6
EXCLUDED_CLUSTER_SYMBOLS = {"wild", "rainbow", "coin", "special"}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def weighted_choice(rng: random.Random, entries: List[Dict[str, Any]]) -> str:
    total = sum(float(e["weight"]) for e in entries)
    pick = rng.random() * total
    seen = 0.0
    for entry in entries:
        seen += float(entry["weight"])
        if pick <= seen:
            return str(entry["symbol"])
    return str(entries[-1]["symbol"])


def generate_grid(rng: random.Random, symbols: List[Dict[str, Any]]) -> List[List[str]]:
    return [[weighted_choice(rng, symbols) for _ in range(COLS)] for _ in range(ROWS)]


def neighbors(r: int, c: int) -> List[Tuple[int, int]]:
    out = []
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            out.append((nr, nc))
    return out


def find_clusters(grid: List[List[str]], min_size: int) -> List[Dict[str, Any]]:
    visited = set()
    clusters = []
    for r in range(ROWS):
        for c in range(COLS):
            symbol = grid[r][c]
            if symbol in EXCLUDED_CLUSTER_SYMBOLS or (r, c) in visited:
                continue
            stack = [(r, c)]
            cells = []
            visited.add((r, c))
            while stack:
                cr, cc = stack.pop()
                cells.append({"row": cr, "col": cc})
                for nr, nc in neighbors(cr, cc):
                    if (nr, nc) not in visited and grid[nr][nc] == symbol:
                        visited.add((nr, nc))
                        stack.append((nr, nc))
            if len(cells) >= min_size:
                clusters.append({"symbol": symbol, "size": len(cells), "cells": cells})
    return clusters


def cluster_pay(cluster: Dict[str, Any], paytable: Dict[str, Any]) -> float:
    entries = paytable["payBySymbolAndClusterSize"].get(cluster["symbol"], [])
    size = int(cluster["size"])
    for entry in entries:
        if int(entry["min"]) <= size <= int(entry["max"]):
            return float(entry["pay"])
    return 0.0


def remove_and_refill(grid: List[List[str]], clusters: List[Dict[str, Any]], rng: random.Random, symbols: List[Dict[str, Any]]) -> Tuple[List[List[str]], List[Dict[str, int]], List[Dict[str, Any]]]:
    removed = {(cell["row"], cell["col"]) for cluster in clusters for cell in cluster["cells"]}
    removed_cells = [{"row": r, "col": c} for r, c in sorted(removed)]
    next_grid = [[grid[r][c] for c in range(COLS)] for r in range(ROWS)]
    refills = []
    for c in range(COLS):
        kept = [grid[r][c] for r in range(ROWS) if (r, c) not in removed]
        missing = ROWS - len(kept)
        new_symbols = [weighted_choice(rng, symbols) for _ in range(missing)]
        column = new_symbols + kept
        for r in range(ROWS):
            next_grid[r][c] = column[r]
        for i, symbol in enumerate(new_symbols):
            refills.append({"row": i, "col": c, "symbol": symbol})
    return next_grid, removed_cells, refills


def win_tier(win_multiplier: float) -> str:
    if win_multiplier >= 10000:
        return "max_win"
    if win_multiplier >= 100:
        return "mega"
    if win_multiplier >= 50:
        return "huge"
    if win_multiplier >= 20:
        return "big"
    if win_multiplier > 0:
        return "small"
    return "none"


def simulate_round(rng: random.Random, model_id: str, model: Dict[str, Any], configs: Dict[str, Any], round_index: int, run_config: Dict[str, Any]) -> Dict[str, Any]:
    symbols = configs["symbol_weights"]["symbols"]
    paytable = configs["cluster_paytable"]
    cascade_rules = configs["cascade_rules"]
    cap_multiplier = float(run_config.get("maxWinCapMultiplier") or configs["max_win_cap_rules"]["capMultiplier"])
    payout_scale = float(model.get("payoutScale", 1.0))
    starting_grid = generate_grid(rng, symbols)
    grid = [row[:] for row in starting_grid]
    total_win = 0.0
    pre_cap_total = 0.0
    cascade_steps = []
    rng_refs = []

    for cascade_index in range(int(cascade_rules.get("maxCascadesPerRound", 8))):
        clusters = find_clusters(grid, int(paytable.get("minimumClusterSize", 5)))
        if not clusters:
            break
        cluster_win = sum(cluster_pay(cluster, paytable) for cluster in clusters) * payout_scale
        pre_cap_total += cluster_win
        capped_total = min(pre_cap_total, cap_multiplier)
        total_win = capped_total
        next_grid, removed_cells, refills = remove_and_refill(grid, clusters, rng, symbols)
        cascade_steps.append({
            "cascadeIndex": cascade_index,
            "clusters": clusters,
            "removedCells": removed_cells,
            "refilledSymbols": refills,
            "cascadeWinMultiplier": round(cluster_win, 4),
            "gridAfter": next_grid,
        })
        rng_refs.append({"drawGroup": "cascade_refill", "cascadeIndex": cascade_index, "drawCount": len(refills), "rawRngStored": False})
        grid = next_grid
        if total_win >= cap_multiplier:
            break

    feature_events = []
    contribution = defaultdict(float)
    contribution["baseGame"] += total_win
    if rng.random() < float(configs["golden_square_rules"].get("creationChanceOnWinningCluster", 0.0)):
        feature_events.append({"type": "golden_square", "status": "candidate"})
        contribution["featureModes"] += 0.1
    if rng.random() < float(configs["rainbow_rules"].get("activationChancePerRound", 0.0)):
        feature_events.append({"type": "rainbow_activation", "status": "candidate"})
        contribution["featureModes"] += 0.25
    if rng.random() < 0.05:
        tier = rng.choices(["bronze", "silver", "gold"], weights=[70, 25, 5], k=1)[0]
        value = {"bronze": 1.0, "silver": 5.0, "gold": 20.0}[tier]
        feature_events.append({"type": "coin_reveal", "tier": tier, "valueMultiplier": value})
        contribution["coinReveal"] += value
        pre_cap_total += value
        total_win = min(pre_cap_total, cap_multiplier)
    if run_config.get("bonusBuyEnabled"):
        contribution["bonusBuy"] += 0.0
    if run_config.get("jackpotEnabled"):
        contribution["jackpot"] += 0.0

    capped = pre_cap_total > cap_multiplier
    return {
        "roundId": f"sample-round-{model_id}-{round_index:04d}",
        "modelId": model_id,
        "startingGrid": starting_grid,
        "cascadeSteps": cascade_steps,
        "finalGrid": grid,
        "preCapWinMultiplier": round(pre_cap_total, 4),
        "totalWinMultiplier": round(total_win, 4),
        "capState": {"capMultiplier": cap_multiplier, "capped": capped, "preCapWinMultiplier": round(pre_cap_total, 4), "cappedWinMultiplier": round(total_win, 4)},
        "winTier": win_tier(total_win),
        "featureEvents": feature_events,
        "featureContribution": {k: round(v, 4) for k, v in contribution.items()},
        "rngDrawReferences": rng_refs + [{"drawGroup": "feature_event_smoke", "drawCount": 3, "rawRngStored": False}],
        "stateVersion": round_index + 1,
        "roundCompletion": {"complete": True, "reason": "smoke_round_finished"},
    }


def summarize(rounds: List[Dict[str, Any]], target_rtp: float) -> Dict[str, Any]:
    count = len(rounds)
    wins = [float(r["totalWinMultiplier"]) for r in rounds]
    total = sum(wins)
    mean = total / count if count else 0.0
    variance = sum((w - mean) ** 2 for w in wins) / count if count else 0.0
    tiers = Counter(r["winTier"] for r in rounds)
    contribution = defaultdict(float)
    for r in rounds:
        for k, v in r.get("featureContribution", {}).items():
            contribution[k] += float(v)
    return {
        "roundCount": count,
        "observedReturnMultiplierPerRound": round(mean, 6),
        "targetRtp": target_rtp,
        "rtpCalibrationStatus": "smoke_not_calibrated",
        "standardDeviation": round(math.sqrt(variance), 6),
        "capHitCount": sum(1 for r in rounds if r["capState"]["capped"]),
        "winTierDistribution": dict(sorted(tiers.items())),
        "featureContributionSummary": {k: round(v, 4) for k, v in sorted(contribution.items())},
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="sample_run_config.json")
    parser.add_argument("--output", default="sample_report.json")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    config_path = (script_dir / args.config).resolve()
    output_path = (script_dir / args.output).resolve()
    refine_dir = script_dir.parent / "simulation_config_refinement"

    run_config = load_json(config_path)
    rtp_profiles = load_json(refine_dir / "rtp_model_profiles.json")["profiles"]
    configs = {
        "symbol_weights": load_json(refine_dir / "symbol_weights.json"),
        "cluster_paytable": load_json(refine_dir / "cluster_paytable.json"),
        "cascade_rules": load_json(refine_dir / "cascade_rules.json"),
        "golden_square_rules": load_json(refine_dir / "golden_square_rules.json"),
        "rainbow_rules": load_json(refine_dir / "rainbow_rules.json"),
        "max_win_cap_rules": load_json(refine_dir / "max_win_cap_rules.json"),
    }

    report = {
        "schemaVersion": "sample-simulation-report-v1",
        "simulationStatus": "deterministic_smoke_simulation",
        "exactValuesFinal": False,
        "certificationClaim": False,
        "walletUsed": False,
        "gsApiUsed": False,
        "browserRngUsed": False,
        "runConfig": run_config,
        "models": {},
        "vabsReplaySample": None,
        "blockers": ["large_scale_rtp_calibration_pending", "bonus_buy_cost_ev_pending", "certification_pending"],
    }

    for model_index, model_id in enumerate(run_config.get("models", [])):
        model = rtp_profiles[model_id]
        rng = random.Random(int(run_config.get("seed", 8001)) + model_index * 100000)
        rounds = [simulate_round(rng, model_id, model, configs, i, run_config) for i in range(int(run_config.get("roundCount", 10)))]
        report["models"][model_id] = summarize(rounds, float(model["targetRtp"]))
        if report["vabsReplaySample"] is None and rounds:
            first = rounds[0]
            report["vabsReplaySample"] = {
                "roundId": first["roundId"],
                "modelId": model_id,
                "startingGrid": first["startingGrid"],
                "cascadeSteps": first["cascadeSteps"],
                "finalGrid": first["finalGrid"],
                "winSummary": {"preCapWinMultiplier": first["preCapWinMultiplier"], "totalWinMultiplier": first["totalWinMultiplier"]},
                "winTier": first["winTier"],
                "capState": first["capState"],
                "featureState": {"events": first["featureEvents"], "featureModesEnabled": True},
                "bonusBuyState": {"bonusBuyEnabledForRun": bool(run_config.get("bonusBuyEnabled")), "authoritativePurchase": False},
                "rngDrawReferences": first["rngDrawReferences"],
                "stateVersion": first["stateVersion"],
                "roundCompletion": first["roundCompletion"],
                "replayPayload": {"replayPreferred": True, "screenshotRequirementStatus": "unverified", "screenshotBinaryStored": False},
            }

    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
