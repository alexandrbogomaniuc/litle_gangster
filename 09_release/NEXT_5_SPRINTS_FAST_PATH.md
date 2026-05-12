# Next 5 Sprints Fast Path

Status: recommended order.

1. Checkpoint git review/push sprint.
   - Reason: many meaningful local sprints have accumulated.
   - Scope: validation/checkpoint only, no implementation.

2. MathModelDesigner calibration sprint.
   - Reason: exact RTP, bonus-buy EV, free-spin rules, symbol weights, paytable, volatility, and cap values remain provisional.
   - Scope: use simulation scripts, summarize outputs, keep exact values non-final unless evidence proves them.

3. ProtocolAndSchemaMapper backend adapter apply or refine decision.
   - Reason: backend adapter plan exists, but source modification and implementation still require explicit approval.
   - Scope: either apply approved backend adapter patch or refine blockers; no automatic implementation.

4. GameClientBuilder fixture/static prototype iteration or implementation gate.
   - Reason: client work depends on backend adapter, runtime proof, and simulation status.
   - Scope: renderer-only unless all implementation gates and explicit user approval are present.

5. GameServerRegistrar registration generate-only planning.
   - Reason: registration generation should wait until math/config values and runtime path are more stable.
   - Scope: planning/generate-only; no DB/Cassandra apply.

## Handoff Comparison

Current handoffs recommend checkpoint git review/push next. That matches this fast path. Implementation remains blocked.

