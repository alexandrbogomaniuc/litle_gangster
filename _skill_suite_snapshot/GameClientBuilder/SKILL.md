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

Run a planning/runtime API contract review before implementation. Full build is blocked until runtime result
owner and result API contract are proven, contract consistency has zero unresolved mismatches, and approved
assets are available. Browser/client authoritative RNG/result generation is forbidden for production outcomes.

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

## Current Launch Route Bootstrap Gate

Future game clients must not hardcode launch route names from old docs, old URLs, or
older game examples. Before implementation, verify the current launch route and
bootstrap field ownership from source/config. The client should consume sanitized
backend/bootstrap route metadata. If `/startgame`, legacy launch aliases, guest/free/real
mode behavior, client/API base URLs, or history route metadata are unproven for the
target project, keep GameClientBuilder implementation blocked.

User-provided launch/bootstrap answers are hypotheses, not implementation approval.
GameClientBuilder must consume current source/config/admin-confirmed route values and
must not hardcode old route names, local examples, private hosts, or numeric game-id
thresholds unless current source proves that exact strategy.

## Game Client Requirements Integration Gate

Future games must run Game Client Requirements integration planning before
GameClientBuilder implementation. Classify each requirement as customer config, bank
property, certification/regulation, game feature, PostMessage/wrapper behavior,
history/VABS, wallet/error-message behavior, rules/paytable/RTP/max-win display,
currency display, home/cashier behavior, FRB/restart, out of scope, or blocked.

The client must not hardcode config-driven behavior. Customer/bank flags, wallet/error
messages, history route metadata, PostMessage behavior, currency display, and
rules/paytable/RTP/max-win display values must come from approved bootstrap/config,
runtime payloads, or registration/math evidence. If registration/runtime/wallet/history
values are unresolved, keep GameClientBuilder implementation blocked.

Reference archives such as Baron Oil may provide workflow lessons only. Do not treat
partial shared code archives as registerable packages, client templates, asset sources,
or proof of GS `BF_BETS`, `MAX_WIN`, wallet, BO/Cassandra, VABS, or release readiness.

## Original Art Package Gate

Before GameClientBuilder implementation, future games should have an original art
production package and asset approval matrix. The package should cover visual identity,
character briefs, symbol briefs, backgrounds, animation/VFX, sound/music, UI/HUD
components, paytable/rules visuals, VABS/replay visuals, export requirements, and safe
prompt packs.

Donor assets are never production assets. Prompt packs must not reference donor game
names, donor URLs, private links, copyrighted characters, real people, or copied slot
screens. Paytable/rules content must remain placeholder-only until final math,
registration, RTP, volatility, BF_BETS, MAX_WIN, and legal/certification values are
approved. GameClientBuilder implementation remains blocked until approved assets and
technical gates are cleared with explicit approval.

## Wireframe / Storyboard Gate

Before GameClientBuilder implementation, future games should have non-production
wireframes and storyboards for the main screen map, desktop layout, mobile layout, base
game, cascades/wins, feature triggers, bonus-buy flow, big-win/max-win presentation,
history/VABS replay, paytable/rules, settings/autoplay/turbo, wallet/error messages,
and PostMessage/client events.

Wireframes/storyboards must not copy donor assets and must not become production
client code. Any unresolved math, registration, RTP, BF_BETS, MAX_WIN, wallet, VABS,
or legal values must remain placeholders. History/VABS and wallet/error flows must be
planned before implementation and endpoint tests.

## Clickable Prototype Specification Gate

Before GameClientBuilder implementation, future games should have a non-executable
clickable-prototype specification. It should cover screen states, clickable/tappable
controls, transitions, disabled states, placeholder data, wallet/error paths,
History/VABS interactions, PostMessage interactions, and mobile/touch behavior.

Clickable-prototype specs must not create executable prototype code, HTML, JS, CSS,
runtime files, production client code, or production assets. Unresolved BF_BETS,
MAX_WIN, BF_RTP, SD key, non-EUR exposure, wallet, VABS, registration, RTP, volatility,
or legal values must remain placeholders until approved. GameClientBuilder
implementation remains blocked until technical gates and asset approvals are cleared.

## Prototype Review Acceptance Gate

Before GameClientBuilder implementation, future games should have prototype review
scripts and an acceptance matrix for the non-production clickable prototype. The matrix
should include scenario owner, prerequisite, user action, expected result,
placeholder policy, whether the scenario blocks implementation, and pass/fail criteria.

Review scripts are planning/QA artifacts, not production code. Placeholder checks and
blocked-state checks are required for unresolved BF_BETS, MAX_WIN, BF_RTP, SD key,
non-EUR exposure, wallet, VABS, registration, RTP, volatility, certification, and
release values. Prototype approval alone must not unlock implementation; technical
gates, wallet/history boundaries, registration readiness, and asset approvals still
need separate clearance.

## Placeholder Asset Binding Gate

Before GameClientBuilder implementation, future games should have a symbol/art/math
mapping and a placeholder asset binding spec. Placeholder bindings may use quarantined
internal reference assets only for non-production planning, and every such binding must
carry non-production, blocked-from-release, and replacement-required status.

Donor/reference assets and donor scripts must not be treated as production assets or
production scripts. Symbol IDs and weight-driven behavior must come from authoritative
math/config, not art names or screenshots. Placeholder asset binding does not unlock
GameClientBuilder implementation until approved production assets and technical gates
are cleared.

## Mechanic-to-Animation Planning Gate

Before GameClientBuilder implementation, future games must have a mechanic-to-animation
mapping based on authoritative math/config. Do not animate unproven wild, scatter,
feature, bonus-buy, max-win, or odds behavior as final client behavior.

Mechanic-to-VABS mapping must exist before History/VABS implementation. Missing or
provisional mechanic proof keeps GameClientBuilder implementation blocked even when
wireframes, prototype specs, review scripts, or placeholder assets exist.

## Mechanic Placeholder Implementation Boundary

Client implementation must not implement unproven mechanics as final gameplay.
Unproven wild behavior, visible scatter-count triggers, retriggers, feature odds,
bonus-buy values, BF_BETS, MAX_WIN, wallet, VABS, and release values must remain
placeholder-only or disabled until their technical gates clear.

Placeholder approval does not unlock GameClientBuilder implementation.

## Non-Production Visual Sandbox Boundary

GameClientBuilder may support planning docs for a local non-production visual sandbox,
but this is not production implementation. Sandbox files must stay outside production
client folders and `Gamesv1/games/<gameId>`. They must not call GS, wallet, DB, BO/CM,
VABS, loopback APIs, or external endpoints.

Use placeholders for unresolved math, registration, wallet, VABS, release, and
certification values. Donor/reference assets or scripts in a sandbox are placeholders
only and do not unlock GameClientBuilder implementation.

VisualPrototypeSandboxBuilder output does not unlock GameClientBuilder production
implementation. GameClientBuilder may read sandbox plans, screen states, placeholder
bindings, and scripted visual outcomes later, but implementation remains blocked until
registration values are resolved, runtime/result API ownership is approved, wallet/
launch/history gates pass, VABS/BO-CM gates pass, production assets are approved, and
release/certification gates are cleared with explicit approval.

Sandbox-only visual effects may use donor/reference assets and animation descriptors as
visual timing references, but they must remain scripted placeholders. Donor scripts must
not become production GameClientBuilder code unless separately approved, and donor
mechanic visuals must not define Little Gangster math, symbol weights, feature odds,
wallet behavior, registration values, release readiness, or certification.
