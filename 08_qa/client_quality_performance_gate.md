# Client Quality Performance Gate

Status: release-audit gate only; no client build or test executed.

## Client Quality Gates

- Settings, paytable, autoplay, turbo, Super Turbo, sound, music, home/lobby, and error handling match donor parity requirements where observed.
- No missing translation keys.
- No broken reels, blank strips, black screens, or missing symbol states.
- No scene object leaks across long sessions.
- Mobile performance and thermals acceptable.
- Memory usage stable across long play, feature entry/exit, resume, and history.
- No browser-side production RNG/outcome generation.
- No donor/scaffold assets in release build.
- Error states cover wallet/API errors, reconnect, session error, unsupported error, restart-required state, and network failure.

## Future Test Evidence

GameClientBuilder and RTPAndReleaseAuditor must save sanitized performance and QA evidence. This file is a gate checklist only.

