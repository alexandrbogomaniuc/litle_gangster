---
name: MathProfileCalibrator
description: Validate, calibrate, and gate 3x3 RTP/volatility math profile matrices using train, validation, tail, and bonus-buy evidence without backend, client, registration, wallet, donor, or release work.
---

# MathProfileCalibrator

## Purpose

Calibrate operator-selectable RTP/volatility profile matrices after
MathModelDesigner has produced an initial math package, 3x3 profile framework,
and simulator or local/external runner.

## When To Use

Use this skill when a game has, or needs, exactly three RTP levels and exactly
three volatility levels:

- RTP levels: `LOW`, `MEDIUM`, `HIGH`
- RTP values: game-specific average theoretical RTP percentages from `91.00`
  through `99.70`, inclusive
- RTP ordering: `LOW < MEDIUM < HIGH`
- Volatility levels: `LOW`, `MEDIUM`, `HIGH`
- Matrix size: 3 x 3 = 9 pretested `mathProfileId` values

Decimal RTP values are allowed and should be normalized or reported to two
decimal places where practical. Operators may select only approved pretested
profiles; they must not enter arbitrary RTP values at runtime.

Also use this skill when train/validation gates are not passed, a user provides
new RTP targets, or profile-specific calibration is required.

## Required Reads

1. Project `project_manifest.json`.
2. Latest MathModelDesigner handoff.
3. Existing RTP/volatility profile matrix.
4. Simulator/local runner documentation or external job package.
5. Latest train, validation, tail, and bonus-buy decision reports if present.

## Core References

- `references/RTP_REQUEST_VALIDATION.md`
- `references/CALIBRATION_LOOP_POLICY.md`
- `references/TRAIN_VALIDATION_SEED_POLICY.md`
- `references/ADJUSTMENT_OVERLAY_POLICY.md`
- `references/CALIBRATION_REPORT_REQUIREMENTS.md`

Use bundled scripts when deterministic checks are needed:

- `scripts/validate_rtp_request.py`
- `scripts/plan_calibration_loop.py`
- `scripts/validate_calibration_report.py`

## Workflow

1. Validate requested RTP and volatility levels before creating or tuning any
   profile.
2. Confirm the 9-profile matrix and `mathProfileId` identity are present.
3. Plan train simulations or import train results using train seeds only.
4. Run a bounded calibration loop with profile-specific overlay adjustments.
5. Run validation only after the train gate passes; never tune from validation
   seeds.
6. Check tail/max-win and bonus-buy status before implementation-adjacent
   handoff.
7. Produce compact reports and explicit gate states.

## Gates

Backend adapter implementation, client implementation, registration generation,
wallet tests, DB/Cassandra actions, donor browsing/capture, and release approval
remain blocked unless a later sprint explicitly opens them.

MathProfileCalibrator may say a profile matrix passed a train/validation stage,
but it must not claim final certified RTP. Tail/max-win, bonus-buy EV, and lab
or certification-scale evidence remain separate gates.

## Forbidden Actions

- No backend adapter implementation.
- No client implementation or production client generation.
- No registration generation.
- No DB/Cassandra execution.
- No wallet/API calls.
- No donor browsing or asset capture.
- No release approval.
- No validation-seed tuning.
- No post-spin payout scaling as release math.
- No certification claim from smoke, fast-train, or local-only evidence.

## Handoff

The handoff must state:

- profiles calibrated: yes/no
- train gate status
- validation gate status
- profiles within and outside tolerance
- bonus-buy status
- tail/max-win status
- backend adapter allowed: yes/no
- registration generation allowed: yes/no
- exact values final/certified: yes/no
