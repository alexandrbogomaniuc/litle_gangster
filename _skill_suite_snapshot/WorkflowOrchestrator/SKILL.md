---
name: WorkflowOrchestrator
description: >
  Decide the next safe iGaming workflow skill from manifest, handoffs, blockers, and gates; refuse
  unsafe implementation jumps and produce the exact next prompt.
---

# WorkflowOrchestrator

## Purpose

WorkflowOrchestrator is the routing and gatekeeping skill. It does not implement game code, generate
registration, call wallets, browse donor URLs, capture assets, or approve release. It reads the current
project state and produces one safe next step.

## Required Inputs

- Project root.
- Skill suite root.
- Current user request.
- `project_manifest.json`.
- All available `00_skill_reports/*/handoff.json`.
- Current blockers and latest sprint report, if present.

## Required Reads

1. Nearest `AGENTS.md`.
2. Project `project_manifest.json`.
3. Project `assumptions.md` and `decisions_log.md`.
4. All `00_skill_reports/*/handoff.json` files.
5. `references/WORKFLOW_GATES.md` when gate interpretation is needed.

## Hard Rules

- Planning allowed is not implementation allowed.
- Never infer approval from completed planning reports.
- Use fast-lane mode for routing and optimization work: one primary purpose, compact reports by default, and
no broad history re-read unless required.
- Prefer `handoff.json`, `project_manifest.json`, and consolidation gate docs as source of truth for fast-lane
decisions.
- Checkpoint git review/push is recommended every 3-4 meaningful local sprints or at a major phase boundary,
but never push automatically.
- Subagents are optional. Use them only when the main agent decides they clearly reduce time or improve
reliability, and never for writing files or source changes.
- Never recommend GameClientBuilder implementation unless runtime owner, result API contract, approved asset
strategy, and explicit client-code approval are all true.
- Never recommend GameServerRegistrar generation unless registration lane, game ID, bank/source,
serializer/workaround, and rollback strategy are proven.
- Never recommend WalletAndLaunchTester execution unless safe test environment and secret references are
available. WalletAndLaunchTester planning/checklist audits may be routed earlier only when they explicitly
forbid endpoint calls, server starts, DB/Cassandra work, client generation, registration generation, and
release approval.
- Never recommend RTPAndReleaseAuditor release approval unless all prior gates pass.
- Never recommend WalletAndLaunchTester or GameServerRegistrar generation when GS,
  wallet, runtime, storage, and client responsibilities are unresolved. Route to
  ProtocolAndSchemaMapper for a responsibility boundary audit first when wallet
  ownership, session/history ownership, pending/stuck transaction ownership, or
  registration wallet/config ownership is unclear.
- Never recommend GameServerRegistrar generation until a registration/config dependency
  resolution step exists. Route to GameServerRegistrar planning when dependencies for
  identity, math/RTP, bet/GL, cap/max-win, features, VABS/history, wallet/bank,
  round/state, QA, or release are unresolved.
- Never recommend GameServerRegistrar generation until current-GS registration field
  schema proof exists. Route to a read-only schema proof audit when proposed fields are
  not mapped to proven current-GS field names, aliases, serializer columns, and
  template/bank/game inheritance paths.
- Never recommend GameServerRegistrar generation when schema proof leaves exact fields
  missing or unproven. Route to a registration field-mapping decision sprint first; it
  must classify each unresolved field as existing, custom-serialized candidate,
  runtime-only, source-patch-required, admin-confirmation-required, or blocked by
  runtime/math/product/BO-CM/wallet evidence.
- Never recommend GameServerRegistrar generation when field-mapping still depends on
  admin/source confirmation. Route to a registration-admin/source confirmation sprint
  first so future games capture exact questions, expected answer schema, and proof
  requirements for custom serialized parameters, candidate fields, VABS/VIEWSESSID,
  wallet/bank values, refund/rollback, round-state helpers, and language settings.
- Never recommend registration generation, GameClientBuilder implementation,
  WalletAndLaunchTester endpoint execution, or release audit from stale launch route
  assumptions. Route to a current launch/config route freshness audit when prompts or
  docs rely on old route names, old URLs, legacy examples, or unproven bootstrap paths.
- Never treat user memory, local launch examples, older game behavior, legacy URLs, or
  old docs as production truth. Route to a user-hypothesis-to-current-source proof
  audit when a workflow depends on user-provided registration, launch, wallet, GL,
  VABS, language, or runtime answers that have not been proven in current source/config.
- When repeated audits reach source-owner gates, stop broad discovery. Create a
  consolidated owner-confirmation package with exact questions, candidate answers,
  owners, expected answer formats, and next actions, then continue only with
  answer-ingestion, explicitly approved narrow patch apply, or safe parallel work.
