# 8001 VABS Alias Route Decision

Date: 2026-05-15

## Decision

`legacy_alias_recommended`

## Rationale

Legacy GS/source evidence proves `/vabs/show.jsp` style visual history semantics for
VBA/VABS round/session access and BO/support history flows. Current Little Gangster
8001 history routes provide canonical new-games JSON/render route foundations, but no
legacy-compatible alias route exists yet.

Because BO/CM acceptance of canonical new-games routes is still unproven, Little
Gangster should support both:

- a legacy-compatible alias or redirect surface for BO/CM and legacy history links;
- canonical `/slot/v1/8001/history/...` routes for new-games/client use.

## Why Not `legacy_alias_required`

The alias is strongly recommended, but exact 8001 registration/config field shape and
BO/CM route acceptance are still blocked. The decision should become
`legacy_alias_required` if integration evidence proves BO/CM cannot be configured to
open canonical 8001 visual routes directly.

## Why Not `new_games_routes_sufficient`

Canonical new-games routes do not by themselves prove BO/CM compatibility. Stored JSON
and `/slot/v1/gethistory` are not equivalent to visual VABS/VBA/Lasthands replay.

## Implementation Status

No alias code was implemented in this sprint. Alias implementation requires explicit
approval.
