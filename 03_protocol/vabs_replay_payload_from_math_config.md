# VABS Replay Payload From Math Config

The refined math config defines a deterministic replay payload shape for VABS/VBA/Lasthands planning.

Required replay fields: starting grid, cascade steps, removed cells, refilled symbols, final grid, win summary, win tier, cap state, feature state, bonus-buy state, RNG draw references, state version, round completion, and replay metadata.

The sample simulator writes `vabsReplaySample` to `04_math/authoritative_server_math_v1/simulation/sample_report.json`. It stores RNG draw references only, not raw RNG secrets. It stores no screenshot binary; screenshot requirement remains
unverified.
