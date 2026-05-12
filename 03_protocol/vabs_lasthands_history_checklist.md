# VABS / Lasthands / History Checklist

Status: advisory current-GS checklist.

## Current Source Signals

| Signal | Evidence | Meaning | Status |
|---|---|---|---|
| VABS by round | `HistoryByRoundAction.java:31-80` builds a `/vabs/show.jsp` redirect from a round id and game session lookup. | GS has a round-to-VABS history route. | proven concept |
| VBA URL by session | `GetVBAAction.java:22-67` builds a VABS URL from a game session id. | GS can generate a session-oriented VABS URL. | proven concept |
| Lasthand data | `CommonWalletManager.java` and transaction data classes reference Lasthand existence and round-finished checks. | Lasthand remains a GS wallet/state/history concern. | proven concept |
| New-games history bridge | `NewGamesInternalApiServlet.java:62-67` exposes `/history/write` and `/history/read`. | New-games runtime can bridge history to GS. | proven concept |
| `/slot/v1/gethistory` | `new-games-server/src/index.ts:1878-1976` reads GS history when available and falls back to local cache. | Browser runtime history endpoint exists. | proven concept |

## Required Future Verification

- Determine whether Little Gangster needs a project-specific VABS renderer/package.
- Determine whether the 6x5 donor-parity result contract writes enough history for replay.
- Determine whether `betData` and `servletData` must include cascade/golden-square/reveal state.
- Verify History button behavior in the final client.
- Verify history by round and history by session.
- Verify sanitized debug output for support without raw SID/token/signature values.

## Blockers

- `vabs_lasthands_history_contract_unverified`
- `little_gangster_vabs_renderer_scope_unknown`
- `slot_v1_gethistory_to_vabs_mapping_unverified`

