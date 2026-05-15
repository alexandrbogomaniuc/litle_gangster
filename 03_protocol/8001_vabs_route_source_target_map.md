# 8001 VABS Route Source Target Map

Generated: 2026-05-15

| Target | Label | Purpose | Risk | Status |
| --- | --- | --- | --- | --- |
| `new-games-server/src/games/little-gangster/history/` | CANDIDATE_SOURCE | Game-specific visual history module. | Medium | Recommended, not
implemented. |
| `new-games-server/src/index.ts` | PROVEN_SOURCE | Route registration host for guarded 8001 paths. | Medium | Future patch target. |
| `new-games-server/src/games/little-gangster/historyMapper.ts` | PROVEN_SOURCE | Existing replay/VABS payload source. | Low | Reuse, no patch this
sprint. |
| `new-games-server/src/games/little-gangster/lifecycle/` | PROVEN_SOURCE | Existing lifecycle/accounting/state/blocker source. | Low | Reuse, no
patch this sprint. |
| `Gamesv1/packages/core-protocol/src/` | PROVEN_SOURCE | Existing JSON `gethistory` protocol. | Medium | Extend only if implementation proves
reusable need. |
| Gamesv1 client History button integration | CANDIDATE_SOURCE | Future client route opener. | High | Strategy documented, implementation blocked. |
| GameServerRegistrar settings mapping | BLOCKED | History route config/registration path. | High | Field shape unproven. |
| Legacy `/vabs/show.jsp` compatibility semantics | PROVEN_SOURCE | CM/backoffice visual route compatibility. | Medium | Must be honored or explicitly
rejected. |

## Recommendation

Implement future 8001 visual history under the Little Gangster history module, register
guarded routes through new-games-server, and provide compatibility with the legacy VABS
parameter model used by GS/CM/backoffice.
