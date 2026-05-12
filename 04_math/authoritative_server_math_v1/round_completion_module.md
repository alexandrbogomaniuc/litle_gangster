# Round Completion Module

Purpose: mark when a round is complete and safe to settle/history-store.

Completion reasons:

- no more base cascades.
- feature completed.
- max-win cap reached.
- bonus-buy feature completed.
- closed after no active round.
- recovery pending, not complete.

Completion output:

- roundComplete boolean.
- completionReason.
- finalGrid.
- totalWin.
- cappedWin.
- stateVersion.
- historySnapshotReference.
- settlementReference outside game payload.

Rules:

- Round completion must be server-owned.
- Browser cannot mark a round complete.
- Incomplete recovery states must remain resumable.

