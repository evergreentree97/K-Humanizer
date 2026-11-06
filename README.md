# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)
[![skills.sh](https://skills.sh/b/evergreentree97/K-Humanizer)](https://skills.sh/evergreentree97/K-Humanizer)

**English:** Setup, three copy-ready prompts, and examples for writing Korean for Korean customers are in [README.en.md](README.en.md).

K-Humanizer는 한국 고객이 읽을 글을 자연스러운 한국어로 옮기고 다듬는 Agent Skill입니다. Codex, Claude, Cursor에서 쓸 수 있습니다.

한국 고객에게 제품을 팔거나 고객 지원을 하지만 한국어가 모국어가 아니거나 아직 능숙하지 않은 사람과 팀을 위해 만들었습니다. 기계 번역한 한국어는 뜻이 맞더라도 영어 어순이 남거나, 한국어에서 잘 쓰지 않는 대명사가 붙거나, 말투가 채널과 맞지 않는 경우가 많습니다. 배송 제외 지역이 빠지거나 원문에 없던 환불 약속이 생겨도 한국어를 꼼꼼히 읽기 어렵다면 알아차리기 쉽지 않습니다. K-Humanizer는 읽는 사람과 채널에 맞게 문장을 고치고, 가격과 날짜, 정책, 변수는 바꾸지 않도록 지침에 정해 두었습니다.

아래는 설명을 위해 지어낸 예시입니다. 수정 후 문장은 실제 모델 출력이 아니라 기대하는 결과를 보여 줍니다.

```text
영어 원문   Refunds can only be requested through in-app chat within 7 days of delivery.
           Opened items cannot be refunded unless they arrived damaged.

기계 번역   환불은 배송일로부터 7일 이내에 앱 내 채팅을 통해서만 요청이 가능합니다.
           개봉된 상품은 파손된 상태로 도착한 경우가 아닌 한 환불이 불가능합니다.

수정 후     환불은 상품을 받은 날부터 7일 이내에 앱 채팅으로만 신청할 수 있습니다.
           개봉한 상품은 받았을 때 이미 파손되어 있던 경우에만 환불받을 수 있습니다.
```

기계 번역도 뜻은 통하지만 두 번째 문장이 `~가 아닌 한 ~불가능합니다`라는 이중 부정이라 읽는 사람이 한 번 더 따져 봐야 합니다. 수정본은 같은 조건을 바로 말합니다. 앱 채팅으로만 신청할 수 있다는 제한과 7일 기한, 받았을 때 이미 파손된 경우라는 예외는 그대로 남겼습니다.

한국어로 직접 쓴 이력서, 지원서, 메일, 문서도 지금처럼 다듬을 수 있습니다.

## 설치

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

## 사용 방법

가지고 있는 글에 따라 세 가지로 부탁할 수 있습니다. 영어로 부탁하는 예시는 [English README](README.en.md#three-ways-to-use-it)에 있습니다.

**영어 원문만 있을 때**는 한국어 어순에 맞게 문장을 새로 짜서 옮깁니다. 영어 단어를 하나씩 맞춰 옮기지 않습니다.

```text
$k-humanizer로 이 영어 문구를 한국 고객용 한국어로 옮겨줘.
랜딩 페이지에 쓸 거고, 읽는 사람은 병원 원장님들이야.
말투는 친절하되 너무 가볍지 않게 해줘.

[영어 원문 붙여 넣기]
```

**영어 원문과 한국어 번역이 함께 있을 때**는 기준이 되는 쪽과 비교해 빠지거나 달라진 내용을 바로잡고 어색한 표현을 고칩니다. 따로 알려 주지 않으면 영어를 기준으로 보고, 한국어 쪽이 승인된 최신 문구라고 알려 주면 다시 묻지 않고 한국어를 따릅니다.

```text
$k-humanizer로 이 한국어 번역을 영어 원문과 비교해줘.
원문과 달라진 부분과 번역투를 고치고, 가격이나 날짜, 정책이 다르면 알려줘.

영어 원문:
[붙여 넣기]

한국어 번역:
[붙여 넣기]
```

**한국어만 있을 때**는 요청한 범위 안에서 고치고, 원래 말투와 구성은 유지합니다.

```text
$k-humanizer로 이 고객 안내문을 자연스럽게 다듬어줘.
지금처럼 격식 있는 말투는 유지해줘.

[한국어 붙여 넣기]
```

지침상 결과는 바로 붙여 넣을 수 있는 한국어부터 보여 줍니다. 단순한 편집이나 번역에는 한국어만 돌려주고, 고칠 곳이 없을 때도 "수정할 부분이 없습니다" 같은 판정이나 수정 목록을 붙이지 않습니다. 영어 원문과 번역이 서로 다른 내용을 말하는 경우처럼 확인이 필요한 일만 한두 문장으로 덧붙입니다. 설명이나 질문을 영어로 받고 싶다면 요청에 그렇게 적어 주세요. 점검에서는 영어로 부탁해도 설명과 질문이 한국어로 나온 경우가 있었습니다.

### 알려 주면 좋은 정보

이 정보가 없으면 글을 보고 추론하거나 무난한 기본값을 씁니다. 영어와 한국어 중 어느 쪽 거래 조건을 따라야 할지 정할 수 없을 때는 먼저 묻도록 되어 있습니다. 가격이나 기간 같은 사실이 빠져 있으면 원문이 뒷받침하는 나머지는 모두 옮기고, 빠진 부분만 `[보증 기간]` 같은 자리 표시자로 남긴 뒤 그 한 가지만 묻도록 지침에 적혀 있습니다. 관련 용어나 가정한 경우를 모두 묻는 질문 목록은 만들지 않습니다.

- 읽는 사람: 일반 소비자, 기업 고객, 파트너, 사내 팀
- 채널: 영업 메일, 광고, 랜딩 페이지, 앱 화면, 고객 지원 답변, 공지
- 브랜드 말투: "격식 있고 차분하게", "친근하게"처럼 적거나 기존 한국어 문구를 함께 붙여 넣기
- 목적: 구매, 정보 전달, 문의, 사과, 안내
- 그대로 둘 용어: 제품명, 요금제 이름, 이미 정해 둔 한국어 용어

### 그대로 지키는 내용

아래는 스킬 지침에 적힌 편집 규칙입니다. 모델이 매번 지킨다고 보장하는 것은 아니며, 관찰한 결과와 한계는 [평가 기록](#평가-기록)에 있습니다. 정책이나 가격은 붙여 넣은 글에 있는 내용을 그대로 옮길 뿐, 그 내용이 맞는지는 따로 확인하지 않습니다.

가격과 통화, 할인과 할인 조건, 제품명과 요금제 이름, 숫자, 날짜와 시간대, 계약과 이용 자격 조건, 환불과 배송 정책, 보증 범위와 예외, `{name}` 같은 UI 변수는 바꾸지 않습니다. 원문에 없는 혜택이나 후기, 구매를 재촉하는 문구, 사과, 약속을 더하지 않고 통화나 시간대를 임의로 바꾸지 않습니다.

영어와 한국어가 가격이나 정책에서 서로 다르면 어느 한쪽을 말없이 고르지 않습니다. 기준으로 삼을 쪽을 알려 주면 다시 묻지 않고 따릅니다. 한국어가 영어를 분명히 잘못 옮긴 경우에는 고친 뒤 한 줄로 알립니다. 어느 쪽이 맞는지 알 수 없고 그 선택에 따라 거래 조건이 달라지면 한 번만 묻거나, 해당 부분을 확인이 필요한 곳으로 표시합니다. 원화 가격이나 부가세 표기만 보고 한국어 쪽이 승인된 문구라고 판단하지 않습니다.

한국어를 고칠 때는 요청한 범위 안에서 구체적인 문제를 말할 수 있는 곳만 바꾸도록 되어 있습니다. 의미나 사실 오류, 문법 오류, 한국어 독자가 번역투로 느낄 표현, 상황에 맞지 않는 말투나 글 형식이 그런 문제입니다. 원래 표현이 그 자리에서 올바르고 흔한데 비슷한 말로 바꾸거나 조사를 줄이는 정도라면 원문을 둡니다. 이미 자연스러운 한국어는 그대로 돌려줍니다. 문단은 이어서 읽고, 원인이나 대조, 순서를 나타내는 연결어는 살리며, 원문에 없던 인과를 새로 만들지 않습니다.

## 채널별 예시

예시마다 상황, 영어 원문, 기계 번역, 수정한 한국어, 고친 이유를 담았습니다. 고칠 필요가 없는 예시도 있습니다. 모든 예시는 지어낸 것이고, 수정한 한국어는 실제 모델 출력이 아니라 기대하는 결과를 보여 주려고 쓴 것입니다.

- [B2B 영업 메일](skills/k-humanizer/references/use-cases.md#b2b-sales-email)
- [마케팅과 광고 문구](skills/k-humanizer/references/use-cases.md#marketing-and-ad-copy)
- [랜딩 페이지와 상품 페이지](skills/k-humanizer/references/use-cases.md#landing-and-product-pages)
- [고객 지원 답변과 서비스 공지](skills/k-humanizer/references/use-cases.md#customer-support-and-service-notices)
- [앱 화면 문구와 알림](skills/k-humanizer/references/use-cases.md#app-ui-and-notifications)

## 한국어로 직접 쓴 글

이력서, 지원서, 문서, 메일, 메신저, 공개 글, 코드 리뷰, 대사도 다듬습니다. 아래 예시도 지어낸 것입니다.

```text
수정 전  고객 문의 분류 기준을 다시 정리하는 작업을 통해 주간 평균 처리 시간을 18시간에서 11시간으로 개선했습니다.
수정 후  고객 문의 분류 기준을 다시 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

여기서는 `작업을 통해`를 빼도 한 일이 달라지지 않습니다. 이력서를 붙여 넣으면 경험의 순서와 팀에서 쓰는 `race condition` 같은 용어는 그대로 두고 어색한 표현을 고칩니다. 업무 메모에서 문장을 새로 쓰거나 공고에 맞춰 경험 순서를 바꾸고 싶다면 그 작업도 요청해 주세요. [한국어 글 예시](skills/k-humanizer/references/use-cases.md#native-korean-writing), [이력서 편집](skills/k-humanizer/references/resume.md), [이력서 작성 순서](skills/k-humanizer/references/resume-workflow.md), [직무별 예시](skills/k-humanizer/references/resume-roles.md)

## 만든 계기

12만 개가 넘는 한국어 응답을 검토하면서 표현을 7,500번 이상 직접 고쳤습니다. 그때 어떤 표현을 고쳤고 어떤 표현을 남겼는지 K-Humanizer에 정리했습니다.

## 평가 기록

비즈니스 한국어 지침은 이번에 새로 넣었습니다. [`evals/fixtures/business_korean.v1.jsonl`](evals/fixtures/business_korean.v1.jsonl)에는 합성 테스트 사례 32건이 들어 있습니다. 27건은 세 가지 입력 방식과 다섯 가지 채널의 15가지 조합을 모두 다루고, 5건은 한국어로 직접 쓴 글을 다듬는 기능이 그대로 동작하는지 확인합니다. 전체 중 7건은 고치지 않아야 하는 글이고, 3건은 빠진 정보를 한 가지만 물어야 하는 글입니다. 실제 고객 자료가 아니라 모델이 작성한 사례입니다. [평가 계획](docs/validation-plan.md)

지침을 고치는 동안 Sonnet 5.5로 출력을 만들고 별도의 Opus 5.5가 채점하는 개발 단계 점검을 했습니다. 마지막 점검에서는 고른 사례 7건과 영어 설명을 요청하는 사례 1건을 요청마다 새 프로세스에서 따로 돌렸습니다. 8건 중 6건이 기대한 동작과 맞았고, 채점 모델이 치명적 실패로 표시한 출력은 없었습니다. 빠진 정보 하나만 물어야 할 때 관련 내용까지 묻는 문제, 영어로 요청해도 설명과 질문이 한국어로 나오는 문제, 번역투 문단이 끊겨 읽히는 문제는 아직 남아 있습니다. 실행마다 사례 수와 채점 설명, 실행 방식이 달라서 수치를 합치거나 개선 폭으로 읽을 수 없습니다. 실패한 사례를 포함한 모든 실행 기록과 한계는 [비즈니스 한국어 점검 보고서](evals/reports/2026-11-07-business-korean/business-review.md)에 있습니다.

이 결과는 모델이 작성한 합성 사례에 한 모델이 출력을 만들고 다른 모델이 채점한 기록입니다. 지침을 고칠 때 쓴 사례로 점검했으므로 처음 보는 사례에서의 성능은 알 수 없습니다. 고객을 대상으로 한 연구가 아니고 한국어 원어민이 검토한 것도 아니므로 품질을 검증했다고 말할 수는 없습니다.

아래 기록은 이전 버전을 한국어 원문만 편집하는 합성 사례로 평가한 결과이며 그대로 두었습니다. 번역이나 비즈니스 현지화 성능을 보여 주지 않습니다. 220건 전체를 현재 지침으로 다시 돌리지는 않았고, 데이터 검사 스크립트만 통과했습니다.

공개한 골든셋은 위에서 검토한 응답과 별도로 만든 합성 예시 220개입니다. 이 중 90개는 이력서 예시이고, 나머지는 지원 동기, 일상 대화, 메일, 문서, 제품 문구, 공개 글, 코드 리뷰 등을 다룹니다. [골든셋 검사 결과](evals/reports/2026-08-25-fixture-baseline.md), [최초 200건 기록](evals/reports/2026-08-17-fixture-baseline.md)

2026년 8월 25일에는 당시 스킬로 `gpt-5.4`가 만든 답변 220개를 별도 Claude Opus 세션에서 채점했습니다. 다섯 항목의 평균은 4.765점, 의미 보존은 4.800점이었습니다. 채점 모델은 중요한 사실이 바뀐 사례를 찾지 못했습니다. 낮은 점수를 받은 답변과 채점 기준에 어긋난 사례도 보고서에 실었습니다. [모델 평가 결과](evals/reports/2026-08-25/model-baseline.md)

채점 기준은 [evaluation.md](skills/k-humanizer/references/evaluation.md)에 있습니다. 가격이나 정책, 약속이 바뀌면 문장이 자연스러워도 실패로 봅니다.

## 로컬에서 확인하기

```bash
npx skills add . --skill k-humanizer --full-depth
```

```bash
python3 scripts/validate_golden_set.py
python3 scripts/validate_business_set.py
python3 -m unittest scripts.test_validate_golden_set scripts.test_validate_model_baseline scripts.test_validate_business_set
python3 scripts/check_public_hygiene.py
python3 scripts/validate_model_baseline.py \
  evals/reports/2026-08-25/model-baseline.jsonl
```

편집 지침과 참고 자료를 볼 수 있습니다. [스킬 파일](skills/k-humanizer/SKILL.md), [사용 사례](skills/k-humanizer/references/use-cases.md), [한국어 표현 참고](skills/k-humanizer/references/patterns.md), [평가 기준](skills/k-humanizer/references/evaluation.md)

## 기여하기

번역투가 남는 문장이나 설치 문제를 발견하면 한국어나 영어로 알려 주세요. 모국어가 아닌 한국어로 한국 고객용 글을 쓰면서 겪은 문제도 환영합니다. 실제 이력서, 메일, 광고, 고객 자료 대신 회사와 제품, 가격을 지어낸 예시로 같은 문제를 보여 주세요. [이슈 등록](https://github.com/evergreentree97/K-Humanizer/issues/new/choose), [기여 안내](CONTRIBUTING.md), [데이터셋 조사](docs/dataset-research.md)

## 라이선스

MIT. [라이선스 전문](LICENSE)
