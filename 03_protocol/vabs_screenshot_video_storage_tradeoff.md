# VABS Screenshot / Video Storage Tradeoff

Generated: 2026-05-15

## Summary

Screenshots and videos are useful supporting evidence, but deterministic replay remains
the authoritative source. Visual HTML/render routes remain required for CM/backoffice
and in-game History unless current GS proves otherwise.

## Screenshot Mode

Supported by policy: yes.

Benefits:

- lower storage cost than video;
- fast to review;
- useful for final result snapshots;
- suitable for sampled QA, large wins, and disputed rounds.

Risks:

- cannot reconstruct animation timing;
- can miss intermediate cascade/feature states unless scoped carefully;
- still needs retention and checksum controls.

## Video Mode

Supported by policy: yes.

Benefits:

- strongest visual walkthrough for complex bonus rounds and disputes;
- useful for operator review when product explicitly asks for it;
- can capture timing-sensitive presentation bugs.

Risks:

- high storage and bandwidth cost;
- higher runtime capture overhead;
- more retention/security complexity;
- not suitable as default for every spin without explicit requirement.

## Recommendation

Default to `deterministic_replay_only` with required visual route. Enable screenshots or
feature/video capture only by game-level policy, operator override, dispute workflow, or
explicit product/release requirement.
