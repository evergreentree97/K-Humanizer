# Promotion Drafts

> **Status: UNPUBLISHED DRAFT.** Nothing in this file has been posted.

## Before posting

- Every claim must match the repository on the day of posting. Recheck the
  README and changelog.
- The business fixture `evals/fixtures/business_korean.v1.jsonl` holds 32
  model-authored synthetic cases (27 business, 5 native-writing regression).
  The model-scored development checks and their open issues are in
  `evals/reports/2026-11-07-business-korean/business-review.md`. Link that
  report instead of quoting a single run's numbers. Do not describe the checks
  as a benchmark, held-out validation, human review, a customer study, or
  proof of quality.
- The 220-case golden set and the 2026-08-25 model scores measured an earlier
  version on synthetic Korean-only editing cases. Do not cite them as business
  localization results.
- The before/after example in each draft is a synthetic illustration taken from
  `use-cases.md`, not a captured model output. Keep that label if it is reused.
- Do not add user counts, customer quotes, conversion changes, rankings, or
  "first" and "best" claims.
- Describe the preservation and unchanged-text rules as the skill's
  instructions, not as a guarantee about every output.
- Drafts below: DEV and GeekNews.

## Short description (English)

One line, for directories and profile fields:

> An Agent Skill that turns English or machine-translated Korean into natural
> Korean for Korean customers, with instructions to keep prices, dates, and
> policies exact.

Two sentences, for a repository card or a short listing:

> K-Humanizer helps people who sell to Korean customers without being fluent
> in Korean. It translates or checks sales emails, ads, landing pages, support
> replies, and app strings so they read naturally in Korean, with instructions
> not to change prices, policies, or promises. MIT licensed, for Codex, Claude,
> and Cursor.

## DEV update (English)

Title: K-Humanizer now helps you write Korean for Korean customers

Tags: `opensource`, `ai`, `localization`, `korean`

Body:

> K-Humanizer started as an Agent Skill for polishing Korean that native
> speakers draft with AI: resumes, emails, and documents. This update aims it
> at a different problem. Many people sell to Korean customers without being
> fluent enough in Korean to check a machine translation closely.
>
> Machine-translated Korean is usually understandable. The trouble is that it
> often reads like a translation, and it is hard to see when it quietly changed
> something. Here is a synthetic example, a shipping banner. The revised line
> illustrates the expected result; it is not a captured model output.
>
> ```text
> English              Free shipping on orders of ₩50,000 or more (excluding Jeju and remote areas).
> Machine translation  50,000원 이상 주문 시 무료 배송을 제공합니다. 지금 바로 쇼핑하세요!
> Revised              5만 원 이상 주문 시 무료 배송 (제주 및 도서산간 지역 제외)
> ```
>
> The machine translation dropped the exclusion and added "Shop now!", which
> the English never said. The revision restores the exclusion, removes the
> added line, and uses the short format Korean shopping banners use.
>
> What the instructions cover now:
>
> - Handles three inputs: English only (translate and localize), English with
>   a Korean draft (fix drift against the version you name as the source, or
>   the English by default), and Korean only (edit within the requested scope).
> - Infers audience, channel, brand tone, and purpose from the text or uses a
>   sensible default. If a fact such as a price or period is missing, its
>   instructions say to translate the rest, leave a placeholder for that fact,
>   and ask one question about it. It also asks when it cannot tell which
>   version's commercial terms govern.
> - Its instructions keep prices, discount conditions, dates, refund and
>   delivery policy, warranty exceptions, and UI placeholders exact, and rule
>   out added urgency, testimonials, apologies, or promises. Policy text is
>   carried over from what you supply; the skill does not check it.
> - Edits supplied Korean only where it can name a concrete problem in the
>   requested scope, keeps connectors that carry cause or contrast, and returns
>   Korean that already reads naturally as it is.
> - Includes synthetic worked examples for B2B sales email, ad copy, landing
>   pages, customer support and notices, and app UI.
>
> The business guidance is new, so treat it as early. The repository has 32
> model-authored synthetic test cases (27 business, 5 native-writing
> regression) and a report of model-judged development checks, including the
> cases that still fail and the open issues:
> https://github.com/evergreentree97/K-Humanizer/blob/main/evals/reports/2026-11-07-business-korean/business-review.md
> Those checks are not human review or a customer study. If you want notes and
> questions in English, say so in your request. The native-writing features
> for resumes, applications, and email are still there.
>
> ```bash
> npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
> ```
>
> MIT licensed. https://github.com/evergreentree97/K-Humanizer

