# Golden-Square Module

Purpose: create, persist, and resolve golden-square overlays.

Server-owned behavior:

- Determine when golden squares are created.
- Persist golden-square cells across cascades and feature steps according to approved rules.
- Store state before and after each cascade and feature spin.
- Emit render hints for overlays only after authoritative state is produced.

State fields:

- active cells.
- creation reason.
- persistence scope.
- created at cascade/spin.
- resolved at event if applicable.

Open blockers:

- Exact creation probability.
- Exact interaction with rainbow activation.
- Exact persistence duration in feature modes.

Client boundary:

- Browser may draw overlays.
- Browser must not create or clear golden-square state.

