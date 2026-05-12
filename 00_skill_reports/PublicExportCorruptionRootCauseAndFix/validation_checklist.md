# PublicExportCorruptionRootCauseAndFix Validation Checklist

- [x] External contradiction recorded for `ca854797d2d67def46f17dd989164b71ce49cc44`.
- [x] Previous checkpoint validation claim reset before trusting new output.
- [x] Root cause report created.
- [x] Project-local raw validator created outside public export.
- [x] Public export rebuilt with newline-preserving copy/redaction.
- [x] Public-export internal validator compiled.
- [x] Public-export internal validator ran and passed.
- [x] Git blob line counts passed.
- [x] Replacement commit pushed to main.
- [x] Project-local raw validator ran against pushed commit `25cbf1c3f8ce1d6f89871f11a43f40478a8e2e6c` and passed.
- [x] Curl raw line counts matched required thresholds.
- [x] No Staging source inspected or modified.
- [x] No game workflow implementation ran.
- [x] No wallet/API/DB/donor browsing/asset capture/release approval occurred.
