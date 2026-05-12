# Current GS Gamesv1 Validation

## Direct Answer

Gamesv1 / Crazy Rooster / `slot-browser-v1` is partially supported by Staging evidence but remains risky as final truth for Little Gangster. It is a strong candidate integration direction, not a release-ready template.

## Evidence Table

| Assumption | Status | Evidence | Decision |
|---|---|---|---|
| Current GS can route configured game IDs to New Games client. | PROVEN | `BaseStartGameAction.java:819-904`; `BankInfo.java:852-862`; `BankInfoCache.xml:112-142`. | Use as candidate route mechanism. |
| `/slot/v1/*` browser API exists in New Games server. | PROVEN | `new-games-server/src/index.ts:1590-1935`. | Candidate runtime API. |
| WebGS internal bridge exists for New Games. | PROVEN | `NewGamesInternalApiServlet.java:62-67`, `156-299`, `301-375`. | Candidate wallet/session/history bridge. |
| Gamesv1 core protocol expects `slot-browser-v1`. | PROVEN in Gamesv1 package | `GsHttpRuntimeTransport.ts:31-33`; `schemas.ts:26-35`, `64-114`, `190-241`. | Useful client protocol reference. |
| Crazy Rooster 7001 is directly reusable. | CONFLICTING_EVIDENCE | 7001 source exists, but current bank route is virtual route config and no proof that 7001 is a release template for 8001. | Do not copy directly. |
| premium-slot is directly reusable. | BLOCKED | Not inspected enough in this sprint; not requested as source of truth. | Do not select as template. |
| New Games server is final Little Gangster result owner. | CANDIDATE | Sample outcomes are generated in `new-games-server`, but no 8001 math integration exists. | Treat as likely candidate, not final. |
| Registration imports math. | NOT_FOUND | No GS registration persister evidence. | Do not assume. |

## Current Recommendation

Use a modified Gamesv1/New Games direction only as a candidate:

- Preserve it for planning because it has the strongest current routing/runtime evidence.
- Do not mark it final until game 8001 registration, client route, runtime owner, and math integration are proven.
- Do not use Crazy Rooster 7001 or premium-slot as direct templates.

## Issues To Fix If Tests Reveal Mismatch

- Add or correct bank route config for 8001.
- Add per-game client URL for 8001 if needed.
- Align `/slot/v1` result envelope with v0.3 Little Gangster result schema.
- Decide whether runtime owner is `new-games-server`, a game-specific backend package, or a GS processor.
- Generate serialized `scn`/`jcn` config through a proven tool before any DB apply.
