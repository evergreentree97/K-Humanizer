# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)
[![skills.sh](https://skills.sh/b/evergreentree97/K-Humanizer)](https://skills.sh/evergreentree97/K-Humanizer)

[English](README.en.md)

K-Humanizer는 AI로 쓴 이력서, 메일, 제품 안내에서 번역한 듯 어색한 한국어를 다듬어 주는 Agent Skill입니다. Cursor, Claude, Codex에서 쓸 수 있습니다.

```text
수정 전  고객 문의 분류 기준을 다시 정리하는 작업을 통해 주간 평균 처리 시간을 18시간에서 11시간으로 개선했습니다.
수정 후  고객 문의 분류 기준을 다시 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

여기서는 `작업을 통해`를 빼도 한 일이 달라지지 않습니다. `이의 신청은 담당 상담사를 통해서만 접수할 수 있습니다`에서는 상담사를 거쳐야 한다는 뜻이 있으니 그대로 둡니다.

## 설치

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

글을 붙여 넣고 어디에 쓸지 알려 주세요. 예를 들어 동료에게 보낼 메일이라면 이렇게 부탁할 수 있습니다.

```text
$k-humanizer로 이 메일을 다듬어줘. 동료에게 보낼 거야.
일정과 부탁할 일은 그대로 두고, 딱딱한 표현만 고쳐줘.

[메일 붙여 넣기]
```

이력서를 붙여 넣으면 경험의 순서와 팀에서 쓰는 `race condition` 같은 용어는 그대로 두고 어색한 표현을 고칩니다. 업무 메모에서 문장을 새로 쓰거나 공고에 맞춰 경험 순서를 바꾸고 싶다면 그 작업도 요청해 주세요.

## 다른 예시

| 어디에 쓰는지 | 수정 전 | 수정 후 |
| --- | --- | --- |
| 제품 도움말 | 검토가 완료되지 않은 경우에도 임시 저장은 가능하나 제출은 불가합니다. | 검토가 끝나지 않아도 임시 저장은 할 수 있어요. 제출하려면 검토가 먼저 끝나야 해요. |
| 팀 메신저 | 해당 일정에 대해 확인한 이후에 공유하도록 하겠습니다. | 일정 확인하고 공유할게요. |

메일, 공개 글, 코드 리뷰 예시도 볼 수 있습니다. [사용 사례](skills/k-humanizer/references/use-cases.md)

## 만든 계기

12만 개가 넘는 한국어 응답을 검토하면서 표현을 7,500번 이상 직접 고쳤습니다. 그때 어떤 표현을 고쳤고 어떤 표현을 남겼는지 K-Humanizer에 정리했습니다.

## 평가 기록

공개한 골든셋은 위에서 검토한 응답과 별도로 만든 합성 예시 220개입니다. 이 중 90개는 이력서 예시이고, 나머지는 지원 동기, 일상 대화, 메일, 문서, 제품 문구, 공개 글, 코드 리뷰 등을 다룹니다. [골든셋 검사 결과](evals/reports/2026-08-25-fixture-baseline.md), [최초 200건 기록](evals/reports/2026-08-17-fixture-baseline.md)

2026년 8월 25일에는 당시 스킬로 `gpt-5.4`가 만든 답변 220개를 별도 Claude Opus 세션에서 채점했습니다. 다섯 항목의 평균은 4.765점, 의미 보존은 4.800점이었습니다. 채점 모델은 중요한 사실이 바뀐 사례를 찾지 못했습니다. 낮은 점수를 받은 답변과 채점 기준에 어긋난 사례도 보고서에 실었습니다. [모델 평가 결과](evals/reports/2026-08-25/model-baseline.md), [평가 계획](docs/validation-plan.md)

지금 쓰는 편집 기준은 짧은 합성 예시로 직접 확인할 수 있습니다. [편집 사례와 채점 기준](skills/k-humanizer/references/evaluation.md#context-and-scope-review-cases)

## 로컬에서 확인하기

```bash
npx skills add . --skill k-humanizer --full-depth
```

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
python3 scripts/validate_model_baseline.py \
  evals/reports/2026-08-25/model-baseline.jsonl
```

편집 지침과 참고 자료를 볼 수 있습니다. [스킬 파일](skills/k-humanizer/SKILL.md), [한국어 표현 참고](skills/k-humanizer/references/patterns.md), [이력서 편집](skills/k-humanizer/references/resume.md), [이력서 작성 순서](skills/k-humanizer/references/resume-workflow.md), [직무별 예시](skills/k-humanizer/references/resume-roles.md), [평가 기준](skills/k-humanizer/references/evaluation.md)

## 기여하기

번역투가 남는 문장이나 설치 문제를 발견하면 한국어나 영어로 알려 주세요. 실제 이력서, 메일, 고객 자료 대신 같은 문제가 드러나는 예시를 만들어 올려 주세요. [이슈 등록](https://github.com/evergreentree97/K-Humanizer/issues/new/choose), [기여 안내](CONTRIBUTING.md), [데이터셋 조사](docs/dataset-research.md)

## 라이선스

MIT. [라이선스 전문](LICENSE)
