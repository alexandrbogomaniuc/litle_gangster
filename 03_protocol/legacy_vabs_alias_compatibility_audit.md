# Legacy VABS Alias Compatibility Audit

Date: 2026-05-15

## Scope

This sprint audited whether Little Gangster 8001 should support a legacy-compatible
VABS/VBA/Lasthands alias route in addition to the canonical new-games history routes.
Staging source was inspected read-only. No Staging source, alias code, BO/CM integration
code, client code, registration artifacts, DB/Cassandra changes, wallet calls, donor
browsing, asset capture, certification, or release approval occurred.

## Sanitized Route Shape Analyzed

Only this sanitized legacy route shape was analyzed:

```text
/vabs/show.jsp?VIEWSESSID_PARAM:[REDACTED_VIEW_SESSION_ID]&GAMEID=[GAME_ID]&LANG=[LANG]&TIMEZONE=[TIMEZONE]&hideClose=[BOOLEAN]
```

No raw local/private URL, SID, token, signature, email, password, or secret is persisted
in this audit.

## Evidence Summary

- PROVEN_SOURCE: legacy GS registers VABS/VBA actions around `historyByRound`,
  `historyByToken`, and `getvba`.
- PROVEN_SOURCE: legacy actions resolve session or round identifiers and redirect to
  `/vabs/show.jsp` semantics.
- PROVEN_SOURCE: legacy VABS templates read `VIEWSESSID`, `ROUNDID`, `GAMEID`, `LANG`,
  `TIMEZONE`, `SESSION` or online-session controls, and `hideClose`.
- PROVEN_SOURCE: support/history JSPs expose or open `historyUrl` values for visual
  VABS windows.
- PROVEN_SOURCE: bank config supports `ENABLE_IN_GAME_HISTORY`, `GAME_HISTORY_URL`, and
  `OPEN_GAME_HISTORY_IN_SAME_WINDOW`.
- PROVEN_SOURCE: Gamesv1/new-games canonical JSON history remains
  `POST /slot/v1/gethistory`.
- PROVEN_SOURCE: current 8001 history foundation registers canonical
  `/slot/v1/8001/history/...` JSON/render routes and already maps `VIEWSESSID` query
  input to the session id field.
- NOT_FOUND: no implemented 8001 `/vabs/show.jsp` alias route exists in new-games-server.
- BLOCKED: exact 8001 registration/config field shape for BO/CM route discovery remains
  unproven.

## Answers To Sprint Questions

1. BO/CM legacy behavior expects visual VABS URL semantics comparable to
   `/vabs/show.jsp`; this is PROVEN_SOURCE for legacy GS/support history flows.
2. A game history URL is configurable at bank/bootstrap level through
   `GAME_HISTORY_URL` and `historyPolicy`, but exact 8001 registration artifact field
   shape is BLOCKED.
3. GS can generate legacy history URLs through actions/builders; whether 8001 should
   rely only on generation or explicit config is BLOCKED until integration evidence.
4. Legacy route parameters include `VIEWSESSID`, `GAMEID`, `LANG`, `TIMEZONE`, and
   `hideClose`; this is PROVEN_SOURCE.
5. `VIEWSESSID` is most safely treated as the visual replay session id. For 8001 it
   should map to `gameSessionId` unless GS proves a separate view-session id. The exact
   equivalence remains LIKELY_SOURCE rather than fully proven for 8001.
6. New-games-server can safely serve a guarded alias route in the 8001 history module;
   current foundation already has the route host and parameter sanitizers. This is
   CANDIDATE_SOURCE for future implementation, not implemented here.
7. Little Gangster should support both canonical new-games routes and a
   legacy-compatible alias or redirect strategy for BO/CM compatibility.
8. Later patch targets are `new-games-server/src/games/little-gangster/history/` and
   guarded route registration in `new-games-server/src/index.ts`.
9. Required registration/config remains blocked on exact field shape, but must carry or
   derive the visual history URL before generation.
10. BO/CM compatibility cannot be claimed until targeted alias, canonical render,
    parameter, not-found, and security tests pass.

## Is New-Games Route Alone Enough?

No. The canonical `/slot/v1/8001/history/...` routes are useful for new-games/client
flows, but legacy GS/BO/CM evidence proves visual `/vabs/show.jsp` style semantics.
Until BO/CM acceptance proves it can be configured directly to the canonical routes,
new-games routes alone are not enough for release.

## Recommended Alias Strategy

Decision: `legacy_alias_recommended`.

Little Gangster should later add a guarded legacy-compatible alias route or redirect
handler that accepts sanitized VABS-style parameters and resolves them to the existing
8001 visual render foundation. The alias should not replace canonical routes; both
surfaces should be tested.

## Release Impact

Alias implementation remains blocked until explicit approval. GameClientBuilder,
GameServerRegistrar generation, wallet/history tests, BO/CM compatibility claim,
certification, and release remain blocked.
