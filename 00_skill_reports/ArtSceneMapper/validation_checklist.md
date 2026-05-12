# ArtSceneMapper Validation Checklist

| Check | Result | Evidence |
|---|---|---|
| `project_manifest.json` parses | PASS | validated before SprintReporter |
| `handoff.json` parses | PASS | validated before SprintReporter |
| `scene_map_schema.json` parses | PASS | validated before SprintReporter |
| `object_id_map.json` parses | PASS | validated before SprintReporter |
| all scene map JSON files parse | PASS | 18 required scene maps validated |
| HTML inspector files exist and non-empty | PASS | `index.html`, `scene_inspector.js`, `scene_inspector.css`, `README.md` |
| `asset_audit.csv` required columns present | PASS | CSV header validated |
| no asset audit row has `approved_for_release` | PASS | all rows are `pending_replacement` |
| no scaffold/reference asset copied into `06_resulting_code` | PASS | no new files there during sprint |
| no donor URL/token in new/updated outputs | PASS | redaction scan passed |
| no raw secret/test token/session/auth/key/JWT/signature/hash values | PASS | redaction scan passed |
| no browser work occurred | PASS | no browser/Chrome/Playwright tools used |
| no new donor asset capture occurred | PASS | no writes under `02_reference_assets` |
| no DB/Cassandra action occurred | PASS | no DB/Cassandra commands used |
| no wallet call occurred | PASS | no endpoint calls made |
| no later skills were run | PASS | only ArtSceneMapper and SprintReporter artifacts updated |
| reports state 6x5 v0.2 selected | PASS | summary, handoff, reports |
| reports state 5x3 v0.1 not used | PASS | summary, handoff, reports |
| final art approval remains pending | PASS | summary, blockers, handoff |