- Never recommend registration generation until registration-relevant settings have a
  proven storage path: BO/admin entry point, validation/controller/service layer,
  DAO/persister/cache layer, Cassandra or approved storage location, runtime cache read,
  and runtime consumer. Do not assume BO users write directly to Cassandra. If storage,
  validation, cache refresh, or runtime read ownership is unproven, route to a read-only
  settings storage path audit or patch-planning sprint first.
- After the responsibility boundary is corrected, route to WalletAndLaunchTester
  planning/checklist audit before real endpoint tests, GameClientBuilder implementation,
  GameServerRegistrar generation, wallet certification, or release audit. Real endpoint
  execution remains blocked until explicit approval and safe environment evidence exist.
- Route to MathProfileCalibrator when a 3x3 math profile matrix exists but
  train/validation gates are not passed, or when requested RTP/volatility
  profiles need calibration.
- Route to ParallelMathValidator when large train/validation/tail simulation is
  needed, bonus-buy EV needs a parallel lane, FRB/promo EV needs validation,
  registration math fields need extracted simulation evidence, certification
  evidence is needed, or the main workflow should continue while math validation
  runs in parallel.
- If the requested next skill is unsafe, refuse the jump and produce the nearest safe prompt.
- Public export validation may be called passed only after local validation, commit, push, and fresh post-push
clone validation.

## Workflow

1. Run or inspect `scripts/decide_next_skill.py` with the project root.
2. If the user requested a specific skill, run `scripts/validate_next_skill_allowed.py --skill <SkillName>`.
3. Prefer ParallelMathValidator over implementation or registration work when
   unresolved large-scale math evidence, bonus-buy EV, FRB/promo liability,
   tail/max-win, registration math fields, or certification evidence blocks a
   downstream gate.
4. Prefer MathProfileCalibrator over backend/client/registration work when
   profile calibration gates are open.
5. Prefer ProtocolAndSchemaMapper responsibility-boundary audit before
   WalletAndLaunchTester when prompts imply that the browser/client or game runtime
   owns real wallet state without current GS proof.
6. Prefer WalletAndLaunchTester planning/checklist audit when the boundary is corrected
   but launch/session, wallet/accounting, VABS/history, BO/CM, pending/stuck,
   close/reconnect/FRB, or registration dependency tests are not yet planned.
7. Prefer GameServerRegistrar registration/config dependency resolution planning after
   wallet/launch/history planning is complete and before any generation, DB/Cassandra,
   or registration artifact work.
8. Prefer GameServerRegistrar current-GS schema proof after dependency resolution when
   exact fields such as BF_RTP/BF_BETS, SD_KEYS, CAP/MAX_WIN, VABS/history URLs,
   wallet/bank config, or round-state settings remain candidate or unproven.
9. Prefer GameServerRegistrar field-mapping decision after schema proof when some fields
   are not exact current-GS fields. This is still planning only and must not generate CQL
   or registration artifacts.
10. Prefer GameServerRegistrar registration-admin/source confirmation after field-mapping
    when custom serialized parameters, candidate GS fields, admin-only values, or
    unproven route/config semantics remain. Generic property storage is not sufficient
    evidence for generation.
11. Prefer GameServerRegistrar current launch/config route freshness audit before
    admin-answer ingestion, registration draft work, client bootstrap work, or
    wallet/launch endpoint tests when route freshness is questioned or historical route
    names appear in prompts.
12. Prefer GameServerRegistrar user-hypothesis source-proof audit before accepting
    admin/source answers when user-provided answers could be stale, remembered,
    local-only, or contradicted by current source.
13. Prefer GameServerRegistrar settings storage path audit before registration draft
    work when BO/admin-configurable values, Cassandra/table ownership, cache refresh,
    runtime-read ownership, or max-bet/exposure validation is unproven.
14. Prefer VisualPrototypeSandboxBuilder when the user asks to see/test visuals before
    production client work, use donor/reference assets as placeholders, create a local
    visual prototype, or update a non-production visual sandbox while GameClientBuilder
    implementation, registration generation, wallet endpoints, and release remain
    blocked.
15. Do not route to VisualPrototypeSandboxBuilder when the request asks for production
    client code, GameClientBuilder implementation, registration generation, wallet/GS/
    BO/CM endpoint calls, release approval, certification approval, or public export of
    donor/reference sandbox assets.
16. Report the allowed next skill, blocked unsafe skills, and exact next Codex prompt.
17. Update project reports only when the sprint asks for it.

## Output Shape

Produce:

- `next_allowed_skill`
- `planning_allowed`
- `implementation_allowed`
- `blocked_skills`
- `blocking_gates`
- `exact_next_prompt`

Keep the output short and decision-focused.

## Fast-Lane References

- `references/FAST_LANE_RULES.md`
- `references/SUBAGENT_USAGE_POLICY.md`

