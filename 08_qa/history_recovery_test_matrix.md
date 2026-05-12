# History Recovery Test Matrix

Status: TEST PLAN ONLY. No wallet/API or history calls were executed.

| Scenario | Expected proof | Status |
|---|---|---|
| Reopen with no unfinished round | `resumegame` or equivalent returns no unfinished state. | blocked |
| Reopen with pending cascade | Restore payload includes grid, cascade index, and pending transitions. | blocked |
| Reopen with feature mode active | Restore payload includes mode and remaining spins/rounds. | blocked |
| Reopen after bonus-buy purchase | Restore payload includes purchased feature start state and accounting boundary. | blocked |
| Reopen after max-win cap | Restore payload marks cap reached and round completion. | blocked |
| History by round | History/replay includes enough v0.3 presentation state to replay. | blocked |
| History by session | History list can summarize rounds without leaking secrets. | blocked |
| LastHand/VABS fallback | Current GS VABS/Lasthand path is mapped or explicitly excluded. | blocked |

## Safety Notes

History reports must use sanitized endpoint paths, request shapes, response shapes, timestamps, game ID, mode, and safe round IDs only. They must not include raw secrets, signatures, session tokens, private links, or full launch URLs.
