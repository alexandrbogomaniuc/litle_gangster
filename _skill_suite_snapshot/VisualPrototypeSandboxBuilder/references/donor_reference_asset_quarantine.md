# Donor / Reference Asset Quarantine

Donor/reference files may be used in the sandbox only as quarantined internal
placeholders.

Every inventory item should record:

- local project-relative path
- asset group
- `placeholderOnly: true`
- `nonProduction: true`
- `productionReady: false`
- `approvedForRelease: false`
- `replacementRequired: true`
- owner/status notes

Do not copy donor/reference assets into reusable skill repositories. Do not move
donor/reference assets into production client folders. Public export must exclude
sandbox placeholder assets and donor/reference script copies unless separately curated
and approved.
