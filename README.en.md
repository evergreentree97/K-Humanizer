# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)
[![skills.sh](https://skills.sh/b/evergreentree97/K-Humanizer)](https://skills.sh/evergreentree97/K-Humanizer)

[한국어](README.md)

K-Humanizer edits awkward Korean in AI-assisted resumes, emails, chat messages,
and product copy. It is an Agent Skill for Cursor, Claude, and Codex.

```text
Before  고객 문의 분류 기준을 다시 정리하는 작업을 통해 주간 평균 처리 시간을 18시간에서 11시간으로 개선했습니다.
After   고객 문의 분류 기준을 다시 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

The shorter sentence still says what changed and gives the same numbers. In
`이의 신청은 담당 상담사를 통해서만 접수할 수 있습니다`, however, the counselor
is the only way to file an appeal. That wording does useful work, so it stays.

## Install

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

Paste your text and tell the skill where it will appear. For an email to a
colleague, try:

```text
Use $k-humanizer to edit this Korean email to a colleague.
Keep the dates and the request. Soften any wording that sounds too formal.

[paste your email]
```

For a resume, the skill edits awkward wording in what you have already written.
It can keep terms your readers use, such as `race condition` in a developer
resume. If you want it to write bullets from notes or reorder your experience
for a job posting, ask for that directly.

## More examples

| Where it appears | Before | After |
| --- | --- | --- |
| Help article | 검토가 완료되지 않은 경우에도 임시 저장은 가능하나 제출은 불가합니다. | 검토가 끝나지 않아도 임시 저장은 할 수 있어요. 제출하려면 검토가 먼저 끝나야 해요. |
| Team chat | 해당 일정에 대해 확인한 이후에 공유하도록 하겠습니다. | 일정 확인하고 공유할게요. |

[More examples for email, public posts, and code review](skills/k-humanizer/references/use-cases.md)

## Why I built it

I reviewed more than 120,000 Korean responses and made over 7,500 edits. I used
those edits to document when to rephrase a sentence and when to leave it alone.

## Evaluation

The public golden set contains 220 synthetic examples, separate from the
responses I reviewed. It includes 90 resume examples, plus applications,
everyday conversation, email, documents, product copy, public posts, and code
review. [Fixture validation report](evals/reports/2026-08-25-fixture-baseline.md), [Original 200-case report](evals/reports/2026-08-17-fixture-baseline.md)

On August 25, 2026, `gpt-5.4` produced 220 answers using that version of the
skill. A separate Claude Opus session scored them. The average across five
measures was 4.765, and meaning fidelity averaged 4.800. The model judge
reported no critical changes to the facts. The report includes low-scoring
answers and a case where the score did not follow the rubric. [Model evaluation report](evals/reports/2026-08-25/model-baseline.md), [Evaluation plan](docs/validation-plan.md)

Try the short synthetic cases to see how the current editing guidance works.
[Review cases and rubric](skills/k-humanizer/references/evaluation.md#context-and-scope-review-cases)

## Try it from a local checkout

```bash
npx skills add . --skill k-humanizer --full-depth
```

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
python3 scripts/validate_model_baseline.py \
  evals/reports/2026-08-25/model-baseline.jsonl
```

The editing instructions are in the [skill file](skills/k-humanizer/SKILL.md).
[Korean wording reference](skills/k-humanizer/references/patterns.md), [Resume editing](skills/k-humanizer/references/resume.md), [Resume workflow](skills/k-humanizer/references/resume-workflow.md), [Role-specific examples](skills/k-humanizer/references/resume-roles.md), [Evaluation rubric](skills/k-humanizer/references/evaluation.md)

## Contributing

Reports about awkward Korean and installation problems are welcome in Korean
or English. Make up an example that shows the same problem as a real resume,
email, or customer document before posting it. [Open an issue](https://github.com/evergreentree97/K-Humanizer/issues/new/choose), [Contribution guide](CONTRIBUTING.md), [Dataset research](docs/dataset-research.md)

## License

MIT. See [LICENSE](LICENSE).
