# Next Project Fast Start Prompt

Use the reusable skill suite for a new donor-based game project.

Run WorkflowOrchestrator first.

Inputs to provide:

- Project name and target folder.
- Authorized donor/reference mode.
- Whether donor features/settings must match exactly.
- Whether scaffold asset capture is authorized.
- Target game ID.
- Target RTPs and volatility.
- Known layout, if any.
- Current GS source root and known runtime lane, if available.
- Registration source/template root, if available.
- Secret references only, never raw secrets.
- Whether public export is required for this checkpoint.

WorkflowOrchestrator must:

- Read `project_manifest.json` if present.
- Read all `00_skill_reports/*/handoff.json` files if present.
- Decide the next allowed skill.
- Refuse unsafe jumps.
- Produce one exact next prompt.
- Distinguish planning allowed from implementation allowed.

Do not run implementation skills unless gate validators pass and the user explicitly approves implementation.
