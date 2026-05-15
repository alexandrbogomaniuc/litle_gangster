# Registration Math Field Extraction

Registration math fields must be evidence-backed or blocked.

## Fields

- `POSSIBLE_MODELS`
- `RTP_MIN`
- `RTP_WITHOUT_BF`
- `RTP_MIN_WITHOUT_BF`
- `BF_RTP`
- `BF_RTP_MIN`
- `BF_BETS`
- `SD_KEYS`
- `CAP_WIN_MULTIPLIER`
- `MAX_WIN`
- `POSSIBLE_MAX_WINS`
- `POSSIBLE_MAX_WINS_WITHOUT_BF` if used
- `VOLATILITY`
- `mathProfileId`
- profile display mapping

## Constraints

- Operators choose only pretested profiles.
- Operators must not enter arbitrary RTP/volatility values at runtime.
- `mathProfileId` identifies RTP, volatility, math version, and rules version.
- VABS/Lasthands/history must store `mathProfileId`, RTP level, volatility
  level, math version, and rules version.
- `SD_KEYS` maps to math model/profile RTP plus standard deviation, not feature
  names.
- `POSSIBLE_MODELS >= max(RTP_WITHOUT_BF, BF_RTP, any supported strategy RTP)`.
- `BF_RTP <= POSSIBLE_MODELS`.
- CAP_WIN/MAX_WIN unresolved states block registration generation.
- GL bet settings must define cluster-equivalent `baseBetCredits` and
  `possibleLines` compatibility.
