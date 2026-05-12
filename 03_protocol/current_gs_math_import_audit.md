# Current GS Math Import Audit

## Direct Answer

No evidence was found that the math model is imported into GS during game registration. Current registration evidence points to metadata/config/routing records. Executable math should live in the proven server/backend runtime owner once selected.

## Evidence

| Audit item | Result | Status | Evidence |
|---|---|---|---|
| Registration config contains reel strips | Not found. | NOT_FOUND | Inspected registration persisters and cache exports expose template/game/bank properties, not reel strips. |
| Registration config contains cluster paytables | Not found. | NOT_FOUND | Same. |
| Registration config contains feature rules | Not found. | NOT_FOUND | Same. |
| Registration config contains executable math package reference | Not found in current GS registration persisters. | NOT_FOUND | `CassandraBaseGameInfoPersister.java` persists `BaseGameInfo` JSON/bytes; no math package parsing found. |
| Registration config contains RTP/display/config values | Yes. | PROVEN | `BaseGameConstants.java:177-191`, `291-344`; runtime cache exports include `RTP`, `MAX_WIN`, `DEFCOIN`, `ISENABLED`, `CDN_SUPPORT`. |
| New Games runtime references math package version | Bootstrap can expose `mathPackageVersion`, but this is runtime metadata, not Cassandra import. | CANDIDATE | `new-games-server/src/index.ts:1590-1647`; `schemas.ts:226-231`. |
| New Games backend consumes math_package.json | Not proven. | BLOCKED | No Little Gangster runtime package exists; sample server has hardcoded/provisional outcome logic. |

## Where Would `math_package.json` Be Consumed?

Likely candidates:

1. New Games backend runtime package.
2. Game-specific server package.
3. Classic GS game processor/class if that lane is selected.
4. Build-time generation of runtime config, not direct Cassandra registration.

Evidence is not yet sufficient to select one.

## What Later Skills Must Do

GameClientBuilder:

- Consume only the result schema and animation state contract needed for rendering.
- Never generate production outcomes in the browser.
- Treat `mathPackageVersion` as display/runtime contract metadata.

GameServerRegistrar:

- Generate registration metadata and routing/config only.
- Keep math package references as metadata unless source proves runtime import.
- Do not put paytables/reels/feature rules into CQL unless current GS schema explicitly requires it.

MathModelDesigner:

- Output a runtime-consumable math contract and simulation package.
- Separately output registration metadata values: RTP display, volatility, max-win/cap, feature flags, bet ranges, model IDs.
