# Little Gangster v0.2 6x5 Cluster Assumptions

All items are `PROVISIONAL_ASSUMPTION` unless later evidence proves them.

- The target layout is 6 reels by 5 rows to align with reference research and downstream art/client needs.
- Wins use orthogonally adjacent connected clusters of at least 5 matching symbols.
- Wild substitutes for cluster pay symbols but not scatter.
- Scatter pays and triggers free spins.
- Free spins use a 2x cluster-win multiplier and allow retriggers capped at 50 free spins.
- Bonus buy is present as a feature contract but is not included in base-spin RTP validation.
- Double-up is a neutral placeholder only.
- Jackpot is not modeled.
- Variant RTP is tuned through explicit paytable values, not runtime scaling.
- Production RNG/result generation must be server/backend-side, not browser-side. Exact owner remains unproven: classic GS, new-games backend, game-specific server package, and GS game processor remain candidates.
- Browser client is not allowed to be authoritative for real-money RNG/results.
