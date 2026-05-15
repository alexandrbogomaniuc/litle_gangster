# 8001 VABS Visual History Storage Contract

Created: 2026-05-15

## Storage Principle

Visual history must be reconstructable from server-owned history data. Browser/client
state may render the replay but must not become the authoritative source.

Deterministic replay is the authoritative source of truth. Screenshot and video media
are optional supporting evidence only.

## Required Sources

- lifecycle wrapper state persistence:
  - `stateVersion`
  - `roundId`
  - `clientOperationId`
  - `idempotencyKey`
  - `lastSuccessfulAction`
  - `pendingAction`
  - `currentCascadeIndex`
  - `featureMode`
  - `freeSpinState`
  - `bonusBuyState`
  - `recoverablePayload`
  - `reconnectHints`
  - `restartRequired`
- backend adapter `historyReplay`
- backend adapter `vabsFields`
- `presentationPayload.gamePayload`
- action accounting:
  - action id
  - action type
  - idempotency key
  - wallet/accounting references
  - pending/stuck action marker
- round completion:
  - cascades complete
  - free spins complete
  - bonus-buy feature complete
  - cap enforcement complete
  - settlement complete
  - restart advisory status

## Wallet / Accounting References

History must include references sufficient for audit and replay:

- wallet operation id
- debit transaction id where applicable
- credit transaction id where applicable
- reserve/settle or equivalent action references
- purchase id for 100x bonus buy
- round id
- game session id
- player session id if available

No wallet endpoint calls are allowed by this planning sprint.

## Durable Storage Blocker

The current local in-memory `historyBySession` and `rounds` cache is useful for local
smoke testing only. Release needs an approved durable source or current GS integration
proof. If storage is unavailable, visual history route implementation must return a
blocked/missing-history response rather than inventing replay data.

## Optional Media Policy

Route foundations should be able to carry:

- `historyEvidenceMode`;
- `historyCaptureScope`;
- media manifest reference;
- screenshot references;
- video references;
- checksums;
- retention expiry;
- storage provider name.

This sprint does not implement durable media storage, screenshot capture, or video
capture. Full video for every spin is not default because of storage and performance
risk.
