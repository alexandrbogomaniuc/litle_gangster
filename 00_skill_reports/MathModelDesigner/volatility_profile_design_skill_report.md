# MathModelDesigner Skill Report - Volatility Profile Simulation Design

Created: 2026-05-13

## Outcome

Completed the volatility profile simulation design sprint in fast-lane mode. Defined LOW / MEDIUM / HIGH volatility levers, patched only the local non-production simulator to resolve `mathProfileId`, and ran all 9 RTP x volatility profiles
in smoke mode.

## Actions

- Created provisional volatility lever design.
- Added in-memory volatility modifier support to the local simulator.
- Added `mathProfileId` profile selection support.
- Ran 9 profiles with 2 deterministic seeds and 2,000 rounds per seed.
- Recorded volatility metrics: hit rate, standard deviation, variance, max observed win, cap frequency, win-tier distribution, feature trigger rate, and average win when hit.

## Result

All 9 profiles ran. The results are useful for directional volatility behavior but not calibrated or certified. Several profiles have material RTP drift, especially HIGH volatility combinations and HIGH RTP LOW/MEDIUM volatility
combinations.

## Gates

Backend adapter implementation, GameClientBuilder implementation, GameServerRegistrar generation, wallet/API tests, DB changes, and release approval remain blocked.

