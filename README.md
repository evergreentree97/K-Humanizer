# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)

[English](README.en.md)

K-Humanizer는 AI가 쓴 듯 딱딱한 한국어를 실제로 쓰는 말에 가깝게 다듬는 Agent Skill입니다. 이력서, 문서, 메신저, 메일, 제품 문구, 리뷰 코멘트처럼 문장이 놓이는 자리에 맞춰 고칩니다.

의미와 사실은 그대로 두고, 한국어답지 않은 번역투와 과한 격식, 뻔한 AI식 마무리를 줄이는 것이 목적입니다.

## 왜 만들었나

AI가 쓴 한국어에는 영어권 글과 다른 티가 납니다.

- `~를 통해`, `~에 대해`, `~에 있어서` 같은 번역투
- `중요성`, `방향성`, `측면`, `효과적` 같은 추상어 남용
- `결론적으로`, `시사하는 바가 크다` 같은 상투적인 마무리
- 영어식 쉼표 리듬
- 문서, 메일, 메신저가 다 같은 문장처럼 보이는 문제

K-Humanizer는 문장이 놓인 자리와 읽는 사람을 보고 필요한 만큼만 고칩니다.

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
$k-humanizer로 아래 메일을 의미는 유지한 채 한국어답게 다듬어줘:

[다듬을 한국어 텍스트]
```

## 예시

아래 `Before`는 일부러 영어 문장 구조가 비치는 LLM식 한국어로 두었습니다.

### 이력서

```text
Before:
저는 여러 프로젝트들을 통해 문제 해결 스킬들을 강화했고 의미 있는 결과들을 만들어냈습니다.

After:
여러 프로젝트를 진행하며 문제 해결 경험을 쌓고 의미 있는 결과를 냈습니다.
```

### 문서

```text
Before:
이 기능은 사용자 경험을 더 나은 방향으로 가져가는 데 있어서 중요한 역할을 수행할 것으로 기대됩니다.

After:
이 기능은 사용자가 더 편하게 작업하는 데 도움이 됩니다.
```

### 메신저

```text
Before:
제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.

After:
일정 확인해보고 공유드릴게요.
```

### 메일

```text
Before:
저는 미팅 일정에 관하여 당신에게 말씀드리기 위해 이 메일을 쓰고 있습니다.

After:
미팅 일정 때문에 메일드립니다.
```

### 실생활

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

### 코드 리뷰

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

## 스킬 구성

실제 스킬은 [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md)에 있습니다.

참고 문서:

- [사용 사례](skills/k-humanizer/references/use-cases.md)
- [AI 문체 패턴](skills/k-humanizer/references/patterns.md)
- [평가 루브릭](skills/k-humanizer/references/evaluation.md)

## 기여

익명화된 한국어 예시, 더 나은 패턴 설명, 평가 리포트, 문서 개선을 환영합니다.

다만 실제 이력서, 개인 메일, 고객 데이터, 내부 프로젝트 등의 문구는 올리지 말아 주세요. 실제 사례를 바탕으로 하더라도 반드시 합성 예시로 바꿔야 합니다.

기여 안내: [CONTRIBUTING.md](CONTRIBUTING.md)

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
