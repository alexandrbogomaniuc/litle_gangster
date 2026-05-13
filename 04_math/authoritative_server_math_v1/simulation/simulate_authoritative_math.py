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
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROWS = 5
COLS = 6
EXCLUDED_CLUSTER_SYMBOLS = {"wild", "rainbow", "coin", "special"}
COIN_REVEAL_SMOKE_PROBABILITY = 0.05
SPECIAL_REVEAL_SMOKE_PROBABILITY = 0.02


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def weighted_choice(rng: random.Random, entries: List[Dict[str, Any]]) -> str:
    total = sum(float(e["weight"]) for e in entries)
    if total <= 0:
        raise ValueError("weighted_choice_requires_positive_weight")
    pick = rng.random() * total
    seen = 0.0
    for entry in entries:
        seen += float(entry["weight"])
        if pick <= seen:
            return str(entry["symbol"])
    return str(entries[-1]["symbol"])


def weighted_mode_choice(rng: random.Random, modes: Dict[str, Dict[str, Any]]) -> str:
    entries = [{"symbol": mode_id, "weight": data.get("weight", 0)} for mode_id, data in modes.items()]
    if not entries:
        raise ValueError("feature_mode_probability_missing")
    return weighted_choice(rng, entries)


def config_value(profile: Dict[str, Any], field: str) -> Any:
    value = profile.get(field)
    if isinstance(value, dict) and "value" in value:
        return value["value"]
    return value


def resolve_bet_profile(model_id: str, configs: Dict[str, Any]) -> Dict[str, Any]:
    profiles = configs["game_settings_profiles"]
    if model_id not in profiles:
        raise ValueError(f"cluster_bet_denominator_missing: no game settings profile for {model_id}")
    profile = profiles[model_id]
    required = ["clusterBaseBetCredits", "clusterBetMultiplier", "minTotalBet", "defaultTotalBet", "maxTotalBet"]
    missing = [field for field in required if config_value(profile, field) is None]
    if missing:
        raise ValueError(f"cluster_bet_denominator_missing: {', '.join(missing)}")

    cluster_base = float(config_value(profile, "clusterBaseBetCredits"))
    cluster_multiplier = float(config_value(profile, "clusterBetMultiplier"))
    min_total = float(config_value(profile, "minTotalBet"))
    default_total = float(config_value(profile, "defaultTotalBet"))
    max_total = float(config_value(profile, "maxTotalBet"))
    if min(cluster_base, cluster_multiplier, min_total, default_total, max_total) <= 0:
        raise ValueError("cluster_bet_denominator_missing: non-positive bet metadata")

    return {
        "clusterBaseBetCredits": cluster_base,
        "clusterBetMultiplier": cluster_multiplier,
        "minTotalBet": min_total,
        "defaultTotalBet": default_total,
        "maxTotalBet": max_total,
        "betDenominator": default_total,
        "denominatorType": "defaultTotalBet_credits_cluster_equivalent",
        "registrationBetFormulaNotes": profile.get("registrationBetFormulaNotes", ""),
    }


def resolve_cluster_pay_multiplier(model_id: str, configs: Dict[str, Any]) -> float:
    tuning = configs["cluster_paytable"].get("modelSpecificCalibration", {})
    model_tuning = tuning.get(model_id, {})
    return float(model_tuning.get("clusterPayMultiplier", 1.0))


def symbol_group(symbol: str) -> str:
    if symbol.startswith("low_"):
        return "low"
    if symbol.startswith("mid_"):
        return "mid"
    if symbol.startswith("high_"):
        return "high"
    return symbol


