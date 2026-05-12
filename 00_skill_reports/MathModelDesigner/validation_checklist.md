# MathModelDesigner Validation Checklist

| Check | Result | Evidence |
|---|---|---|
| `project_manifest.json` parses | pass | Python JSON parse succeeded |
| `math_package.json` parses | pass | Python JSON parse succeeded |
| `result_schema.json` parses | pass | Python JSON parse succeeded |
| `simulation_config.json` parses | pass | Python JSON parse succeeded |
| RTP target model JSON parses | pass | all `model_config`, `reel_strips`, `paytable`, and `feature_rules` files parsed |
| `simulate_math.py` compiles | pass | `python3 -m py_compile` succeeded |
| Smoke/full simulation can run | pass | 1,000,000 rounds per variant completed |
| Required math output files exist | pass | required file existence/non-empty check passed |
| No browser work occurred | pass | no browser/Chrome MCP tools used |
| No donor asset capture occurred | pass | no files added under `02_reference_assets` during this sprint |
| No donor asset bodies inspected for math | pass | only summary/inventory text was read |
| No DB/Cassandra action occurred | pass | no Cassandra/DB commands run |
| No wallet calls occurred | pass | no wallet endpoints called |
| No raw secrets present | pass | sensitive string scan passed |
| No full donor URL/token values present | pass | sensitive string scan passed |
| Provisional assumptions listed | pass | `04_math/math_assumptions.md` |
| Registration boundary states math import status | pass | `04_math/math_to_gs_registration_boundary.md` says executable math import is UNKNOWN and not assumed |
| Runtime integration contract states where math lives | pass | `04_math/math_runtime_integration_contract.md` |
| RTP report states validation level | pass | `04_math/rtp_report.md` says full-size provisional workflow simulation, not release certification |
| No later skills were run | pass | no later-skill report directories were created |
