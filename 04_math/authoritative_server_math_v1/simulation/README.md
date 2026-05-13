# Local Authoritative Math Simulator

This artifact is planning and local simulation material only. It is not production math, not backend adapter code, not registration output, not wallet integration, not client code, and not release approval. Exact values are not final or
certified.


This folder contains a local deterministic smoke simulator. It is not production code and must not be used for wallet, GS, runtime, or certification flows.

## Run

```bash
python3 simulate_authoritative_math.py --config sample_run_config.json --output sample_report.json
```

The script loads planning configs from `../simulation_config_refinement`, generates deterministic pseudo-rounds, and writes a sample report with feature contribution, cap frequency, win-tier distribution, and one deterministic replay
payload.
