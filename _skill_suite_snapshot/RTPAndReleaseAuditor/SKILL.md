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
  context for certification, VABS/VBA/history, process-transaction-equivalent behavior, restart/resume, FRB/OCB/promos, error/translations, and client
  performance/memory.
5. Audit ParallelMathValidator evidence when present: train/validation
   separation, no validation-seed tuning, tail/max-win confidence, bonus-buy
   EV, FRB/promo liability, registration math field extraction, and
   certification package status.
6. Mark status: APPROVED, APPROVED_WITH_MINOR_RISKS, or BLOCKED.

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
