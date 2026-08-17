# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)
[![skills.sh](https://skills.sh/b/evergreentree97/K-Humanizer)](https://skills.sh/evergreentree97/K-Humanizer)

[English](README.en.md)

K-Humanizer는 LLM이 만든 한국어를 한국 독자에게 자연스럽게 다듬는 Agent
Skill입니다. Cursor, Claude, Codex에서 사용할 수 있습니다.

사실, 수치, 고유명사와 전문용어는 건드리지 않습니다. 원문이 조심스럽게 말한
내용을 단정하지 않고, 작성자의 말투도 가능한 한 지킵니다. 이미 자연스러운
문장은 억지로 고치지 않습니다.

```text
Before: 고객 문의 분류 체계 고도화를 통해 주간 평균 처리 시간을 18시간에서 11시간으로 크게 개선했습니다.
After:  고객 문의 분류 기준을 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

두 문장의 사실은 같습니다. 두 번째 문장은 추상적인 표현을 덜어내고, 무엇을 해서
처리 시간이 줄었는지 바로 보여 줍니다.

## 이런 분에게 맞습니다

- 한국어가 모국어는 아니지만 한국 사용자를 위한 제품 문구, 메일, 문서를 써야 하는 분
- AI로 작성한 이력서나 경력 문장이 딱딱하고 과장되어 보이는 분
- 메신저, 메일, 제품 화면마다 어울리는 말투를 구분하고 싶은 분
- 문장을 다듬는 동안 사실, 수치, 전문용어가 바뀌지 않기를 원하는 분

## 한 달 동안 데이터를 정제하며 모은 규칙

한 달 동안 매일 한국어 텍스트 데이터를 정제했습니다. 문법은 맞지만 영어
어순이 남은 문장, 필요 이상으로 격식을 차린 표현, 구체적인 행동을 가리는
추상어가 계속 보였습니다. 그때 쌓은 메모에서 반복되는 수정 방식을 추려 적용
조건과 예외를 정리했습니다.

단어를 일괄 치환하지는 않습니다. 같은 `~를 통해`라도 실제 경로나 중개 과정을
뜻하면 남기고, 단순히 문장을 길게 만드는 경우에만 직접적인 표현으로 바꿉니다.

## 바로 써보기

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

설치한 뒤, 글의 용도와 읽는 사람을 함께 알려 주세요.

```text
$k-humanizer로 아래 한국어를 제품 안내 문구에 맞게 다듬어줘.
읽는 사람은 한국 사용자야. 사실, 수치, 고유명사와 제품 용어는 바꾸지 말고
번역투와 과한 격식만 고쳐줘.

[다듬을 글]
```

이력서라면 이렇게 요청할 수 있습니다.

```text
$k-humanizer로 아래 이력서의 사실, 수치, 직무 용어는 그대로 두고
번역투와 뻔한 AI식 성과 표현만 자연스럽게 다듬어줘.

[이력서]
```

## 무엇을 바꾸고 무엇을 지키나

| 확인하는 내용 | 처리 방식 |
|---|---|
| 영어식 어순과 번역투 | 한국어에서 자연스러운 주어, 목적어, 서술어 순서로 조정 |
| 추상어와 긴 명사 표현 | 원문에 있는 행동과 결과를 직접 서술 |
| 메신저, 메일, 문서, 제품 화면의 말투 | 읽는 사람과 채널에 맞게 격식과 문장 길이를 조정 |
| 사실, 수치, 이름, 출처, 전문용어 | 원문 그대로 유지 |
| 담당 범위와 완료 여부, 불확실성 | 원문보다 강하게 만들지 않음 |
| 근거 없는 성과나 감정 | 새로 만들지 않음 |
| 이미 자연스러운 문장 | 유지하거나 필요한 부분만 최소 수정 |

K-Humanizer는 AI 탐지기 우회를 보장하지 않습니다. 이력서 성과를 지어내거나
원문보다 더 확신에 찬 문장으로 바꾸는 도구도 아닙니다.

## 사용 예시

### 이력서

```text
Before:
저는 고객 문의 분류 체계 고도화를 통해 주간 평균 처리 시간을 18시간에서 11시간으로 크게 개선했습니다.

After:
고객 문의 분류 기준을 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

### 제품 문구

```text
Before: 이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.
After:  업로드한 문서와 처리 상태를 보여줍니다.
```

### 메신저

```text
Before: 제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.
After:  일정 확인해보고 공유드릴게요.
```

### 일상 문장

```text
Before: 현재 비가 오고 있는 상황이므로 우산을 챙기는 것이 좋을 것으로 보입니다.
After:  비 와서 우산 챙기는 게 좋겠어.
```

자세한 예시는 [사용 사례](skills/k-humanizer/references/use-cases.md)에서 볼 수
있습니다.

## 이력서와 경력 문서

완성된 문장을 다듬는 작업과, 메모에서 새 문장을 만드는 작업을 구분합니다.
기본 동작은 기존 문장의 사실과 직무 용어를 지키면서 어색한 표현만 고치는
것입니다. 메모를 경력 문장으로 구성하거나 채용 공고에 맞춰 순서를 바꾸는 일은
사용자가 요청했을 때만 합니다.

| 가지고 있는 자료 | 스킬이 하는 일 |
|---|---|
| 완성된 경력 문장 | 사실과 주장 강도를 유지하면서 번역투와 AI투를 고침 |
| 이력서 전체 | 직무 용어와 개인 말투를 살리면서 반복되는 문체 문제를 정리 |
| 업무 메모나 작업 목록 | 요청한 경우에만 확인된 내용으로 경력 문장을 구성 |
| 채용 공고와 기존 이력서 | 요청한 경우에만 관련 있는 기존 경험의 순서를 조정 |

직군마다 실제로 쓰는 용어는 그대로 살립니다. 운영의 예외 처리, 기획의 범위
결정, QA의 재현 조건, 디자인의 설계 판단처럼 업무를 설명하는 핵심 정보는
두루뭉술한 성과 문구로 바꾸지 않습니다.

- [이력서와 경력 문서 규칙](skills/k-humanizer/references/resume.md)
- [이력서 구성 흐름](skills/k-humanizer/references/resume-workflow.md)
- [직무별 이력서 규칙](skills/k-humanizer/references/resume-roles.md)

## 스킬 구성

실제 스킬 파일은 [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md)에
있습니다.

- [사용 사례](skills/k-humanizer/references/use-cases.md)
- [AI 문체 패턴](skills/k-humanizer/references/patterns.md)
- [평가 루브릭](skills/k-humanizer/references/evaluation.md)

로컬 저장소에서 현재 구성을 시험하려면 다음 명령을 사용합니다.

```bash
npx skills add . --skill k-humanizer --full-depth
```

## 검증과 데이터

v0 골든셋은 합성하고 익명화한 예시 200개로 구성했습니다.

- 이력서 90개, 이 중 직무별 평가 40개
- 일상 20개
- 메신저 20개
- 메일 20개
- 문서 20개
- 제품과 UI 문구 10개
- 대화 10개
- 코드 리뷰 10개

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

- [v0 데이터셋 무결성 리포트](evals/reports/2026-08-17-fixture-baseline.md)
- [평가 계획과 v1.0 통과 기준](docs/validation-plan.md)

현재 공개 리포트는 데이터 구조, 도메인 분포, 중복 ID, 필수 필드와 공개 저장소
위생을 검증합니다. 실제 출력의 자연스러움과 의미 보존 점수는 별도의 수동 평가
리포트로 공개할 예정입니다.

이 저장소에는 제3자 데이터셋을 포함하지 않습니다. 실제 이력서, 개인 메일,
대화 기록, 고객 데이터와 내부 프로젝트 문구도 공개 예시로 받지 않습니다. 실제
사례를 바탕으로 기여할 때는 개인과 조직을 식별할 수 없도록 합성 예시로 바꿔 주세요.

자세한 내용은 [데이터셋 조사 기록](docs/dataset-research.md)과
[기여 안내](CONTRIBUTING.md)를 참고하세요.

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
