# Little Gangster Pilot Pipeline Lessons

Generated: 2026-05-11 12:32:07 

## Purpose

This report captures reusable pipeline lessons from the Little Gangster pilot. It is a process-hardening artifact only. It does not approve math, assets, client build, registration, wallet tests, or release.

## Summary

The pilot proved that donor-based iGaming work needs stricter early evidence gates. The fastest future path is not to skip research, but to ask sharper intake questions, prove donor feature/settings parity before math selection, inventory
authorized scaffold assets before art direction, prove the current GS lane/registration/RNG ownership before implementation assumptions, and run a contract consistency audit before GameClientBuilder.

## Lessons Captured

1. ProjectCreator should ask for donor authorization mode, exact feature/settings parity requirement, scaffold capture mode, target game ID, RTPs, volatility, known layout, current GS source roots, candidate lane roots, secret references,
and public export needs.
2. Donor URLs must remain in memory only. Persist only redacted placeholders and secret references. Fresh token handling and safe demo/test confirmation must be explicit every donor sprint.
3. Donor feature/settings parity must run before selected math model finalization. Every donor setting/feature must be matched, blocked, or explicitly rejected by the user.
4. Reference asset workflow must distinguish observation-only, authorized scaffold capture, and licensed release reuse. Scaffold assets stay quarantined, inventoried, replacement-required, and blocked from release.
5. MathModelDesigner must create a layout alignment report before model generation. Layout mismatch caused avoidable rework in this pilot.
6. Math simulators must be audited for payout scaling, post-normalization, and forced RTP before their results are trusted.
7. Prior-agent runtime directions are candidate evidence only. Current GS source/config must prove lane, registration process, math import boundary, and RNG/result owner.
8. External collaboration notes such as Mantis/ExtGame must remain advisory checklists unless current GS source proves that lane.
9. A current-GS registration/RNG/math ownership audit should occur before GameClientBuilder and GameServerRegistrar.
10. Complex donor parity needs a rich result contract before builder work: cascade, golden-square, rainbow, coin reveals, feature modes, max-win cap, winRatio/winTier, round completion, state persistence, registration metadata boundary, and
runtime handoff.
11. ArtSceneMapper must update scene maps whenever the math/result schema changes.
12. A Math/Art/Runtime Contract Consistency Audit must run before GameClientBuilder planning. Unresolved field mismatches must be zero or explicitly blocked.
13. Sanitized public/private export is valuable after major sprints, but it needs strict sanitizer rules and current README/reviewer guidance.
14. SprintReporter must run after every sprint and include files changed, validations, blockers, trust level, and exact next prompt.

## Approval Status

No approval gates changed. GameClientBuilder remains planning-only until runtime/result API contract review. Release remains blocked.
