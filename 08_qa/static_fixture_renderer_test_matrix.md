# Static Fixture Renderer Test Matrix

Status: MANUAL_LOCAL_QA_PLAN_ONLY.

Do not run browser automation in this sprint.

| Area | Manual check | Expected result |
|---|---|---|
| Prototype warning | Open `index.html` | Non-production and not-a-game-client warnings are visible. |
| Fixture selection | Select all 24 fixtures | Each fixture loads or the file fallback message appears under file restrictions. |
| Grid | Inspect preview | A 6x5 placeholder grid is visible for every fixture. |
| Cascades | Load fixtures 03 and 04 | Removed, dropped, refilled, cluster, and win state indicators appear. |
| Golden-square | Load fixtures 05 and 06 | Golden-square overlays appear. |
| Rainbow | Load fixture 07 | Rainbow activation badge and grid state appear. |
| Coin reveals | Load fixtures 08 to 10 | Coin reveal state appears for bronze, silver, and gold. |
| Special reveals | Load fixtures 11 and 12 | Pot/clover reveal state appears. |
| Feature modes | Load fixtures 13 to 15 | Feature mode badges and detail panels appear. |
| Bonus buy | Load fixtures 16 and 17 | Bonus-buy selection and purchased feature state appear without accounting authority. |
| Win tiers | Load fixtures 18 to 20 | Big, huge, and mega win labels appear. |
| Max cap | Load fixture 21 | Max-win cap overlay/card appears. |
| Completion | Load fixture 22 | Round completion ready state appears. |
| Recovery | Load fixtures 23 and 24 | Reconnect/recovery pending state appears. |
| Safety | Inspect files | No donor/scaffold assets, endpoint calls, package manifest, or dependencies exist. |
