# Math Config To Backend Adapter Input

Future backend adapter input should combine an authoritative math result with selected model/config metadata.

Required adapter input groups:

- `authoritativeResult`: v0.3 server-owned result object.
- `modelProfile`: selected `rtp_96`, `rtp_94`, or `rtp_92` profile.
- `gameSettingsProfile`: cluster bet settings, feature flags, bonus-buy settings, jackpot disabled state, history flags.
- `statePersistence`: state version, round completion, recovery snapshot, feature state.
- `historyReplay`: deterministic replay payload for VABS/VBA/Lasthands.
- `accountingBoundary`: wallet and purchase references outside `presentationPayload.gamePayload`.

The browser must not provide authoritative result, RNG, win, cap, or wallet fields.
