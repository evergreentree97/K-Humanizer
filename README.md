# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](docs/open-source-plan.md)

K-Humanizer is a Korean writing polish skill for AI agents. It makes Korean text sound natural for the actual channel: resume, document, messenger, email, product copy, review comment, or dialogue.

It is **not** an AI detector bypass tool. The goal is better Korean: less translationese, less stiff chatbot rhythm, fewer generic closers, and a tone that fits the reader.

## 한국어 요약

K-Humanizer는 AI가 쓴 듯 딱딱한 한국어를 더 자연스럽게 다듬는 Agent Skill입니다.

- 의미, 사실, 숫자, 고유명사는 보존합니다.
- 이력서, 문서, 메신저, 메일처럼 실제 사용 맥락에 맞춰 톤을 조정합니다.
- `~를 통해`, `~에 대해`, `~에 있어서`, `결론적으로`, `시사하는 바가 크다` 같은 한국어 AI 문체 신호를 줄입니다.
- 과한 윤문, 허위 성과 추가, 탐지기 우회 목적의 재작성은 지향하지 않습니다.

## Why This Exists

Korean AI output has different failure modes from English AI output:

- Translationese: `~를 통해`, `~에 대해`, `~에 있어서`
- Stiff abstract nouns: `중요성`, `방향성`, `측면`, `효과적`
- Generic closers: `결론적으로`, `시사하는 바가 크다`
- English-like comma rhythm
- Tone mismatch between document Korean, email Korean, and messenger Korean

K-Humanizer focuses on Korean-native editing judgment rather than generic paraphrasing.

## Install

Install the skill from GitHub:

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

Install locally while developing:

```bash
npx skills add . --skill k-humanizer --full-depth
```

Then ask your agent naturally:

```text
Use $k-humanizer to make this Korean email more natural while preserving meaning:

[paste text]
```

## Common Use Cases

### Resume and Profile

Turns inflated, generic self-description into credible achievement-oriented Korean.

```text
Before:
다양한 프로젝트를 통해 문제 해결 역량을 강화하고 의미 있는 성과를 창출했습니다.

After:
여러 프로젝트에서 요구사항을 정리하고 병목을 해결하며 실제 배포까지 이어지는 경험을 쌓았습니다.
```

### Documents and Reports

Makes business writing clearer without making it casual.

```text
Before:
해당 기능은 사용자 경험 개선에 있어서 중요한 역할을 할 것으로 기대됩니다.

After:
이 기능은 사용자가 작업을 더 빨리 끝내는 데 도움이 됩니다.
```

### Messenger and Casual Korean

Shortens stiff assistant-like Korean into natural chat wording.

```text
Before:
해당 일정에 대해서 확인 후 공유드릴 수 있도록 하겠습니다.

After:
일정 확인해보고 공유드릴게요.
```

### Email

Keeps politeness but removes unnecessary ceremony.

```text
Before:
다름이 아니오라 미팅 일정과 관련하여 말씀드리고자 연락드립니다.

After:
미팅 일정 때문에 연락드립니다.
```

### Dialogue

Preserves speaker voice and emotional pacing instead of flattening the line into generic polite Korean.

## What The Skill Does

The actual portable skill lives in [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md).

It uses a small workflow:

1. Detect the writing context.
2. Check Korean AI-tell patterns.
3. Rewrite surgically.
4. Self-check meaning, tone, and over-editing.

Detailed references:

- [Use cases](skills/k-humanizer/references/use-cases.md)
- [Pattern checklist](skills/k-humanizer/references/patterns.md)
- [Evaluation rubric](skills/k-humanizer/references/evaluation.md)

## Validation

The v0 fixture contains 80 synthetic, anonymized examples:

- 20 resume/profile examples
- 20 document/report examples
- 20 messenger/casual examples
- 20 email examples

Validate the fixture:

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

Current fixture: [evals/fixtures/golden_set.v0.jsonl](evals/fixtures/golden_set.v0.jsonl)

Evaluation plan: [docs/validation-plan.md](docs/validation-plan.md)

## Dataset Research

This repository does not vendor third-party datasets. Public datasets are used only as research references unless their license and attribution requirements are confirmed.

Potential references:

- `coastral/korean-writing-style-instruct` on Hugging Face: Korean writing-style synthetic data, Apache-2.0.
- `jojo0217/korean_safe_conversation` on Hugging Face: Korean daily conversation data, Apache-2.0.
- KatFish/KatFishNet: Korean LLM-generated text benchmark and linguistic features for Korean AI-tell detection.
- `DaleSeo/korean-skills`: existing Korean humanizer, grammar checker, and style guide skills.
- `epoko77-ai/im-not-ai`: existing Korean AI-tell rewriting harness.

Research notes: [docs/dataset-research.md](docs/dataset-research.md)

## Project Structure

```text
K-Humanizer/
├── .github/workflows/validate.yml
├── docs/
├── evals/
│   ├── datasets/        # gitignored local datasets
│   ├── fixtures/        # public synthetic fixtures
│   └── reports/         # generated reports
├── scripts/
└── skills/
    └── k-humanizer/
```

## Roadmap

- v0.1: Portable `SKILL.md`, public README, MIT license, CI, and 80-item v0 fixture.
- v0.2: Manual evaluation report over the v0 golden set.
- v0.3: Lightweight metric script for pattern counts and change-rate checks.
- v0.4: More examples for resume, email, docs, messenger, product copy, review comments, and dialogue.
- v1.0: Stable public release with documented evaluation results.

Detailed plan: [docs/open-source-plan.md](docs/open-source-plan.md)

## Contributing

Contributions are welcome, especially:

- More anonymized Korean examples
- Better rewrite rules for a specific channel
- Evaluation reports
- Documentation improvements

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting examples. Do not submit private resumes, private emails, real chat logs, customer data, or proprietary project text.

## License

MIT. See [LICENSE](LICENSE).
