# Backend Adapter Unit Test Plan

Status: TEST_PLAN_ONLY.

Future unit tests should cover:

- valid adapter output for all 24 strict fixtures;
- `gameKey` equals `little-gangster`;
- `schemaVersion` equals `v0.3`;
- v0.3 payload is nested under `presentationPayload.gamePayload.payload`;
- wallet/accounting values are outside `gamePayload`;
- browser/client input cannot supply authoritative result fields;
- max-win cap output is backend-owned;
- feature mode and bonus-buy state output is backend-owned;
- non-production fixture metadata is rejected or absent in production-mode adapter tests.

No tests were run in this planning sprint.

