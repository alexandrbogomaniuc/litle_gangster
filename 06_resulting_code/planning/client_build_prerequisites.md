# Client Build Prerequisites

Status: blocking gate list before actual client code generation.

The following must be true before GameClientBuilder implementation:

- runtime result owner proven.
- result API contract proven or a reviewed fixture contract approved.
- `@gamesv1/core-protocol` or equivalent selected.
- New Games server/API or equivalent runtime inspected deeply enough for 8001.
- v0.3 scene/object map complete and current.
- final or placeholder asset strategy explicitly approved.
- scaffold release exclusion enforced.
- package/template lane selected.
- build stack selected.
- wallet/launch boundary known.
- history/VABS/Lasthands boundary known.
- registration metadata boundary known.
- math release validation status understood.
- explicit user approval to generate client code.

Until then, implementation remains blocked.

