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

글을 어디에 쓰고 누가 읽는지 먼저 살핍니다. 어색한 표현은 앞뒤 문장과 함께
읽고 뜻을 파악한 뒤 고칩니다. 이미 자연스러운 문장은 그대로 둡니다.
사실과 수치, 누가 한 일인지, 어떤 조건이 붙는지, 무엇을 확인했는지도
원문대로 전합니다.

```text
Before: 고객 문의 분류 기준을 다시 정리하는 작업을 통해 주간 평균 처리 시간을 18시간에서 11시간으로 개선했습니다.
After:  고객 문의 분류 기준을 다시 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

`다시 정리하는 작업을 통해`를 `다시 정리해`로 줄였습니다. 한 일과 결과는 그대로입니다.

## 이런 분에게 맞습니다

- 한국어가 모국어는 아니지만 한국 사용자를 위한 제품 문구, 메일, 문서를 써야 하는 분
- AI로 작성한 이력서나 경력 문장이 딱딱하고 과장되어 보이는 분
- 메신저, 메일, 제품 화면마다 어울리는 말투를 구분하고 싶은 분
- 지원 동기나 공개 글에서 과장 없이 경험과 수치를 전달하고 싶은 분
- 문장을 다듬는 동안 사실, 수치, 전문용어가 바뀌지 않기를 원하는 분

## 12만 개 응답과 7,500번의 수정에서 나온 한국어 다듬기 노하우

AI가 쓴 한국어는 문법이 맞아도 어색할 때가 많습니다. 영어식 어순이 남아 있고
말투는 상황보다 딱딱합니다. 추상적인 단어가 많아 정작 무엇을 했는지도 잘
보이지 않습니다.

이 저장소에 공개한 합성 예시 220개와는 별개로, 12만 개가 넘는 한국어 응답을
검토하면서 7,500번 이상 표현을 직접 고쳤습니다. 같은 표현도 문맥에 따라
자연스럽기도 하고 어색하기도 했습니다. 이 과정에서 어떤 표현을 언제, 어떻게
바꿔야 하는지 정리해 K-Humanizer에 담았습니다.

K-Humanizer는 번역투와 뻔한 AI식 표현을 덜어내면서 사실, 수치, 전문용어와
작성자의 말투는 그대로 유지합니다. 이력서, 지원서, 메일, 메신저, 제품 문구,
공개 글처럼 용도가 달라지면 말투와 문장 길이도 그에 맞게 조정합니다.

`상담사를 통해서만 접수할 수 있습니다`에서는 상담사가 꼭 거쳐야 할 접수 창구입니다.
이처럼 같은 표현이라도 문장 속에서 하는 일에 따라 다듬습니다. 개발자가 평소 쓰는
`race condition`처럼 독자에게 익숙한 용어는 영어로 쓸 수 있습니다.

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

공개 글이라면 수치가 가리키는 범위와 과장 여부도 함께 확인할 수 있습니다.

```text
$k-humanizer로 아래 공개 글을 자연스럽게 다듬어줘.
사실과 수치는 그대로 두고 클릭을 유도하는 표현과 과장된 동사만 고쳐줘.

[공개할 글]
```

## 무엇을 바꾸고 무엇을 지키나

| 확인하는 내용 | 처리 방식 |
|---|---|
| 영어식 어순과 번역투 | 한국어에서 자연스러운 주어, 목적어, 서술어 순서로 조정 |
| 추상어와 긴 명사 표현 | 원문에 있는 행동과 결과를 직접 서술 |
| 메신저, 메일, 문서, 제품 화면, 공개 글의 말투 | 읽는 사람과 채널에 맞게 격식과 문장 길이를 조정 |
| 사실, 수치, 이름, 출처, 전문용어 | 원문 그대로 유지 |
| 담당 범위와 완료 여부, 불확실성 | 원문이 밝힌 책임과 확인된 범위를 유지 |
| 부정, 예외, 적용 조건 | 문장을 줄여도 독자의 해석이 달라지지 않도록 유지 |
| 근거 없는 성과나 감정 | 새로 만들지 않음 |
| 이미 자연스러운 문장 | 유지하거나 필요한 부분만 최소 수정 |

편집 범위는 요청과 원문의 상태에 따라 정합니다. 어색한 버튼 문구는 통째로
고칠 수 있고, 자연스러운 문단은 일부 표현만 손봐도 충분합니다. 경험의 순서나
내용을 바꾸는 작업은 따로 요청해 주세요.

## 사용 예시

### 이력서

```text
Before:
저는 고객 문의 분류 기준을 다시 정리하는 작업을 통해 주간 평균 처리 시간을 18시간에서 11시간으로 개선했습니다.

