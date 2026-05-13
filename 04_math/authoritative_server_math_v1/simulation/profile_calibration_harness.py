#!/usr/bin/env python3
"""Bounded 3x3 RTP/volatility calibration harness.

Non-production only. This harness creates profile-specific adjustment overlays
for local smoke calibration. It does not edit base rule JSON, does not use
post-spin payout scaling, and does not produce certification evidence.
"""
from __future__ import annotations

import json
import math
import random
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import simulate_authoritative_math as sim

SEEDS = [8501, 8502]
ROUNDS_PER_SEED = 1000
MAX_ITERATIONS = 2
TOLERANCE_PERCENT_POINTS = 2.0


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def load_inputs(script_dir: Path) -> Dict[str, Any]:
    root = script_dir.parent
    refine_dir = root / "simulation_config_refinement"
    return {
        "root": root,
        "refine_dir": refine_dir,
        "profile_matrix": sim.load_json(root / "rtp_volatility_profile_matrix.json"),
        "volatility_levers": sim.load_json(root / "volatility_profile_levers.json"),
        "rtp_profiles": sim.load_json(refine_dir / "rtp_model_profiles.json")["profiles"],
        "configs": sim.load_configs(refine_dir),
    }


def run_profiles(inputs: Dict[str, Any], adjustments: Dict[str, Any], iteration: int) -> Dict[str, Any]:
    profiles = inputs["profile_matrix"]["profiles"]
    summaries: Dict[str, Any] = {}
    for profile_index, profile in enumerate(profiles):
        model_id = profile["legacyRtpModelId"]
        model = inputs["rtp_profiles"][model_id]
        effective_configs = sim.apply_volatility_modifiers(inputs["configs"], profile["volatilityLevel"], inputs["volatility_levers"])
        effective_configs = sim.apply_profile_calibration_adjustments(effective_configs, profile, adjustments)
        bet_profile = sim.resolve_bet_profile(model_id, effective_configs)
        rounds = []
        for seed_index, seed in enumerate(SEEDS):
            rng = random.Random(seed + profile_index * 100000 + seed_index * 1000)
            for i in range(ROUNDS_PER_SEED):
                round_index = i + seed_index * ROUNDS_PER_SEED
                run_config = {
                    "bonusBuyEnabled": False,
                    "jackpotEnabled": False,
                    "maxWinCapMultiplier": profile.get("maxWinCapMultiplier", 10000),
                }
                rounds.append(sim.simulate_round(rng, model_id, model, effective_configs, round_index, run_config, profile))
        summary = sim.summarize(rounds, float(profile["targetRtpPercent"]), bet_profile, profile)
        delta = float(summary["observedRtpPercent"]) - float(profile["targetRtpPercent"])
        summary.update({
            "iteration": iteration,
            "rtpDeltaFromTarget": round(delta, 6),
            "withinSmokeTolerance": abs(delta) <= TOLERANCE_PERCENT_POINTS,
        })
        summaries[profile["mathProfileId"]] = summary
    return summaries


