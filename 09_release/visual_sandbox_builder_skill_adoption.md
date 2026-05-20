# VisualPrototypeSandboxBuilder Skill Adoption

Status: adopted as reusable workflow guidance.

Little Gangster sandbox v2 is pilot evidence that a local non-production visual sandbox
can help owner review while all production gates remain closed. Future games should use
`VisualPrototypeSandboxBuilder` instead of ad hoc prompts when they need an internal
visual sandbox with quarantined donor/reference placeholders and scripted visual
outcomes.

The reusable skill keeps these boundaries:

- donor/reference assets are sandbox-only unless rights and release approval are explicit.
- donor/reference scripts are visual timing references only.
- scripted outcomes are not math, RTP, feature-odds, registration, wallet, release, or
  certification evidence.
- visual sandbox completion does not unlock GameClientBuilder implementation.
- visual sandbox completion does not unlock registration generation.
- visual sandbox completion does not unlock wallet endpoint tests.
- visual sandbox completion does not unlock release or certification.

Little Gangster active sandbox changed this sprint: false.
