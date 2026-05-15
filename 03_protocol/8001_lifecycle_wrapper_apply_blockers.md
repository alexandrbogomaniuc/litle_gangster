# Little Gangster 8001 Lifecycle Wrapper Apply Blockers

Created: 2026-05-15

## Remaining Blockers

- VABS/VBA/Lasthands visual history route implementation remains pending.
- Wallet/accounting runtime tests remain pending.
- Bonus-buy runtime validation remains pending.
- Bonus-buy wallet/accounting test remains pending.
- Bonus-buy VABS/Lasthands test remains pending.
- Bonus-buy tail/max-win confirmation remains pending.
- 100x bonus buy remains not certified and not release-approved.
- 125x/150x premium/super bonus-buy tiers remain blocked.
- GameClientBuilder implementation remains blocked.
- GameServerRegistrar generation remains blocked.
- Registration artifacts remain blocked.
- Release remains blocked.

## Typecheck Blocker

The focused Little Gangster lifecycle files pass TypeScript checking, and targeted tests
pass. A broader `src/index.ts` typecheck remains blocked by existing checkout/server
dependency and strictness issues outside the lifecycle wrapper scope.

## Out Of Scope This Sprint

- No VABS visual history route implementation.
- No Gamesv1/games/8001 package.
- No production client code.
- No registration generation.
- No DB/Cassandra action.
- No wallet/API calls.
- No donor browsing or asset capture.
- No release approval.
