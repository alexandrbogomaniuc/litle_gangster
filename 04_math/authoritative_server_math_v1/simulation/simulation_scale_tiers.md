# Simulation Scale Tiers

Created: 2026-05-13T11:00:00+00:00

These tiers correct the workflow interpretation for Little Gangster and future
games. The numbers are planning approximations, not a replacement for lab
requirements.

## Wiring Smoke

- Approximate rounds: 2k to 10k.
- Purpose: verify simulator starts, denominator, profile routing, RNG
  determinism, result fields, and impossible configs.
- Allowed decisions: fix wiring, denominator, and profile-selection bugs.
- Forbidden decisions: RTP approval, profile rejection, backend unlock,
  registration unlock, or release.
- Backend adapter: no.
- Registration: no.
- Release: no.

## Diagnostic Smoke

- Approximate rounds: 10k to 50k.
- Purpose: observe contribution direction and obvious drift.
- Allowed decisions: prioritize investigation areas and catch broken feature
  paths.
- Forbidden decisions: approve or reject RTP, tune aggressively, unlock backend,
  or unlock registration.
- Backend adapter: no.
- Registration: no.
- Release: no.

## Calibration Trend

- Approximate rounds: 100k to 500k.
- Purpose: early trend checks across multiple seeds.
- Allowed decisions: guide cautious tuning candidates.
- Forbidden decisions: certify RTP, approve high-volatility profiles, or open
  release gates.
- Backend adapter: no by default.
- Registration: no.
- Release: no.

## Calibration Confidence

- Approximate rounds: 1M to 5M.
- Purpose: confidence begins for ordinary model tuning.
- Allowed decisions: tune model levers if train/validation evidence holds.
- Forbidden decisions: release approval or rare-tail approval.
- Backend adapter: planning may proceed only with explicit approval and open
  blockers accepted.
- Registration: no generation.
- Release: no.

## Pre-Certification

- Approximate rounds: 10M to 50M.
- Purpose: better RTP and volatility confidence before lab-scale work.
- Allowed decisions: prepare implementation-adjacent handoff if non-RTP blockers
  are resolved.
- Forbidden decisions: final certification or max-win tail proof if still
  unobserved.
- Backend adapter: only if the user explicitly approves and gates allow.
- Registration: generate-only planning if values are approved.
- Release: no.

## Certification / Lab Scale

- Approximate rounds: 100M to 1B.
- Purpose: lab-style validation, rare feature convergence, max-win/tail
  discovery, and jackpot/tail behavior.
- Allowed decisions: certification package preparation subject to product and
  lab rules.
- Forbidden decisions: shortcut release without independent review or lab
  evidence.
- Backend adapter: already implemented systems can be validated.
- Registration: only after approved values.
- Release: only after formal approvals.

## Tail / Max-Win Discovery

- Approximate rounds: 100M to 1B, or a validated tail-focused method.
- Purpose: exercise rare bonuses, jackpot hooks, and max-win cap behavior.
- Allowed decisions: assess cap frequency and tail distribution.
- Forbidden decisions: artificially force cap hits as RTP evidence.
- Backend adapter: no by itself.
- Registration: no by itself.
- Release: no by itself.

## Small Sample Boundary

Small samples can prove wiring, denominator sanity, deterministic routing,
obvious broken logic, and impossible configs. They cannot prove true RTP,
high-volatility convergence, bonus-buy EV, jackpot behavior, cap frequency, or
release readiness.
