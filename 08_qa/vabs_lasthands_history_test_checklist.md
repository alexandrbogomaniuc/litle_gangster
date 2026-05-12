# VABS / Lasthands / History Test Checklist

Status: QA gate only; no tests executed.

## Required Tests

- In-game History button opens the correct current-GS history path.
- History by round works for Little Gangster.
- History by session works for Little Gangster.
- `/slot/v1/gethistory` returns enough data for player-facing history.
- VABS/replay package, if required, can render a representative Little Gangster round.
- Lasthand or equivalent state records survive reload/reconnect.
- Support/debug output is sanitized and excludes raw SID, token, signature, PASS_KEY, and credentials.

## Blockers

- `vabs_lasthands_history_contract_unverified`
- `little_gangster_vabs_renderer_scope_unknown`

