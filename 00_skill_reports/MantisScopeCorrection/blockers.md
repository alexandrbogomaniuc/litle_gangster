# Mantis Scope Correction Blockers

Generated: 2026-05-11

## Open Blockers

- `extgame_lane_unverified_for_current_gs`: current GS did not prove Little Gangster must implement an ExtGame external endpoint.
- `vabs_lasthands_history_contract_unverified`: GS concepts exist, but Little Gangster history/replay contract is not verified.
- `process_transaction_equivalent_unverified_for_current_gs`: Mantis `processTransactions` must be translated to current-lane process-equivalent validation.
- `round_completion_contract_unverified_for_current_gs`: current GS helper concepts exist, but 8001 mapping is not verified.
- `production_rng_owner_unverified_for_current_gs`: backend/provisional RNG signals exist, but production RNG ownership/certification remains unverified.
- `frb_ocb_promo_support_decision_pending`: FRB/OCB/promo scope must be decided and proven.
- `current_gs_expected_staging_paths_mismatch`: the expected Staging paths and compose-derived actual paths differ.
- `math_parity_retry_required`: next MathModelDesigner retry/audit must incorporate the corrected checklist.

## Not Blockers For This Sprint

- No raw Mantis source was required; the user provided a sanitized checklist in the prompt.
- ExtGame not selected is the intended correction, not a failure.

