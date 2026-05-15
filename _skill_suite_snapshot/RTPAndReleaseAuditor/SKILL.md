---
name: RTPAndReleaseAuditor
description: Audit all prior project reports and release gates, marking release approved, approved with minor risks, or blocked.
---

# RTPAndReleaseAuditor

## Purpose
Run strict final audit before release.

## When To Use
Use after client, registration, wallet/launch, math, and asset gates are complete.

## Required Inputs
Manifest, all skill reports, asset manifest, RTP reports, wallet/launch reports, registration/rollback artifacts, client build outputs.

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
2. Validate manifest, authorization, assets, math/RTP, protocol, wallet/launch tests, client build, registration, rollback, Game Client Requirements,
   secrets, DB apply mode.
3. Produce final checklist, risk register, release readiness report, signoff.
4. Audit Mantis-derived current-GS checklist gates where applicable: local test environment, bot/long-run tests, production RNG owner, source/build
   context for certification, VABS/VBA/history, process-transaction-equivalent behavior, restart/resume, FRB/OCB/promos, error/translations, and
   client performance/memory.
5. Audit ParallelMathValidator evidence when present: train/validation
   separation, no validation-seed tuning, tail/max-win confidence, bonus-buy
   EV, FRB/promo liability, registration math field extraction, and
   certification package status.
6. Audit GS/wallet/runtime responsibility evidence. Release remains blocked if the
   browser/client or runtime is treated as real wallet owner without current GS proof,
   if pending/stuck transaction ownership is unresolved, or if wallet/config ownership
   is unknown before wallet/launch tests and registration generation.
7. Mark status: APPROVED, APPROVED_WITH_MINOR_RISKS, or BLOCKED.

## Output Files
`09_release/final_checklist.md`, `risk_register.md`, `release_readiness_report.md`, `signoff.md`, reports.

## Validation Checklist
No release-blocking unknowns; all tests passed or risks accepted by evidence. Current-GS lane is proven, and Mantis-derived checklist gates are either
satisfied or explicitly accepted with evidence.

## Handoff To Next Skill
Next: SprintReporter.

## Failure / Blocker Handling
Any unresolved release blocker yields BLOCKED.

## SprintReporter Handoff
Report final status, blockers, risks, and exact evidence.

## Pilot Pipeline Hardening Addendum

Final release gates must require current GS lane proven, runtime owner proven, registration and rollback validated, math multi-seed validation
complete, original assets approved, wallet/launch tests complete, VABS/history covered where required, contract consistency with zero unresolved
mismatches, and public/private export leak validation if used.

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

Release audit must verify the selected VABS evidence policy: deterministic replay is
authoritative, visual route is present or explicitly accepted as blocked, screenshot and
video capture are optional policy-controlled modes, and storage/retention/security gates
pass before any media evidence is relied on.
