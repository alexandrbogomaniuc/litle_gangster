# RTP / Volatility Profile Framework

Created: 2026-05-13T08:55:01Z

## Product Rule

Every future game must define exactly three RTP levels: `LOW`, `MEDIUM`, and `HIGH`. The actual percentages are game-specific, but each approved RTP must be within `92.00%` and `99.00%`. Values outside that range are blocked unless explicit
product and regulatory approval exists.

Every future game must also define exactly three volatility levels: `LOW`, `MEDIUM`, and `HIGH`. Operators may select only pretested approved RTP/volatility combinations. Arbitrary untested operator values are not allowed.

## Little Gangster Provisional Mapping

- LOW RTP: `92.00%` (`0.92` return multiplier), legacy model `rtp_92`.
- MEDIUM RTP: `94.00%` (`0.94` return multiplier), legacy model `rtp_94`.
- HIGH RTP: `96.00%` (`0.96` return multiplier), legacy model `rtp_96`.

These values are Little Gangster provisional values only. Future games may use different LOW/MEDIUM/HIGH values inside the allowed range.

## Required Separation

- Registration display RTP is metadata.
- Actual math RTP is produced by a pretested math profile.
- RTP with bonus buy and RTP without bonus buy must be reported separately.
- Every profile must carry `mathProfileId`, `modelVersion`, `mathVersion`, and `ruleSetVersion`.
- Bonus-buy EV remains separate and currently blocked for Little Gangster.

## Volatility Dimensions

Volatility profiles are game-specific and must be pretested. Volatility may affect symbol weights, paytable distribution, feature frequency, feature size, coin reveal values, max-win frequency, hit rate, and standard deviation. Volatility
cannot be changed dynamically outside approved profiles.

## Operator Rule

Operator choice resolves to one approved `mathProfileId`, for example:

```json
{
  "rtpLevel": "MEDIUM",
  "volatilityLevel": "HIGH",
  "mathProfileId": "LG_8001_RTP_MEDIUM_VOL_HIGH"
}
```

The client/browser may display profile identity for history/replay, but it must not choose or mutate the profile.
