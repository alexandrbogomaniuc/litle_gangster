# MathModelDesigner Calibration Diagnostics Skill Report

Created: 2026-05-13T03:56:32Z

## Completed

- Ran bounded diagnostics for rtp_96, rtp_94, and rtp_92.
- Used 3 deterministic seeds per model and 10,000 rounds per seed.
- Documented simulator sanity status and observed return formula.
- Skipped tuning because calibration sanity checks did not pass.

## Key Finding

The simulator runs, but it is not reliable for calibration. The low observed returns are caused by structural modeling gaps, not only tiny sample size.

## Gate Status

- Backend adapter implementation allowed: false
- GameServerRegistrar generation allowed: false
- GameClientBuilder implementation allowed: false
- Release approved: false
