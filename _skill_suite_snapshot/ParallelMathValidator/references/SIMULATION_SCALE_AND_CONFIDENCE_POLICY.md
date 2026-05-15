# Simulation Scale And Confidence Policy

Simulation results must state scale, seed family, confidence, and limitations.

## Minimum Reporting Fields

- `mathProfileId`
- RTP level and requested RTP
- volatility level
- rounds simulated
- RTP result
- standard deviation
- hit rate
- cap frequency
- max observed win
- seed family
- simulator version
- exact values final: yes/no
- certification status: yes/no

## Confidence Labels

- `smoke`: proves path executes only.
- `train`: suitable for train-only calibration decisions.
- `validation`: independent confirmation against declared target.
- `tail_pilot`: planning evidence for max-win/cap behavior, not final.
- `tail_large`: stronger cap/max-win confidence, still not certification by
  itself unless the release/lab gate approves.
- `certification_package`: assembled evidence for review, not approval.

## Gate Discipline

Do not compare validation results against a target that was tuned using
validation seeds. Do not call values final unless final lab/release approval is
explicit.
