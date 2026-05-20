---
name: VisualPrototypeSandboxBuilder
description: >
  Create and validate a local non-production visual sandbox for iGaming projects using quarantined
  donor/reference placeholders and scripted visual outcomes while production client, registration,
  wallet, DB, public export, release, and certification gates stay blocked.
---

# VisualPrototypeSandboxBuilder

## Purpose

Build or update a project-local visual sandbox that lets owners review screen layout,
placeholder art, and scripted visual flows before production implementation is allowed.

The sandbox is an internal prototype only. It is not GameClientBuilder implementation,
not release evidence, not math evidence, and not registration readiness evidence.

## Required Inputs

- Project root and game id.
- Current gate state from `project_manifest.json` and handoffs.
- Requested sandbox slug or safe default.
- Existing local donor/reference placeholder inventory, if available.
- Current placeholder and mechanic policies for unresolved math/registration values.

## Required Reads

1. Project `AGENTS.md`.
2. Project `project_manifest.json`.
3. Current `00_skill_reports/*/handoff.json` files.
4. Current visual planning, placeholder policy, and release blocker docs.
5. Reference files in this skill only as needed:
   - `references/non_production_sandbox_policy.md`
   - `references/donor_reference_asset_quarantine.md`
   - `references/sandbox_file_structure.md`
   - `references/scripted_visual_outcomes.md`
   - `references/sandbox_no_endpoint_policy.md`
   - `references/future_game_visual_sandbox_gate.md`

## Hard Boundaries

- Sandbox path must be project-local under
  `11_prototypes/<gameId>_<slug>_visual_sandbox/`.
- Never write to Staging source, production client folders, public export folders, or
  `Gamesv1/games/<gameId>`.
- Do not generate production client code or run GameClientBuilder implementation.
- Do not generate registration artifacts, CQL, DB/Cassandra changes, wallet tests, GS
  calls, BO/CM calls, VABS calls, public export, release approval, or certification.
- Donor/reference assets are placeholders only: non-production, blocked from release,
  replacement-required unless rights and release approval are explicit.
- Donor/reference scripts are visual timing references only. They are not production
  GameClientBuilder logic.
- Scripted outcomes are visual-only and are not math, RTP, feature-odds, wallet,
  registration, release, or certification evidence.

## Workflow

1. Validate the request with `scripts/validate_visual_sandbox_request.py`.
2. Confirm production client, registration, wallet endpoint, public export, release, and
   certification gates remain closed.
3. Create or update the sandbox under `11_prototypes` only.
4. Inventory local donor/reference placeholders if present; do not fetch or persist
   private URLs or secrets.
5. Create/update:
   - `README.md`
   - `PROTOTYPE_STATUS.md`
   - `asset_inventory.json`
   - `placeholder_binding.json`
   - `scripted_outcomes.json`
   - `screen_states.json`
   - optional non-production `index.html`, `prototype.css`, `prototype.js`
6. Add sandbox-only visual effects for scripted flows when safe.
7. Add `SMOKE_TEST_CHECKLIST.md`, `BLOCKERS.md`, and a non-release gate doc.
8. Generate a manifest with `scripts/create_sandbox_manifest.py`.
9. Validate outputs with `scripts/validate_visual_sandbox_outputs.py`.
10. Update handoff with all production gates still false.

## Output Contract

Handoff fields should include:

- `visual_sandbox_bootstrap_completed`
- `sandbox_path`
- `executable_visual_sandbox_created`
- `asset_inventory_created`
- `placeholder_binding_created`
- `scripted_outcomes_created`
- `screen_states_created`
- `donor_assets_used_as_placeholders`
- `donor_assets_used_as_production: false`
- `donor_scripts_used_as_production: false`
- `production_client_code_generated: false`
- `gs_calls_enabled: false`
- `wallet_calls_enabled: false`
- `external_calls_enabled: false`
- `gameclientbuilder_implementation_allowed: false`
- `registration_generation_allowed: false`
- `wallet_endpoint_tests_allowed: false`
- `release_allowed: false`

## Validation Checklist

- Request validator rejects production, endpoint, registration, public export, donor
  production, and release/certification approvals.
- Sandbox files are under `11_prototypes` only.
- Required JSON files parse.
- Asset inventory marks donor/reference items as placeholder and non-production.
- Sandbox contains no GS, wallet, BO/CM, VABS, DB, or external network calls.
- Sandbox contains no raw private URLs, tokenized query strings, SIDs, signatures, or
  secrets.
- GameClientBuilder implementation, registration generation, wallet endpoint tests,
  release, and certification remain false.
