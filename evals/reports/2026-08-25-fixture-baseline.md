# Expanded v0 Fixture Integrity Baseline

Date: 2026-08-25

Status: Passed

## Scope

This report covers the structural integrity and public hygiene of the expanded
synthetic v0 golden set. It adds application-motivation and public-post coverage
to the original 200-case fixture.

This structural report is not a naturalness benchmark. Generated outputs and
rubric scores are published separately in the
[Claude-scored model baseline](2026-08-25/model-baseline.md).

## Commands

```bash
python3 scripts/validate_golden_set.py
python3 -m unittest scripts.test_validate_golden_set
python3 scripts/check_public_hygiene.py
```

## Results

All three checks passed on 2026-08-25.

| Domain | Cases |
|---|---:|
| Resume | 90 |
| Application writing | 10 |
| Document | 20 |
| Personal/everyday | 20 |
| Messenger | 20 |
| Email | 20 |
| Product/UI copy | 10 |
| Public/social post | 10 |
| Code review | 10 |
| Dialogue | 10 |
| Total | 220 |

The resume set still includes five cases for each supported role group:

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
- Required fields contain non-empty values.
- Domain and role counts match the v0 specification.
- The repository passes the public hygiene check.

The regression tests also confirmed that the validator rejects:

- A fixture with only 9 public-post cases.
- An unknown domain.
- A duplicate ID.

## Quality Baseline

The 2026-08-25 model baseline now covers all 220 cases, records the generator
and judge models, saves all five rubric scores, publishes domain averages, and
retains weak cases and failure labels. Human review remains separate from that
model-scored result.
