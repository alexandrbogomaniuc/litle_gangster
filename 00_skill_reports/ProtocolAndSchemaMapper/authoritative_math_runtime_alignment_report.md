# ProtocolAndSchemaMapper Report: Authoritative Math Runtime Alignment

Sprint: AuthoritativeServerMathDesign

Status: completed as planning review only.

Evidence labels:

- PROVEN: `presentationPayload.gamePayload` support was patched in prior sprint evidence.
- PROVEN: 24 strict fixtures validated against patched schemas in prior sprint outputs.
- PROVEN: UI-kit preservation of `gamePayload` is recorded in prior sprint outputs.
- CANDIDATE: future backend adapter target is `new-games-server/src/games/little-gangster` plus a guarded 8001 branch.
- NOT_PROVEN: Little Gangster 8001 runtime owner.
- NOT_PROVEN: Little Gangster production result API.
- NOT_AUTHORITATIVE: 7001 math model.

Runtime alignment:

- Authoritative math should produce a server-owned result object.
- Backend adapter should map that result into a valid `/slot/v1` envelope.
- Game render data should be carried in `presentationPayload.gamePayload`.
- Wallet/accounting fields remain outside `gamePayload`.
- Browser remains renderer-only.

History alignment:

- Authoritative history must store cascade steps, feature state, cap state, recovery state, and compact replay/presentation snapshots.
- VABS/Lasthands replay must derive from server state.
- Reconnect must not re-consume RNG.

Registration alignment:

- Registration may identify RTP variants and feature flags.
- Registration must not import or execute math.

Implementation status:

- No backend adapter applied.
- No Staging source modified.
- No 8001 package created.
- No client build allowed.

Next recommendation:

- Refine authoritative simulation design or apply backend adapter only after explicit approval.

