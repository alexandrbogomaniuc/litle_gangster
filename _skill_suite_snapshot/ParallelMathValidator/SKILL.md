---
name: ParallelMathValidator
description: Run or coordinate parallel large-scale math validation for reusable iGaming projects, including 3x3 RTP/volatility train-validation-tail
gates, bonus-buy EV, FRB/promo liability, registration math field extraction, and non-certified evidence packaging without blocking the main workflow
or changing active configs.
---

# ParallelMathValidator

## Purpose

ParallelMathValidator coordinates math validation evidence that is too large,
slow, or independent to keep inside the main workflow. It can prepare local
jobs, external server jobs, subagent instructions, or parallel GPT thread
prompts, then import and validate the result package.

It is generic. Do not encode project-specific math, assets, or game names in
this skill.

## When To Run

Use this skill when a game needs:

- larger train, validation, or tail/max-win simulations;
- train validation tail gate coordination in a parallel lane;
- a parallel lane while the main workflow continues;
- bonus-buy EV validation;
- FRB/free-round/promo liability validation;
- registration math field extraction backed by simulation evidence;
- certification/lab evidence package preparation;
- confidence reporting across all 3 x 3 profiles.

## When Not To Run

Do not use this skill to design initial math, tune active configs, write
backend/client code, generate registration artifacts, call wallets, browse
donor URLs, capture assets, or approve release.

## Relationship To Other Skills

- MathModelDesigner creates the model, rules, simulator contract, and initial
  RTP/volatility framework.
- MathProfileCalibrator performs bounded train-only calibration. When large
  loops, tail jobs, bonus-buy validation, FRB liability, or certification-scale
  evidence is needed, it hands off here.
- GameServerRegistrar requires ParallelMathValidator outputs when registration
  math fields depend on unresolved simulation evidence, including registration
  math fields for `POSSIBLE_MODELS`, RTP, BF_RTP, SD keys, cap/max-win, and
  profile display mapping.
- RTPAndReleaseAuditor checks ParallelMathValidator outputs when present and
  keeps release blocked if required validation evidence is missing.

## Parallel/Subagent/Thread Mode

Parallel workers must write only to a declared parallel output folder. They may
run simulations or summarize existing server jobs only within the approved
scope. They must not change active configs or project source. Use
`scripts/generate_parallel_math_thread_prompt.py` to generate a safe prompt.

The main workflow owns imports, decisions, handoffs, and downstream routing.

## Required Inputs

- Game key and optional game ID.
- Three RTP labels: `LOW`, `MEDIUM`, `HIGH`.
- Three strictly ascending RTP values in `91.00 <= RTP <= 99.70`.
- Three volatility labels: `LOW`, `MEDIUM`, `HIGH`.
- Nine planned or existing `mathProfileId` entries unless product explicitly
  chooses a smaller matrix.
- Simulation scope: train, validation, tail/max-win, bonus-buy, FRB/promo,
  jackpot, or certification evidence.
- Seed policy and output folder.
- Flags for bonus buy, FRB/promo, and jackpot presence.

## Required Outputs

- Machine-readable request validation.
- Parallel prompt or server job instruction package.
- Imported result validation report.
- Profile-level confidence report.
- Registration math field extraction or explicit blockers.
- Certification evidence package draft when requested.
- Handoff JSON with gate states and next recommended skill.

## Forbidden Actions

- No active config changes.
- No validation-seed tuning.
- No backend/client/registration/release actions.
- No DB/Cassandra execution.
- No wallet/API calls.
- No donor browsing or asset capture.
- No certification or release claim unless explicitly approved by a separate
  final gate.

## Seed Policy

Train seeds may be used for tuning. Validation seeds are for validation only.
Tail/max-win seeds are separate from train and validation. Do not tune from
tail seeds unless the sprint explicitly reclassifies them as train seeds before
use. See `references/TRAIN_VALIDATION_TAIL_SEED_POLICY.md`.

## Bonus-Buy Policy

Bonus-buy RTP is separate from base RTP. `BF_RTP`, `BF_RTP_MIN`, `BF_BETS`,
and bonus-buy cap behavior must be validated separately when bonus buy exists.
`BF_RTP` may differ from `RTP_WITHOUT_BF`, but `POSSIBLE_MODELS` must cover the
max supported RTP across base, bonus buy, and other supported strategies.

## FRB/Promo Policy

FRB/free-round campaigns are not automatically base RTP. Treat FRB as promo EV,
campaign liability, state/history behavior, settlement/accounting behavior,
replay/VABS behavior, and cap behavior unless product/GS rules explicitly
require otherwise. See `references/FRB_PROMO_VALIDATION_POLICY.md`.

## Registration Field Extraction

Registration math fields must remain evidence-backed and explicitly blocked
when unresolved.

Use `scripts/extract_registration_math_fields.py` to extract or propose:
`POSSIBLE_MODELS`, `RTP_MIN`, `RTP_WITHOUT_BF`,
`RTP_MIN_WITHOUT_BF`, `BF_RTP`, `BF_RTP_MIN`, `BF_BETS`, `SD_KEYS`,
`CAP_WIN_MULTIPLIER`, `MAX_WIN`, `POSSIBLE_MAX_WINS`, `VOLATILITY`,
`mathProfileId`, and display mapping. Missing or unsupported fields must be
explicit blockers, not guesses.

## Certification Evidence Policy

Parallel evidence is non-certified unless a separate lab/release gate explicitly
approves it. Evidence packages must label source, seed families, round counts,
confidence limits, unresolved blockers, and whether values are final.

## Handoff Format

Include:

- `parallel_math_validation_completed`
- `parallel_mode`
- `request_valid`
- `profiles_expected_count`
- `profiles_tested_count`
- `train_gate_status`
- `validation_gate_status`
- `tail_maxwin_gate_status`
- `bonus_buy_gate_status`
- `frb_promo_gate_status`
- `registration_fields_ready`
- `certification_evidence_ready`
- `exact_values_final: false` unless explicitly approved
- `certification_status: false` unless explicitly approved
- `active_config_changed: false`
- `validation_seeds_used_for_tuning: false`
- `backend_adapter_implementation_allowed: false`
- `gameclientbuilder_implementation_allowed: false`
- `gameserverregistrar_generation_allowed: false`
- `release_allowed: false`
- `unresolved_blockers`
- `suggested_next_skill`
- `suggested_next_prompt_summary`

## References

Read only the relevant reference for the current task:

- `references/PARALLEL_MATH_VALIDATION_WORKFLOW.md`
- `references/SIMULATION_SCALE_AND_CONFIDENCE_POLICY.md`
- `references/TRAIN_VALIDATION_TAIL_SEED_POLICY.md`
- `references/BONUS_BUY_VALIDATION_POLICY.md`
- `references/FRB_PROMO_VALIDATION_POLICY.md`
- `references/REGISTRATION_MATH_FIELD_EXTRACTION.md`
- `references/CERTIFICATION_EVIDENCE_PACKAGE.md`