def apply_volatility_modifiers(configs: Dict[str, Any], volatility_level: str, levers: Dict[str, Any]) -> Dict[str, Any]:
    """Apply transparent smoke-test volatility modifiers without mutating source rule files."""
    level = levers.get("levels", {}).get(volatility_level)
    if not level:
        raise ValueError(f"volatility_profile_missing: {volatility_level}")

    out = deepcopy(configs)
    modifiers = level.get("modifiers", {})
    symbol_modifiers = modifiers.get("symbolWeightMultipliers", {})
    for entry in out["symbol_weights"].get("symbols", []):
        group = symbol_group(str(entry.get("symbol", "")))
        entry["weight"] = float(entry["weight"]) * float(symbol_modifiers.get(group, 1.0))

    pay_modifiers = modifiers.get("clusterPaytableMultipliers", {})
    small_scale = float(pay_modifiers.get("smallCluster", 1.0))
    medium_scale = float(pay_modifiers.get("mediumCluster", 1.0))
    top_scale = float(pay_modifiers.get("topCluster", 1.0))
    for entries in out["cluster_paytable"].get("payBySymbolAndClusterSize", {}).values():
        for entry in entries:
            max_size = int(entry.get("max", 0))
            if max_size >= 11:
                scale = top_scale
            elif max_size >= 8:
                scale = medium_scale
            else:
                scale = small_scale
            entry["pay"] = float(entry["pay"]) * scale

    trigger = out["feature_rules"].get("featureTrigger", {})
    if trigger.get("probabilityCandidate") is not None:
        trigger["probabilityCandidate"] = min(
            1.0,
            float(trigger["probabilityCandidate"]) * float(modifiers.get("featureTriggerProbabilityMultiplier", 1.0)),
        )

    spin_multiplier = float(modifiers.get("freeSpinCountMultiplier", 1.0))
    starting_spins = out["free_spin_rules"].get("startingSpins", {})
    for mode_id, count in list(starting_spins.items()):
        starting_spins[mode_id] = max(1, int(round(float(count) * spin_multiplier)))

    out["_volatility"] = {
        "level": volatility_level,
        "status": level.get("status", "provisional_pending_simulation"),
        "description": level.get("description", ""),
        "targetBands": level.get("targetBands", {}),
        "modifiers": modifiers,
    }
    return out


def apply_profile_calibration_adjustments(configs: Dict[str, Any], profile: Dict[str, Any], adjustments: Dict[str, Any]) -> Dict[str, Any]:
    """Apply profile-specific calibration overlays without editing base rule JSON."""
    profile_adjustments = adjustments.get("profiles", {}).get(profile["mathProfileId"], {})
    if not profile_adjustments:
        return configs

    out = deepcopy(configs)
    low_weight = float(profile_adjustments.get("lowSymbolWeightAdjustment", 1.0))
    high_weight = float(profile_adjustments.get("highSymbolWeightAdjustment", 1.0))
    for entry in out["symbol_weights"].get("symbols", []):
        group = symbol_group(str(entry.get("symbol", "")))
        if group == "low":
            entry["weight"] = float(entry["weight"]) * low_weight
        elif group == "high":
            entry["weight"] = float(entry["weight"]) * high_weight

    cluster_scale = float(profile_adjustments.get("clusterPaytableMultiplierAdjustment", 1.0))
    for entries in out["cluster_paytable"].get("payBySymbolAndClusterSize", {}).values():
        for entry in entries:
            entry["pay"] = float(entry["pay"]) * cluster_scale

    trigger = out["feature_rules"].get("featureTrigger", {})
    if trigger.get("probabilityCandidate") is not None:
        trigger["probabilityCandidate"] = min(
            1.0,
            float(trigger["probabilityCandidate"]) * float(profile_adjustments.get("featureTriggerAdjustment", 1.0)),
        )

    out.setdefault("_calibration", {})
    out["_calibration"]["profileAdjustment"] = profile_adjustments
    out["_calibration"]["freeSpinValueAdjustment"] = float(profile_adjustments.get("freeSpinValueAdjustment", 1.0))
    return out


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


def remove_and_refill(
    grid: List[List[str]],
    clusters: List[Dict[str, Any]],
    rng: random.Random,
    symbols: List[Dict[str, Any]],
) -> Tuple[List[List[str]], List[Dict[str, int]], List[Dict[str, Any]]]:
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


def evaluate_cluster_cascades(
    rng: random.Random,
    symbols: List[Dict[str, Any]],
    paytable: Dict[str, Any],
    cascade_rules: Dict[str, Any],
    payout_scale: float,
    cap_multiplier: float,
) -> Dict[str, Any]:
    starting_grid = generate_grid(rng, symbols)
    grid = [row[:] for row in starting_grid]
    total_win = 0.0
    pre_cap_total = 0.0
    cascade_steps = []
    rng_refs = []
    cluster_hit_count = 0

    for cascade_index in range(int(cascade_rules.get("maxCascadesPerRound", 8))):
        clusters = find_clusters(grid, int(paytable.get("minimumClusterSize", 5)))
        if not clusters:
            break
        cluster_hit_count += len(clusters)
        cluster_win = sum(cluster_pay(cluster, paytable) for cluster in clusters) * payout_scale
        pre_cap_total += cluster_win
        total_win = min(pre_cap_total, cap_multiplier)
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

    return {
        "startingGrid": starting_grid,
        "finalGrid": grid,
        "preCapWinMultiplier": pre_cap_total,
        "totalWinMultiplier": total_win,
        "cascadeSteps": cascade_steps,
        "cascadeCount": len(cascade_steps),
        "clusterHitCount": cluster_hit_count,
        "rngDrawReferences": rng_refs,
    }


