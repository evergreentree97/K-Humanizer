# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)

[English](README.en.md)

K-Humanizer는 AI가 쓴 듯 딱딱한 한국어를 실제로 쓰는 말에 가깝게 다듬는 Agent Skill입니다. 일상 대화, 개인 글, 이력서, 문서, 메신저, 메일, 제품 문구와 창작 대사처럼 문장이 놓이는 자리에 맞춰 고칩니다.

의미와 사실은 그대로 두고, 한국어답지 않은 번역투와 과한 격식, 뻔한 AI식 마무리를 줄이는 것이 목적입니다.

## 왜 만들었나

AI가 쓴 한국어에는 영어권 글과 다른 티가 납니다.

- `~를 통해`, `~에 대해`, `~에 있어서` 같은 번역투
- `중요성`, `방향성`, `측면`, `효과적` 같은 추상어 남용
- `결론적으로`, `시사하는 바가 크다` 같은 상투적인 마무리
- 영어식 쉼표 리듬
- 문서, 메일, 메신저가 다 같은 문장처럼 보이는 문제

K-Humanizer는 문장이 놓인 자리와 읽는 사람을 보고 필요한 만큼만 고칩니다.

## 핵심 방식

"자연스럽게 써라"라는 지시만으로는 영어식 어순과 AI 문체가 안정적으로
사라지지 않습니다. K-Humanizer는 문장 안의 조건을 먼저 확인하고 그 조건에
맞는 표현을 고릅니다.

| X일 때 | Y를 사용 |
|---|---|
| `~를 통해`가 단순한 수단을 뜻할 때 | `~로`, `~에서`, 또는 직접 동사 |
| `좋은 경험`, `의미 있는 변화`만 있고 내용이 없을 때 | 원문에 있는 사건이나 변화를 구체화. 없으면 만들지 않음 |
| 일상 문장에 `~할 수 있도록 하겠습니다` 같은 격식이 붙을 때 | 관계와 상황에 맞는 평소 말로 조정 |
| 이름, 수치, 출처와 전문용어가 있을 때 | 정확한 내용과 불확실성은 그대로 유지 |
| 전문 분야의 내부 용어가 일반 독자에게 낯설 때 | 정확한 뜻은 유지하고 독자가 이해할 말로 풀어 씀 |
| 화면 소개가 제목과 보이는 내용을 반복할 때 | 독자가 확인할 항목과 상태만 서술 |
| 개인 글에 감정이나 말투가 살아 있을 때 | 어색한 부분만 고치고 그 사람의 목소리는 유지 |
| 이미 자연스러운 문장일 때 | 그대로 두거나 필요한 부분만 최소 수정 |

표는 무조건 치환하는 사전이 아닙니다. `~를 통해`가 실제 중개 과정이나 경로를
뜻하면 유지할 수 있습니다. 각 규칙에는 적용 조건과 예외가 함께 있습니다.

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
저는 고객 문의 분류 체계 고도화를 통해 주간 평균 처리 시간을 18시간에서 11시간으로 크게 개선했습니다.

After:
고객 문의 분류 기준을 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

원문이 `의미 있는 성과를 냈다`처럼 근거 없이 추상적이면 그럴듯한 성과를 새로
만들지 않습니다. 어떤 문제를 맡았고 무엇을 바꿨으며 어디까지 본인이 했는지
확인하거나, 근거가 없으면 해당 주장을 뺍니다.

#### 직무별 이력서

같은 경험도 지원 직무가 보는 판단 기준에 맞춰 앞에 둘 근거가 달라집니다. 공고의
단어를 복사하지 않고 확인된 경험의 순서와 설명만 바꿉니다.

| 직무 | 먼저 보여 줄 내용 |
|---|---|
| 운영 | 반복 업무, 예외, 인계, 마감과 처리량 |
| 서비스/제품 기획 | 사용자 또는 사업 문제, 우선순위, 범위 결정과 검증 상태 |
| QA | 테스트 범위, 재현 조건, 심각도, 출시 판단과 수정 확인 |
| 디자인 | 사용자 과업, 정보 구조, 제약, 설계 판단과 사용성 검증 |
| 마케팅/콘텐츠 | 대상, 채널, 가설, 메시지와 측정 조건 |
| 고객지원/영업 | 문의나 고객 문제, 정책, 대응, 후속 조치와 확인 결과 |
| 리서치/데이터 | 질문, 방법, 표본, 한계, 발견과 의사결정 지원 |
| 교육/조직 운영 | 참여자 문제, 프로그램 판단, 운영 범위와 후속 확인 |

직무별 세부 기준은 [직무별 이력서 규칙](skills/k-humanizer/references/resume-roles.md)에 있습니다.

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

### 제품 문구

```text
Before:
이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.

After:
업로드한 문서와 처리 상태를 보여줍니다.
```

### 일상

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

## 스킬 구성

실제 스킬은 [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md)에 있습니다.

참고 문서:

- [사용 사례](skills/k-humanizer/references/use-cases.md)
- [이력서와 경력 문서 규칙](skills/k-humanizer/references/resume.md)
- [직무별 이력서 규칙](skills/k-humanizer/references/resume-roles.md)
- [AI 문체 패턴](skills/k-humanizer/references/patterns.md)
- [평가 루브릭](skills/k-humanizer/references/evaluation.md)

## 검증

v0 골든셋은 합성하고 익명화한 예시 200개로 구성했습니다.

- 일상 20개
- 메신저 20개
- 메일 20개
- 문서 20개
- 이력서 90개, 이 중 직무별 평가 40개
- 제품/UI 문구 10개
- 대화 10개
- 코드 리뷰 10개

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

## 기여

익명화된 한국어 예시, 더 나은 패턴 설명, 평가 리포트, 문서 개선을 환영합니다.

다만 실제 이력서, 개인 메일, 고객 데이터, 내부 프로젝트 등의 문구는 올리지 말아 주세요. 실제 사례를 바탕으로 하더라도 반드시 합성 예시로 바꿔야 합니다.

기여 안내: [CONTRIBUTING.md](CONTRIBUTING.md)

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
