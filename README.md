# K-Humanizer

![K-Humanizer](assets/k-humanizer-hero.jpg)

[English](README.en.md)

[![Version](https://img.shields.io/github/v/release/evergreentree97/K-Humanizer?label=version&color=2f6feb)](CHANGELOG.md)

K-Humanizer는 한국 고객에게 보낼 메시지를 자연스러운 한국어로 번역하고 다듬어주는 지침입니다. 한국어가 모국어가 아닌 해외 팀이 영업 메일, 광고, 제품 소개, 고객 지원, 앱 안내 등을 작성할 때 겪는 번역투와 어색한 표현을 해결하는 데 초점을 맞췄습니다.

외국어 텍스트뿐만 아니라, 한국어로 직접 작성한 문서, 메일 등의 표현을 매끄럽게 다듬는 용도로도 사용할 수 있습니다. 이력서와 지원서는 별도 스킬인 [K-Humanizer Resume](skills/k-humanizer-resume/SKILL.md)에서 다룹니다.

---

## 사용 예시

| 구분 | 내용 |
| :--- | :--- |
| **작성할 내용** | Could you send us your available times for next week? |
| **일반적인 AI 번역** | 다음 주 귀하의 이용 가능한 시간을 저희에게 보내주실 수 있으신가요? |
| **다듬은 문장** | 다음 주 가능한 시간을 알려주실 수 있을까요? |

---

## 사용 방법

[SKILL.md](skills/k-humanizer/SKILL.md)의 지침과 필요한 [비즈니스 한국어](skills/k-humanizer/references/business-korean.md)와 [한국어 글쓰기 사례](skills/k-humanizer/references/native-writing.md)를 LLM에 전달한 뒤, 다음과 같이 요청해 보세요.

- 한국어 초안만 있을 때: 어색한 표현과 번역투를 자연스럽게 다듬습니다.
- 외국어와 한국어 초안이 함께 있을 때: 두 내용을 비교해 누락되거나 왜곡된 부분, 어색한 표현을 바로잡습니다.
- 외국어만 있을 때: 독자와 채널 특성에 맞는 한국어로 번역합니다.

영어로 점검했으며, 다른 외국어 입력은 아직 평가하지 않았습니다.
> 읽는 사람, 사용할 채널, 원하는 말투를 함께 알려 주시면 훨씬 더 알맞은 문구를 얻을 수 있습니다. 설명을 영어로 받고 싶다면 요청 시 함께 적어주세요.

---

## 사용 환경

Claude Code와 Codex에서는 플러그인으로 두 스킬을 함께 설치할 수 있습니다.

Claude Code:

```bash
claude plugin marketplace add evergreentree97/K-Humanizer
claude plugin install k-humanizer@k-humanizer
```

Codex:

```bash
codex plugin marketplace add evergreentree97/K-Humanizer
codex plugin add k-humanizer@k-humanizer
```

Cursor 같은 다른 에이전트에서는 스킬을 개별 설치하세요.

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

이력서와 지원서를 다듬으려면 이력서 스킬도 설치하세요.

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer-resume --full-depth
```

웹 채팅이나 API에서 쓸 때는 링크만 알려 주면 모델이 파일을 읽지 못할 수 있으므로, [SKILL.md](skills/k-humanizer/SKILL.md)와 필요한 참고 파일([비즈니스 한국어](skills/k-humanizer/references/business-korean.md)와 [한국어 글쓰기 사례](skills/k-humanizer/references/native-writing.md) 등)의 텍스트를 직접 붙여 넣어 주세요.

---

## 평가

같은 모델(Claude Sonnet 5.5)에 비즈니스 한국어 요청 32건을 스킬 없이 한 번, 스킬과 함께 한 번 맡겨 결과를 비교했습니다. 채점은 Claude Opus 5.5가 어느 쪽 결과인지 모르는 상태로 했습니다.

| 항목 (32건) | 스킬 없음 | 스킬 사용 |
| :--- | ---: | ---: |
| 원문에 없는 내용을 덧붙임 | 12건 | 0건 |
| 요구 사항을 빠뜨림 | 6건 | 0건 |
| 이미 자연스러운 글을 그대로 둠 (7건 중) | 2건 | 6건 |
| 요청한 대로 처리함 | 25건 | 29건 |

결과와 원본 출력은 [비교 보고서](evals/reports/2026-11-10-skill-vs-baseline/README.md)에, 이전 점검 기록은 [비즈니스 한국어 점검 보고서](evals/reports/2026-11-07-business-korean/business-review.md)에 있습니다.

## 라이선스

[MIT](LICENSE)