After:
고객 문의 분류 기준을 다시 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

### 제품 문구

```text
Before: 이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.
After:  업로드한 문서와 처리 상태를 보여줍니다.
```

### 메신저

```text
Before: 제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.
After:  일정 확인해 보고 공유드릴게요.
```

### 일상 문장

```text
Before: 현재 비가 오고 있는 상황이므로 우산을 챙기는 것이 좋을 것으로 보입니다.
After:  비 와서 우산 챙기는 게 좋겠어.
```

### 공개 글

```text
Before: 12만 개가 넘는 한국어 응답을 훑고 7,500번 이상 표현을 직접 고쳐 압도적인 노하우를 완성했습니다.
After:  12만 개가 넘는 한국어 응답을 검토하면서 7,500번 이상 표현을 직접 고쳤습니다.
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

v0 골든셋은 실제 개인정보나 사내 자료를 포함하지 않은 합성 예시 220개로
구성했습니다.

- 이력서 90개, 이 중 직무별 평가 40개
- 지원 동기 10개
- 일상 20개
- 메신저 20개
- 메일 20개
- 문서 20개
- 제품과 UI 문구 10개
- 공개 글과 소셜 게시물 10개
- 대화 10개
- 코드 리뷰 10개

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
python3 scripts/validate_model_baseline.py \
  evals/reports/2026-08-25/model-baseline.jsonl
```

- [현재 v0 데이터셋 무결성 리포트](evals/reports/2026-08-25-fixture-baseline.md)
- [2026년 8월 25일 모델 출력 평가](evals/reports/2026-08-25/model-baseline.md)
- [최초 200개 기준 기록](evals/reports/2026-08-17-fixture-baseline.md)
- [평가 계획과 v1.0 통과 기준](docs/validation-plan.md)

2026년 8월 25일 평가에서는 `gpt-5.4`로 출력 220개를 생성하고 별도 Claude Opus
세션에서 채점했습니다.
다섯 항목 평균은 4.765점, 의미 보존은 4.800점이었고 치명적인 사실 변경은
발견되지 않았습니다. 이는 합성 예시를 한 채점 모델이 평가한 결과이며 사람의 검수를
대신하지는 않습니다. 낮은 점수, 실패 사례, 공개 평가 기준과 점수가 어긋난 사례도
전체 평가 리포트에 함께 공개합니다. 이 점수는 당시 스킬 버전에 해당합니다.
이번 편집 원칙을 확인할 [합성 사례](skills/k-humanizer/references/evaluation.md#context-and-scope-review-cases)는 별도로 정리했습니다.

이 저장소에는 제3자 데이터셋을 포함하지 않습니다. 실제 이력서, 개인 메일,
대화 기록, 고객 데이터와 내부 프로젝트 문구도 공개 예시로 받지 않습니다. 실제
사례를 바탕으로 기여할 때는 개인과 조직을 식별할 수 없도록 합성 예시로 바꿔 주세요.

자세한 내용은 [데이터셋 조사 기록](docs/dataset-research.md)과
[기여 안내](CONTRIBUTING.md)를 참고하세요.

## 기여하기

한국어가 여전히 번역투로 들리는 사례, 반복해서 보이는 AI 문체, 새 사용 사례,
설치나 문서 문제를 제보할 수 있습니다. 한국어나 영어로 작성해도 됩니다.

실제 이력서, 메일, 대화, 고객 자료는 올리지 말고 같은 문제를 보여주는 합성
예시로 바꿔 주세요. 참여 방법과 PR 기준은 [기여 안내](CONTRIBUTING.md)에
정리했습니다. 바로 제보하려면
[Issue 양식](https://github.com/evergreentree97/K-Humanizer/issues/new/choose)을
이용해 주세요.

## 라이선스

MIT. 자세한 내용은 [LICENSE](LICENSE)를 참고하세요.
