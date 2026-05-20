---
name: RTPAndReleaseAuditor
description: >
  Audit all prior project reports and release gates, marking release approved, approved with minor
  risks, or blocked.
---

# RTPAndReleaseAuditor

## Purpose
Run strict final audit before release.

## When To Use
Use after client, registration, wallet/launch, math, and asset gates are complete.

## Required Inputs
Manifest, all skill reports, asset manifest, RTP reports, wallet/launch reports, registration/rollback
artifacts, client build outputs.

## Preconditions
Read all prior handoffs and `SPRINT_REPORTING_STANDARD.md`.

If ParallelMathValidator outputs exist, read them and include their gate states
in the release audit. Release remains blocked if large-scale validation,
bonus-buy EV, FRB/promo liability, registration math field extraction, or
tail/max-win evidence is missing or marked non-final when the game scope
requires it.

## Forbidden Actions
No code creation, DB changes, or approving unresolved blockers.

## Workflow
1. Inspect all prior reports.
2. Validate manifest, authorization, assets, math/RTP, protocol, wallet/launch tests, client build,
registration, rollback, Game Client Requirements, secrets, DB apply mode.
3. Produce final checklist, risk register, release readiness report, signoff.
4. Audit Mantis-derived current-GS checklist gates where applicable: local test environment, bot/long-run
tests, production RNG owner, source/build context for certification, VABS/VBA/history,
process-transaction-equivalent behavior, restart/resume, FRB/OCB/promos, error/translations, and client
performance/memory.
5. Audit ParallelMathValidator evidence when present: train/validation
   separation, no validation-seed tuning, tail/max-win confidence, bonus-buy
   EV, FRB/promo liability, registration math field extraction, and
   certification package status.
6. Audit GS/wallet/runtime responsibility evidence. Release remains blocked if the
   browser/client or runtime is treated as real wallet owner without current GS proof,
   if pending/stuck transaction ownership is unresolved, or if wallet/config ownership
   is unknown before wallet/launch tests and registration generation.
7. Audit wallet/launch/history planning and execution evidence. Release remains blocked
   if launch/session, wallet/accounting boundary, canonical VABS routes, legacy alias
   routes when enabled, BO/CM acceptance, pending/stuck/retry/close/reconnect/FRB
   transitions, or registration/config dependencies are missing, untested, or only
   planned without accepted blockers.
8. Audit registration/config dependency resolution. Release remains blocked if
   GameServerRegistrar generation happened without a field dependency matrix, if
   `POSSIBLE_MODELS`/`BF_RTP`, `SD_KEYS`, `CAP_WIN_MULTIPLIER`/`MAX_WIN`,
   VABS/history, wallet/bank, round/state, LQA/licensee, wallet/launch/history, BO/CM,
   certification, or release fields are unresolved, or if production registration was
   generated from candidate-only values.
9. Audit current-GS schema proof before release. Release remains blocked if registration
   fields were generated from runtime payload concepts without proven current-GS field
   names, aliases, serializer columns, and template/bank/game inheritance paths.
10. Audit registration field-mapping decisions before release. Release remains blocked
    when exact fields are missing and no explicit decision exists, or when custom
    serialized parameters / custom serialized parameters lack registration-admin/source confirmation, runtime tests,
    math certification, BO/CM acceptance, wallet/bank values, or product approval.
11. Audit registration-admin/source confirmation before release. Release remains blocked
    when admin/source owner answers are missing for custom BF fields, POSSIBLE_MODELS
    and BF_RTP policy, SD_KEYS, FeatureKPI, CAP/MAX_WIN, GL/baseBetCredits,
    VABS/VIEWSESSID and New Games routes, wallet/bank values, refund/rollback,
    roundFinishedHelper/endRoundSignature, FRB/OCB/cash bonus flags, or supported
    languages. Generic property-map storage is not enough to prove production
    registration semantics.
12. Audit current launch/config route freshness before release. Release remains blocked
    when launch, guest/free/real mode, client bootstrap, VABS/history, or BO/CM route
    names are copied from old docs or older games without current source/config proof.
    Stale route assumptions are release blockers, and the current launch route freshness
    gate must pass before release can be considered.
13. Audit user-hypothesis source proof before release. Release remains blocked if
    registration, launch, GL, wallet/bank, VABS, language, or runtime fields were
    accepted from user memory, local examples, old docs, or older games without current
    GS source/config or admin/source-owner confirmation.
14. Audit settings storage path proof before release. Release remains blocked if
    registration-relevant or BO-editable settings lack proven persistence, validation,
    cache-read, runtime-consumer, and client/server boundary evidence. BO users must not
    be assumed to write directly to Cassandra; manual/direct Cassandra edits are unsafe
    unless explicitly approved as a maintenance procedure. BO-editable values must have
    validators before release.
15. Mark status: APPROVED, APPROVED_WITH_MINOR_RISKS, or BLOCKED.

## Output Files
`09_release/final_checklist.md`, `risk_register.md`, `release_readiness_report.md`, `signoff.md`, reports.

## Validation Checklist
No release-blocking unknowns; all tests passed or risks accepted by evidence. Current-GS lane is proven, and
Mantis-derived checklist gates are either satisfied or explicitly accepted with evidence.

## Handoff To Next Skill
Next: SprintReporter.

## Failure / Blocker Handling
Any unresolved release blocker yields BLOCKED.

## SprintReporter Handoff
Report final status, blockers, risks, and exact evidence.

## Pilot Pipeline Hardening Addendum

Final release gates must require current GS lane proven, runtime owner proven, registration and rollback
validated, math multi-seed validation complete, original assets approved, wallet/launch tests complete,
VABS/history covered where required, contract consistency with zero unresolved mismatches, and public/private
export leak validation if used.

