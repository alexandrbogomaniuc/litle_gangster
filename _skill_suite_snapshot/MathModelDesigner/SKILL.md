---
name: MathModelDesigner
description: Design and validate internal math packages from approved templates, targets, and simulations rather than screenshots alone.
---

# MathModelDesigner

## Purpose
Create validated internal math packages.

## When To Use
Use after manifest and protocol context exist.

## Required Inputs
Target RTPs, volatility target, max win, bet model, approved math template path,
feature requirements, and any proven or advisory protocol/runtime state
contracts. Mantis/ExtGame items such as `processTransactions`, `gameState`,
`roundFinishedHelper`, and `restartGame` are lane-dependent checklist items
unless current GS proves ExtGame.

## Preconditions
Read manifest, `references/BARONOIL_MATH_REFERENCE_SUMMARY.md`, and any explicit internal math templates.

## Forbidden Actions
No math from screenshots only, no unvalidated RTP, no client-side RNG assumption without docs, no release approval if simulation fails.

## Workflow
1. Treat reference observations as clues only.
2. Use internal templates and user targets.
3. Produce paytables, reels, bonus/free-spin/buy-feature rules, simulation config, RTP/volatility/max-win reports.
4. Support multiple RTP variants when requested.
5. Run simulations with multiple seeds and tolerance policy.
6. Record confidence and blockers.
7. Include backend-owned result/state fields for transaction-equivalent
   accounting, restore state, round completion, and restart/resume. Use ExtGame
   names such as `processTransactions`, `gameState`, `roundFinishedHelper`, and
   `restartGame` only when that lane is proven. Otherwise map the same checklist
   to the selected current-GS lane. Do not make the browser authoritative for
   settlement, RNG, or round completion.

## Calibration Fast Lane
Before any RTP tuning, use `references/CALIBRATION_FAST_LANE.md`. Do not tune
paytables, weights, features, or bonus-buy until denominator and RTP unit sanity
pass. Report RTP percent and return multiplier separately, and report RTP with
bonus-buy separately from RTP without bonus-buy. Do not use post-spin payout
scaling as release math; any diagnostic scale must be labelled
`diagnostic_only_not_release_math`. Keep exact values non-final until multi-seed
validation and certification-scale validation pass. Maintain GL/registration bet
metadata mapping throughout calibration.

## RTP Simulation Confidence Tiers
Use `references/RTP_SIMULATION_CONFIDENCE_TIERS.md` before interpreting
simulation results. Never treat 2k, 5k, 10k, or 50k runs as RTP approval. Small
runs are smoke evidence for wiring, denominator, profile routing, and obvious
broken logic only. Always separate "simulator wiring passed" from "RTP
calibrated", report confidence intervals or explicitly state confidence cannot
be estimated, and use "outside smoke tolerance" instead of "failed profile"
unless a statistical confidence threshold is met. Backend adapter, registration,
and release gates must not open from smoke-only RTP evidence.

## RTP / Volatility Profile Matrix
For reusable game setup, use `references/RTP_VOLATILITY_PROFILE_MATRIX.md`. Do
not hardcode reusable models as `rtp_92`, `rtp_94`, or `rtp_96`; every game must
define LOW/MEDIUM/HIGH RTP levels and LOW/MEDIUM/HIGH volatility levels,
producing a pretested 3x3 matrix of `mathProfileId` values. Store profile
identity in runtime and VABS/history outputs, and keep registration metadata
separate from executable math.

## Output Files
`04_math/math_model_summary.md`, `math_package.json`, paytables, reels, simulations, reports, skill reports.

## Validation Checklist
Package schema valid, RTP within tolerance, variance reported, max win checked.
Handoff explicitly covers transaction-equivalent processing, restart/resume
state, round-finished fields, RNG boundary, VABS/history state where relevant,
and unresolved lane blockers.

## Handoff To Next Skill
Next: ArtSceneMapper.

## Failure / Blocker Handling
Missing templates, targets, or simulation tooling block release math.

## SprintReporter Handoff
Report math assumptions, simulation commands, seed counts, tolerance, and results.

## Pilot Pipeline Hardening Addendum

Create a layout alignment report before model generation. Review donor
feature/settings parity before selecting the math model. Run a simulator trust
audit for payout scaling, post-normalization, and forced RTP. Reject artificial
payout scaling for release claims unless clearly labelled non-release. For
complex donor parity, create a v0.3-style result contract with cascade/state and
feature fields, and keep registration metadata separate from executable math.
