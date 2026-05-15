---
name: GameClientBuilder
description: Build the game client with verified legacy PIXI/Vue/Webpack/template rules and approved assets only.
---

# GameClientBuilder

## Purpose
Build the client using verified architecture and template rules.

## When To Use
Use after math, art replacement, protocol mapping, and source paths are ready.

## Required Inputs
Client source root, template game path, build command, approved assets manifest, math package, protocol contract.

## Preconditions
Read `CLIENT_BUILD_AND_ARCHITECTURE_SUMMARY.md`, manifest, and approved assets manifest.

## Forbidden Actions
No generic Pixi modernization, Node upgrade, Vite assumption, donor asset release, or DB changes.

## Workflow
1. Verify live source path exists.
2. Use verified stack: PIXI.js Legacy, Vue 2.6, Webpack 4, Babel, Mustache, Node 16.20.2 only if docs/source confirm.
3. Respect JSP/template launch contract and `window.gameConfig`.
4. Build/update client, assets, config, math, protocol adapter, tests, dist.
5. Validate asset references and build outputs.
6. Keep scaffold/unapproved assets out of release dist.

## Output Files
`06_resulting_code/*`, client reports, validation outputs.

## Validation Checklist
Build succeeds, expected outputs exist, no unapproved assets, config references valid.

## Handoff To Next Skill
Next: GameServerRegistrar.

## Failure / Blocker Handling
Missing source roots/templates/build command block build.

## SprintReporter Handoff
Report source paths, build commands, outputs, skipped checks, and blockers.

## Pilot Pipeline Hardening Addendum

Run a planning/runtime API contract review before implementation. Full build is blocked until runtime result owner and result API contract are proven,
contract consistency has zero unresolved mismatches, and approved assets are available. Browser/client authoritative RNG/result generation is
forbidden for production outcomes.

## Visual History Client Gate

Do not treat the in-game History button as complete unless the current project has a
mapped VABS/VBA/Lasthands visual history route or an explicit blocker. Future game
clients must know whether history opens JSON replay, visual HTML/render replay, or a
backoffice-compatible URL. If visual history route behavior is unknown, GameClientBuilder
must keep production client implementation blocked for release scope.

If a route-resolution audit exists, follow its selected model. The History button should
use bootstrap/configured or backend-generated route metadata rather than hardcoded paths,
and must remain blocked if CM/backoffice visual route behavior is unresolved.

Client history UX must respect the selected evidence policy. Deterministic replay and
visual route are required; screenshot/video media, if enabled, are supporting evidence
only and must follow configured storage/retention/security policy.
