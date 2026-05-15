# Future Game RTP Range Rule

This rule applies to reusable future-game math profile requests. It does not
change Little Gangster's current RTP values.

## Required RTP Levels

Every future game has exactly three requested average theoretical RTP levels:

- `LOW`
- `MEDIUM`
- `HIGH`

These are labels, not fixed values. Actual percentage values are game-specific.

## Allowed Range

Each requested average theoretical RTP value must be within this inclusive
range:

- minimum: `91.00%`
- maximum: `99.70%`

Decimal RTP values are allowed. Values should be normalized or reported to two
decimal places where practical.

## Ordering

The requested RTP values must be strictly ascending:

`LOW < MEDIUM < HIGH`

Duplicate RTP levels are not allowed.

## Operator Selection

Operators may choose only from approved pretested profiles. They must not enter
arbitrary RTP values at runtime. Runtime profile selection must resolve the
chosen RTP level and volatility level to an approved `mathProfileId`.

## Valid Examples

- `LOW = 91.00`, `MEDIUM = 96.00`, `HIGH = 99.70`
- `LOW = 93.24`, `MEDIUM = 96.32`, `HIGH = 99.30`
- `LOW = 92.50`, `MEDIUM = 95.75`, `HIGH = 98.90`

## Invalid Examples

- `LOW = 90.99`, `MEDIUM = 96.00`, `HIGH = 99.70`: LOW is below `91.00`.
- `LOW = 91.00`, `MEDIUM = 96.00`, `HIGH = 99.71`: HIGH is above `99.70`.
- `LOW = 95.00`, `MEDIUM = 94.00`, `HIGH = 98.00`: values are not strictly ascending.
- `LOW = 94.00`, `MEDIUM = 94.00`, `HIGH = 98.00`: duplicate RTP levels are not allowed.

## Exception Process

Only explicit product and regulatory approval may override the `91.00%` to
`99.70%` range. Any override must be recorded as a blocker or exception with
approval source, date, scope, and affected profiles. Overrides must not be
silently accepted by calibration scripts or handoffs.

## Little Gangster Current Values

Little Gangster currently remains:

- `LOW = 92.00%`
- `MEDIUM = 94.00%`
- `HIGH = 96.00%`

These values remain unchanged unless a future sprint explicitly requests a
Little Gangster RTP profile change.
