# Prototype Limitations

Status: NON_PRODUCTION_FIXTURE_ONLY.

This prototype exists only to inspect visual/state coverage of the 24 Little Gangster v0.3 planning fixtures.

## It Does Not Prove

- Little Gangster / 8001 runtime owner.
- Little Gangster v0.3 production result API.
- `presentationPayload.gamePayload` schema approval.
- Backend adapter correctness.
- Production payout, RNG, max-win, or RTP behavior.
- Wallet/accounting behavior.
- Registration metadata readiness.
- Release asset readiness.

## Technical Limits

- Uses placeholder shapes and labels only.
- Uses symbolic fixture grids, not approved production symbol IDs.
- Loads static local JSON files only.
- Does not animate with production timing.
- Does not package assets.
- Does not depend on npm, Pixi, Vite, Webpack, or template code.

## Gate Impact

This prototype does not unlock full GameClientBuilder implementation. It only helps reviewers inspect fixture coverage before schema extension review and backend/runtime adapter implementation planning.

## Strict Fixture Limitation

The strict schema fixtures are response-envelope examples, not the original renderer-planning wrapper objects.

The renderer can consume the nested v0.3 payload path if a strict file is loaded manually, but the manifest,
fixture metadata panels, expected scene states, expected object states, and notes are still optimized for the
original fixture examples.

Blocker: `static_renderer_strict_fixture_support_pending`.

No renderer code was changed in the strict fixture update sprint.
