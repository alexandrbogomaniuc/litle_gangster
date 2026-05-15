# 8001 VABS Alias Implementation Gate

Date: 2026-05-15

## Gate Status

Alias implementation is not approved in this sprint.

## Requirements Before Implementation

- Explicit approval to modify Staging source for alias implementation.
- Accepted route contract for `VIEWSESSID`, `GAMEID`, `LANG`, `TIMEZONE`, `hideClose`,
  round replay, session replay, and whole-session replay.
- Decision whether alias direct-renders or redirects to canonical 8001 render route.
- Test plan covering BO/CM, canonical route, security, missing session, and wrong game id.

## Requirements Before Compatibility Claim

- Targeted alias route tests pass.
- Canonical 8001 route tests still pass.
- BO/CM iframe/window/redirect behavior is tested or explicitly blocked.
- Registration/bootstrap path for the visual URL is proven.
- Durable history storage path is proven or accepted as a blocker for non-release test
  environments.

## Still Blocked

- `alias_implementation_not_approved`
- `bo_cm_alias_acceptance_untested`
- `exact_registration_config_field_shape_unproven`
- `durable_history_storage_unproven`
- `gameclientbuilder_implementation_blocked`
- `gameserverregistrar_generation_blocked`
- `release_not_approved`