## ExtGame Protocol Conformance Routing

When a protocol PDF or protocol summary introduces fields that registration, client bootstrap, wallet tests,
or release would depend on, route to GameServerRegistrar ExtGame protocol conformance audit before generation
or implementation. Current GS source wins; protocol-only fields are blockers until source/admin proof or patch
planning exists.

## ExtGame Source Patch-Gap Planning Gate

If current GS source does not prove ExtGame protocol support, route to a patch-gap planning sprint before
source patching, registration generation, GameClientBuilder, WalletAndLaunchTester endpoint tests, or release
audit. Current source wins over old docs and old games; protocol-only findings become conformance gaps until
patched or confirmed.

## ExtGame PDF/Current Source Truth Routing

When a user supplies a current protocol PDF, route through a PDF-vs-current-source
resolution sprint before accepting admin answers, approving patches, generating
registration, building client bootstrap, running wallet endpoint tests, or release
audit. Treat user ideas as product direction, not technical truth. If the PDF is
missing, request it instead of continuing from memory.

## BO Max Bet / Exposure Dependency Routing

When GL min/default/max bet, target max exposure, `MAX_WIN`, `CAP_WIN_MULTIPLIER`, baseBetCredits, or
bonus-buy cap denominator are unresolved, route to GameServerRegistrar for a BO max-bet/exposure dependency
audit before registration generation, wallet endpoint tests, release audit, or certification. Require proof
that `maxWinMultiplier` is math-profile-locked, max bet/exposure formulas are enforced, derived max bet rounds
down, exposure is currency-aware, and registration is blocked if BO-configurable values can violate
cap/exposure.

## Currency Exposure Policy Routing

When a prompt assumes base-currency exposure conversion, exchange-rate behavior, or non-EUR max-bet
derivation, route to GameServerRegistrar for a currency exposure proof audit before patching, registration
generation, wallet endpoint tests, or release audit. Require current-source proof of base currency, rate
direction, scheduler/update cadence, stale-rate behavior, rounding, and audit/snapshot retention. If any proof
is missing, prefer explicit per-currency exposure values or keep the workflow blocked.

## Game Client Requirements Integration Routing

Before GameClientBuilder implementation, route to a Game Client Requirements integration
planning sprint when the current project has not classified the latest client
requirements by customer config, bank properties, certification/regulation, feature
scope, PostMessage, history/VABS, wallet/error messages, rules/paytable/RTP/max-win,
currency display, home/cashier, FRB/restart, out-of-scope, and blocked items. Keep
GameClientBuilder implementation blocked if registration/runtime/wallet/history values,
approved assets, bootstrap config ownership, or customer/bank config values are
unresolved.

Treat reference archives such as Baron Oil as workflow lessons only unless current GS
source and project evidence prove they are registerable packages for the target game.

## Source-Owner Consolidation Routing

When decision sprints and source-proof audits have reduced the remaining work to
owner confirmations, do not reopen broad GS/client/registration discovery unless new
evidence appears. Route to a WorkflowOrchestrator consolidated confirmation package
that groups blockers by owner and records the exact question, current candidate
answer, why it matters, expected answer format, next action if confirmed, and next
action if rejected or unclear.

After this package exists, route future work to one of three lanes only:
owner-answer ingestion, explicitly approved narrow patch apply, or safe parallel
work that cannot generate registration, call endpoints, modify DB/Cassandra, build
production client code, or approve release.

## Original Art Production Planning Routing

When technical gates are parked at source-owner, registration, runtime, wallet, or
release blockers, future games may continue with original art production planning only.
Route to an art/design planning sprint when the project needs character briefs, symbol
briefs, background briefs, animation/VFX shot lists, sound/music cue lists, UI visual
component specs, paytable/rules outlines, VABS/replay art specs, export checklists,
safe prompt packs, or asset approval matrices.

Donor assets are never production assets. Prompt packs must avoid copyrighted
characters, real people, donor names, donor URLs, private links, and direct recreation
of existing slot screens. Art planning must not generate production client code,
import production assets, capture donor assets, generate registration, call endpoints,
touch DB/Cassandra, approve release, or claim certification.

## Wireframe / Storyboard Planning Routing

Future games should create non-production wireframes and storyboards before
GameClientBuilder implementation. Route to safe wireframe/storyboard planning when the
project needs screen maps, desktop/mobile layout plans, base-game flow, cascade/win
flow, feature triggers, bonus-buy flow, big-win/max-win presentation, history/VABS
presentation, paytable/rules structure, settings/autoplay/turbo behavior,
wallet/error-message states, or PostMessage/client-event planning.

Wireframes and storyboards are planning artifacts, not production client code. Donor
assets must not be copied. Math/registration values that are not final must remain
placeholders. VABS/history storyboards must exist before History button implementation,
and wallet/error-message storyboards must exist before wallet endpoint tests. Client
implementation remains blocked until technical gates and asset approvals are cleared.

