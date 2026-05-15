# Bonus-Buy Validation Policy

Bonus buy is separate from base RTP.

## Required Decisions

- Is bonus buy in scope?
- What cost options exist?
- What is the purchased feature start state?
- Does the purchased feature have profile-specific or volatility-specific
  behavior?
- Is BF_RTP equal to base RTP, product-defined, or observed-and-declared?
- What are BF_RTP, BF_RTP_MIN, and BF_BETS?

## Formula

`BF_RTP = 100 * totalPurchasedFeatureWinCredits / totalBonusBuyCostCredits`

## Registration Rules

- Keep `RTP_WITHOUT_BF` separate from `BF_RTP`.
- Keep `RTP_MIN_WITHOUT_BF` separate from `BF_RTP_MIN`.
- `BF_RTP` must not exceed `POSSIBLE_MODELS`.
- `POSSIBLE_MODELS` must cover the maximum RTP across base, bonus buy, and any
  other supported strategy.
- CAP_WIN applies to bonus buy based on base bet, not bonus-buy stake.

## Blockers

If bonus-buy runtime, wallet accounting, history/VABS, tail/max-win, or product
approval is missing, keep registration and release blocked.
