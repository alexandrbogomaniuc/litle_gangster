# Math Engine State Machine

State machine status: DESIGN ONLY.

States:

1. `session_ready`
   - Server has validated session context and game config.
   - No RNG consumed.

2. `round_start`
   - Server creates round id, bet context, RTP variant, state version, and initial audit envelope.
   - Wallet debit/accounting happens outside game payload.

3. `base_grid_generate`
   - Server consumes RNG for the 6x5 starting grid.
   - Grid is stored as the first history snapshot.

4. `cluster_evaluate`
   - Server finds orthogonally adjacent clusters using Little Gangster pay rules.
   - Cluster threshold, paytable, and wild handling must come from approved Little Gangster math config.

5. `cascade_step`
   - Winning cells are removed.
   - Existing symbols drop.
   - Server consumes RNG for refills.
   - Each cascade records removed cells, dropped cells, refill symbols, cluster wins, and cumulative win.

6. `golden_square_update`
   - Server creates or preserves golden-square state based on approved Little Gangster rules.
   - State before and after every cascade is persisted.

7. `rainbow_activation`
   - Server evaluates rainbow activation.
   - Activation source, affected cells, and resulting symbol or coin state are recorded.

8. `coin_reveal`
   - Server reveals bronze, silver, or gold coin values when rules require.
   - Coin values and display tier are authoritative output.

9. `special_reveal`
   - Server evaluates pot-of-gold and four-leaf-clover reveal candidates.
   - Exact probability and reward rules remain product/math blockers.

10. `feature_trigger_check`
   - Server evaluates feature trigger after base or cascade resolution.
   - Trigger source, qualifying state, and selected feature path are stored.

11. `feature_mode_select`
   - Server selects or validates the feature mode.
   - Player selection versus random selection remains a product decision.

12. `feature_spin_loop`
   - Server repeats feature spin generation, cascade evaluation, golden-square, rainbow, coin, and special reveal rules until feature completion.
   - Free spins remaining and retrigger state are persisted after each spin.

13. `bonus_buy_purchase`
   - Server validates bonus-buy eligibility and purchase request.
   - Wallet/accounting remains outside game payload.
   - Cost/EV is blocked until product approval.

14. `bonus_buy_feature_start`
   - Server creates purchased feature state after accounting succeeds.
   - No browser-selected authoritative outcomes are accepted.

15. `max_win_cap_check`
   - Server compares cumulative win with cap.
   - Pre-cap and capped values are recorded.
   - Round may terminate immediately when cap is reached.

16. `win_tier_classify`
   - Server assigns win ratio and display tier.
   - Classification is display metadata, not separate payout authority.

17. `round_complete`
   - Server marks final state, completion reason, final win, cap status, and persistence snapshot.
   - Wallet settlement happens outside game payload.

18. `history_snapshot_commit`
   - Server writes replay, Lasthands, VABS/VBA, and audit references.

19. `recovery_snapshot_ready`
   - Server stores current state for reconnect and resumegame behavior.

20. `session_close`
   - Server finalizes close/session state without changing completed round math.

Failure handling:

- Any crash or reconnect must resume from persisted server state.
- Idempotency keys and request counters must prevent duplicate round resolution.
- Recovery must not consume extra RNG for already resolved steps.

