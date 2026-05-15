# 8001 VABS Visual History Implementation Gate

Created: 2026-05-15

## Gate Status

VABS/VBA/Lasthands visual history route implementation is not approved by this sprint.

## Implementation Requires Explicit Approval

A future implementation sprint must explicitly approve:

- creation of `new-games-server/src/games/little-gangster/history/`;
- guarded route registration in `new-games-server/src/index.ts`;
- tests under `new-games-server/test/little-gangster/`;
- any core-protocol or UI-kit changes if required.

## Release Rules

Release remains blocked until:

- JSON replay route is implemented and tested;
- visual HTML/render response is implemented or explicitly blocked/accepted with evidence;
- in-game History button behavior is tested;
- Casino Manager/backoffice access is tested;
- round, session, and whole-session replay are tested;
- wallet/accounting references are present;
- no raw tokens, signatures, private URLs, or secrets are exposed.

GameClientBuilder remains blocked for release scope until visual history behavior is
accepted. GameServerRegistrar generation remains blocked until runtime/history gates and
registration settings are resolved.
