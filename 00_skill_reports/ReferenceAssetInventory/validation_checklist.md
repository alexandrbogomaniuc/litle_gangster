# ReferenceAssetInventory Supplemental Validation Checklist

- [x] `project_manifest.json` parsed.
- [x] `final_inventory.csv` has the required columns.
- [x] `asset_ownership_register.csv` exists.
- [x] `sha256_manifest.csv` exists.
- [x] Every inventoried scaffold file has SHA-256.
- [x] Every scaffold file is `scaffold_internal_only`.
- [x] Every scaffold file is `blocked_from_release`.
- [x] No file is marked `approved_for_release`.
- [x] No scaffold file was copied into `06_resulting_code`.
