# Authoritative Simulation Smoke Test Matrix

| Test | Expected result | Status |
| --- | --- | --- |
| Simulator config parses | `sample_run_config.json` loads | required |
| RTP profiles load | rtp_96, rtp_94, rtp_92 available | required |
| Rule JSON files load | symbol, paytable, feature, cap rules available | required |
| Deterministic seed repeatability | Same seed produces same sample report | future test |
| Sample report generated | `sample_report.json` parses | required |
| Certification claim absent | `certificationClaim=false` | required |
