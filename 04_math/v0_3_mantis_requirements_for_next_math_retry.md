# v0.3 Mantis Requirements For Next Math Retry

Status: next-retry requirements only.

## Required Additions / Checks

The next MathModelDesigner retry should verify or patch the `v0.3_donor_feature_parity_provisional` contract to include:

- Cascade/golden-square/rainbow/coin/feature-mode donor parity.
- Round completion state that can map to current GS/new-games and, if needed, `roundFinishedHelper` / `endRoundSignature`.
- `winRatio` and `winTier` animation hints.
- Max-win cap fields:
  - theoretical/observed possible max win,
  - possible max win credits,
  - cap multiplier,
  - cap reached flag,
  - pre-cap win,
  - capped win,
  - cap reached at step.
- 6x5 cluster bet formula mapping to current GS configuration.
- State/lastAction/Lasthand handoff fields for restore and history.
- Process-transaction-equivalent handoff fields for current lane.
- RNG consumption boundary and production RNG ownership blocker.
- No active double-up/gamble unless donor evidence appears.

## Current-Lane Translation

If current GS uses the new-games `slot-browser-v1` lane, translate Mantis transaction lessons into:

- `/slot/v1/playround` selected bet and idempotency behavior.
- New-games backend wallet reserve/placebet behavior.
- `/slot/v1/featureaction` collect/feature continuation behavior.
- `/slot/v1/resumegame` restore behavior.
- `/slot/v1/gethistory` history/replay behavior.
- GS internal history and wallet bridge behavior.

If current GS later proves ExtGame, then and only then map to ExtGame endpoint names.

## Release Boundary

These requirements do not approve math for release. RTP, RNG, bot testing, certification, and runtime integration remain release blockers.

