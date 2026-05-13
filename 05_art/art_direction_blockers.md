# Art Direction Blockers

## Release Blockers

- `approved_release_assets_missing`: final approved asset count is 0.
- `scaffold_assets_blocked_from_release`: 135 scene objects reference scaffold assets for planning only.
- `replacement_required`: 140 scene objects require original, internal-approved, or licensed replacement assets.
- `observed_asset_coverage_not_100_percent`: asset coverage is observed, not exhaustive.

## Product Decisions

1. Bonus buy
   - Current plan: keep in scope provisionally as `Start the Job`.
   - Needed: final wording, pricing display rules, confirmation copy, and math EV confirmation.

2. Double-up/gamble
   - Current plan: keep as placeholder only.
   - Needed: product/regulatory decision to remove or implement.

3. Mobile
   - Current plan: design safe-area placeholders and responsive controls.
   - Needed: final mobile validation during GameClientBuilder.

4. Big win
   - Current plan: `Vault Break` tiers and money-burst effect.
   - Needed: final thresholds/effect triggers from runtime/math integration.

5. Sound
   - Current plan: original or licensed noir/heist audio package.
   - Needed: ownership evidence and implementation format.

6. Asset approval
   - Current plan: no scaffold asset can ship.
   - Needed: explicit approval/replacement evidence for every release asset.

## Targeted Donor Re-check Decision

Targeted donor re-check was skipped. The 5 unmatched objects are a cluster-highlight overlay and desktop/mobile layout helper objects; they are better handled as original design/implementation assets than as additional donor scaffold
captures.

## Sprint Update: Donor Feature/Settings Parity (2026-05-10 19:52:26 BST)

Target feature policy is now `match_donor_features_and_settings`. Prior successful donor evidence supports a 6x5 cluster game with cascade/removal/refill behavior, golden-square cell states, rainbow activation, coin/reveal mechanics,
bonus-buy entry, separate Sound/Music settings, separate Super Turbo/Turbo settings, Info, Home, demo balance/bet controls, and 10,000x max-win messaging.

The fresh clean Playwright retry in this sprint reached an error shell and RGS/API failures, so this sprint does not claim complete feature coverage. No new asset bodies were saved. No release approvals changed.

Strict parity creates a required MathModelDesigner retry before full GameClientBuilder: the v0.2 math/result contract must be extended for cascade steps, golden-square state, rainbow/coin reveal mechanics, three feature modes, and exact
bonus-buy behavior or explicitly marked as accepted placeholders.
