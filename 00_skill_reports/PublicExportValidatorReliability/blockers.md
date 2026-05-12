# Public Export Validator Reliability Blockers

## Resolved

- Prior public validation confidence was blocked by the external reviewer-observed mismatch between the reported pass and collapsed public files.
- The validator did not previously self-check for collapsed/minified Python.
- The validator used looser public Markdown readability thresholds.
- Some public Markdown files still contained very long lines that made review uncomfortable.

## Remaining

- No blocker remains for the public export formatting/validator reliability fix.
- The next project blocker remains technical, not export-related: Little Gangster still needs ProtocolAndSchemaMapper runtime adapter planning before any GameClientBuilder implementation.
