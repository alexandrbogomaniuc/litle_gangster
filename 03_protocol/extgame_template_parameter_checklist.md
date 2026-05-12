# ExtGame Template Parameter Advisory Checklist

Generated: 2026-05-11
Corrected: 2026-05-11

## Scope

Candidate fields from Mantis/ExtGame material are advisory only. Do not assume `HOSTING_MODE=EXTGAME`, do not assume fields exist in current GS, and do not generate registration artifacts from this file alone.

Use `03_protocol/template_parameter_checklist_from_mantis.md` and `07_registration/mantis_template_parameter_registration_checklist.md` as the corrected registration checklist.

## Required Future Rule

GameServerRegistrar must verify every field against current GS schema/config/source before generation. Missing values are blockers. Registration remains generate-only unless a later approved dev/stage apply explicitly changes that.

