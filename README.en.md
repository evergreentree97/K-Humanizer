# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)

[한국어](README.md)

K-Humanizer is an agent skill for making stiff Korean sound closer to writing people actually use. It adapts to everyday conversation, personal writing, resumes, documents, messages, emails, product copy, and dialogue.

It is not an AI detector bypass tool. The goal is straightforward: preserve meaning and facts while removing translationese, stiff formality, and generic AI-style phrasing.

## Why It Exists

AI-written Korean has its own tells:

- Translationese such as `~를 통해`, `~에 대해`, `~에 있어서`
- Abstract filler such as `중요성`, `방향성`, `측면`, `효과적`
- Generic closers such as `결론적으로`, `시사하는 바가 크다`
- English-like comma rhythm
- Sentences that look the same in documents, emails, and chat messages

K-Humanizer edits only as much as the reader and context require.

## Core Method

"Make it natural" is too vague to remove English-shaped Korean and AI-style
phrasing consistently. K-Humanizer first identifies the condition inside the
sentence, then applies the matching rewrite.

| When X is true | Use Y |
|---|---|
| `~를 통해` only marks a means | `~로`, `~에서`, or a direct verb |
| `좋은 경험` or `의미 있는 변화` has no concrete content | Use only the event or change already present in the source; do not invent one |
| Everyday writing uses ceremony such as `~할 수 있도록 하겠습니다` | Match the ordinary wording to the relationship and situation |
| The source contains names, numbers, sources, or domain terms | Preserve the exact content and uncertainty |
| Insider terminology is unfamiliar to a general reader | Keep the exact meaning and explain it in reader-friendly words |
| A screen introduction repeats the title and visible content | State only the items and states the reader can inspect |
| Personal writing has a distinct emotion or voice | Fix only the awkward parts and preserve the writer's voice |
| The sentence already sounds natural | Keep it or edit only the necessary span |

This is not blind replacement. A phrase stays when its literal function matters,
and every rule includes its condition and exception.

## Install

Install from GitHub:

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

Test locally:

```bash
npx skills add . --skill k-humanizer --full-depth
```

Example prompt:

```text
Use $k-humanizer to make this Korean email more natural while preserving meaning:

[paste Korean text]
```

## Examples

The `Before` text intentionally uses English-to-Korean translationese that sounds like LLM output.

### Resume

```text
Before:
저는 고객 문의 분류 체계 고도화를 통해 주간 평균 처리 시간을 18시간에서 11시간으로 크게 개선했습니다.

After:
고객 문의 분류 기준을 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

If the source only says that it produced a "meaningful result," the skill does
not manufacture a polished achievement. It asks for or flags the missing
problem, action, ownership, and result, and omits unsupported claims.

#### Role-aware resumes

The same experience should lead with different evidence depending on what the
target role evaluates. K-Humanizer changes the order and explanation of verified
evidence without copying the posting or changing the facts.

| Role | Lead with |
|---|---|
| Operations | Repeated work, exceptions, handoffs, deadlines, and volume |
| Service/product planning | User or business problem, priority, scope decision, and validation state |
| QA | Test scope, reproduction condition, severity, release decision, and fix verification |
| Design | User task, information hierarchy, constraint, design decision, and usability evidence |
| Marketing/content | Audience, channel, hypothesis, message, and measurement conditions |
| Customer service/sales | Customer problem, policy, response, follow-up, and confirmed outcome |
| Research/data | Question, method, sample, limitation, finding, and supported decision |
| People operations/education | Learner or team need, program decision, delivery scope, and follow-up |

See [role-aware resume rules](skills/k-humanizer/references/resume-roles.md) for the detailed routing guide.

### Document

```text
Before:
이 기능은 사용자 경험을 더 나은 방향으로 가져가는 데 있어서 중요한 역할을 수행할 것으로 기대됩니다.

After:
이 기능은 사용자가 더 편하게 작업하는 데 도움이 됩니다.
```

### Messenger

```text
Before:
제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.

After:
일정 확인해보고 공유드릴게요.
```

### Email

```text
Before:
저는 미팅 일정에 관하여 당신에게 말씀드리기 위해 이 메일을 쓰고 있습니다.

After:
미팅 일정 때문에 메일드립니다.
```

### Product Copy

```text
Before:
이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.

After:
업로드한 문서와 처리 상태를 보여줍니다.
```

### Everyday

```text
Before:
제가 오늘 저녁 식사에 필요한 재료들을 구매하는 역할을 수행할 수 있도록 하겠습니다.

After:
저녁 재료는 내가 사갈게.

Before:
당신이 괜찮다면 저는 내일 오전 시간대에 병원을 방문하는 일정을 진행하고자 합니다.

After:
괜찮으면 나 내일 오전에 병원 다녀올게.

Before:
현재 비가 오고 있는 상황이므로 우산을 챙기는 것이 좋을 것으로 보입니다.

After:
비 와서 우산 챙기는 게 좋겠어.
```

## Skill Files

The portable skill lives in [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md).

References:

- [Use cases](skills/k-humanizer/references/use-cases.md)
- [Resume and career-document rules](skills/k-humanizer/references/resume.md)
- [Role-aware resume rules](skills/k-humanizer/references/resume-roles.md)
- [Pattern checklist](skills/k-humanizer/references/patterns.md)
- [Evaluation rubric](skills/k-humanizer/references/evaluation.md)

## Validation

The v0 fixture contains 200 synthetic, anonymized examples:

- 20 personal/everyday examples
- 20 messenger examples
- 20 email examples
- 20 document examples
- 90 resume examples, including 40 role-specific cases
- 10 product/UI copy examples
- 10 dialogue examples
- 10 code review comment examples

Run:

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

Fixture: [evals/fixtures/golden_set.v0.jsonl](evals/fixtures/golden_set.v0.jsonl)

Evaluation plan: [docs/validation-plan.md](docs/validation-plan.md)

## Dataset Policy

This repository does not vendor third-party datasets. Public datasets are documented as research references only, unless their license and attribution requirements are clear.

Research notes: [docs/dataset-research.md](docs/dataset-research.md)

## Contributing

Anonymized Korean examples, better pattern descriptions, evaluation reports, and documentation fixes are welcome.

Do not submit private resumes, personal emails, real chat logs, customer data, or proprietary project text. If an example came from real work, rewrite it as a synthetic example first.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
