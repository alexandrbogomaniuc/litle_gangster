# Reviewer Start Here

This checkpoint is a public-safe review export. It is intended to show the
current reusable workflow infrastructure and the latest Little Gangster lifecycle
planning state.

It is not a release build, not a production client, not a registration package,
and not a certification claim.

## Recommended Reading Order

1. `10_sprint_reports/sprint_report_latest.md`
2. `project_manifest.json`
3. `GAME_STATUS_CURRENT.md`
4. `09_release/parallel_math_validation_skill_adoption.md`
5. `09_release/future_game_parallel_math_validation_playbook.md`
6. `09_release/parallel_math_validation_gate_matrix.json`
7. `_skill_suite_snapshot/ParallelMathValidator/SKILL.md`
8. `_skill_suite_snapshot/ParallelMathValidator/references/PARALLEL_MATH_VALIDATION_WORKFLOW.md`
9. `_skill_suite_snapshot/ParallelMathValidator/scripts/validate_parallel_math_request.py`
10. `00_skill_reports/ParallelMathValidatorSkillCreation/handoff.json`
11. `03_protocol/8001_lifecycle_wrapper_plan.md`
12. `03_protocol/8001_vabs_visual_history_route_plan.md`
13. `03_protocol/8001_history_payload_schema.json`
14. `09_release/8001_lifecycle_wrapper_implementation_gate.md`

## Review Notes

- ParallelMathValidator is generic and not Little-Gangster-specific.
- Future games may use LOW/MEDIUM/HIGH RTP values inside the approved range,
  with LOW/MEDIUM/HIGH volatility and pretested profiles.
- The current 8001 adapter remains a payload mapper only.
- A lifecycle wrapper is required.
- A VABS visual history route is required.
- GameClientBuilder remains blocked.
- GameServerRegistrar generation remains blocked.
- Release remains blocked.

## Public Safety Notes

The export removes donor assets, screenshots, HAR files, raw logs, private local
paths, full donor URLs, tokenized URLs, secrets, SIDs, signatures, emails, and
passwords. Planning documents are included as public-safe copies.