def build_iteration_adjustments(
    profiles: List[Dict[str, Any]],
    summaries: Dict[str, Any],
    previous: Dict[str, Any] | None = None,
    iteration: int = 1,
) -> Dict[str, Any]:
    previous_profiles = (previous or {}).get("profiles", {})
    out = {
        "schemaVersion": "profile-calibration-adjustments-v1",
        "artifactType": "profile_specific_overlay",
        "iteration": iteration,
        "exactValuesFinal": False,
        "certificationClaim": False,
        "postSpinForcedPayoutScalingUsed": False,
        "bonusBuyTuned": False,
        "profiles": {},
    }
    for profile in profiles:
        pid = profile["mathProfileId"]
        summary = summaries[pid]
        target = float(profile["targetRtpPercent"])
        observed = float(summary["observedRtpPercent"])
        ratio = target / observed if observed > 0 else 1.0
        prev = previous_profiles.get(pid, {})
        prior_cluster = float(prev.get("clusterPaytableMultiplierAdjustment", 1.0))
        prior_feature = float(prev.get("featureTriggerAdjustment", 1.0))
        prior_free = float(prev.get("freeSpinValueAdjustment", 1.0))
        prior_high = float(prev.get("highSymbolWeightAdjustment", 1.0))
        prior_low = float(prev.get("lowSymbolWeightAdjustment", 1.0))
        delta = observed - target

        if abs(delta) <= TOLERANCE_PERCENT_POINTS:
            out["profiles"][pid] = {
                "mathProfileId": pid,
                "rtpLevel": profile["rtpLevel"],
                "volatilityLevel": profile["volatilityLevel"],
                "targetRtpPercent": target,
                "observedRtpPercentBefore": observed,
                "observedRtpPercentAfter": None,
                "rtpDeltaBefore": round(delta, 6),
                "rtpDeltaAfter": None,
                "clusterPaytableMultiplierAdjustment": round(prior_cluster, 6),
                "featureTriggerAdjustment": round(prior_feature, 6),
                "freeSpinValueAdjustment": round(prior_free, 6),
                "highSymbolWeightAdjustment": round(prior_high, 6),
                "lowSymbolWeightAdjustment": round(prior_low, 6),
                "volatilityPreservationNotes": "Already within smoke tolerance for this iteration; previous overlay retained.",
                "status": "within_smoke_tolerance_no_new_adjustment",
            }
            continue

        cluster_step = clamp(ratio, 0.86 if iteration == 1 else 0.9, 1.16 if iteration == 1 else 1.1)
        free_step = clamp(math.sqrt(ratio), 0.94 if iteration == 1 else 0.97, 1.06 if iteration == 1 else 1.03)

        volatility = profile["volatilityLevel"]
        under_target = delta < -TOLERANCE_PERCENT_POINTS
        over_target = delta > TOLERANCE_PERCENT_POINTS
        high_step = 1.0
        low_step = 1.0
        feature_step = 1.0
        if volatility == "HIGH" and under_target:
            high_step = 1.02 if iteration == 1 else 1.01
            low_step = 0.99
        elif volatility == "LOW" and over_target:
            high_step = 0.99
            low_step = 0.995
            feature_step = 0.99
        elif volatility == "MEDIUM" and over_target:
            feature_step = 0.99

        adjusted = {
            "mathProfileId": pid,
            "rtpLevel": profile["rtpLevel"],
            "volatilityLevel": volatility,
            "targetRtpPercent": target,
            "observedRtpPercentBefore": observed,
            "observedRtpPercentAfter": None,
            "rtpDeltaBefore": round(delta, 6),
            "rtpDeltaAfter": None,
            "clusterPaytableMultiplierAdjustment": round(prior_cluster * cluster_step, 6),
            "featureTriggerAdjustment": round(prior_feature * feature_step, 6),
            "freeSpinValueAdjustment": round(prior_free * free_step, 6),
            "highSymbolWeightAdjustment": round(prior_high * high_step, 6),
            "lowSymbolWeightAdjustment": round(prior_low * low_step, 6),
            "volatilityPreservationNotes": "Profile-specific overlay; no global rule JSON changed; hit-rate/standard-deviation ordering checked after run.",
            "status": "first_pass_overlay_pending_validation",
        }
        out["profiles"][pid] = adjusted
    return out


def merge_after_metrics(adjustments: Dict[str, Any], before: Dict[str, Any], after: Dict[str, Any]) -> Dict[str, Any]:
    out = deepcopy(adjustments)
    for pid, adj in out["profiles"].items():
        final = after[pid]
        target = float(adj["targetRtpPercent"])
        adj["observedRtpPercentBefore"] = float(before[pid]["observedRtpPercent"])
        adj["observedRtpPercentAfter"] = float(final["observedRtpPercent"])
        adj["rtpDeltaBefore"] = round(float(before[pid]["observedRtpPercent"]) - target, 6)
        adj["rtpDeltaAfter"] = round(float(final["observedRtpPercent"]) - target, 6)
        adj["status"] = "within_smoke_tolerance" if abs(adj["rtpDeltaAfter"]) <= TOLERANCE_PERCENT_POINTS else "calibration_pending"
    return out


