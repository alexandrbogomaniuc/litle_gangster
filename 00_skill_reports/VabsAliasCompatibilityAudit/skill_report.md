# VABS Alias Compatibility Audit Skill Report

Date: 2026-05-15

## Sprint

ProtocolAndSchemaMapper legacy VABS alias compatibility audit and GameServerRegistrar
VABS route configuration audit only.

## Outcome

Completed. Staging source was inspected read-only. No Staging source was modified and
no alias, BO/CM, client, registration, wallet, DB, or release action was performed.

## Decision

Recommended alias decision: `legacy_alias_recommended`.

Legacy `/vabs/show.jsp` semantics are proven in GS/source for visual VBA/VABS history
flows. Current 8001 canonical new-games history routes are useful but do not by
themselves prove BO/CM compatibility.

## Registration Finding

Registration/config is required as a concept, but exact 8001 field shape remains
blocked. `GAME_HISTORY_URL` and bootstrap `historyPolicy.gameHistoryUrl` are proven; an
8001-specific `vabsUrl`, `vbaUrl`, `historyUrl`, or `historyBaseUrl` generation path is
not proven.

## Safety

The user-provided legacy route was recorded only in sanitized shape. No raw [REDACTED_LOOPBACK_HOST]
URL, private URL, SID, token, signature, email, password, or secret was persisted.
