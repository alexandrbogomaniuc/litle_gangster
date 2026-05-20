# Public Export Sanitization Rules

## Exclude

- Donor/scaffold asset bodies.
- Screenshots, videos, HAR, event logs, raw network logs.
- Playwright folders, browser profiles, npm caches, node_modules, build outputs.
- Raw secrets, tokens, SIDs, signatures, emails, private links, and full donor URLs.
- Local absolute private paths.
- Non-production visual sandbox donor/reference assets, sandbox screenshots, copied
  donor/reference scripts, and `11_prototypes/*_visual_sandbox/assets_placeholder/`
  bodies unless a separate curated export approval explicitly replaces or clears them.

## Redact

- Donor URLs: `[REDACTED_DONOR_URL]`.
- Sensitive query values: `[REDACTED]`.
- Scaffold asset body paths: `02_reference_assets/authorized_raw/[REDACTED_ASSET_FILE]`.
- Secret-like assignments: `[REDACTED_SECRET]`.
- Local absolute paths: project-relative paths or `[REDACTED_LOCAL_PATH]`.

## Gitignore Rules

Use folder ignore patterns, not redacted placeholder filenames:

```gitignore
02_reference_assets/authorized_raw/
02_reference_assets/authorized_normalized/
02_reference_assets/quarantine/
01_reference_research/har/
01_reference_research/screenshots/
01_reference_research/videos/
01_reference_research/event_logs/
11_prototypes/*_visual_sandbox/assets_placeholder/
11_prototypes/*_visual_sandbox/scripts_reference/
11_prototypes/*_visual_sandbox/*.png
11_prototypes/*_visual_sandbox/*.jpg
11_prototypes/*_visual_sandbox/*.jpeg
11_prototypes/*_visual_sandbox/*.webp
.playwright-tool/
.playwright-browsers/
.npm-cache/
.secrets/
*.secret
*.secrets
*.env*
*.log
```

## Validation

A public export validator must fail on sensitive URL query keys, raw SID/signature/token patterns,
emails/private links, donor media/binary files, screenshots/HAR/event_logs, absolute private paths, unredacted
scaffold asset body paths, and donor/reference visual sandbox asset or script bodies. Safe text placeholders
are allowed.
