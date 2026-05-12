# Backend Adapter Fixture Usage Plan

Status: NON_PRODUCTION_TEST_CONTRACT.

Use the 24 strict fixtures as:

- expected-output examples for adapter unit tests;
- patched response schema validation examples;
- v0.3 payload regression examples;
- future client planning fixtures.

Do not use the strict fixtures as:

- production runtime proof;
- wallet/accounting truth;
- registration metadata;
- release evidence;
- browser-authoritative outcome source.

The adapter test harness must strip or isolate non-production fixture metadata when production-mode tests are added.

