# ParallelMathValidator Skill Adoption

Status: reusable skill-suite adoption note. This sprint did not run simulations and did not change Little Gangster active math.

## Why The Skill Exists

Future game-development projects need a way to validate math profiles at larger scale without trapping the main workflow in long simulation loops.
ParallelMathValidator provides that lane. It can prepare safe prompts for subagents or parallel GPT threads, coordinate local or external server jobs,
import result packages, validate seed separation, and extract registration math fields.

## How Future Games Use It

Future games should still start with MathModelDesigner and MathProfileCalibrator:

1. Design the initial math model.
2. Define LOW / MEDIUM / HIGH RTP levels inside 91.00% to 99.70%.
3. Define LOW / MEDIUM / HIGH volatility levels.
4. Create nine pretested `mathProfileId` values unless product explicitly approves a smaller matrix.
5. Use train seeds for calibration.
6. Hand larger train/validation/tail, bonus-buy, FRB/promo, registration field, or certification evidence work to ParallelMathValidator.

## How It Avoids Loops

MathProfileCalibrator remains bounded and train-focused. If the work becomes large, slow, tail-heavy, bonus-buy-specific, FRB-specific, or
certification-like, the workflow routes to ParallelMathValidator instead of repeating main-thread tuning loops.

## Parallel Thread And Subagent Support

ParallelMathValidator includes a prompt generator that restricts workers to a parallel output folder and forbids:

- active config changes;
- validation-seed tuning;
- backend/client/registration/release actions;
- DB/Cassandra execution;
- wallet/API calls;
- donor browsing or asset capture;
- certification or release claims.

## Main Workflow Impact

The main workflow may continue with unrelated planning while parallel math evidence runs. It must not pass downstream gates that depend on missing
evidence. Real math blockers still block GameServerRegistrar generation, RTPAndReleaseAuditor approval, and release.

## Little Gangster Status

This adoption sprint created reusable skill-suite docs/scripts only. Little Gangster active math values, active bonus-buy config, RTP/volatility
profiles, and Staging source were not changed.