## GeekNews Show (Korean)

Title: Show GN: K-Humanizer - 한국 고객에게 보낼 글을 자연스러운 한국어로 옮기는 Agent Skill

Body:

> K-Humanizer는 Codex, Claude, Cursor에서 쓰는 Agent Skill입니다. 원래는 AI로 쓴 이력서나 메일의 어색한 한국어를 다듬는 용도였는데, 이번에 한국어가 능숙하지 않아도 한국 고객을 상대하는 사람과 팀이 쓸 수 있도록 지침을 바꿨습니다.
>
> 한국어가 능숙하지 않으면 기계 번역 결과를 꼼꼼히 확인하기 어렵습니다. 문장이 어색한 것도 문제지만, 배송 제외 지역이 빠지거나 원문에 없던 환불 약속이 생겨도 알아차리기 쉽지 않습니다. 아래는 설명을 위해 지어낸 예시이고, 수정 후 문장은 실제 모델 출력이 아닙니다.
>
> ```text
> 영어 원문   Free shipping on orders of ₩50,000 or more (excluding Jeju and remote areas).
> 기계 번역   50,000원 이상 주문 시 무료 배송을 제공합니다. 지금 바로 쇼핑하세요!
> 수정 후     5만 원 이상 주문 시 무료 배송 (제주 및 도서산간 지역 제외)
> ```
>
> 기계 번역에서는 제외 지역이 빠졌고, 원문에 없던 "지금 바로 쇼핑하세요!"가 붙었습니다. 수정본은 제외 지역을 되살리고 덧붙은 문장을 지운 뒤 쇼핑몰 배너에서 흔히 쓰는 짧은 형식으로 바꿨습니다.
>
> 이번에 바뀐 점
>
> - 영어 원문만 있으면 한국어 어순에 맞게 새로 옮기고, 원문과 번역이 함께 있으면 기준으로 정한 쪽(따로 정하지 않으면 영어)과 비교해 빠지거나 달라진 내용을 고칩니다. 한국어만 있으면 요청한 범위 안에서 다듬습니다.
> - 읽는 사람, 채널, 브랜드 말투, 목적을 글에서 추론하거나 무난한 기본값을 씁니다. 가격이나 기간 같은 사실이 빠지면 나머지는 옮기고 그 부분만 자리 표시자로 남겨 한 가지만 묻도록 지침에 적었습니다. 어느 쪽 거래 조건을 따를지 알 수 없을 때도 묻습니다.
> - 지침에는 가격과 할인 조건, 날짜, 환불과 배송 정책, 보증 예외, UI 변수를 그대로 두고, 원문에 없는 혜택이나 재촉하는 문구, 사과, 약속은 더하지 않는다고 적었습니다. 정책 내용은 붙여 넣은 글을 옮길 뿐 맞는지 따로 확인하지 않습니다.
> - 고칠 구체적인 문제를 말할 수 있는 곳만 바꾸고, 원인이나 대조를 잇는 연결어는 살립니다. 이미 자연스러운 한국어는 그대로 돌려줍니다.
> - B2B 영업 메일, 광고 문구, 랜딩 페이지, 고객 지원과 공지, 앱 화면과 알림 예시를 채널마다 세 개 이상 넣었습니다. 모두 지어낸 예시입니다.
>
> 아직 부족한 점도 적어 둡니다. 테스트 사례 32건(비즈니스 한국어 27건, 기존 기능 회귀 확인 5건)은 모델이 작성한 합성 예시입니다. 모델이 출력을 만들고 다른 모델이 채점한 개발 단계 점검 기록과 아직 실패하는 사례, 남은 문제는 보고서에 모두 적었습니다. 사람이 검토하거나 고객을 대상으로 한 연구는 아닙니다. https://github.com/evergreentree97/K-Humanizer/blob/main/evals/reports/2026-11-07-business-korean/business-review.md 예전에 공개한 220건 평가는 한국어 원문만 편집하는 합성 사례로 이전 버전을 평가한 기록입니다. 한국어로 직접 쓴 이력서나 메일을 다듬는 기능은 그대로 쓸 수 있습니다.
>
> ```bash
> npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
> ```
>
> MIT 라이선스로 공개했습니다. https://github.com/evergreentree97/K-Humanizer
