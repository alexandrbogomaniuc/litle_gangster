# RTP Request Validation

Validate the request before any profile generation, simulation, or tuning.

## Required RTP Levels

Every game must define exactly these levels:

- `LOW`
- `MEDIUM`
- `HIGH`

Values are game-specific average theoretical RTP percentages. Decimal RTP values
are allowed and should be normalized or reported to two decimal places where
practical. The allowed range is inclusive:

- minimum: `91.00`
- maximum: `99.70`

Block any value below `91.00` or above `99.70` unless explicit product and
regulatory approval is recorded as a blocker or exception. Do not silently
accept out-of-range values.

## Required Ordering

The target values must be strictly ascending:

`LOW < MEDIUM < HIGH`

Duplicate RTP values are not allowed.

## Examples

Valid requested RTP sets:

- `LOW = 91.00`, `MEDIUM = 96.00`, `HIGH = 99.70`
- `LOW = 93.24`, `MEDIUM = 96.32`, `HIGH = 99.30`
- `LOW = 92.50`, `MEDIUM = 95.75`, `HIGH = 98.90`

Invalid requested RTP sets:

- `LOW = 90.99`, `MEDIUM = 96.00`, `HIGH = 99.70`: LOW is below minimum.
- `LOW = 91.00`, `MEDIUM = 96.00`, `HIGH = 99.71`: HIGH is above maximum.
- `LOW = 95.00`, `MEDIUM = 94.00`, `HIGH = 98.00`: not strictly ascending.
- `LOW = 94.00`, `MEDIUM = 94.00`, `HIGH = 98.00`: duplicate RTP levels.

## Required Volatility Levels

Every game must define exactly:

- `LOW`
- `MEDIUM`
- `HIGH`

Operators select pretested volatility profiles only. They must not enter
arbitrary volatility values.

## Required Matrix

The 3 x 3 matrix must contain exactly 9 profiles. Every profile must include:

- `mathProfileId`
- `rtpLevel`
- `volatilityLevel`
- `targetRtpPercent`
- `targetReturnMultiplier`
- `modelVersion`
- `mathVersion`
- `ruleSetVersion`

Runtime, VABS, Lasthands, and replay history must preserve `mathProfileId`,
RTP level, volatility level, math version, and rules version.
