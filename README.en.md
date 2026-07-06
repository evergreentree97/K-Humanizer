# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)

[한국어](README.md)

K-Humanizer is an agent skill for making stiff Korean sound closer to writing people actually use. It edits Korean by context: resumes, documents, messenger replies, emails, product copy, review comments, and dialogue.

It is not an AI detector bypass tool. The goal is straightforward: preserve meaning and facts while removing translationese, stiff formality, and generic AI-style phrasing.

## Why It Exists

AI-written Korean has its own tells:

- Translationese such as `~를 통해`, `~에 대해`, `~에 있어서`
- Abstract filler such as `중요성`, `방향성`, `측면`, `효과적`
- Generic closers such as `결론적으로`, `시사하는 바가 크다`
- English-like comma rhythm
- Sentences that look the same in documents, emails, and chat messages

K-Humanizer edits only as much as the reader and context require.

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
저는 여러 프로젝트들을 통해 문제 해결 스킬들을 강화했고 의미 있는 결과들을 만들어냈습니다.

After:
여러 프로젝트를 진행하며 문제 해결 경험을 쌓고 의미 있는 결과를 냈습니다.
```

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

### Code Review

```text
Before:
해당 로직은 가독성 측면에서 개선의 여지가 있을 것으로 판단됩니다. 별도 함수로 분리하는 방향을 고려해볼 수 있을 것 같습니다.

After:
이 로직은 함수로 빼면 읽기 쉬울 것 같아요.

Before:
현재 구현은 예외 상황에 대한 처리가 충분하지 않은 상태로 보입니다. 실패 케이스를 고려한 방어 로직을 추가하는 것이 적절할 것 같습니다.

After:
실패 케이스 처리가 빠져 있어서 방어 로직을 추가해야 할 것 같아요.

Before:
이 변수명은 실제로 담고 있는 데이터의 의미를 명확하게 전달하지 못하고 있는 것으로 판단됩니다.

After:
이 변수명만 보면 어떤 값인지 바로 알기 어려워요.
```

## Skill Files

The portable skill lives in [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md).

References:

- [Use cases](skills/k-humanizer/references/use-cases.md)
- [Pattern checklist](skills/k-humanizer/references/patterns.md)
- [Evaluation rubric](skills/k-humanizer/references/evaluation.md)

## Validation

The v0 fixture contains 80 synthetic, anonymized examples:

- 20 resume examples
- 20 document examples
- 20 messenger examples
- 20 email examples

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
