# AuthorizedReferenceResearcher Retry Preflight

## Sprint

- Timestamp: 2026-05-07T10:56:45+0100.
- Skill lane: AuthorizedReferenceResearcher retry.
- SprintReporter will run after this skill.

## Required Files Read

- `[SKILL_SUITE_ROOT]/AGENTS.md`
- `[SKILL_SUITE_ROOT]/SKILL_INDEX.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/AuthorizedReferenceResearcher/SKILL.md`
- `[SKILL_SUITE_ROOT]/.agents/skills/SprintReporter/SKILL.md`
- `[PROJECT_ROOT]/AGENTS.md`
- `[PROJECT_ROOT]/project_manifest.json`
- `[PROJECT_ROOT]/assumptions.md`
- `[PROJECT_ROOT]/decisions_log.md`
- `[PROJECT_ROOT]/00_skill_reports/AuthorizedReferenceResearcher/handoff.json`
- `[PROJECT_ROOT]/01_reference_research/blockers.md`
- `[PROJECT_ROOT]/01_reference_research/scenario_coverage.md`
- `[PROJECT_ROOT]/01_reference_research/network_observations.md`

## Preflight Checks

| Check | Result | Evidence |
|---|---|---|
| Project-local Playwright package usable | pass | `require('[PROJECT_ROOT]/.playwright-tool/node_modules/playwright')` succeeded. |
| Project-local Chromium executable available | pass | Playwright `chromium.executablePath()` returned an executable path. |
| No Playwright reinstall needed | pass | Existing project-local install was usable. |
| `.gitignore` excludes `.playwright-tool/` | pass | Entry present. |
| `.gitignore` excludes `.playwright-browsers/` | pass | Entry present. |
| `.gitignore` excludes `.npm-cache/` | pass | Entry present. |
| `.gitignore` excludes `01_reference_research/har/` | pass | Entry present. |
| `.gitignore` excludes `02_reference_assets/authorized_raw/` | pass | Entry present. |
| `.gitignore` excludes `02_reference_assets/authorized_normalized/` | pass | Entry present. |
| `.gitignore` excludes `02_reference_assets/quarantine/` | pass | Entry present. |
| `.gitignore` excludes secrets/token logs | pass | `.secrets/`, `*.secret`, `*.secrets`, `*.env*`, `*.log`, `*token*.log`, `*session*.log`, and `*auth*.log` entries are present. |
| `project_manifest.json` parses before browser work | pass | JSON parse check succeeded. |
| Fresh donor/demo/test URL provided | fail | The prompt contained a placeholder instead of a usable URL. |

## Browser Retry Decision

Browser retry initially did not run. The supplied fresh donor/reference URL field was a placeholder, not a usable URL. The user later clarified that the previously supplied donor URL remains the current in-memory URL for this project and
explicitly asked Codex to use the visible in-app browser like a normal player.

Tool discovery did not expose a Google Chrome MCP or Browser Use Node REPL `js` control tool. After the explicit user clarification, Codex used OS-level normal-user clicks and cropped screenshots against the already-open Codex browser. This
produced visible-player evidence but not DevTools selectors, HAR, or browser-side network telemetry.

No full donor URL or token-like query value was persisted.

## Visible-Browser Retry Addendum

| Check | Result |
|---|---|
| Google Chrome MCP exposed to Codex | no |
| Browser Use Node REPL `js` exposed to Codex | no |
| OS-level visible-browser click/screenshot available | yes |
| Headless browser used for visible retry | no |
| Safe demo mode visible before spin | yes, `DEMO BALANCE` and `DEMO BET` were visible |
| One normal-user demo spin attempted | yes |
| Spin completed | no |
| Blocking result | in-game wallet connection error after spin attempt |
| Asset bodies saved | no |
| Response bodies saved | no |
| DB/Cassandra touched | no |

## Chrome MCP Retry Addendum

After the visible-browser retry, the user asked Codex to retry Google Chrome MCP. Tool discovery then exposed `mcp__chrome_devtools__`.

| Check | Result |
|---|---|
| Google Chrome MCP exposed after retry | yes |
| Donor launch opened in Chrome MCP | yes |
| Full donor URL/token persisted | no |
| Intro screen reached | yes |
| Base demo screen reached | yes |
| Safe demo mode confirmed | yes, `DEMO BALANCE` and `DEMO BET` were visible in accessibility snapshot |
| Accessible spin control clicked | yes |
| Demo spin/bet requests observed | yes, sanitized request metadata showed RGS `bet` calls returning HTTP 200 |
| Menu opened | yes |
| Game info opened | yes |
| Request bodies saved | no |
| Response bodies saved | no |
| Asset bodies saved | no |
| DB/Cassandra touched | no |

## Blocker

- `fresh_donor_url_placeholder_not_usable`: resolved by user clarification that the previously supplied URL remains current for this project.
- `donor_wallet_connection_lost_on_visible_demo_spin`: superseded for Chrome MCP by successful demo spin/bet metadata. Still note as an in-app visible-browser discrepancy.
- `in_app_network_metadata_not_available`: mitigated by Chrome MCP request metadata. Response bodies still intentionally not saved.
