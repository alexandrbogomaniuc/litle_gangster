# Presentation Payload Extension Options Matrix

Status: COMPLETED_RECOMMENDATION_RECORDED
Scope: planning only; no source patch was applied.

| Option | Source compatibility | Future reuse value | Migration risk | Schema change required | UI-kit impact | New-games-server impact | GameClientBuilder impact | History/recovery impact | Recommended status |
|---|---|---|---|---|---|---|---|---|---|
| `presentationPayload.gamePayload` | Not accepted by strict core schema; compatible with permissive transport/server record paths. | High. One reusable extension for Little Gangster and future games. | Moderate. Requires schema and mapper
policy plus 7001 compatibility decision. | Yes. Add optional generic extension field. | Required if shared mapper must preserve/expose extension. | Required for an 8001 payload builder or equivalent branch. | Stable generic extension path
for renderer consumption. | Good if the payload snapshot or reconstructable state is persisted. | RECOMMENDED |
| `presentationPayload.littleGangsterV03` | Not accepted by strict core schema. | Low to medium. One-game field does not generalize. | Lower for one game, higher for future field sprawl. | Yes. Add game-specific optional field. | Required
if shared mapper must preserve/expose extension. | Required for 8001 only. | Simple for Little Gangster, weak reusable pattern. | Works for 8001 only. | ACCEPTABLE_FALLBACK |
| Reuse or generalize `presentationPayload.mathBridge` | Existing 7001 source emits and reads `mathBridge`, but strict core schema does not accept it. | Medium only if renamed/generalized; low if kept as `mathBridge`. | High. Name implies
math internals and 7001 provisional semantics. | Yes if made canonical. | Required if shared mapper must expose it. | Existing 7001 uses it; 8001 would need a new shape. | Confusing for v0.3 cascade/feature render payload. | Possible but
semantically muddy. | CANDIDATE_PATTERN_ONLY; NOT_RECOMMENDED_AS_FINAL |
| Keep strict schema and place v0.3 data elsewhere in envelope | Could overload `round`, `feature`, `restore`, `history`, `labels`, or `counters`. | Low. Hard to reuse cleanly. | High. Risks brittle replay/reconnect and hidden render state.
| Maybe no presentation schema change, but other fields become overloaded. | Mapper would not naturally receive full v0.3 state. | Server would need awkward envelope packing. | Client would need scattered reads. | Poor: state spread across
unrelated groups. | BLOCKED; NOT_RECOMMENDED |

## Decision

Recommend `presentationPayload.gamePayload` as the future reusable extension point.

Use `presentationPayload.littleGangsterV03` only as a fallback if the schema/runtime team rejects the generic extension.

Keep `presentationPayload.mathBridge` as source-backed reference evidence for an adapter pattern, not as the Little Gangster final contract.