def simulate_feature_spins(
    rng: random.Random,
    mode_id: str,
    spin_count: int,
    model: Dict[str, Any],
    configs: Dict[str, Any],
    cap_multiplier: float,
) -> Dict[str, Any]:
    symbols = configs["symbol_weights"]["symbols"]
    paytable = configs["cluster_paytable"]
    cascade_rules = configs["cascade_rules"]
    payout_scale = float(model.get("payoutScale", 1.0))
    total_win = 0.0
    cascade_count = 0
    cluster_hit_count = 0
    samples = []
    for spin_index in range(spin_count):
        outcome = evaluate_cluster_cascades(rng, symbols, paytable, cascade_rules, payout_scale, cap_multiplier)
        total_win += float(outcome["preCapWinMultiplier"])
        cascade_count += int(outcome["cascadeCount"])
        cluster_hit_count += int(outcome["clusterHitCount"])
        if spin_index < 3:
            samples.append({
                "spinIndex": spin_index,
                "modeId": mode_id,
                "preCapWinMultiplier": round(float(outcome["preCapWinMultiplier"]), 4),
                "cascadeCount": int(outcome["cascadeCount"]),
                "clusterHitCount": int(outcome["clusterHitCount"]),
            })
    feature_multiplier = float(configs.get("_volatility", {}).get("modifiers", {}).get("featureModeWinMultiplier", 1.0))
    feature_multiplier *= float(configs.get("_calibration", {}).get("freeSpinValueAdjustment", 1.0))
    total_win *= feature_multiplier
    return {
        "modeId": mode_id,
        "featureSpins": spin_count,
        "featureWinMultiplier": total_win,
        "featureCascadeCount": cascade_count,
        "featureClusterHitCount": cluster_hit_count,
        "featureSpinSamples": samples,
    }


def maybe_trigger_feature(rng: random.Random, model: Dict[str, Any], configs: Dict[str, Any], cap_multiplier: float) -> Dict[str, Any]:
    feature_rules = configs["feature_rules"]
    free_spin_rules = configs["free_spin_rules"]
    probability = feature_rules.get("featureTrigger", {}).get("probabilityCandidate")
    if probability is None:
        return {"status": "feature_mode_probability_missing", "triggered": False}
    if rng.random() >= float(probability):
        return {"status": "provisional_smoke_path_not_triggered", "triggered": False, "probabilityCandidate": float(probability), "featureSpins": 0, "featureWinMultiplier": 0.0}
    mode_id = weighted_mode_choice(rng, configs["feature_mode_rules"].get("modes", {}))
    starting_spins = free_spin_rules.get("startingSpins", {}).get(mode_id)
    if starting_spins is None:
        return {"status": "feature_mode_probability_missing", "triggered": True, "modeId": mode_id, "featureSpins": 0, "featureWinMultiplier": 0.0}
    feature = simulate_feature_spins(rng, mode_id, int(starting_spins), model, configs, cap_multiplier)
    feature.update({
        "status": "provisional_smoke_path",
        "triggered": True,
        "probabilityCandidate": float(probability),
        "retriggerStatus": free_spin_rules.get("retrigger", "not_configured"),
    })
    return feature


def simulate_bonus_buy(rng: random.Random, model: Dict[str, Any], configs: Dict[str, Any], cap_multiplier: float, run_config: Dict[str, Any]) -> Dict[str, Any]:
    bonus_rules = configs["bonus_buy_rules"]
    costs = bonus_rules.get("costMultiplierCandidates", {})
    if not costs:
        return {"enabled": True, "status": "bonus_buy_cost_ev_pending", "blocker": "bonus_buy_cost_ev_pending"}
    mode_id = run_config.get("bonusBuyMode")
    if mode_id not in costs:
        mode_id = weighted_mode_choice(rng, configs["feature_mode_rules"].get("modes", {}))
    cost_multiplier = float(costs[mode_id])
    starting_spins = configs["free_spin_rules"].get("startingSpins", {}).get(mode_id)
    if starting_spins is None:
        return {"enabled": True, "status": "bonus_buy_cost_ev_pending", "blocker": "bonus_buy_cost_ev_pending"}
    feature = simulate_feature_spins(rng, mode_id, int(starting_spins), model, configs, cap_multiplier)
    win_multiplier = float(feature["featureWinMultiplier"])
    return {
        "enabled": True,
        "status": "provisional_smoke_path_ev_pending",
        "bonusBuyEvStatus": bonus_rules.get("blockerStatus", "bonus_buy_cost_ev_pending"),
        "modeId": mode_id,
        "buyCostMultiplier": cost_multiplier,
        "bonusBuyWinMultiplier": round(win_multiplier, 4),
        "bonusBuyObservedReturnMultiplier": round(win_multiplier / cost_multiplier, 6) if cost_multiplier else 0,
        "featureSpins": int(feature["featureSpins"]),
        "featureCascadeCount": int(feature["featureCascadeCount"]),
        "featureClusterHitCount": int(feature["featureClusterHitCount"]),
        "featureSpinSamples": feature["featureSpinSamples"],
    }


