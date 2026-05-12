# Backend Adapter Implementation Approval Gate

Status: IMPLEMENTATION_NOT_APPLIED.

Backend adapter implementation remains blocked.

## Approval Required

Before source modification, the user must explicitly approve:

- modifying Staging source;
- creating `new-games-server/src/games/little-gangster/` files;
- adding a guarded 8001 branch to `new-games-server/src/index.ts`;
- adding tests under `new-games-server/test/little-gangster/`;
- running scoped local tests.

## Future Scope

Approved future scope should be limited to backend adapter source, schema tests, history/recovery tests, and a guarded
non-live 8001 payload branch.

## Rollback Required

The future implementation sprint must record:

- pre-patch git status;
- pre-patch commit hash or hash evidence;
- changed files;
- exact rollback command or file restore path;
- validation commands after rollback.

## Tests Required

- Adapter unit tests.
- Patched response schema tests.
- v0.3 result schema tests.
- History/recovery tests.
- 7001 regression tests.
- UI-kit passthrough regression if affected.

## Gate Result

`backend_adapter_implementation_allowed=false`

`gameclientbuilder_implementation_allowed=false`

