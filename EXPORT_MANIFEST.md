# Export Manifest

Export type: raw-safe sanitized review checkpoint.
Project: Little Gangster.
Public repository: GitHub repository for Little Gangster review.
Branch: main.
Release build: false.
Production client: false.
Backend adapter: false.
Registration artifacts: false.
Wallet calls: false.
DB actions: false.
Release approved: false.

Included safe artifact groups:

- Current compact sprint report.
- Safe project manifest summary.
- Safe assumptions and decisions excerpts.
- Future-game RTP range rule.
- MathProfileCalibrator skill snapshot.
- MathProfileCalibrator RTP validation reference.
- MathProfileCalibrator calibration references.
- MathProfileCalibrator validator and planner scripts.
- MathProfileCalibrator handoff and RTP range update reports.

Reusable rule highlighted in this checkpoint:

- Future requested average theoretical RTP range is 91.00% to 99.70%, inclusive.
- Every future game has exactly LOW, MEDIUM, and HIGH RTP levels.
- RTP values must be strictly ascending: LOW < MEDIUM < HIGH.
- Operators choose only pretested approved profiles.
- Arbitrary runtime RTP values are not allowed.
- Little Gangster RTP values were not changed.

Excluded unsafe artifact groups:

- Donor asset bodies.
- Scaffold asset bodies.
- Screenshots.
- HAR files.
- Event logs.
- Raw network logs.
- Raw secrets.
- Full donor URLs.
- Tokenized URLs.
- Local browser profiles.
- Build artifacts.
- Generated client/runtime code.
- Registration artifacts.
- DB or wallet outputs.
