# Scene Replacement Plan

## Scene Direction

| Scene | Original Treatment | Key Object IDs | Priority |
|---|---|---|---|
| Loading / intro | Neon alley title reveal with three original feature cards | `scene.loading.*` | high |
| Base game | Night city / backroom board with 6x5 neon vault grid | `scene.base.*`, `scene.base.grid.*` | critical |
| Free spins | `Heist Mode` with warmer gold lighting and vault-progress overlays | `scene.free_spins.*` | critical |
| Bonus buy | `Start the Job` purchase panel with clear cost/confirm/cancel states | `scene.bonus_buy.*` | critical |
| Big win | `Vault Break` money burst, animated counter, tier labels | `scene.big_win.*` | critical |
| Settings/help/rules | Dark metal panels, readable cream text, simple icon language | `scene.settings.*`, `scene.rules.*` | high |
| Desktop/mobile layouts | Safe-area validated positioning, no cropped core controls | `scene.layout.*` | medium |
| Error/reconnect | Calm modal style with clear retry/home actions | `scene.error.*`, `scene.reconnect.*` | high |

## Scaffold Use

Scaffold preview paths in `05_art/scaffold_asset_object_mapping.json` may be used to understand placement and scale. They must not be used in release.
