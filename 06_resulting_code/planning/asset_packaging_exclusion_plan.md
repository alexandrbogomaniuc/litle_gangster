# Asset Packaging Exclusion Plan

Status: planning-only safety gate.

## Release Exclusion Rules

- Donor/scaffold assets under `02_reference_assets` must never be packaged into a release build.
- Scaffold previews can be used only for internal planning and mapping.
- Release assets must come from approved original, approved internal, or approved licensed sources.
- `approved_assets_manifest.json` currently has zero final approved assets.
- Production build must fail if any production asset manifest references `02_reference_assets`.
- Production build must fail if any asset has `release_status=blocked_from_release`.
- Production build must fail if any scaffold capture path, donor asset body, screenshot, HAR, or raw network log is referenced.

## Later Build Checks

GameClientBuilder implementation must include an asset-manifest validation step before any release packaging. That validation must reject blocked scaffold references even if they render correctly in internal previews.

