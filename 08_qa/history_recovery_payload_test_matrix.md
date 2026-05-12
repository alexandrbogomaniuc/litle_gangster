# History Recovery Payload Test Matrix

Status: TEST_PLAN_ONLY_NOT_RUN.

| Test | Purpose | Expected result | Evidence label |
|---|---|---|---|
| Resume unfinished round | Verify restore payload can reconstruct v0.3 render state. | Reconnect resumes same round/cascade/feature state. | BLOCKED_8001 |
| Get history final round | Verify replay includes final v0.3 presentation snapshot or reconstructable state. | Replay renders same final state. | BLOCKED_8001 |
| VABS/Lasthand archive | Verify platform history payload includes needed betData/servletData or equivalent. | Audit/replay fields present. | BLOCKED_8001 |
| Idempotent duplicate request | Verify duplicate operation does not create second outcome. | Same response or safe duplicate marker. | REQUIRED_TEST |
| Cap and feature history | Verify max-win cap and feature modes are replayable. | History contains cap/feature state. | REQUIRED_TEST |
| Client memory loss | Verify browser refresh does not lose authoritative state. | Backend restore/history owns recovery. | REQUIRED_TEST |
