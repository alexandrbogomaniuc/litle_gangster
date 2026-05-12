# Public Export Validation Push Without Workflow Checklist

| Check | Result |
|---|---|
| GitHub Actions workflow deferred | pass |
| Workflow scope missing recorded | pass |
| Workflow file excluded from staged changes | pass |
| Workflow file excluded from commit | pass |
| Working-tree `validate_public_export.py` compile | pass |
| Working-tree `validate_git_blob_content.py` compile | pass |
| Working-tree `validate_github_raw_commit.py` compile | pass |
| Working-tree public export validator | pass |
| Working-tree README line count >= 20 | pass |
| Working-tree reviewer guide line count >= 25 | pass |
| Working-tree validator line count >= 200 | pass |
| Git blob validator | pass |
| Git blob README line count >= 20 | pass |
| Git blob reviewer guide line count >= 25 | pass |
| Git blob validator line count >= 200 | pass |
| No `.github/workflows/` file in commit | pass |
| Push to public `main` | pass |
| GitHub raw validator for pushed commit | pass |
| GitHub raw README line count >= 20 | pass |
| GitHub raw reviewer guide line count >= 25 | pass |
| GitHub raw validator line count >= 200 | pass |
| Public export validation can be claimed as passed | pass |
| No donor asset bodies pushed | pass |
| No screenshots, HAR, or raw logs pushed | pass |
| No raw secrets, SIDs, signatures, private links, emails, tokenized URLs, or full donor URLs pushed | pass |
| No client/runtime/registration code, DB action, wallet call, or release approval | pass |
