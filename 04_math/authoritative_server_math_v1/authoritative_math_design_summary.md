# Authoritative Math Design Summary

Evidence basis:

- PROVEN: v0.3 result contract exists under the project math package.
- PROVEN: strict fixture variants can carry v0.3 payloads through `presentationPayload.gamePayload`.
- PROVEN: browser/client authority is disallowed by project contracts.
- PROVEN: registration is metadata/config/routing, not executable math import.
- CANDIDATE: backend integration should use a future game-specific server module and runtime adapter.
- NOT AUTHORITATIVE: 7001 / Crazy Rooster math, RNG, feature probabilities, history behavior, jackpot behavior, and state machine.

The Little Gangster math owner should be a server-side game module that produces authoritative results before the runtime adapter maps them into `/slot/v1` responses. The browser must only render server output and request user actions.

The v1 design covers:

1. Base game 6x5 cluster evaluation.
2. Cascades with removed, dropped, and refilled cells.
3. Golden-square creation and persistence.
4. Rainbow activation.
5. Coin reveals.
6. Pot and clover special reveal candidates.
7. Three feature modes.
8. Free-spin / feature-spin loop.
9. Bonus-buy state boundary.
10. Optional jackpot hooks.
11. Max-win cap.
12. Win tiers.
13. RNG draw ownership.
14. State persistence and recovery.
15. VABS / VBA / Lasthands / history storage.
16. Local simulation, bot testing, and lab readiness.
17. Backend adapter input and runtime payload output contracts.
18. Registration metadata separation.

Implementation status:

- Math design completed as planning documentation.
- No implementation code created.
- No backend adapter created.
- No 8001 package created.
- No Staging source modified.
- Release remains blocked.

