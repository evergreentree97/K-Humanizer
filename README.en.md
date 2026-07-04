# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)

[한국어](README.md)

K-Humanizer is an agent skill for polishing Korean writing. It helps AI-generated Korean sound natural in real contexts: resumes, documents, messenger replies, emails, product copy, review comments, and dialogue.

It is not an AI detector bypass tool. The goal is straightforward: preserve meaning and facts while removing translationese, stiff formality, and generic AI-style phrasing.

## Why It Exists

AI-written Korean has its own tells:

- Translationese such as `~를 통해`, `~에 대해`, `~에 있어서`
- Abstract filler such as `중요성`, `방향성`, `측면`, `효과적`
- Generic closers such as `결론적으로`, `시사하는 바가 크다`
- English-like comma rhythm
- Tone that fails to distinguish documents, emails, and chat messages

K-Humanizer edits with the reader and channel in mind.

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

### Resume

```text
Before:
다양한 프로젝트를 통해 문제 해결 역량을 강화하고 의미 있는 성과를 창출했습니다.

After:
여러 프로젝트에서 요구사항을 정리하고 병목을 해결하며 실제 배포까지 이어지는 경험을 쌓았습니다.
```

### Document

```text
Before:
해당 기능은 사용자 경험 개선에 있어서 중요한 역할을 할 것으로 기대됩니다.

After:
이 기능은 사용자가 작업을 더 빨리 끝내는 데 도움이 됩니다.
```

### Messenger

```text
Before:
해당 일정에 대해서 확인 후 공유드릴 수 있도록 하겠습니다.

After:
일정 확인해보고 공유드릴게요.
```

### Email

```text
Before:
다름이 아니오라 미팅 일정과 관련하여 말씀드리고자 연락드립니다.

After:
미팅 일정 때문에 연락드립니다.
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
