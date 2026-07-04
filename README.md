# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)

[English](README.en.md)

K-Humanizer는 AI가 쓴 듯 딱딱한 한국어를 자연스럽게 다듬는 Agent Skill입니다. 이력서, 문서, 메신저, 메일, 제품 문구, 리뷰 코멘트처럼 실제로 쓰는 글의 톤을 맞추는 데 초점을 둡니다.

탐지기 우회를 목표로 하지 않습니다. 의미와 사실은 그대로 두고, 한국어답지 않은 번역투와 과한 격식, 뻔한 AI식 마무리를 줄이는 도구입니다.

## 왜 만들었나

AI가 쓴 한국어에는 영어권 글과 다른 티가 납니다.

- `~를 통해`, `~에 대해`, `~에 있어서` 같은 번역투
- `중요성`, `방향성`, `측면`, `효과적` 같은 추상어 남용
- `결론적으로`, `시사하는 바가 크다` 같은 상투적인 마무리
- 영어식 쉼표 리듬
- 문서, 메일, 메신저를 구분하지 못하는 톤

K-Humanizer는 이런 문장을 무작정 바꾸지 않고, 글이 놓일 자리와 읽는 사람을 먼저 봅니다.

## 설치

GitHub에서 설치:

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

로컬에서 테스트:

```bash
npx skills add . --skill k-humanizer --full-depth
```

사용 예:

```text
Use $k-humanizer to make this Korean email more natural while preserving meaning:

[다듬을 한국어 텍스트]
```

## 예시

### 이력서

```text
Before:
다양한 프로젝트를 통해 문제 해결 역량을 강화하고 의미 있는 성과를 창출했습니다.

After:
여러 프로젝트에서 요구사항을 정리하고 병목을 해결하며 실제 배포까지 이어지는 경험을 쌓았습니다.
```

### 문서

```text
Before:
해당 기능은 사용자 경험 개선에 있어서 중요한 역할을 할 것으로 기대됩니다.

After:
이 기능은 사용자가 작업을 더 빨리 끝내는 데 도움이 됩니다.
```

### 메신저

```text
Before:
해당 일정에 대해서 확인 후 공유드릴 수 있도록 하겠습니다.

After:
일정 확인해보고 공유드릴게요.
```

### 메일

```text
Before:
다름이 아니오라 미팅 일정과 관련하여 말씀드리고자 연락드립니다.

After:
미팅 일정 때문에 연락드립니다.
```

## 스킬 구성

실제 스킬은 [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md)에 있습니다.

참고 문서:

- [사용 사례](skills/k-humanizer/references/use-cases.md)
- [AI 문체 패턴](skills/k-humanizer/references/patterns.md)
- [평가 루브릭](skills/k-humanizer/references/evaluation.md)

## 검증

v0 검증셋은 개인정보가 없는 합성 예시 80개로 구성했습니다.

- 이력서 20개
- 문서 20개
- 메신저 20개
- 메일 20개

검증:

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

검증셋: [evals/fixtures/golden_set.v0.jsonl](evals/fixtures/golden_set.v0.jsonl)

평가 계획: [docs/validation-plan.md](docs/validation-plan.md)

## 데이터셋 원칙

이 저장소는 외부 데이터셋을 포함하지 않습니다. Hugging Face나 공개 코퍼스는 조사 참고용으로만 기록하고, 라이선스와 출처가 명확한 경우에만 평가에 사용합니다.

조사 노트: [docs/dataset-research.md](docs/dataset-research.md)

## 기여

익명화된 한국어 예시, 더 나은 패턴 설명, 평가 리포트, 문서 개선을 환영합니다.

다만 실제 이력서, 개인 메일, 실사용 채팅 로그, 고객 데이터, 내부 프로젝트 문구는 올리지 말아 주세요. 실제 사례를 바탕으로 하더라도 반드시 합성 예시로 바꿔야 합니다.

기여 안내: [CONTRIBUTING.md](CONTRIBUTING.md)

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
