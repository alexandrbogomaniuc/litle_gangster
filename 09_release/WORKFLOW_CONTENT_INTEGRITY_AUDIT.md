# Workflow Content Integrity Audit

This audit checks public-safe review files for real content and safety-sensitive omissions.

## _skill_suite_snapshot/ParallelMathValidator/SKILL.md
- exists: true
- line_count: 173
- not_one_line_placeholder: true
- expected_key_concepts_present: train/validation/tail=true, bonus buy=true, FRB/promo=true, registration math fields=true, certification evidence=true, no validation-seed tuning=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## _skill_suite_snapshot/ParallelMathValidator/scripts/validate_parallel_math_request.py
- exists: true
- line_count: 122
- not_one_line_placeholder: true
- expected_key_concepts_present: LOW/MEDIUM/HIGH=true, RTP=true, volatility=true, profile=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## _skill_suite_snapshot/ParallelMathValidator/scripts/extract_registration_math_fields.py
- exists: true
- line_count: 113
- not_one_line_placeholder: true
- expected_key_concepts_present: POSSIBLE_MODELS=true, BF_RTP=true, SD_KEYS=true, CAP_WIN_MULTIPLIER=true, MAX_WIN=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## _skill_suite_snapshot/WalletAndLaunchTester/SKILL.md
- exists: true
- line_count: 91
- not_one_line_placeholder: true
- expected_key_concepts_present: responsibility boundary=true, no real wallet endpoint calls without approval=true, canonical VABS routes=true, legacy alias routes=true, BO/CM acceptance=true, pending/stuck/retry/close/reconnect/FRB tests=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## _skill_suite_snapshot/GameServerRegistrar/SKILL.md
- exists: true
- line_count: 83
- not_one_line_placeholder: true
- expected_key_concepts_present: POSSIBLE_MODELS >= BF_RTP=true, CAP_WIN/MAX_WIN=true, SD_KEYS=true, wallet/config dependency=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## _skill_suite_snapshot/RTPAndReleaseAuditor/SKILL.md
- exists: true
- line_count: 90
- not_one_line_placeholder: true
- expected_key_concepts_present: ParallelMathValidator evidence=true, VABS/Lasthands=true, wallet/launch/history tests=true, release blocks if missing=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 03_protocol/8001_lifecycle_wrapper_apply_summary.md
- exists: true
- line_count: 57
- not_one_line_placeholder: true
- expected_key_concepts_present: lifecycle wrapper=true, Staging applied summary=true, planning/testing status=true, release blocked=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 03_protocol/8001_vabs_visual_history_route_apply_summary.md
- exists: true
- line_count: 74
- not_one_line_placeholder: true
- expected_key_concepts_present: JSON replay response exists=true, visual HTML response exists=true, media manifest support exists=true, durable storage not implemented=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 03_protocol/8001_vabs_legacy_alias_apply_summary.md
- exists: true
- line_count: 58
- not_one_line_placeholder: true
- expected_key_concepts_present: legacy alias exists=true, canonical routes preserved=true, BO/CM acceptance untested=true, durable storage not implemented=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 03_protocol/gs_wallet_accounting_responsibility_audit.md
- exists: true
- line_count: 167
- not_one_line_placeholder: true
- expected_key_concepts_present: browser/client is not real wallet owner=true, game runtime is not production real wallet owner unless proven=true, current GS/wallet provider owns real balance=true, pending/stuck owner GS or blocked=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 03_protocol/8001_runtime_vs_gs_responsibility_matrix.md
- exists: true
- line_count: 68
- not_one_line_placeholder: true
- expected_key_concepts_present: browser/client=true, game runtime=true, wallet=true, pending/stuck=true, registration=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 08_qa/8001_wallet_launch_test_scope_correction.md
- exists: true
- line_count: 50
- not_one_line_placeholder: true
- expected_key_concepts_present: responsibility boundary=true, wallet=true, approved endpoints=true, no client wallet ownership=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 07_registration/8001_wallet_config_registration_dependency.md
- exists: true
- line_count: 45
- not_one_line_placeholder: true
- expected_key_concepts_present: BankInfo/config/wallet dependency=true, generation blocked if unresolved=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## GAME_STATUS_CURRENT.md
- exists: true
- line_count: 427
- not_one_line_placeholder: true
- expected_key_concepts_present: release blocked=true, wallet tests missing=true, GameClientBuilder blocked=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true

## 09_release/current_release_blockers.md
- exists: true
- line_count: 277
- not_one_line_placeholder: true
- expected_key_concepts_present: release blocked=true, wallet/history blockers=true
- safety: private_paths_absent=true, raw_private_urls_absent=true, donor_hosts_absent=true, raw_secrets_absent=true, staging_source_code_absent=true, release_approval_claims_absent=true
