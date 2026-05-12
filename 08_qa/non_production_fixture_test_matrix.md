# Non-Production Fixture Test Matrix

Status: TEST_PLAN_ONLY.

| Test area | Fixtures | Expected result | Boundary |
|---|---|---|---|
| Base idle/no-win | 01, 02 | Grid and round-ready states render without wins. | No RNG or outcome generation. |
| Cascades | 03, 04 | Removed, dropped, refilled, cluster, and total win states sequence in order. | Client consumes backend-shaped data only. |
| Golden/rainbow | 05, 06, 07 | Golden overlays and rainbow affected cells display. | Persistence is fixture state, not runtime proof. |
| Coin/special reveals | 08, 09, 10, 11, 12 | Reveal tier/candidate states display. | Values are not certified payouts. |
| Feature modes | 13, 14, 15 | Three mode panels can be selected/displayed by fixture state. | Feature progression remains backend-owned. |
| Bonus buy | 16, 17 | Selection and purchased start state display without wallet authority. | No wallet call or accounting mutation. |
| Win tiers/cap | 18, 19, 20, 21 | Big/huge/mega and cap overlays display from fixture fields. | Cap is backend-owned. |
| Round/reconnect | 22, 23, 24 | Completion, restore, and recovery-pending states display. | Restore truth remains backend-owned. |
