# Static Fixture Renderer v0.1

Status: NON-PRODUCTION FIXTURE RENDERER.

This prototype is a local planning viewer for the 24 Little Gangster v0.3 non-production renderer fixtures.

It is not a game client, not release code, not wallet integration, and not authoritative result generation.

## Scope

- Plain static HTML, CSS, and JavaScript only.
- Uses fixture JSON from `06_resulting_code/planning/fixtures/examples/`.
- Uses placeholder shapes, colors, labels, and text only.
- Shows v0.3 state coverage for cascades, golden-square overlays, rainbow, coin reveals, feature modes, bonus buy, win tiers, max-win cap, round completion, and reconnect/recovery.
- Keeps the browser/client renderer-only.

## Non-Goals

- No production runtime transport.
- No production random number generation.
- No authoritative win calculation.
- No payout calculation.
- No wallet or accounting mutation.
- No real session handling.
- No registration metadata generation.
- No release asset packaging.

## How To Open Locally

Open `index.html` in a browser. If local JSON loading is blocked by `file://`, serve this project root from a local-only static server and open this folder's `index.html` through that local server.

The prototype includes a file-picker fallback for manually loading one of the fixture JSON files if direct local fixture loading is blocked.

## Fixture Boundaries

The renderer prefers `presentationPayload.gamePayload` and documents `presentationPayload.littleGangsterV03` as fallback.

Little Gangster runtime owner and v0.3 result API remain unproven. Full GameClientBuilder implementation remains blocked.

## Strict Schema Fixtures

Strict-schema candidate runtime-envelope fixtures now exist under:

`../../planning/fixtures/strict_schema_examples/`

Those files validate against the patched `/slot/v1` response schemas and carry v0.3 data through
`presentationPayload.gamePayload`.

The current static renderer was built for the original renderer-planning fixture wrapper. It can read the nested
`presentationPayload.gamePayload.payload` shape, but its fixture list and metadata panels remain wired to the
original fixture manifest.

Status: `static_renderer_strict_fixture_support_pending`.
