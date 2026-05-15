# Train, Validation, And Tail Seed Policy

## Train Seeds

Train seeds are the only seeds allowed for calibration, overlays, and tuning.
Train results may justify model adjustments when the sprint explicitly permits
tuning.

## Validation Seeds

Validation seeds are independent. They are used only after the train gate is
declared ready. If validation fails, record blockers. Do not tune from the
validation result.

## Tail Seeds

Tail/max-win seeds are separate. They estimate cap behavior, max observed win,
tail frequency, and max-win confidence. Tail results do not replace validation.

## Required Reporting

- seed family names or IDs;
- whether validation seeds were used for tuning, always expected false;
- profile coverage;
- round counts;
- any runtime limit or early stop;
- exact values final: false unless separately approved.
