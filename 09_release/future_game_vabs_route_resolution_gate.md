# Future Game VABS Route Resolution Gate

Generated: 2026-05-15

## Reusable Rule

Future games must run a VABS/VBA/Lasthands route-resolution audit before implementing
visual history routes or before marking visual history complete.

## Required Evidence Areas

- legacy/global GS visual history routes;
- current new-games-server history routes;
- game client History button route behavior;
- Casino Manager/backoffice route discovery;
- registration/bootstrap/bank configuration path;
- round replay route;
- session replay route;
- whole-session replay route;
- deterministic replay payload source;
- wallet/accounting reference handling;
- safe blocked/not-found/error behavior.

## Evidence Labels

Use `PROVEN_SOURCE`, `LIKELY_SOURCE`, `CANDIDATE_SOURCE`, `NOT_FOUND`, and `BLOCKED`.

## Release Rule

Stored JSON replay alone is not enough unless current GS/backoffice evidence proves
JSON-only replay is acceptable. If visual route resolution is blocked, GameClientBuilder,
GameServerRegistrar generation, wallet/history tests, and release must remain blocked.
