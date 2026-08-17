# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)
[![skills.sh](https://skills.sh/b/evergreentree97/K-Humanizer)](https://skills.sh/evergreentree97/K-Humanizer)

[한국어](README.md)

K-Humanizer is an Agent Skill that helps Cursor, Claude, and Codex write Korean
that sounds natural to Korean readers.

It rewrites awkward phrasing without changing the source's facts, numbers,
names, domain terms, or level of certainty. If a sentence already reads
naturally, the skill leaves it alone.

```text
Before: 고객 문의 분류 체계 고도화를 통해 주간 평균 처리 시간을 18시간에서 11시간으로 크게 개선했습니다.
After:  고객 문의 분류 기준을 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

Both sentences report the same result. The second is more direct: it says what
changed and reports the result without abstract, translation-like phrasing.

## Who It Is For

- Non-native Korean writers creating product copy, emails, or documents for Korean users
- Job seekers whose AI-assisted Korean resumes sound stiff or exaggerated
- Teams that need different levels of formality for chat, email, documents, and product UI
- Writers who want to improve the Korean without losing facts or domain terminology

## A Month of Cleaning Korean Text, Turned into a Skill

I spent a month cleaning Korean text data every day. The same problems kept
returning: grammatically correct sentences shaped like English, unnecessary
formality, and abstract nouns hiding the actual action. I kept notes on those
cases and turned the repeated corrections into rules with clear conditions and
exceptions.

K-Humanizer does not blindly replace words. For example, it keeps `~를 통해`
when the phrase describes a real route or intermediary. It rewrites the phrase
only when it makes a simple action harder to read.

## Try It

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

After installation, tell the skill where the text will appear and who will read
it.

```text
Use $k-humanizer to rewrite the Korean product copy below for Korean users.
Keep the facts, numbers, names, and product terms unchanged. Remove only
translation-like phrasing and unnecessary formality.

[paste text]
```

For a resume:

```text
Use $k-humanizer to polish the Korean resume below.
Keep its facts, numbers, and field-specific terms unchanged. Remove only
translationese and generic AI-style achievement language.

[paste resume]
```

## What It Changes and What It Preserves

| What the skill checks | What it does |
|---|---|
| English-shaped syntax and translationese | Uses word order and sentence structure that Korean readers expect |
| Abstract nouns and long noun phrases | States the action and result already present in the source |
| Tone across chat, email, documents, and product UI | Adjusts formality and sentence length for the reader and channel |
| Facts, numbers, names, sources, and domain terms | Preserves them as written |
| Ownership, completion state, and uncertainty | Does not make the claim stronger than the source |
| Unsupported results or emotions | Does not invent them |
| Text that already sounds natural | Keeps it or edits only the necessary span |

K-Humanizer is not an AI-detector bypass tool. It does not invent resume
achievements or make the source sound more certain than it is.

## Examples

### Resume

```text
Before:
저는 고객 문의 분류 체계 고도화를 통해 주간 평균 처리 시간을 18시간에서 11시간으로 크게 개선했습니다.

After:
고객 문의 분류 기준을 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

### Product Copy

```text
Before: 이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.
After:  업로드한 문서와 처리 상태를 보여줍니다.
```

### Messenger

```text
Before: 제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.
After:  일정 확인해보고 공유드릴게요.
```

### Everyday Korean

```text
Before: 현재 비가 오고 있는 상황이므로 우산을 챙기는 것이 좋을 것으로 보입니다.
After:  비 와서 우산 챙기는 게 좋겠어.
```

See [use cases](skills/k-humanizer/references/use-cases.md) for more examples.

## Resumes and Career Documents

K-Humanizer treats editing an existing sentence and writing a new sentence from
notes as different tasks. By default, it keeps the resume's facts and
field-specific language and changes only the awkward phrasing. It writes from
notes or reorders experience for a job posting only when asked.

| Material supplied | What the skill does |
|---|---|
| Finished career bullets | Removes translationese and AI-sounding phrasing without changing facts or claim strength |
| A full resume | Fixes recurring style problems while preserving field-specific terms and personal voice |
| Notes or task lists | Writes career bullets from confirmed details only when requested |
| A job posting and an existing resume | Reorders relevant existing experience only when requested |

The skill keeps the details that make each role specific. Operational
exceptions, planning scope decisions, QA reproduction conditions, and design
rationale stay specific instead of becoming generic achievement language.

- [Resume and career-document rules](skills/k-humanizer/references/resume.md)
- [Resume workflow](skills/k-humanizer/references/resume-workflow.md)
- [Role-aware resume rules](skills/k-humanizer/references/resume-roles.md)

## Skill Files

The portable skill lives in [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md).

- [Use cases](skills/k-humanizer/references/use-cases.md)
- [Pattern checklist](skills/k-humanizer/references/patterns.md)
- [Evaluation rubric](skills/k-humanizer/references/evaluation.md)

To test the current files from a local checkout:

```bash
npx skills add . --skill k-humanizer --full-depth
```

## Validation and Data

The v0 fixture contains 200 synthetic examples with no real personal or
proprietary data:

- 90 resume examples, including 40 role-specific cases
- 20 personal and everyday examples
- 20 messenger examples
- 20 email examples
- 20 document examples
- 10 product and UI copy examples
- 10 dialogue examples
- 10 code review comment examples

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

- [v0 fixture integrity report](evals/reports/2026-08-17-fixture-baseline.md)
- [Evaluation plan and v1.0 acceptance criteria](docs/validation-plan.md)

The public baseline currently checks fixture structure, domain distribution,
unique IDs, required fields, and repository hygiene. Naturalness and meaning
fidelity scores will be published in a separate manual evaluation report.

This repository does not include third-party datasets. Do not submit private
resumes, personal emails, real chat logs, customer data, or proprietary project
text. Rewrite any example based on real work as a synthetic example that cannot
identify a person or organization.

See the [dataset research notes](docs/dataset-research.md) and
[contribution guide](CONTRIBUTING.md) for details.

## Contributing

You can report Korean that still sounds translated, propose a recurring
AI-writing pattern, request a new use case, or fix an installation or
documentation problem. Contributions are welcome in Korean or English.

Do not submit real resumes, emails, chats, or customer data. Recreate the same
writing problem as a synthetic example. See the [contribution guide](CONTRIBUTING.md)
for the workflow and pull request criteria, or choose an
[issue form](https://github.com/evergreentree97/K-Humanizer/issues/new/choose)
to get started.

## License

MIT. See [LICENSE](LICENSE).
