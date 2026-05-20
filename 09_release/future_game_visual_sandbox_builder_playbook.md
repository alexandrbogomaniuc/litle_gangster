# Future Game Visual Sandbox Builder Playbook

Use `VisualPrototypeSandboxBuilder` when a future game needs visual review before
production client work is approved.

Required sequence:

1. Confirm the request is sandbox-only.
2. Confirm GameClientBuilder implementation, registration generation, wallet endpoint
   tests, public donor export, release, and certification remain false.
3. Create the sandbox under `11_prototypes/<gameId>_<slug>_visual_sandbox/`.
4. Inventory donor/reference files only when already locally available or explicitly
   supplied.
5. Mark every donor/reference item as placeholder, non-production, blocked from release,
   and replacement-required.
6. Create placeholder binding, scripted visual outcomes, screen states, status docs, and
   smoke checklist.
7. Validate no GS, wallet, BO/CM, VABS, DB, loopback API, or external calls were added.
8. Keep all production gates blocked in handoff and release docs.

Future games should not repeat manual sandbox prompts unless the reusable skill is
missing a required project-specific extension.
