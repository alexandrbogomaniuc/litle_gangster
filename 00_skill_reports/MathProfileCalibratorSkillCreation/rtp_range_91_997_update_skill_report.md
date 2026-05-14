# RTP Range 91.00-99.70 Update Skill Report

Created: 2026-05-14

## Outcome

Updated MathProfileCalibrator reusable future-game RTP request rules.

## Rule

- Allowed requested average theoretical RTP range: 91.00% to 99.70%, inclusive.
- Required labels: LOW / MEDIUM / HIGH.
- Required ordering: LOW < MEDIUM < HIGH.
- Decimal RTP values are allowed and reported to two decimals where practical.
- Operators may choose only approved pretested profiles at runtime.

## Scope Guardrails

- Little Gangster RTP values remain 92.00 / 94.00 / 96.00.
- No simulations were run.
- No Little Gangster math values were changed.
- Backend, client, registration, DB, wallet, donor, asset, and release work remained blocked.
