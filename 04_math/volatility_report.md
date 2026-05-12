# Volatility Report

Generated: 2026-05-11 07:45:26 

## Target
High volatility.

## Observed Workflow Proxies
- Highest observed standard deviation by variant: `{'rtp_96': 9.352953, 'rtp_94': 9.158891, 'rtp_92': 8.96061}`.
- Feature trigger frequencies by weighted run: `{'rtp_96': 5.90325, 'rtp_94': 5.90325, 'rtp_92': 5.90325}`.
- High variance is visible in individual 100k/200k seed RTP drift; this is expected from the provisional feature reveal model and remains a release-validation risk.

## Status
High-volatility proxy satisfied for workflow planning, but independent certification-grade volatility/RTP validation remains blocked.
