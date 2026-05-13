# Crazy Rooster 7001 Template Validity

Status: useful integration reference, not release-ready source of truth for Little Gangster.

## Direct Answers

### Is Crazy Rooster 7001 live/working enough to use as a production template?

NO as a direct production template for Little Gangster.

Evidence:

- The 7001 handoff says the intended GS launch route should redirect to a game-specific 7001 client and warns not to use the general Plinko client as Crazy Rooster truth:
`[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/CRAZY_ROOSTER_7001_FRESH_AGENT_HANDOFF_20260505.md:32-68`, `163-168`.
- The 7001 final status says 7001 proof is pending and Docker was unavailable for proof capture in that environment: `[DEV_ROOT]/_worktrees/7000-release-pack-skeleton-20260322-1858/Gamesv1/games/7001/docs/GS_7001_FINAL_STATUS.md:20-39`.
- 7001 VABS status says some evidence remains legacy 7000 proof and a dedicated 7001 authoritative proof pack is still required: `GS_VABS_LIVE_ARCHETYPE_STATUS.md:1-8`.

Therefore 7001 is not sufficient as release-template truth by itself.

### If not live, what evidence is still useful?

Useful evidence:

- New-games launch/routing pattern from GS to game-specific client.
- Vite/Pixi v8/package dependency shape.
- `slot-browser-v1` runtime client pattern.
- `GS_HTTP_RUNTIME` transport usage and operation sequencing.
- Math package folder shape and manifest reference pattern.
- Game settings structure and runtime target.
- History/replay/VABS integration concepts.

Evidence:

- 7001 package dependencies: `Gamesv1/games/7001/package.json:16-27`.
- 7001 runtime client: `GsRuntimeClient.ts:1-23`, `96-130`, `173-237`, `265-392`.
- 7001 `game.settings.json` has `runtimeTarget: slot-browser-v1` and `mathManifestPath`: `game.settings.json:70-80`.
- 7001 runbook defines new-games API/client containers and `/slot/v1/*` flow: `GS_7001_NEWGAMES_RUNBOOK.md:10-18`, `59-66`.

### What evidence is missing?

Missing or blocked:

- Actual `new-games-server` source inspection.
- `@gamesv1/core-protocol` package root inspection.
- Dedicated, current 7001 proof pack confirming full canonical flow for the re-identified 7001 lane.
- 8001-specific registration.
- 8001-specific math package and runtime integration.
- 8001 approved original/licensed asset pack.

### Can it be used as a source of truth for Little Gangster runtime?

Only as a reference pattern, not as source of truth.

Rules:

- Use 7001 to understand the new-games lane and integration seams.
- Do not copy 7001 math, art, asset provider config, game id defaults, or Crazy Rooster-specific settings into 8001.
- Do not treat 7001 proof gaps as Little Gangster proof.

### Should GameClientBuilder copy from 7001, premium-slot, legacy Dragonstone-style docs, or wait?

GameClientBuilder should wait until MathModelDesigner and ArtDirection/asset approval inputs exist. When it does run:

- Use premium-slot as the safer base architecture reference if it is confirmed as the intended template.
- Use 7001 as concrete integration evidence for new-games routing/runtime.
- Use Dragonstone-style docs only for Cassandra/config registration patterns, not as the browser/runtime template.
- Do not blindly copy 7001.

## Validity Table

| Question | Answer | Evidence / reason |
|---|---|---|
| 7001 identity useful? | YES | 7001 docs identify Crazy Rooster and warn against Plinko truth: handoff lines 9-16. |
| 7001 route pattern useful? | YES | handoff lines 32-68; `BaseStartGameAction.java:878-940`. |
| 7001 client stack useful? | YES | `package.json:16-27`; `GsRuntimeClient.ts`. |
| 7001 production-template complete? | NO_BLOCKED | final status lines 20-39 says proof pending. |
| 7001 math reusable for Little Gangster? | NO | different game; MathModelDesigner must produce internal 8001 math. |
| 7001 assets release-approved for Little Gangster? | NO | asset ownership/replacement remains separate; Little Gangster scaffold assets stay blocked. |

## Conclusion

Crazy Rooster is a strong new-games integration reference but not a release-ready template to copy. Little Gangster should use the new-games lane with explicit 8001 math, assets, config, and validation.
