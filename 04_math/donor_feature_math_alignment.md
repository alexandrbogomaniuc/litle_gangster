# Donor Feature Math Alignment

Generated: 2026-05-11 11:05:00 Europe/London

## Alignment Status After v0.3 Contract Completion

| Donor feature | v0.3 status | Notes |
|---|---|---|
| 6x5 cluster grid | represented | Selected layout remains 6 columns by 5 rows. |
| Super cascade | represented at contract level | Result schema exposes removal, drop, refill, repeat sequence, cascade index, cascade win, and final grid. |
| Golden squares | represented provisionally | State fields exist; exact persistence remains blocked. |
| Rainbow activation | represented provisionally | Activation events expose rainbow positions and affected golden squares. |
| Bronze/silver/gold coin reveal | represented provisionally | Result schema exposes tier/value/source/cascade fields; values/probabilities remain blocked. |
| Pot/clover reveal chance | represented as candidate | Exact probability/value remains blocked. |
| Three feature modes | represented provisionally | Neutral mode keys used until exact names/rules are confirmed. |
| Bonus buy | contract updated | Cost/EV/current-GS representation and confirmation flow remain blocked. |
| Max win 10,000x | represented | Cap fields include cap, pre-cap/capped win, cap step, and possible-max-win placeholders. |
| Win tiers | represented as candidate | Uses Mantis advisory thresholds pending current-GS/product confirmation. |
| Round completion/state persistence | represented | Backend-owned completion and persistence fields added. |
| Double-up/gamble | removed from active scope | Not observed in donor; requires user override to re-add. |

## Build Impact

v0.3 completes the math/result contract, but ArtSceneMapper update is required before GameClientBuilder because explicit v0.3 animation states are not yet fully mapped in scene JSON. Full GameClientBuilder remains blocked.
