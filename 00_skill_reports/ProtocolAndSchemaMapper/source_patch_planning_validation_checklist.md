# Source Patch Planning Validation Checklist

| Check | Result | Evidence label |
|---|---|---|
| `project_manifest.json` parses. | PASS | PROVEN_VALIDATION |
| ProtocolAndSchemaMapper `handoff.json` parses. | PASS | PROVEN_VALIDATION |
| `source_patch_planning_file_changes.json` parses. | PASS | PROVEN_VALIDATION |
| Required 03_protocol source patch planning files exist and are non-empty. | PASS | PROVEN_OUTPUT |
| Required 06_resulting_code/planning files exist and are non-empty. | PASS | PROVEN_OUTPUT |
| Required 08_qa files exist and are non-empty. | PASS | PROVEN_OUTPUT |
| `09_release/schema_patch_approval_gate.md` exists and is non-empty. | PASS | PROVEN_GATE |
| Patch proposal `.diff.md` files exist and are non-empty. | PASS | PROVEN_PROPOSAL |
| No real `.diff` or `.patch` file was created. | PASS | PROVEN_SAFETY_GUARD |
| No file under `[STAGING_ROOT]` was modified. | PASS | PROVEN_PROCESS_GUARD |
| No source patch was applied. | PASS | PROVEN_SCOPE_GUARD |
| No implementation code was generated. | PASS | PROVEN_SCOPE_GUARD |
| No production client code was generated. | PASS | PROVEN_SCOPE_GUARD |
| No `package.json`, `src`, `public`, `dist`, or `build` was created. | PASS | PROVEN_SCOPE_GUARD |
| No registration artifact was generated. | PASS | PROVEN_SCOPE_GUARD |
| No DB/Cassandra action occurred. | PASS | PROVEN_SCOPE_GUARD |
| No wallet/API call occurred. | PASS | PROVEN_SCOPE_GUARD |
| No donor browsing occurred. | PASS | PROVEN_SCOPE_GUARD |
| No asset capture occurred. | PASS | PROVEN_SCOPE_GUARD |
| No release approval occurred. | PASS | PROVEN_SCOPE_GUARD |
| No raw email/secret-like values are present in sprint outputs. | PASS | PROVEN_SAFETY_GUARD |
| Patch proposal docs clearly state NOT APPLIED. | PASS | PROVEN_PROPOSAL_GUARD |
| Reports state approval is required before source modification. | PASS | PROVEN_APPROVAL_GATE |