def volatility_ordering(summaries: Dict[str, Any]) -> Dict[str, Any]:
    by_rtp: Dict[str, Dict[str, Any]] = {}
    preserved = True
    for summary in summaries.values():
        by_rtp.setdefault(summary["rtpLevel"], {})[summary["volatilityLevel"]] = summary
    checks = {}
    for rtp_level, group in by_rtp.items():
        low = group["LOW"]
        medium = group["MEDIUM"]
        high = group["HIGH"]
        hit_ok = float(low["hitRate"]) >= float(medium["hitRate"]) >= float(high["hitRate"])
        sd_ok = float(low["standardDeviation"]) <= float(medium["standardDeviation"]) <= float(high["standardDeviation"])
        checks[rtp_level] = {
            "hitRateOrderingPreserved": hit_ok,
            "standardDeviationOrderingPreserved": sd_ok,
            "hitRates": {
                "LOW": low["hitRate"],
                "MEDIUM": medium["hitRate"],
                "HIGH": high["hitRate"],
            },
            "standardDeviations": {
                "LOW": low["standardDeviation"],
                "MEDIUM": medium["standardDeviation"],
                "HIGH": high["standardDeviation"],
            },
        }
        preserved = preserved and hit_ok and sd_ok
    return {"preserved": preserved, "checks": checks}


def compact_profile(summary: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "mathProfileId": summary["mathProfileId"],
        "rtpLevel": summary["rtpLevel"],
        "volatilityLevel": summary["volatilityLevel"],
        "targetRtpPercent": summary["targetRtpPercent"],
        "observedRtpPercent": summary["observedRtpPercent"],
        "rtpDeltaFromTarget": summary["rtpDeltaFromTarget"],
        "withinSmokeTolerance": summary["withinSmokeTolerance"],
        "hitRate": summary["hitRate"],
        "standardDeviation": summary["standardDeviation"],
        "capFrequency": summary["capFrequency"],
        "winTierDistribution": summary["winTierDistribution"],
    }


