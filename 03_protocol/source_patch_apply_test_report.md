# Source Patch Apply Test Report

Sprint: ProtocolAndSchemaMapper source patch apply for `presentationPayload.gamePayload`

Status: validations passed with existing toolchain caveats

## Passing Validations

- `python3 -m json.tool` over the six patched canonical response JSON schemas: passed.
- AJV validation of each `presentationPayload` schema occurrence: passed.
- AJV confirmed `gamePayload` is accepted and unknown top-level presentation fields remain rejected.
- Core-protocol Zod parse smoke test for `RuntimeEnvelopeResponseSchema`: passed.
- Core-protocol Zod smoke test confirmed unknown top-level presentation fields remain rejected.
- UI-kit mapper smoke test confirmed `gamePayload` is preserved untouched: passed.
- Browser runtime contract test via local `tsx`: passed, 10 passed and 0 failed.
- Presentation mapper test via local `tsx` with a minimal `navigator` shim: passed, 4 passed and 0 failed.

## Commands Run

```text
python3 -m json.tool <six response schema files>
node --input-type=module <AJV presentationPayload schema validation>
./node_modules/.bin/tsx tests/contract/browser-runtime.contract.test.ts
./node_modules/.bin/tsx tests/game/presentation-mapper.test.ts
./node_modules/.bin/tsx --eval <core-protocol gamePayload parse smoke test>
./node_modules/.bin/tsx --eval <UI-kit gamePayload passthrough smoke test>
./node_modules/.bin/tsc -p tsconfig.json --noEmit
./node_modules/.bin/tsc -p packages/ui-kit/tsconfig.json --noEmit
```

## Failed Or Skipped Commands

Evidence label: BLOCKED_BY_LOCAL_TOOLCHAIN

The repo's documented direct Node command uses `--experimental-transform-types`, but the active Node binary is
Node v18.20.8 and does not support that flag. The tests were rerun with local `tsx`.

Evidence label: PRE_EXISTING_CONFIG_FAILURE

Root and UI-kit TypeScript typechecks failed on existing repository configuration issues, primarily
`allowImportingTsExtensions` and package `rootDir` constraints. These failures are not specific to the
`gamePayload` patch and were present across many unrelated package files.

Evidence label: NOT_RUN_NOT_MODIFIED

`new-games-server` tests were not run because no `new-games-server` source file was modified and this sprint
did not implement a server emission branch.

## Test Outcome

Patch-specific schema and mapper validations passed.

Full TypeScript typecheck remains blocked by existing repo configuration and should be addressed separately
before source release.
