# RTP Flexibility Notes

The package supports `rtp_96`, `rtp_94`, and `rtp_92` through separate model profiles. The simulator reads the selected model by `modelId` instead of hardcoding one RTP target.

Each model records target RTP, RTP without bonus buy, bonus-buy RTP, min/max RTP, volatility, contribution targets, max-win values, and status fields. The candidate values are not final and must be calibrated by large-scale simulation
before use in implementation or registration.