def write_markdown_report(path: Path, results: Dict[str, Any]) -> None:
    lines = [
        "# 3x3 RTP / Volatility Calibration Report",
        "",
        f"Created: {results['createdAt']}",
        "",
        "## Scope",
        "",
        "First-pass local smoke calibration only. This is not certification, not final math approval, and not production runtime code.",
        "",
        "## Run",
        "",
        f"- Profiles tested: {results['profilesTestedCount']} / {results['expectedProfilesCount']}.",
        f"- Seeds per profile: {len(SEEDS)}.",
        f"- Rounds per seed: {ROUNDS_PER_SEED}.",
        f"- Calibration iterations used: {results['calibrationIterationsUsed']}.",
        "- Bonus buy tuned: false.",
        "- Jackpot enabled: false.",
        "- Exact values final: false.",
        "- Certification status: false.",
        "",
        "## Final Results",
        "",
        "| mathProfileId | Target RTP | Before RTP | After RTP | Delta After | Hit Rate | Std Dev | Cap Freq | Status |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for pid, final in results["finalProfiles"].items():
        before = results["baselineProfiles"][pid]
        status = "within_tolerance" if final["withinSmokeTolerance"] else "calibration_pending"
        lines.append(
            f"| {pid} | {final['targetRtpPercent']:.2f}% | {before['observedRtpPercent']:.6f}% | "
            f"{final['observedRtpPercent']:.6f}% | {final['rtpDeltaFromTarget']:.6f} | "
            f"{final['hitRate']:.6f} | {final['standardDeviation']:.6f} | {final['capFrequency']:.8f} | {status} |"
        )
    lines.extend([
        "",
        "## Summary",
        "",
        f"- Profiles within +/-2.0 percentage points: {results['profilesWithinSmokeToleranceCount']}.",
        f"- Profiles outside +/-2.0 percentage points: {results['profilesOutsideSmokeToleranceCount']}.",
        f"- Volatility ordering preserved: {str(results['volatilityOrdering']['preserved']).lower()}.",
        "",
        "## Blockers",
        "",
    ])
    for blocker in results["unresolvedBlockers"]:
        lines.append(f"- `{blocker}`")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def write_blockers(path: Path, blockers: List[str]) -> None:
    lines = ["# 3x3 Profile Calibration Blockers", "", "Created: 2026-05-13", ""]
    for blocker in blockers:
        lines.append(f"- `{blocker}`")
    lines.extend([
        "",
        "Backend adapter implementation, GameClientBuilder implementation, GameServerRegistrar generation, wallet/API work, DB work, donor browsing, asset capture, and release approval remain blocked.",
        "",
    ])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    inputs = load_inputs(script_dir)
    profiles = inputs["profile_matrix"]["profiles"]
    baseline = run_profiles(inputs, {"profiles": {}}, iteration=0)
    adjustments = build_iteration_adjustments(profiles, baseline, iteration=1)
    iteration1 = run_profiles(inputs, adjustments, iteration=1)
    final = iteration1
    calibration_iterations_used = 1

    outside = [pid for pid, summary in final.items() if not summary["withinSmokeTolerance"]]
    if outside and MAX_ITERATIONS >= 2:
        adjustments = build_iteration_adjustments(profiles, iteration1, previous=adjustments, iteration=2)
        final = run_profiles(inputs, adjustments, iteration=2)
        calibration_iterations_used = 2

    adjustments = merge_after_metrics(adjustments, baseline, final)
    ordering = volatility_ordering(final)
    within = sum(1 for summary in final.values() if summary["withinSmokeTolerance"])
    outside_count = len(final) - within
    blockers = []
    if outside_count:
        blockers.append("profile_rtp_smoke_tolerance_pending")
    if not ordering["preserved"]:
        blockers.append("volatility_ordering_not_preserved")
    blockers.extend([
        "profile_stability_large_sample_pending",
        "bonus_buy_ev_pending",
        "max_win_tail_frequency_unproven",
        "standard_deviation_targets_pending_large_simulation",
        "certification_pending",
    ])

    results = {
        "schemaVersion": "profile-calibration-results-v1",
        "createdAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "profileCalibrationCompleted": True,
        "calibrationHarnessCreated": True,
        "profileAdjustmentOverlayCreated": True,
        "calibrationIterationsUsed": calibration_iterations_used,
        "maxCalibrationIterations": MAX_ITERATIONS,
        "seeds": SEEDS,
        "roundsPerSeed": ROUNDS_PER_SEED,
        "bonusBuyTuned": False,
        "bonusBuyEnabled": False,
        "jackpotEnabled": False,
        "postSpinForcedPayoutScalingUsed": False,
        "exactValuesFinal": False,
        "certificationStatus": False,
        "tolerancePercentPoints": TOLERANCE_PERCENT_POINTS,
        "profilesTestedCount": len(final),
        "expectedProfilesCount": 9,
        "profilesWithinSmokeToleranceCount": within,
        "profilesOutsideSmokeToleranceCount": outside_count,
        "volatilityOrdering": ordering,
        "baselineProfiles": {pid: compact_profile(summary) for pid, summary in baseline.items()},
        "finalProfiles": {pid: compact_profile(summary) for pid, summary in final.items()},
        "unresolvedBlockers": blockers,
    }

    (script_dir / "profile_calibration_adjustments.json").write_text(json.dumps(adjustments, indent=2) + "\n", encoding="utf-8")
    (script_dir / "profile_calibration_results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    write_markdown_report(script_dir / "profile_calibration_report.md", results)
    write_blockers(script_dir / "profile_calibration_blockers.md", blockers)
    print(json.dumps({
        "profilesTestedCount": len(final),
        "profilesWithinSmokeToleranceCount": within,
        "profilesOutsideSmokeToleranceCount": outside_count,
        "volatilityOrderingPreserved": ordering["preserved"],
        "calibrationIterationsUsed": calibration_iterations_used,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
