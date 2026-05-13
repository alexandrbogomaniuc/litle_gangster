# Project Rules

1. Read `project_manifest.json` before every skill.
2. Read the nearest `AGENTS.md` before acting.
3. No broad filesystem search.
4. Do not search outside this project, the skill suite, uploaded docs already available in the session, or explicit user-provided paths.
5. No raw secrets. Store secret references only.
6. Do not print or persist the full donor URL when it contains tokens or similar sensitive parameters.
7. No production DB apply.
8. No Cassandra execution unless a future approved dev/stage task explicitly authorizes it.
9. No unauthorized asset release.
10. Unknown/protected donor/reference/scaffold assets block release.
11. Do not claim 100% coverage without direct proof.
12. Write `skill_report.md`, `validation_checklist.md`, `blockers.md`, and `handoff.json` after every skill run.
13. Run SprintReporter after every sprint.

## Security Boundaries

1. Do not create or modify persistent jobs without explicit user approval in the active conversation. This includes `launchd`, cron, background loops, `nohup`, `tmux`, `screen`, heartbeat/tick jobs, hooks, and recurring automations.
2. Any approved persistent job must have a clear purpose, an expiry or stop condition, a log path, and cleanup instructions. Prefer disabled-by-default jobs unless the user explicitly asks to start them.
3. Do not use VPN routes, private/internal IP ranges, company domains, inventory files, browser history, mail caches, Teams/Slack caches, Downloads, Keychain, SSH config/keys, or VPN configs for infrastructure discovery unless the user
provides an explicit allowlist in the active conversation.
4. Do not run SSH, SCP, SFTP, remote `rsync`, `nc`, `nmap`, `telnet`, `cqlsh`, `nodetool`, Kubernetes commands, or port/service probes against non-local targets without an explicit host allowlist and command allowlist from the user.
5. Non-local targets include anything other than `localhost`, `127.0.0.1`, `::1`, or a dev server started for the current task. Private ranges such as `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, and VPN interfaces such as `utun`,
`tun`, `tap`, or `ppp` are considered sensitive.
6. Broad goals such as "unblock", "keep going", "find evidence", "do not stop", or "fix all blockers" are not permission to scan networks, use VPN access, read sensitive local sources, or install persistence.
7. If external network access is truly needed, stop and ask for an allowlist containing exact hosts, exact commands, expected duration, and whether persistence is allowed.
8. Keep agents and MCPs/plugins minimal. Do not install or run unknown MCP servers, plugins, or background helpers without reviewing their source and getting user approval.
9. Redact secrets, tokens, personal account identifiers, exact sensitive file names, and internal host details when preparing logs or messages for third parties.
