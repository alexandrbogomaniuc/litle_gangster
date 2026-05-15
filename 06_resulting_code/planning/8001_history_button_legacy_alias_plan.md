# 8001 History Button Legacy Alias Plan

Date: 2026-05-15

## Client Strategy

GameClientBuilder must not hardcode a private host or raw visual history URL. The
in-game History button should use a bootstrap/backend-generated history URL.

## Recommended Runtime Behavior

1. Read `historyPolicy.gameHistoryUrl` or equivalent bootstrap/backend field.
2. If the configured URL is a legacy alias route, append or preserve sanitized
   `LANG`, `TIMEZONE`, and `hideClose` controls as required by the backend contract.
3. If the configured URL is canonical, use the backend-generated
   `/slot/v1/8001/history/render/...` visual route.
4. If no visual route is provided, show a blocked/not-available state instead of
   pretending JSON history is visual VABS.
5. Never build a private absolute host in client code.

## Preferred Route Source

Use bootstrap/backend-generated URL strategy.

Allowed future route families:

- legacy-compatible alias route for BO/CM if configured;
- canonical `/slot/v1/8001/history/...` route for new-games/client use.

## Blockers

- `gameclientbuilder_implementation_blocked`
- `history_button_route_runtime_not_tested`
- `bo_cm_alias_acceptance_untested`
- `exact_registration_config_field_shape_unproven`
