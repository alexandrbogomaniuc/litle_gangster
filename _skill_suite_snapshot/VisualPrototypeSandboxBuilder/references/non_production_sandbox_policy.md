# Non-Production Sandbox Policy

A visual sandbox is an internal review surface for layout, placeholder art, and scripted
flow timing. It is allowed only when production gates remain closed.

Required status:

- `nonProduction: true`
- `productionClientCodeGenerated: false`
- `gameclientbuilder_implementation_allowed: false`
- `registration_generation_allowed: false`
- `wallet_endpoint_tests_allowed: false`
- `release_allowed: false`
- `certification_status: false`

The sandbox may be executable locally only as a static, offline prototype. It must not
be wired to GS, wallet, BO/CM, VABS, DB, loopback APIs, or external endpoints.
