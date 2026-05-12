# Client Animation State Contract

Generated/updated: 2026-05-11 11:05:00 Europe/London

Status: PROVISIONAL_CONTRACT. This is not donor-true certified math, not runtime code, not registration generation, and not release approval.

## Animation Inputs From Backend Result

- initial/final 6x5 grid;
- cascade-step removal, drop, refill, and win amounts;
- golden-square before/after and event overlays;
- rainbow symbol activation events;
- bronze/silver/gold coin reveal events;
- pot/clover special reveal candidate events;
- feature-mode intro/active/outro state;
- bonus-buy selected mode and purchased feature start;
- max-win cap reached event;
- winRatio/winTier for win presentation.

## Settings Not Payout Math

Super Turbo, Turbo, Sound, Music, Home/Lobby, and Autoplay are client/runtime settings. They must not change outcome math. Autoplay stop conditions remain blocked pending donor/source evidence.

## Scene-Map Impact

Existing scene maps provide base scaffolding, but ArtSceneMapper should update explicit object/state coverage for v0.3 animation events before GameClientBuilder.
