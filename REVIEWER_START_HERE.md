# Reviewer Start Here

This raw-safe checkpoint is intended for external review of real committed files.
Start with these files in order.

1. 10_sprint_reports/sprint_report_latest.md
2. project_manifest.json
3. assumptions.md
4. decisions_log.md
5. 09_release/future_game_rtp_range_rule.md
6. _skill_suite_snapshot/MathProfileCalibrator/SKILL.md
7. _skill_suite_snapshot/MathProfileCalibrator/references/RTP_REQUEST_VALIDATION.md
8. _skill_suite_snapshot/MathProfileCalibrator/references/CALIBRATION_LOOP_POLICY.md
9. _skill_suite_snapshot/MathProfileCalibrator/references/TRAIN_VALIDATION_SEED_POLICY.md
10. _skill_suite_snapshot/MathProfileCalibrator/references/ADJUSTMENT_OVERLAY_POLICY.md
11. _skill_suite_snapshot/MathProfileCalibrator/references/CALIBRATION_REPORT_REQUIREMENTS.md
12. _skill_suite_snapshot/MathProfileCalibrator/scripts/validate_rtp_request.py
13. _skill_suite_snapshot/MathProfileCalibrator/scripts/plan_calibration_loop.py
14. _skill_suite_snapshot/MathProfileCalibrator/scripts/validate_calibration_report.py
15. 00_skill_reports/MathProfileCalibratorSkillCreation/handoff.json
16. 00_skill_reports/MathProfileCalibratorSkillCreation/rtp_range_91_997_update_skill_report.md
17. 00_skill_reports/MathProfileCalibratorSkillCreation/rtp_range_91_997_update_validation_checklist.md
18. 00_skill_reports/MathProfileCalibratorSkillCreation/rtp_range_91_997_update_blockers.md

Review notes:

- The reusable RTP request range is now 91.00% to 99.70%, inclusive.
- LOW, MEDIUM, and HIGH are labels, not fixed reusable values.
- Future-game RTP values must be strictly ascending.
- Operators may choose only approved pretested math profiles.
- Arbitrary runtime RTP entry is not allowed.
- Little Gangster RTP values were not changed.
- Little Gangster remains 92.00%, 94.00%, and 96.00%.
- Bonus-buy EV remains blocked.
- Backend adapter implementation remains blocked.
- GameClientBuilder implementation remains blocked.
- Registration generation remains blocked.
- Wallet work remains blocked.
- DB and Cassandra work remain blocked.
- Release remains blocked.

Unsafe material is intentionally excluded.
Do not treat this repository as a playable game package.