def simulate_round(
    rng: random.Random,
    model_id: str,
    model: Dict[str, Any],
    configs: Dict[str, Any],
    round_index: int,
    run_config: Dict[str, Any],
    profile: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    symbols = configs["symbol_weights"]["symbols"]
    paytable = configs["cluster_paytable"]
    cascade_rules = configs["cascade_rules"]
    bet_profile = resolve_bet_profile(model_id, configs)
    bet_denominator = float(bet_profile["betDenominator"])
    cap_multiplier = float(run_config.get("maxWinCapMultiplier") or configs["max_win_cap_rules"]["capMultiplier"])
    payout_scale = float(model.get("payoutScale", 1.0)) * resolve_cluster_pay_multiplier(model_id, configs)
    contribution = defaultdict(float)
    feature_events = []
    rng_refs = []
    bonus_buy_state = {"enabled": bool(run_config.get("bonusBuyEnabled")), "status": "disabled_for_run"}
    total_bet_multiplier = 1.0
    pre_cap_total = 0.0

    if run_config.get("bonusBuyEnabled"):
        bonus_buy_state = simulate_bonus_buy(rng, model, configs, cap_multiplier, run_config)
        total_bet_multiplier = float(bonus_buy_state.get("buyCostMultiplier", 0.0))
        pre_cap_total = float(bonus_buy_state.get("bonusBuyWinMultiplier", 0.0))
        contribution["bonusBuy"] += pre_cap_total
        starting_grid = generate_grid(rng, symbols)
        grid = [row[:] for row in starting_grid]
        cascade_steps = []
        cascade_count = 0
        cluster_hit_count = 0
        base_win_multiplier = 0.0
    else:
        base_outcome = evaluate_cluster_cascades(rng, symbols, paytable, cascade_rules, payout_scale, cap_multiplier)
        starting_grid = base_outcome["startingGrid"]
        grid = base_outcome["finalGrid"]
        cascade_steps = base_outcome["cascadeSteps"]
        cascade_count = int(base_outcome["cascadeCount"])
        cluster_hit_count = int(base_outcome["clusterHitCount"])
        pre_cap_total = float(base_outcome["preCapWinMultiplier"])
        base_win_multiplier = float(base_outcome["totalWinMultiplier"])
        contribution["baseGame"] += pre_cap_total
        rng_refs.extend(base_outcome["rngDrawReferences"])

    if rng.random() < float(configs["golden_square_rules"].get("creationChanceOnWinningCluster", 0.0)):
        feature_events.append({"type": "golden_square", "status": "candidate"})
        contribution["featureModes"] += 0.1
    if rng.random() < float(configs["rainbow_rules"].get("activationChancePerRound", 0.0)):
        feature_events.append({"type": "rainbow_activation", "status": "candidate"})
        contribution["featureModes"] += 0.25

    if run_config.get("bonusBuyEnabled"):
        feature_state = {
            "status": "covered_by_bonus_buy_smoke_path",
            "triggered": False,
            "featureSpins": int(bonus_buy_state.get("featureSpins", 0)),
            "featureWinMultiplier": float(bonus_buy_state.get("bonusBuyWinMultiplier", 0.0)),
        }
    else:
        feature_state = maybe_trigger_feature(rng, model, configs, cap_multiplier)
        if feature_state.get("triggered"):
            feature_win = float(feature_state.get("featureWinMultiplier", 0.0))
            pre_cap_total += feature_win
            contribution["freeSpins"] += feature_win
            contribution["featureModes"] += feature_win
            feature_events.append({"type": "feature_mode", "modeId": feature_state.get("modeId"), "featureSpins": feature_state.get("featureSpins")})

    if rng.random() < COIN_REVEAL_SMOKE_PROBABILITY:
        tiers = configs["coin_reveal_rules"].get("tiers", [])
        if tiers:
            tier = rng.choices([t["tier"] for t in tiers], weights=[float(t["weight"]) for t in tiers], k=1)[0]
            coin_multiplier = float(configs.get("_volatility", {}).get("modifiers", {}).get("coinRevealValueMultiplier", 1.0))
            value = float(next(t["valueMultiplier"] for t in tiers if t["tier"] == tier)) * coin_multiplier
        else:
            tier = "missing"
            value = 0.0
        feature_events.append({"type": "coin_reveal", "tier": tier, "valueMultiplier": value})
        contribution["coinReveal"] += value
        pre_cap_total += value

    if rng.random() < SPECIAL_REVEAL_SMOKE_PROBABILITY * float(configs.get("_volatility", {}).get("modifiers", {}).get("specialRevealProbabilityMultiplier", 1.0)):
        reveals = configs["special_reveal_rules"].get("reveals", [])
        if reveals:
            reveal_type = rng.choices([r["type"] for r in reveals], weights=[float(r["weight"]) for r in reveals], k=1)[0]
        else:
            reveal_type = "missing"
        value = float(configs.get("_volatility", {}).get("modifiers", {}).get("specialRevealValueMultiplier", 1.0))
        feature_events.append({"type": "special_reveal", "revealType": reveal_type, "valueMultiplier": value, "status": "diagnostic_smoke_value"})
        contribution["specialReveal"] += value
        pre_cap_total += value

    jackpot_state = {
        "jackpotEnabled": bool(run_config.get("jackpotEnabled", False)),
        "jackpotContribution": 0.0,
        "jackpotStatus": "disabled_pending_product_decision",
    }
    total_win = min(pre_cap_total, cap_multiplier)
    capped = pre_cap_total > cap_multiplier
    total_bet_amount = bet_denominator * total_bet_multiplier
    total_win_amount = total_win * bet_denominator
    if bonus_buy_state.get("enabled"):
        bonus_buy_state["bonusBuyCappedWinMultiplier"] = round(total_win, 4)
        bonus_buy_state["bonusBuyCappedWinTotal"] = round(total_win_amount, 4)
    return {
        "roundId": f"sample-round-{model_id}-{round_index:04d}",
        "modelId": model_id,
        "mathProfileId": profile.get("mathProfileId") if profile else model_id,
        "rtpLevel": profile.get("rtpLevel") if profile else model.get("rtpLevel"),
        "volatilityLevel": profile.get("volatilityLevel") if profile else configs.get("_volatility", {}).get("level"),
        "roundIndex": round_index,
        "roundType": "bonus_buy_smoke" if run_config.get("bonusBuyEnabled") else "base_game_smoke",
        "startingGrid": starting_grid,
        "cascadeSteps": cascade_steps,
        "finalGrid": grid,
        "preCapWinMultiplier": round(pre_cap_total, 4),
        "totalWinMultiplier": round(total_win, 4),
        "totalBetAmount": round(total_bet_amount, 4),
        "totalWinAmount": round(total_win_amount, 4),
        "observedReturnMultiplier": round(total_win_amount / total_bet_amount, 6) if total_bet_amount else 0,
        "betProfile": bet_profile,
        "baseGame": {
            "baseRounds": 0 if run_config.get("bonusBuyEnabled") else 1,
            "baseBetTotal": 0 if run_config.get("bonusBuyEnabled") else round(bet_denominator, 4),
            "baseWinTotal": 0 if run_config.get("bonusBuyEnabled") else round(base_win_multiplier * bet_denominator, 4),
            "baseObservedReturnMultiplier": 0 if run_config.get("bonusBuyEnabled") else round(base_win_multiplier, 6),
            "cascadeCount": cascade_count,
            "clusterHitCount": cluster_hit_count,
        },
        "featureState": feature_state,
        "bonusBuyState": bonus_buy_state,
        "jackpotState": jackpot_state,
        "capState": {
            "capMultiplier": cap_multiplier,
            "capped": capped,
            "preCapWinMultiplier": round(pre_cap_total, 4),
            "cappedWinMultiplier": round(total_win, 4),
            "preCapWinTotal": round(pre_cap_total * bet_denominator, 4),
            "cappedWinTotal": round(total_win_amount, 4),
        },
        "winTier": win_tier(total_win),
        "featureEvents": feature_events,
        "featureContribution": {k: round(v, 4) for k, v in contribution.items()},
        "rngDrawReferences": rng_refs + [{"drawGroup": "feature_event_smoke", "drawCount": 4, "rawRngStored": False}],
        "stateVersion": round_index + 1,
        "roundCompletion": {"complete": True, "reason": "smoke_round_finished"},
    }


def summarize(rounds: List[Dict[str, Any]], target_rtp: float, bet_profile: Dict[str, Any], profile: Dict[str, Any] | None = None) -> Dict[str, Any]:
    count = len(rounds)
    win_amounts = [float(r["totalWinAmount"]) for r in rounds]
    bet_amounts = [float(r["totalBetAmount"]) for r in rounds]
    multipliers = [float(r["observedReturnMultiplier"]) for r in rounds]
    total_win_amount = sum(win_amounts)
    total_bet_amount = sum(bet_amounts)
    observed = total_win_amount / total_bet_amount if total_bet_amount else 0.0
    mean = sum(multipliers) / count if count else 0.0
    variance = sum((w - mean) ** 2 for w in multipliers) / count if count else 0.0
    tiers = Counter(r["winTier"] for r in rounds)
    contribution = defaultdict(float)
    base_bet_total = 0.0
    base_win_total = 0.0
    cascade_count = 0
    cluster_hit_count = 0
    feature_triggers = 0
    feature_spins = 0
    feature_wins = 0.0
    bonus_buy_cost_total = 0.0
    bonus_buy_win_total = 0.0
    for r in rounds:
        for k, v in r.get("featureContribution", {}).items():
            contribution[k] += float(v)
        base = r.get("baseGame", {})
        base_bet_total += float(base.get("baseBetTotal", 0.0))
        base_win_total += float(base.get("baseWinTotal", 0.0))
        cascade_count += int(base.get("cascadeCount", 0))
        cluster_hit_count += int(base.get("clusterHitCount", 0))
        feature = r.get("featureState", {})
        if feature.get("triggered"):
            feature_triggers += 1
        feature_spins += int(feature.get("featureSpins", 0) or 0)
        if feature.get("triggered"):
            feature_wins += float(feature.get("featureWinMultiplier", 0.0) or 0.0) * float(bet_profile["betDenominator"])
        bonus = r.get("bonusBuyState", {})
        if bonus.get("enabled"):
            bonus_buy_cost_total += float(bonus.get("buyCostMultiplier", 0.0) or 0.0) * float(bet_profile["betDenominator"])
            bonus_buy_win_total += float(bonus.get("bonusBuyCappedWinMultiplier", 0.0) or 0.0) * float(bet_profile["betDenominator"])
    target_rtp_percent = float(target_rtp)
    target_return_multiplier = target_rtp_percent / 100.0
    cap_hits = sum(1 for r in rounds if r["capState"]["capped"])
    hit_rounds = [r for r in rounds if float(r["totalWinMultiplier"]) > 0]
    feature_trigger_rate = feature_triggers / count if count else 0
    max_observed_win = max((float(r["totalWinMultiplier"]) for r in rounds), default=0.0)
    average_win_when_hit = sum(float(r["totalWinMultiplier"]) for r in hit_rounds) / len(hit_rounds) if hit_rounds else 0.0
    return {
        "mathProfileId": profile.get("mathProfileId") if profile else None,
        "modelId": profile.get("legacyRtpModelId") if profile else None,
        "rtpLevel": profile.get("rtpLevel") if profile else None,
        "volatilityLevel": profile.get("volatilityLevel") if profile else None,
        "roundCount": count,
        "totalRounds": count,
        "targetRtp": target_rtp_percent,
        "targetRtpPercent": target_rtp_percent,
        "targetReturnMultiplier": round(target_return_multiplier, 6),
        "observedReturnMultiplier": round(observed, 6),
        "observedReturnMultiplierPerRound": round(mean, 6),
        "observedRtpPercent": round(observed * 100.0, 6),
        "totalBetAmount": round(total_bet_amount, 4),
        "totalWinAmount": round(total_win_amount, 4),
        "betDenominator": round(float(bet_profile["betDenominator"]), 4),
        "denominatorType": bet_profile["denominatorType"],
        "betProfile": bet_profile,
        "rtpCalibrationStatus": "smoke_not_calibrated",
        "volatilitySimulationStatus": "volatility_profile_smoke_not_certified",
        "hitRate": round(len(hit_rounds) / count, 8) if count else 0,
        "noWinFrequency": round((count - len(hit_rounds)) / count, 8) if count else 0,
        "variance": round(variance, 8),
        "standardDeviation": round(math.sqrt(variance), 6),
        "maxObservedWin": round(max_observed_win, 4),
        "averageWinWhenHit": round(average_win_when_hit, 6),
        "featureTriggerRate": round(feature_trigger_rate, 8),
        "maxWinCapMultiplier": rounds[0]["capState"]["capMultiplier"] if rounds else None,
        "capHits": cap_hits,
        "capHitCount": cap_hits,
        "capFrequency": round(cap_hits / count, 8) if count else 0,
        "preCapWinTotal": round(sum(float(r["capState"]["preCapWinTotal"]) for r in rounds), 4),
        "cappedWinTotal": round(sum(float(r["capState"]["cappedWinTotal"]) for r in rounds), 4),
        "winTierDistribution": dict(sorted(tiers.items())),
        "featureContributionSummary": {k: round(v, 4) for k, v in sorted(contribution.items())},
        "baseGame": {
            "baseRounds": sum(int(r.get("baseGame", {}).get("baseRounds", 0)) for r in rounds),
            "baseBetTotal": round(base_bet_total, 4),
            "baseWinTotal": round(base_win_total, 4),
            "baseObservedReturnMultiplier": round(base_win_total / base_bet_total, 6) if base_bet_total else 0,
            "cascadeCount": cascade_count,
            "clusterHitCount": cluster_hit_count,
        },
        "featureModeSmoke": {
            "status": "provisional_smoke_path",
            "triggerCount": feature_triggers,
            "featureSpins": feature_spins,
            "featureWinTotal": round(feature_wins, 4),
            "featureObservedReturnMultiplier": round(feature_wins / total_bet_amount, 6) if total_bet_amount else 0,
        },
        "bonusBuySmoke": {
            "status": "provisional_smoke_path_ev_pending" if bonus_buy_cost_total else "disabled_for_run",
            "bonusBuyEvStatus": "bonus_buy_cost_ev_pending",
            "bonusBuyCostTotal": round(bonus_buy_cost_total, 4),
            "bonusBuyWinTotal": round(bonus_buy_win_total, 4),
            "bonusBuyObservedReturnMultiplier": round(bonus_buy_win_total / bonus_buy_cost_total, 6) if bonus_buy_cost_total else 0,
        },
        "jackpot": {
            "jackpotEnabled": False,
            "jackpotContribution": 0,
            "jackpotStatus": "disabled_pending_product_decision",
        },
        "profileApprovalStatus": profile.get("profileApprovalStatus") if profile else "legacy_model_smoke",
        "simulationStatus": "smoke_completed_not_certified",
        "blockers": ["large_scale_rtp_calibration_pending", "bonus_buy_ev_pending", "certification_pending"],
    }


def load_configs(refine_dir: Path) -> Dict[str, Any]:
    return {
        "game_settings_profiles": load_json(refine_dir / "game_settings_profiles.json")["profiles"],
        "symbol_weights": load_json(refine_dir / "symbol_weights.json"),
        "cluster_paytable": load_json(refine_dir / "cluster_paytable.json"),
        "cascade_rules": load_json(refine_dir / "cascade_rules.json"),
        "golden_square_rules": load_json(refine_dir / "golden_square_rules.json"),
        "rainbow_rules": load_json(refine_dir / "rainbow_rules.json"),
        "coin_reveal_rules": load_json(refine_dir / "coin_reveal_rules.json"),
        "special_reveal_rules": load_json(refine_dir / "special_reveal_rules.json"),
        "free_spin_rules": load_json(refine_dir / "free_spin_rules.json"),
        "feature_rules": load_json(refine_dir / "feature_rules.json"),
        "feature_mode_rules": load_json(refine_dir / "feature_mode_rules.json"),
    "bonus_buy_rules": load_json(refine_dir / "bonus_buy_rules.json"),
        "jackpot_hook_rules": load_json(refine_dir / "jackpot_hook_rules.json"),
        "max_win_cap_rules": load_json(refine_dir / "max_win_cap_rules.json"),
    }


def resolve_profile_run_list(run_config: Dict[str, Any], profile_matrix: Dict[str, Any]) -> List[Dict[str, Any]]:
    profiles = profile_matrix.get("profiles", [])
    by_id = {profile["mathProfileId"]: profile for profile in profiles}
    requested = run_config.get("mathProfiles") or run_config.get("mathProfileIds")
    if requested:
        missing = [profile_id for profile_id in requested if profile_id not in by_id]
        if missing:
            raise ValueError(f"unknown_mathProfileId: {', '.join(missing)}")
        return [by_id[profile_id] for profile_id in requested]

    legacy = run_config.get("models", [])
    out = []
    for model_id in legacy:
        matches = [profile for profile in profiles if profile.get("legacyRtpModelId") == model_id and profile.get("volatilityLevel") == "MEDIUM"]
        if matches:
            out.append(matches[0])
    return out


def load_optional_adjustments(script_dir: Path, run_config: Dict[str, Any]) -> Dict[str, Any]:
    path_value = run_config.get("calibrationAdjustmentsPath")
    if not path_value:
        return {"profiles": {}}
    path = Path(path_value)
    if not path.is_absolute():
        path = script_dir / path
    return load_json(path)


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
    profile_matrix = load_json(script_dir.parent / "rtp_volatility_profile_matrix.json")
    volatility_levers = load_json(script_dir.parent / "volatility_profile_levers.json")
    calibration_adjustments = load_optional_adjustments(script_dir, run_config)
    configs = load_configs(refine_dir)
    profile_run_list = resolve_profile_run_list(run_config, profile_matrix)
    seeds = run_config.get("seeds") or [run_config.get("seed", 8001)]

    report = {
        "schemaVersion": "sample-simulation-report-v3",
        "simulationStatus": "deterministic_calibration_smoke_simulation",
        "simulatorCompletenessStatus": "mathProfileId_and_volatility_profile_smoke_supported_not_certified",
        "exactValuesFinal": False,
        "certificationClaim": False,
        "walletUsed": False,
        "gsApiUsed": False,
        "browserRngUsed": False,
        "runConfig": run_config,
        "profileCount": len(profile_run_list),
        "seedCount": len(seeds),
        "models": {},
        "profiles": {},
        "vabsReplaySample": None,
        "blockers": ["large_scale_rtp_calibration_pending", "bonus_buy_ev_pending", "certification_pending"],
    }

    for profile_index, profile in enumerate(profile_run_list):
        model_id = profile["legacyRtpModelId"]
        model = rtp_profiles[model_id]
        effective_configs = apply_volatility_modifiers(configs, profile["volatilityLevel"], volatility_levers)
        effective_configs = apply_profile_calibration_adjustments(effective_configs, profile, calibration_adjustments)
        bet_profile = resolve_bet_profile(model_id, effective_configs)
        rounds = []
        for seed_index, seed in enumerate(seeds):
            rng = random.Random(int(seed) + profile_index * 100000 + seed_index * 1000)
            rounds.extend(
                simulate_round(rng, model_id, model, effective_configs, i + seed_index * int(run_config.get("roundCount", 10)), run_config, profile)
                for i in range(int(run_config.get("roundCount", 10)))
            )
        profile_summary = summarize(rounds, float(profile["targetRtpPercent"]), bet_profile, profile)
        profile_summary["volatilityTargetBands"] = volatility_levers.get("levels", {}).get(profile["volatilityLevel"], {}).get("targetBands", {})
        profile_summary["volatilityModifierStatus"] = volatility_levers.get("levels", {}).get(profile["volatilityLevel"], {}).get("status", "provisional_pending_simulation")
        report["profiles"][profile["mathProfileId"]] = profile_summary
        report["models"][profile["mathProfileId"]] = profile_summary
        if report["vabsReplaySample"] is None and rounds:
            first = rounds[0]
            report["vabsReplaySample"] = {
                "roundId": first["roundId"],
                "modelId": model_id,
                "mathProfileId": profile["mathProfileId"],
                "rtpLevel": profile["rtpLevel"],
                "volatilityLevel": profile["volatilityLevel"],
                "seed": int(seeds[0]),
                "roundIndex": first["roundIndex"],
                "startingGrid": first["startingGrid"],
                "cascadeSteps": first["cascadeSteps"],
                "finalGrid": first["finalGrid"],
                "totalWin": first["totalWinAmount"],
                "totalBet": first["totalBetAmount"],
                "observedReturnMultiplier": first["observedReturnMultiplier"],
                "winSummary": {
                    "preCapWinMultiplier": first["preCapWinMultiplier"],
                    "totalWinMultiplier": first["totalWinMultiplier"],
                    "totalWinAmount": first["totalWinAmount"],
                    "totalBetAmount": first["totalBetAmount"],
                },
                "winTier": first["winTier"],
                "featureState": first["featureState"],
                "bonusBuyState": first["bonusBuyState"],
                "capState": first["capState"],
                "rngDrawReferences": first["rngDrawReferences"],
                "stateVersion": first["stateVersion"],
                "roundCompletion": first["roundCompletion"],
                "historyReplayPayload": {
                    "replayPreferred": True,
                    "screenshotRequirementStatus": "unverified",
                    "screenshotBinaryStored": False,
                    "payloadType": "deterministic_smoke_replay",
                },
                "replayPayload": {
                    "replayPreferred": True,
                    "screenshotRequirementStatus": "unverified",
                    "screenshotBinaryStored": False,
                },
                "screenshotRequirementStatus": "unverified",
                "replayPreferred": True,
            }

    output_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
