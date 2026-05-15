# 8001 VABS Alias Route Contract

Date: 2026-05-15

## Status

Planning only. No alias route was implemented in this sprint.

Recommended decision: `legacy_alias_recommended`.

## Alias Route Pattern

Future implementation should support one guarded legacy-compatible alias pattern for
gameId 8001:

```text
GET /vabs/show.jsp?VIEWSESSID_PARAM:[REDACTED_VIEW_SESSION_ID]&GAMEID=[GAME_ID]&LANG=[LANG]&TIMEZONE=[TIMEZONE]&hideClose=[BOOLEAN]
```

The implementation may either directly render the 8001 visual replay response or safely
redirect to a canonical 8001 render route. The final choice must be verified against
BO/CM behavior.

## Parameter Mapping

| Legacy Parameter | 8001 Mapping | Status |
| --- | --- | --- |
| `VIEWSESSID` | Map to `gameSessionId` unless GS proves a separate view-session id. | LIKELY_SOURCE, needs runtime confirmation |
| `GAMEID` | Must equal `8001`; wrong game id returns safe not-found/blocked response. | PROVEN_SOURCE concept, implementation pending |
| `LANG` | Map to sanitized `lang` / `language`. | PROVEN_SOURCE |
| `TIMEZONE` | Map to sanitized `timeZone`. | PROVEN_SOURCE |
| `hideClose` | Map to boolean display control. | PROVEN_SOURCE |
| `ROUNDID` | Optional round replay id when provided by legacy round history flow. | PROVEN_SOURCE |
| `WHOLE_SESSION` / `wholeSession` | Map to whole-session session replay. | PROVEN_SOURCE |
| `SESSION` / online controls | Accept only if runtime evidence proves needed; otherwise reject safely. | BLOCKED |

## Redirect Vs Direct Render

Recommended first implementation:

- parse and sanitize alias parameters;
- validate `GAMEID = 8001`;
- resolve session/round through the same storage provider used by canonical routes;
- redirect internally or respond with the same safe visual HTML renderer used by
  `/slot/v1/8001/history/render/...`;
- keep canonical routes available and tested.

If BO/CM requires the browser-visible path to remain `/vabs/show.jsp`, direct render is
preferred. If BO/CM accepts redirects, redirecting to canonical routes is acceptable.

## Security And Privacy Requirements

- Do not accept raw tokens, signatures, private hosts, emails, passwords, or secrets.
- Do not persist raw full URLs.
- Sanitize `LANG` and `TIMEZONE`.
- Escape all visual HTML content.
- Do not leak storage errors, wallet refs, or internal source paths.
- Return safe blocked/not-found responses for missing `VIEWSESSID`, wrong `GAMEID`, or
  missing durable replay data.

## Blockers

- `alias_implementation_not_approved`
- `view_session_id_equivalence_unproven_for_8001`
- `exact_registration_config_field_shape_unproven`
- `bo_cm_alias_acceptance_untested`
- `durable_history_storage_unproven`
