# VABS Route Resolution Decision Matrix

Generated: 2026-05-15

| Model | Description | Evidence | Fit for 8001 | Risk | Decision |
| --- | --- | --- | --- | --- | --- |
| Model A | GS/global legacy routes generate history/VBA links. | PROVEN_SOURCE: legacy `/vabs/historyByRound`, `/vabs/historyByToken`, `/getvba`,
`/vabs/show.jsp`, game-history JSP/XML. | Strong for CM/backoffice compatibility. | Does not by itself provide new-games 8001 render module or payload
mapping. | Keep compatibility requirement. |
| Model B | Game/bank/registration config stores external VBA/VABS base URL. | LIKELY_SOURCE: bank history URL and bootstrap history policy.
NOT_FOUND: explicit release-registration VABS URL field. | Needed as config concept, but exact registration field is blocked. | Registration
generation could guess wrong fields. | Required, but field shape blocked. |
| Model C | new-games-server serves per-game history/VBA routes. | PROVEN_SOURCE: new-games-server route host and `/slot/v1/gethistory`;
CANDIDATE_SOURCE for visual 8001 routes. | Best location for 8001-specific JSON replay and visual render wrapper. | Must avoid bypassing GS/CM
discovery expectations. | Use as implementation host. |
| Model D | Game client contains/render route path and GS/CM redirects into it. | CANDIDATE_SOURCE only; Gamesv1 has a History control, but visual
VABS route is not proven. | Not enough proof to make client own history URL resolution. | Hardcoded client URLs could break CM/backoffice. | Do not
select alone. |
| Model E | Hybrid: GS/CM uses configured or generated visual route; new-games-server serves visual replay; client links to same resolved route. |
Supported by legacy visual route evidence plus new-games JSON/payload evidence. | Best fit for Little Gangster and reusable future-game workflow. |
Requires explicit config mapping and tests across launch, client, and CM/backoffice. | Recommended. |

## Recommended Model

Use Model E.

Little Gangster should implement a game-specific 8001 visual history module under
new-games-server and expose route shapes that can serve both new `/slot/v1/8001/history`
access and legacy-compatible VABS access/redirect semantics. Registration/config must
carry or derive the history route explicitly before GameServerRegistrar generation.