Release audit must also require a GS/wallet responsibility boundary when real-money
flows are in scope: wallet/provider settlement owner, GS session/history owner,
pending/stuck transaction owner, and registration wallet/config owner must be proven or
explicitly blocked before release can be considered.

## Visual History Release Gate

Future games are release-blocked unless VABS/VBA/Lasthands visual history is implemented
and tested, or explicitly blocked/accepted with current GS and product evidence. The
audit must distinguish stored JSON replay evidence from visual HTML/render route
evidence, and must check round replay, session replay, whole-session replay, in-game
History button behavior, Casino Manager/backoffice access, deterministic replay fields,
and wallet/accounting references.

Release audit must also check that a VABS/VBA/Lasthands route-resolution decision exists.
If the project has only JSON history evidence and no visual route implementation or
accepted blocker, release remains blocked.
When enabled by route-resolution planning, legacy alias routes must have explicit test
or acceptance evidence; canonical routes alone do not prove BO/CM compatibility.

Release audit must verify the selected VABS evidence policy: deterministic replay is
authoritative, visual route is present or explicitly accepted as blocked, screenshot and
video capture are optional policy-controlled modes, and storage/retention/security gates
pass before any media evidence is relied on.

## ExtGame Protocol Release Gate

Release remains blocked while ExtGame protocol conformance gaps are unresolved. Audit must verify
BF/POSSIBLE_MODELS/SD_KEYS/FeatureKPI, cap/max-win, buy-feature accounting, FRB/restart, VABS/VBA, bootstrap
URL, language, state persistence, and round-finished evidence against current GS source, admin proof, tests,
or accepted blockers.

## ExtGame Patch-Gap Release Gate

Release and certification remain blocked while ExtGame conformance gaps are only planned. BF fields, SD_KEYS,
POSSIBLE_MODELS validation, cap/max-win enforcement, VABS/history, wallet/accounting, bootstrap, state
persistence, and round-finished items must be patched or explicitly resolved and tested before release
consideration.

## ExtGame PDF/Current Source Release Truth

Release audit must verify that the latest protocol PDF/current protocol document was
compared against current GS source and that every protocol-required field or behavior is
source-proven, patched, tested, or explicitly blocked. User product direction, legacy
routes, old Mantis examples, and older games are not release evidence. Certification and
release remain false while PDF/source gaps, admin confirmations, wallet tests,
VABS/VBA evidence, or registration generation gates are unresolved.

## BO Exposure Release Gate

Release remains blocked if GL max bet and target exposure can be edited independently or hardcoded without
validation. Audit must verify `maxWinMultiplier` comes from approved math profile evidence, `GL_MAX_BET` is
constrained by `targetMaxExposure / maxWinMultiplier`, derived max bet rounds down to the nearest allowed bet,
bonus-buy cap denominator is base bet, exposure validation is currency-aware, and registration generation was
blocked until these dependencies were proven or patched.

## Currency Exposure Release Gate

Release remains blocked unless currency exposure policy is proven for every enabled
currency. If base-currency exposure conversion is used, audit must verify source evidence
for base currency, rate direction, update cadence, stale-rate blocking, rounding down to
the nearest allowed bet, and audit/snapshot retention. If conversion proof is incomplete,
release must require explicit per-currency exposure values or remain blocked.

## Game Client Requirements Release Gate

Release remains blocked unless Game Client Requirements integration planning exists and
all applicable client requirements are implemented, tested, or explicitly marked
non-applicable with evidence. Audit customer config, bank properties,
certification/regulation behavior, game features, PostMessage, history/VABS,
wallet/error messages, rules/paytable/RTP/max-win display, currency display,
home/cashier, and FRB/restart behavior. Candidate math or registration values must not
appear as final client display values. Reference archives such as Baron Oil are workflow
lessons only unless separately proven as current registerable source for the target game.

## Donor Placeholder / Symbol Weight Release Gate

Release remains blocked while donor/reference assets are used as placeholders without
explicit rights and release approval. Donor assets must be quarantined, marked
non-production, blocked from release, and replacement-required until approved.

Release audit must verify that symbol weights, reels/elements, grid generation,
cascade refill behavior, free-spin/feature weights, bonus-buy start-state behavior, and
profile-specific overlays come from authoritative math/config, not donor visuals or
screenshots. Missing or provisional symbol weights, unapproved production assets, or
placeholder-only bindings block release and certification.

## Mechanic Source-Proof Release Gate

Release remains blocked unless mechanic behavior is proven from authoritative source or
simulation evidence. Audit wild behavior, scatter/feature triggers, cascade/refill,
paytable payouts, feature odds, bonus-buy start states, cap behavior, and
profile-specific overlays before certification claims.

Mechanic-to-animation mapping does not approve release by itself. Mechanic-to-VABS
mapping must exist before VABS/history acceptance, and wallet/error reviews do not
replace wallet endpoint tests.

## Mechanic Acceptance Release Boundary

Release audit must reject paytable/rules or client displays that claim unproven mechanics
as final gameplay. Placeholder-only mechanics, disabled-state mechanics, provisional
feature odds, unresolved BF_BETS, unresolved MAX_WIN, or uncertified paytable/profile
values keep release and certification blocked.

## Visual Sandbox Release Boundary

VisualPrototypeSandboxBuilder output is not release evidence by itself. Donor/reference
sandbox assets, sandbox scripts, scripted visual outcomes, static sandbox files, smoke
checklists, and owner visual approval are never release evidence unless the assets are
separately replaced or rights-approved and the production client, registration, wallet,
VABS/BO-CM, math/certification, public-export, and release gates all pass.
