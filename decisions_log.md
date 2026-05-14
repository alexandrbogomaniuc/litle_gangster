# Decisions Log

This raw-safe public file is a sanitized excerpt of current project decisions.
It is not the full private working document.

## MathProfileCalibrator RTP Range Update

- Decision: update reusable MathProfileCalibrator RTP validation range to 91.00%-99.70% inclusive.
- Decision: require strict RTP ordering LOW < MEDIUM < HIGH.
- Decision: reject duplicate RTP levels.
- Decision: keep operators restricted to approved pretested mathProfileIds.
- Decision: do not allow arbitrary runtime RTP entry.
- Decision: do not change Little Gangster RTP profiles in this sprint.
- Decision: keep backend adapter implementation blocked.
- Decision: keep GameClientBuilder implementation blocked.
- Decision: keep GameServerRegistrar generation blocked.
- Decision: keep DB, wallet, donor, asset, and release work blocked.