## Clickable Prototype Specification Routing

Future games should create a non-executable clickable-prototype specification before
GameClientBuilder implementation. Route to this planning lane when a project needs
screen-state maps, interaction flows, button behavior, transitions, disabled states,
placeholder-data policy, wallet/error paths, History/VABS interactions, PostMessage
interactions, or mobile/touch behavior.

Clickable-prototype specs are planning artifacts, not executable prototype code. Do not
generate HTML, JS, CSS, runtime files, production client code, production assets,
registration artifacts, endpoint calls, DB/Cassandra actions, release approval, or
certification during this lane. Prototype docs must use placeholders for unresolved
math/registration values, and GameClientBuilder implementation remains blocked until
technical gates and asset approvals are cleared.

## Clickable Prototype Review Script Routing

Future games should create prototype review scripts before GameClientBuilder
implementation. Route to this planning lane when product, QA, design, or future
GameClientBuilder agents need a consistent non-executable review script for base game,
bet panel, spin/cascade, win presentation, feature flows, big-win/max-win,
History/VABS, paytable/rules, settings/autoplay/turbo, wallet/error messages,
PostMessage, mobile/touch, accessibility/readability, placeholder data, or blocked
states.

Review scripts are planning/QA artifacts, not production code. They must include
placeholder checks for unresolved math/registration values and explicit blocked-state
checks. Prototype approval does not unlock GameClientBuilder implementation unless
technical gates and asset approvals are cleared. Wallet/error review scripts do not
replace wallet endpoint tests, and History/VABS review scripts do not replace BO/CM
acceptance tests.

## Donor Placeholder / Symbol Weight Mapping Routing

Future games may inventory donor/reference assets as internal placeholders only when
they are already present in the private project tree or explicitly supplied. Do not
browse donor URLs, capture donor assets, persist raw private URLs/tokens/SIDs/signatures,
or treat donor assets/scripts as production material unless rights and approval are
explicit.

Route to this planning lane when a project needs a donor-placeholder quarantine policy,
placeholder asset inventory, placeholder-to-final replacement plan, symbol/art/math
mapping, or source-proof audit for reels/elements/symbol weights. Symbol weights,
reels, strips, grid generators, cascade refill weights, feature weights, and bonus-buy
start-state weights must come from authoritative math/config, not visuals. Missing or
provisional weights block registration/release, not art planning. Placeholder asset
binding does not unlock GameClientBuilder implementation.

## Mechanic Source-Proof Routing

When mechanics, wild behavior, scatter or feature triggers, cascade/refill rules,
paytable behavior, feature odds, bonus-buy start states, or VABS replay implications are
unresolved, route to MathModelDesigner for a mechanic source-proof sprint before
GameClientBuilder implementation.

Future games must create mechanic-to-animation and mechanic-to-VABS mappings before
client implementation or VABS release acceptance. Do not treat donor visuals, symbol art,
or product intuition as proof of mechanic odds or symbol math.

## Mechanic Acceptance Routing

When source proof identifies blocked mechanics, route to mechanic acceptance and
placeholder policy planning before any prototype/client implementation work. The policy
must decide source-proven status, prototype display status, final-client readiness,
placeholder allowance, disabled-state requirements, and registration/release blockers
for each known mechanic.

Placeholder mechanics do not unblock registration generation, wallet endpoint tests,
GameClientBuilder implementation, release, or certification.

## Non-Production Visual Sandbox Routing

Future games may create a local non-production visual sandbox before GameClientBuilder
implementation when owners need a quick visual review surface. The sandbox must live
outside Staging source, production client folders, public export folders, and
`Gamesv1/games/<gameId>`.

Visual sandboxes are not production client code. They must not call GS, wallet, DB,
BO/CM, VABS, loopback APIs, or external endpoints. Donor/reference assets and scripts
may be used only as quarantined placeholders with replacement-required status. Scripted
visual outcomes are not math, RTP, wallet, registration, release, or certification
evidence.

Future games may visually imitate a donor/reference game inside a quarantined
non-production sandbox for internal review only. Final art must be replaced or
explicitly approved. Donor/reference scripts or animation descriptors may be reviewed
for broad visual timing only; production logic must be rewritten or approved. Donor
mechanic visuals do not define math behavior, and sandbox approval does not unlock
GameClientBuilder production implementation, registration, wallet tests, release, or
certification.

Route this lane to `VisualPrototypeSandboxBuilder`. The skill is the reusable owner for
creating/updating sandbox manifests, placeholder bindings, scripted visual outcomes,
screen-state files, static offline sandbox files when safe, smoke tests, and non-release
gates. It is explicitly not a GameClientBuilder implementation route.
