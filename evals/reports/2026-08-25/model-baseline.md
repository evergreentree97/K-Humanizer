# Claude-Scored v0 Model Baseline

Date: 2026-08-25

Status: Passed the model-scored v1.0 thresholds, with 10 low-scoring cases
retained for follow-up

## Scope

This report covers all 220 synthetic cases in
`evals/fixtures/golden_set.v0.jsonl`. K-Humanizer outputs were generated with
`gpt-5.4` and scored in separate, non-persistent sessions by
`claude-opus-5`. The evaluated skill revision was
`814ffb022be6+skill-dfc50447df35`.

Claude received each source, expected traits, preservation requirements,
avoidance hints, and candidate output. It did not receive the K-Humanizer
generation instructions. The Claude CLI also reported an auxiliary Haiku call
for structured-output handling in each batch; the written evaluations and
scores came from Opus.

This is an independent model-scored baseline, not a human review. It measures a
single generator and a single judge on synthetic fixtures and does not claim
that every output is ready to publish.

The complete per-case inputs, outputs, scores, failure labels, and review notes
are in [model-baseline.jsonl](model-baseline.jsonl).

## Integrity Check

```bash
python3 scripts/validate_model_baseline.py \
  evals/reports/2026-08-25/model-baseline.jsonl
```

The validator confirmed all 220 fixture IDs, exact source inputs and domains,
one generator model, one judge model, five integer scores per case, and explicit
failure records. No case was omitted.

## Overall Results

| Measure | Score | Required | Result |
|---|---:|---:|---|
| Average across all five measures | 4.765 | 4.200 | Passed |
| Meaning fidelity | 4.800 | 4.700 | Passed |
| Korean naturalness | 4.827 | Not separately set | Reported |
| Context fit | 4.786 | Not separately set | Reported |
| Edit discipline | 4.745 | Not separately set | Reported |
| Practical usefulness | 4.664 | 4.200 | Passed |
| Critical factual or evidence failures | 0 | 0 | Passed |

## Domain Results

| Domain | Cases | Meaning | Naturalness | Context | Discipline | Usefulness | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| Application writing | 10 | 4.60 | 4.80 | 4.50 | 4.70 | 4.50 | 4.62 |
| Code review | 10 | 4.80 | 5.00 | 5.00 | 4.70 | 5.00 | 4.90 |
| Dialogue | 10 | 4.70 | 5.00 | 5.00 | 4.90 | 5.00 | 4.92 |
| Documents/reports | 20 | 4.50 | 4.55 | 4.50 | 4.60 | 4.20 | 4.47 |
| Email | 20 | 4.90 | 4.80 | 4.90 | 4.90 | 4.90 | 4.88 |
| Personal/everyday | 20 | 4.95 | 4.90 | 5.00 | 4.85 | 4.90 | 4.92 |
| Messenger/casual | 20 | 4.85 | 4.65 | 4.60 | 4.55 | 4.60 | 4.65 |
| Product/UI copy | 10 | 5.00 | 5.00 | 5.00 | 5.00 | 4.90 | 4.98 |
| Public/social post | 10 | 5.00 | 4.90 | 4.70 | 4.80 | 4.70 | 4.82 |
| Resume/profile | 90 | 4.79 | 4.86 | 4.79 | 4.72 | 4.59 | 4.75 |

Every domain average exceeded 4.2. Documents/reports had the lowest overall
average at 4.47, mainly because two outputs remained awkward or insufficiently
edited.

## Observed Failure Types

The judge assigned 21 failure labels across the 220 cases. Only five of the ten
available categories appeared:

| Failure type | Cases |
|---|---:|
| Under-editing | 12 |
| Unnatural Korean | 4 |
| Context mismatch | 3 |
| Over-editing | 1 |
| Generic organization fit | 1 |

No factual drift, number drift, ownership inflation, completion-state change,
or evidence-type mix-up was marked as a critical failure.

## Lowest-Scoring Cases

Ten cases averaged below 4.0 or received at least one score of 2:

| ID | Domain | Average | Lowest | Main finding |
|---|---|---:|---:|---|
| `doc_004` | Document | 3.20 | 2 | The rewrite preserved the point but introduced an awkward modifier. |
| `doc_012` | Document | 3.40 | 3 | Repeated `예외` wording remained awkward and narrowed the source slightly. |
| `resume_004` | Resume | 3.40 | 3 | The sentence stayed generic and was still difficult to use as evidence. |
| `application_001` | Application | 3.60 | 3 | It avoided invention but remained reusable for almost any organization. |
| `chat_003` | Messenger | 3.60 | 3 | It repeated the same absence meaning and kept a tentative ending. |
| `public_007` | Public post | 3.60 | 3 | It reduced hype but still retained unnecessary internal-detail wording. |
| `resume_005` | Resume | 3.60 | 3 | `힘을 보탰습니다` was too conversational for the resume context. |
| `resume_013` | Resume | 3.60 | 3 | The strength statement became too tentative for a resume. |
| `resume_001` | Resume | 3.80 | 3 | `성과를 냈습니다` remained generic and unsupported. |
| `resume_017` | Resume | 3.80 | 3 | The rewrite inferred repeated unnecessary work from a broader inefficiency claim. |

The full JSONL keeps the judge's notes for these and every other case. Failed
or weak outputs were not removed from the averages.

## Decision

The expanded K-Humanizer skill passes the current model-scored release
criteria. Its strongest areas in this run were product/UI copy, dialogue,
everyday writing, email, and code review. The next refinement should focus on
under-editing in low-information resumes and documents, while preserving the
current factual boundaries.

A human review of the ten lowest-scoring cases remains useful before treating
this model-scored result as a human-validated benchmark.
