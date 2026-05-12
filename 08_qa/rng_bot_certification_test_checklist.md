# RNG Bot Certification Test Checklist

Status: release-audit gate only; no tests executed.

## Required Gates

- Production RNG owner proven from current GS/new-games/backend runtime.
- Browser RNG excluded from production outcome generation.
- Deterministic teststand or scenario reproduction available.
- Bot testing covers base spins, cascades, golden-square state, rainbow activation, coin reveals, feature modes, bonus buy, max-win cap, resume/restart, and history.
- Long-run spin count target defined by certification/product policy.
- RTP reports saved and reproducible.
- Source code and runnable local test environment available for certification lab if required.
- State recovery and request retry behavior inspectable.

## Blockers

- `production_rng_owner_unverified_for_current_gs`
- `certification_bot_test_plan_missing`
- `release_rtp_certification_missing`

