# v0 Fixture Integrity Baseline

Date: 2026-08-17

Status: Passed

Baseline commit: `6736310`

## Scope

This report covers the structural integrity and public hygiene of the synthetic
v0 golden set. It does not score generated text and must not be presented as
evidence that K-Humanizer has reached its naturalness or meaning-fidelity
targets.

## Commands

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

## Results

Both checks passed.

| Domain | Cases |
|---|---:|
| Resume | 90 |
| Document | 20 |
| Personal/everyday | 20 |
| Messenger | 20 |
| Email | 20 |
| Product/UI copy | 10 |
| Code review | 10 |
| Dialogue | 10 |
| Total | 200 |

The resume set includes five cases for each supported role group:

- Operations
- Planning
- QA
- Design
- Marketing/content
- Customer service
- Research/data
- People/education

The validator confirmed:

- Every line is valid JSON.
- Every case has a unique, non-empty ID.
- Every case has a supported domain.
- Required fields are present and contain non-empty values.
- Domain counts match the v0 specification.
- Role-specific resume counts match the v0 specification.
- The repository passes the public hygiene check.

## What This Baseline Does Not Prove

This baseline does not measure whether generated outputs:

- Preserve meaning and contribution boundaries.
- Sound natural in Korean.
- Fit the reader, relationship, channel, or purpose.
- Avoid unnecessary rewriting.
- Are ready to paste or publish.

Those properties require saved model outputs and human review against the
five-part rubric in [the validation plan](../../docs/validation-plan.md).

## Next Evaluation Gate

Before calling v0.2 a validation baseline:

1. Run K-Humanizer on all 200 cases with the model and version recorded.
2. Save every output in a dated report directory.
3. Score meaning fidelity, Korean naturalness, context fit, edit discipline,
   and practical usefulness from 1 to 5.
4. Publish averages by domain and the ten most common failure types.
5. Report every critical factual drift, fabricated metric, changed completion
   state, or inflated ownership claim without hiding failed cases.
