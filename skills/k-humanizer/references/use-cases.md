# Use Cases

All examples are synthetic. The revised versions illustrate expected behavior;
they are not recorded model outputs. Each is one acceptable answer, not an
exact-match target. Another wording passes if it keeps the same facts,
conditions, register, and reader action.

The first part covers Korean written for Korean customers, often by people who
do not read Korean fluently. The second part covers native Korean writing such
as resumes, applications, chat, and dialogue.

## Business Korean for Korean customers

Each example lists the input mode, the context the skill used, the English
original, a plausible AI translation, the revised Korean, and the reason for
the change. In Korean-only examples, the English is shown for reference; the
user pasted only the Korean.

Some examples leave the Korean unchanged. Returning good text as is counts as a
correct result.

### B2B sales email

Defaults: 합쇼체. Address the recipient by full name and title, or by company
and title. Put the reason for writing and the request near the top, and make
each request the source contains clear. Do not add urgency, client references,
or results the source does not supply.

#### First outreach to a logistics company

- **Mode:** English only, Korean requested
- **Context:** A dispatch-planning software company writes to Kim Jiyeon, the
  operations manager at a mid-size Korean logistics company. Polite and direct.
  Purpose: request a call.

English original:

```text
Hi Jiyeon,

I'm reaching out because I saw that your team recently opened three new
warehouses. Routeplan helps operations teams cut down on manual dispatch
planning. Would you be open to a 20-minute call next week to see whether it
fits your workflow?
```

AI-translated Korean:

```text
지연 님, 안녕하세요.

귀하의 팀이 최근 세 개의 새로운 창고를 오픈했다는 것을 보고 연락드리게 되었습니다. Routeplan은 운영팀이 수동 배차 계획을 줄이는 데 도움을 줍니다. 귀하의 워크플로우에 적합한지 확인하기 위해 다음 주에 20분 통화를 하실 의향이 있으신가요?
```

Revised Korean:

```text
김지연 매니저님, 안녕하세요.

최근 창고 세 곳을 새로 여셨다는 소식을 보고 연락드립니다. Routeplan은 운영팀의 수작업 배차 계획을 줄여 주는 서비스입니다. 다음 주에 20분 통화로 지금 업무 방식에 맞을지 함께 살펴볼 수 있을까요?
```

Why this is better: In Korean business email, a first name alone is too
familiar for a prospect. The context supplies her full name and title, so the
revision uses them. The draft follows English word order and repeats `귀하의`,
which reads like a form letter. `연락드리게 되었습니다` becomes the direct
`연락드립니다`, and `워크플로우에 적합한지` becomes plain Korean. The request
is still a 20-minute call next week that she can accept or decline. No results
or pricing were added.

#### Quote follow-up with a billing condition

- **Mode:** English source with a Korean draft
- **Context:** An account executive follows up after a demo with a Korean
  buyer. The quote is in US dollars. 합쇼체. Purpose: confirm the commercial
  terms.

English original:

```text
As we discussed, the Annual plan is $18 per user per month, billed annually.
The 15% discount applies only if the contract is signed by December 15.
Implementation support is included for the first 60 days.
```

AI-translated Korean:

```text
논의한 바와 같이, Annual 플랜은 사용자당 월 18달러입니다. 12월 15일까지 계약이 체결되면 15% 할인이 적용됩니다. 처음 60일 동안 구현 지원이 포함됩니다.
```

Revised Korean:

```text
말씀 나눈 대로 Annual 플랜은 사용자 1명당 월 18달러이며, 요금은 1년 단위로 청구됩니다. 15% 할인은 12월 15일까지 계약하시는 경우에만 적용됩니다. 처음 60일 동안은 도입 지원이 포함됩니다.
```

Note returned with the result: "The Korean draft left out 'billed annually'
and softened 'only if'. Both are restored."

Why this is better: Billing frequency changes what the customer expects to pay
up front, so dropping it is a material error. `경우에만` keeps the deadline as
a condition of the discount. `구현 지원` is a literal rendering; Korean B2B
buyers call this `도입 지원`. The plan name stays in English as the product
uses it, and the price stays in US dollars, as the context states, because a
won conversion would be a new commercial term.

#### Renewal reminder that already works

- **Mode:** Korean only
- **Context:** A reminder to an existing business customer. The user wrote it
  with machine translation and asked for a check. 합쇼체. Purpose: guidance.

English original (for reference):

```text
Your current contract ends on March 31. If you'd like to renew on the same
terms, please let us know by March 15. We'll send the renewal form once we
hear from you.
```

AI-translated Korean:

```text
현재 계약은 3월 31일에 종료됩니다. 같은 조건으로 갱신을 원하시면 3월 15일까지 알려 주세요. 회신 주시면 갱신 신청서를 보내 드리겠습니다.
```

Revised Korean: unchanged.

Why this is better: It already reads as if a Korean account manager wrote it.
`종료됩니다` and `갱신` are the usual contract words, the deadline and next
step are clear, and `알려 주세요` is polite enough for an existing customer.
Rewriting it would only add risk, so the skill returns it as is.

### Marketing and ad copy

Defaults: follow the brand's register. Headlines and banners can be noun
phrases. Keep each offer next to its conditions and deadline. Do not add
urgency, scarcity, superlatives, or social proof.

#### Sunscreen launch ad

- **Mode:** English only, Korean requested
- **Context:** Instagram feed ad for a skincare brand launching in Korea.
  Friendly 해요체. Purpose: purchase.

English original:

```text
Meet your new everyday sunscreen.
Lightweight, no white cast, SPF 50+ PA++++.
Get 20% off your first order, this week only.
```

AI-translated Korean:

```text
당신의 새로운 데일리 선크림을 만나보세요.
가벼움, 백탁 없음, SPF 50+ PA++++.
이번 주에만 첫 주문 20% 할인을 받으세요.
```

Revised Korean:

```text
매일 바르기 좋은 가벼운 선크림
백탁 없이 발려요. SPF 50+ PA++++
첫 주문 20% 할인은 이번 주에만 드려요.
```

Why this is better: `당신의` sounds like a translated letter, and a Korean ad
headline does not need a pronoun. The list of fragments becomes a short claim a
person would say. The SPF and PA ratings, the 20% discount, the first-order
condition, and "this week only" all stay. Nothing like "selling out fast" was
added.

#### Free shipping banner with an exclusion

- **Mode:** English source with a Korean draft
- **Context:** Site-wide banner for an online furniture store. Plain, neutral
  brand voice. Purpose: information.

English original:

```text
Free shipping on orders of ₩50,000 or more (excluding Jeju and remote areas).
```

AI-translated Korean:

```text
50,000원 이상 주문 시 무료 배송을 제공합니다. 지금 바로 쇼핑하세요!
```

Revised Korean:

```text
5만 원 이상 주문 시 무료 배송 (제주 및 도서산간 지역 제외)
```

Note returned with the result: "The Korean draft dropped the Jeju and
remote-area exclusion and added '지금 바로 쇼핑하세요!', which is not in the
English. The exclusion is restored and the added line removed."

Why this is better: The exclusion is delivery policy. Leaving it out promises
free shipping to customers who will be charged. The added "shop now" line is a
sales hook the source did not include. Korean shopping banners usually state
this kind of offer as a short phrase with the exclusion in parentheses, which
suits a neutral brand. `제공합니다` was not wrong; the banner simply does not
need a full sentence. The amount is the same, written as `5만 원`.

#### Restrained B2B ad

- **Mode:** English only, Korean requested
- **Context:** LinkedIn ad for accounting software aimed at finance leads at
  Korean companies. The brand voice is calm and formal. Purpose: start a trial.

English original:

```text
Close your books faster.
Ledgerline automates bank reconciliation for finance teams.
Start a 14-day free trial. No credit card required.
```

AI-translated Korean:

```text
당신의 장부를 더 빠르게 마감하세요.
Ledgerline은 재무팀을 위해 은행 조정을 자동화합니다.
14일 무료 평가판을 시작하세요. 신용카드가 필요하지 않습니다.
```

Revised Korean:

```text
결산 마감을 더 빠르게
Ledgerline은 재무팀의 은행 거래 대사를 자동화합니다.
14일 무료 체험은 신용카드 등록 없이 시작할 수 있습니다.
```

Why this is better: The brand speaks formally to finance leads, so the
revision keeps 합쇼체 instead of switching to chatty 해요체. `당신의 장부` is a
literal "your books"; Korean finance teams talk about `결산` and `마감`.
`은행 조정` is a dictionary rendering of "reconciliation", while the working
term is `대사`. The trial length, "free", and the no-card condition stay, and
"automates" is not strengthened into "fully automates".

### Landing and product pages

Defaults: the hero says what the product lets the reader do. Spec tables and
feature labels use short noun phrases. Keep qualifiers such as "up to" and
"about", and keep prices, currencies, and VAT notes as the source gives them.

#### Booking software hero section

- **Mode:** English only, Korean requested
- **Context:** Landing page for appointment software sold to Korean clinic
  owners. Friendly 합쇼체. Purpose: sign-up.

English original:

```text
Let patients book appointments 24/7
Automatic reminders reduce no-shows. Setup takes less than 10 minutes.
[Get started free]
```

AI-translated Korean:

```text
환자들이 연중무휴 24시간 예약할 수 있도록 하세요
자동 리마인더는 노쇼를 줄입니다. 설정은 10분 미만이 소요됩니다.
[무료로 시작하세요]
```

Revised Korean:

```text
환자가 24시간 언제든 예약할 수 있습니다
자동 알림으로 노쇼를 줄여 줍니다. 설정에는 10분도 걸리지 않습니다.
[무료로 시작하기]
```

Why this is better: `~할 수 있도록 하세요` turns the headline into an
instruction aimed at the clinic owner, and `연중무휴 24시간` says "always"
twice. The revision states what patients can do. `노쇼` is the word Korean
clinic staff use, so it stays. `리마인더` becomes `알림`, which is clearer to a
general owner. The button uses the usual `~하기` form. "Reduce no-shows" keeps
the same strength, with no number added. `10분 미만이 소요됩니다` is stiff, but
`10분 안에` would include exactly 10 minutes; `10분도 걸리지 않습니다` keeps
"less than".

#### Spec table that already works

- **Mode:** English source with a Korean draft
- **Context:** Product detail page for a robot vacuum. Neutral register.
  Purpose: information.

English original:

```text
Battery life: Up to 120 minutes (Eco mode)
Charging time: About 4 hours
Dust bin: 0.4 L
```

AI-translated Korean:

```text
사용 시간: 최대 120분 (에코 모드 기준)
충전 시간: 약 4시간
먼지통 용량: 0.4L
```

Revised Korean: unchanged.

Why this is better: Korean spec tables use short noun phrases, so turning them
into sentences would not help. `최대`, `기준`, and `약` carry "up to", the Eco
mode condition, and "about". `사용 시간` is how Korean product pages label
battery life. A rewrite could only lose one of those qualifiers.

#### Warranty section with one translated sentence

- **Mode:** Korean only
- **Context:** Product page for a furniture brand. Neutral 합쇼체. Purpose:
  information.

English original (for reference):

```text
Every sofa comes with a 5-year frame warranty. Fabric and cushions are covered
for 1 year. Damage caused by pets or misuse is not covered.
```

AI-translated Korean:

```text
모든 소파에는 5년 프레임 보증이 함께 제공됩니다. 패브릭과 쿠션은 1년 동안 보증의 적용을 받습니다. 반려동물 또는 오용으로 인한 손상은 보증 대상에 포함되지 않습니다.
```

Revised Korean:

```text
모든 소파에는 5년 프레임 보증이 함께 제공됩니다. 패브릭과 쿠션의 보증 기간은 1년입니다. 반려동물 또는 오용으로 인한 손상은 보증 대상에 포함되지 않습니다.
```

Why this is better: Only the second sentence is a literal rendering of "are
covered". The first and third sentences read like ordinary Korean product
pages, including `제공됩니다`, so they stay. The warranty periods and the
exclusion are unchanged.

#### Local price that differs from the English

- **Mode:** English source with a Korean draft
- **Context:** Pricing page. The user says the Korea team sets Korean prices
  separately and the Korean price is current. Neutral register. Purpose:
  purchase.

English original:

```text
Pro: $12 per month, billed monthly. Cancel anytime.
```

AI-translated Korean:

```text
Pro: 월 16,500원 (VAT 포함, 매월 결제)
언제든 해지할 수 있습니다.
```

Revised Korean: unchanged.

Why this is better: The user named the Korean price as current, so the skill
follows it without asking again. Replacing it with a conversion of $12 would
create a price nobody approved. Monthly billing and "cancel anytime" match the
English, and the Korean already reads naturally. Without the user's statement,
a won price with VAT would not by itself show which version governs; the skill
would ask one question or mark the price as unresolved instead of returning it
as verified copy.

### Customer support and service notices

Defaults: formal notices use plain 합쇼체. Support replies follow the brand's
register. Keep the apology at the level the source uses, keep commitments
exactly as stated, and keep policy limits and their exceptions.

#### Maintenance notice that already works

- **Mode:** English source with a Korean draft
- **Context:** Scheduled maintenance notice on the website and in the app.
  Formal 합쇼체. Purpose: information.

English original:

```text
[Scheduled maintenance]
Our service will be unavailable on November 20 from 2:00 to 4:00 a.m. KST.
Orders placed before maintenance begins will ship as scheduled.
```

AI-translated Korean:

```text
[서비스 점검 안내]
11월 20일 오전 2시부터 4시까지(한국 시간) 서비스 점검으로 이용이 중단됩니다.
점검 시작 전에 접수된 주문은 예정대로 출고됩니다.
```

Revised Korean: unchanged.

Why this is better: Korean readers expect service notices to be formal and
plain, and this one is. The date, time window, time zone, and shipping
commitment match the English. `출고됩니다` matches "ship": it promises dispatch
on schedule, not a delivery date, which `배송됩니다` could suggest. The source
has no apology. Adding `불편을 드려 죄송합니다` would be the brand's decision,
not the translator's.

#### Late delivery reply with an invented refund

- **Mode:** English source with a Korean draft
- **Context:** Support email to a customer asking where their order is. Polite
  합쇼체. Purpose: apology and guidance.

English original:

```text
Sorry for the delay. Your order left our warehouse on May 3 and should arrive
within 2–3 business days. If it hasn't arrived by May 8, reply to this email
and we'll look into it.
```

AI-translated Korean:

```text
불편을 드려 대단히 죄송합니다. 고객님의 주문은 5월 3일에 당사 창고에서 출고되었으며, 영업일 기준 2~3일 이내에 도착할 예정입니다. 5월 8일까지 도착하지 않을 경우 본 메일에 회신해 주시면 즉시 환불해 드리겠습니다.
```

Revised Korean:

```text
배송이 늦어져 죄송합니다. 주문하신 상품은 5월 3일에 출고되었고, 영업일 기준 2~3일 안에 도착할 예정입니다. 5월 8일까지 받지 못하시면 이 메일에 회신해 주세요. 확인해 드리겠습니다.
```

Note returned with the result: "The Korean draft promised an immediate refund
(즉시 환불). The English only says you will look into it, so the revision
matches the English."

Why this is better: Customers will hold support to a refund the business never
offered. The apology stays at the level of the English instead of
`대단히 죄송합니다`. `출고` is the standard word for "left our warehouse".
"Business days", May 3, and the May 8 cutoff stay exact.

#### Refund policy with a single channel

- **Mode:** English only, Korean requested
- **Context:** Help center article for a shopping app. 합쇼체. Purpose:
  guidance.

English original:

```text
Refunds can only be requested through in-app chat within 7 days of delivery.
Opened items cannot be refunded unless they arrived damaged.
```

AI-translated Korean:

```text
환불은 배송일로부터 7일 이내에 앱 내 채팅을 통해서만 요청이 가능합니다. 개봉된 상품은 파손된 상태로 도착한 경우가 아닌 한 환불이 불가능합니다.
```

Revised Korean:

```text
환불은 상품을 받은 날부터 7일 이내에 앱 채팅으로만 신청할 수 있습니다. 개봉한 상품은 받았을 때 이미 파손되어 있던 경우에만 환불받을 수 있습니다.
```

Why this is better: "Only" and the damaged-on-arrival exception are policy
limits, so both survive, through `으로만` and `경우에만`. The draft states the
exception as a double negative (`~가 아닌 한 ... 불가능합니다`), which makes
readers work backward. `요청이 가능합니다` becomes `신청할 수 있습니다`, the
usual way to say what a customer can do. `통해` is not banned; here the shorter
particle reads more naturally and keeps the same restriction.

### App UI and notifications

Defaults: match the register of the app's existing strings. Buttons name the
action. Keep keys, variables, and markup exactly as written, and keep the real
outcome of destructive or paid actions.

#### Fitness app strings

- **Mode:** English only, Korean requested
- **Context:** Consumer fitness app whose existing Korean strings use 해요체.
  Purpose: encourage a daily habit.

English original:

```text
push.streak: "{name}, you're on a {days}-day streak! Don't break it now."
button.log_workout: "Log workout"
toast.workout_saved: "Workout saved"
```

AI-translated Korean:

```text
push.streak: "{name}, 당신은 {days}일 연속 기록 중입니다! 지금 그것을 깨지 마세요."
button.log_workout: "운동 로그"
toast.workout_saved: "운동 저장됨"
```

Revised Korean:

```text
push.streak: "{name}님, {days}일 연속 기록 중이에요! 이대로 이어가 보세요."
button.log_workout: "운동 기록하기"
toast.workout_saved: "운동 기록을 저장했어요"
```

Why this is better: `당신` and `그것` are English pronouns that Korean leaves
out. `기록을 깨다` usually means setting a new record, the opposite of the
intended meaning, so the revision encourages the user to keep the streak
going. `{name}` and `{days}` stay exactly as written. `님` after `{name}` is
safe because it does not depend on the last sound of the name. The button says
what tapping it does, and the toast follows the app's 해요체. No reward or
emoji was added.

#### Delete confirmation with dropped details

- **Mode:** English source with a Korean draft
- **Context:** Project management dashboard for business teams. Formal
  합쇼체. Purpose: confirm a destructive action.

English original:

```text
title: "Delete project?"
body: "This permanently deletes {project_name} and all of its files for everyone on your team. This can't be undone."
confirm: "Delete"
cancel: "Cancel"
```

AI-translated Korean:

```text
title: "프로젝트를 삭제하시겠습니까?"
body: "{project_name}과 해당 파일이 삭제됩니다."
confirm: "확인"
cancel: "취소"
```

Revised Korean:

```text
title: "프로젝트를 삭제하시겠습니까?"
body: "{project_name} 프로젝트와 모든 파일이 팀 전체에서 영구 삭제됩니다. 삭제한 후에는 되돌릴 수 없습니다."
confirm: "삭제"
cancel: "취소"
```

Note returned with the result: "The Korean draft dropped 'permanently', 'for
everyone on your team', and 'can't be undone'. They are restored."

Why this is better: Those three details are the reason the dialog exists.
`확인` does not tell the user that the button deletes anything, so it becomes
`삭제`. `과` after `{project_name}` is correct only when the name ends in a
consonant; adding `프로젝트` after the variable makes `와` correct for every
name. The title already fits the product's formal voice, so it stays.

#### Delivery notifications with one awkward string

- **Mode:** Korean only
- **Context:** Food delivery app with 해요체 strings. The user pasted only the
  Korean. Purpose: status updates and a review request.

English original (for reference):

```text
order.on_the_way: "Your order is on the way. Arriving around {eta}."
rider.nearby: "Your rider is nearby."
review.prompt: "Rate your order"
```

AI-translated Korean:

```text
order.on_the_way: "주문하신 음식이 배달 중이에요. {eta}쯤 도착해요."
rider.nearby: "라이더가 근처에 있어요."
review.prompt: "당신의 주문을 평가하세요"
```

Revised Korean:

```text
order.on_the_way: "주문하신 음식이 배달 중이에요. {eta}쯤 도착해요."
rider.nearby: "라이더가 근처에 있어요."
review.prompt: "이번 주문을 평가해 주세요"
```

Why this is better: The first two strings already read naturally in the app's
해요체, so they stay. The third adds `당신의`, which Korean notifications rarely
use, and ends in a bare command that sounds abrupt next to the others. Only
that string changes. If the app calls this feature `리뷰` or `별점` elsewhere,
use that word instead.

#### Dashboard subtitle that introduces itself

- **Mode:** Korean only
- **Context:** Subtitle under the title `문서 처리 현황` in an internal document
  tool. Neutral register. Purpose: information.

English original (for reference):

```text
This dashboard gives you an at-a-glance view of your uploaded documents and
their processing status.
```

AI-translated Korean:

```text
이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.
```

Revised Korean:

```text
업로드한 문서와 처리 상태를 보여줍니다.
```

Why this is better: The title already says what the screen is, so
`이 화면은 ... 대시보드입니다` repeats it. The subtitle now says what the screen
shows. `한눈에` can work elsewhere; here it adds nothing the reader can check.

## Native Korean writing

These sections cover Korean written by and for Korean speakers. The same
facts-first rules apply.

### Resume and Profile

Goal: make achievements concrete, credible, and easy to scan.

Rules:
- Start with the resume references linked in [SKILL.md](../SKILL.md).
- Prefer problem or scope, judgment and action, then confirmed result over broad self-description.
- Remove inflated adjectives such as `탁월한`, `혁신적인`, `압도적인` unless proven by evidence.
- Keep numbers with their comparison and measurement conditions.
- Keep individual, led, shared, and supporting work distinct.
- If the source has no evidence for an effect, keep the concrete action or flag the gap instead of inventing a result.
- Preserve the established language and actual work of operations, planning,
  QA, design, marketing, customer service, research, or education. Do not turn
  every field into one generic achievement template.
- Select, remove, or reorder experience only when the user asks for composition,
  tailoring, or a structural review.
- Match the document's established bullet style. Use complete sentences for an
  introduction or application essay; concise action-noun endings such as
  `설계`, `구현`, `검증`, or `담당` can be natural in compact resume bullets.
- Within one section, do not alternate between noun endings and full predicates
  without a content or layout reason. Rewrite noun endings when they hide the
  action behind repeated abstractions such as `개선` or `강화`.
- Return paste-ready wording before diagnosis. Add questions only when a missing
  fact would materially change ownership, completion state, or claim strength.

See `resume.md` for the minimal examples that define evidence and contribution
boundaries.

### Application Motivation

Goal: connect a real experience to a specific organization or role and explain
a contribution the applicant can credibly make.

Rules:
- Start with one defensible connection, not a chronological self-introduction.
- Join the applicant's actual problem, choice, action, or learning with the
  organization's specific work and the role's responsibility.
- Do not place company praise beside an unrelated experience and call it a fit.
- Replace an interest declaration with the supplied reason the interest began
  and any action the applicant already took.
- Explain future contribution as an application of verified experience, not a
  large promise.
- Swap in another organization name as a diagnostic check. If the paragraph
  still works unchanged, make the connection more specific without inventing
  private company information.

Example:

Before: 고객 문의를 유형별로 나누면서 반복 문의가 환불 조건에서 시작된다는 점을 확인했습니다. 문의 데이터를 제품 정책에 반영하는 귀사의 운영 방식에 매료되어, 이 경험을 바탕으로 함께 성장하고 싶습니다.

After: 고객 문의를 유형별로 나눠 반복 문의가 환불 조건에서 시작된다는 점을 확인했습니다. 문의 데이터를 제품 정책에 반영하는 귀사의 운영 방식과 제 경험이 맞닿아 있어 지원했습니다.

### Documents and Reports

Goal: make the writing clear, structured, and professional without corporate fog.

Rules:
- Keep consistent terms for the same concept.
- Recast translation-like phrasing when it obscures the actual action. Keep
  a qualifier or intermediary when it changes the meaning.
- Keep formal vocabulary that fits a report. Do not swap a correct word for a
  more casual one only because it is shorter.
- Explain a necessary specialist term once at first use for a mixed audience.
  Do not repeat the same English expansion in parentheses after that.
- Avoid summary paragraphs that only repeat the section title.
- If a comparison or mismatch matters, name both sides. If the source only says
  that a check was run, do not write as though a defect was found.

Example:

Before: 자동 저장 기능을 통해 사용자가 작업 중이던 문서를 더 쉽게 다시 열 수 있을 것으로 예상합니다.

After: 자동 저장 기능으로 사용자가 작업 중이던 문서를 더 쉽게 다시 열 수 있을 것으로 예상합니다.

### Personal and Everyday Korean

Goal: make ordinary plans, requests, reactions, and personal writing sound
natural without flattening the writer's personality.

Rules:
- Keep the relationship, emotion, humor, and level of familiarity in the source.
- Prefer the words a person would actually use in that situation.
- Do not add warmth, jokes, slang, intimacy, or a stronger feeling than the
  source contains.

Example, in a message to a housemate who uses 반말:

Before: 제가 오늘 저녁 식사에 필요한 재료들을 구매하는 역할을 수행할 수 있도록 하겠습니다.

After: 오늘 저녁 재료는 내가 살게.

### Messenger and Chat

Goal: make the text sound like a real person wrote it in chat.

Rules:
- Keep messages concise without cutting one connected thought into isolated
  statements. Use natural connective endings or conjunctions where needed.
- Match the relationship, not the medium. A chat with a client or a senior can
  stay in 합쇼체; use contractions and softer endings only when they fit.
- Do not add emojis, slang, or over-familiarity unless already present.

Example, in work chat to a team lead:

Before: 제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.

After: 일정 확인해 보고 공유드릴게요.

### Email Between Colleagues

Goal: polite, clear, and low-friction. For email to customers, see
[B2B sales email](#b2b-sales-email).

Rules:
- Keep greeting and closing proportional to the relationship.
- Put the request early.
- Remove repeated apologies and ceremonial phrases when they slow the message.

Example:

Before: 저는 미팅 일정에 관하여 당신에게 말씀드리기 위해 이 메일을 쓰고 있습니다.

After: 미팅 일정 때문에 메일드립니다.

### Code Review Comments

Goal: make review comments clear, specific, and respectful without hiding the point.

Rules:
- Comment on the code, not the author.
- Replace vague evaluation such as `개선의 여지` with a concrete suggestion.
- Keep uncertainty only when the reviewer is actually unsure.
- Do not soften so much that the requested change becomes unclear.

Example:

Before: 해당 로직은 가독성 측면에서 개선의 여지가 있을 것으로 판단됩니다. 별도 함수로 분리하는 방향을 고려해볼 수 있을 것 같습니다.

After: 이 로직은 함수로 빼면 읽기 쉬울 것 같아요.

Before: 현재 구현은 예외 상황에 대한 처리가 충분하지 않은 상태로 보입니다. 실패 케이스를 고려한 방어 로직을 추가하는 것이 적절할 것 같습니다.

After: 현재 코드는 실패 상황을 충분히 처리하지 못하는 것 같아요. 실패 처리 로직을 보완하면 좋겠습니다.

Before: 이 변수명은 실제로 담고 있는 데이터의 의미를 명확하게 전달하지 못하고 있는 것으로 판단됩니다.

After: 이 변수명만 보면 어떤 값인지 바로 알기 어려워요.

### Public and Social Posts

Goal: make a public post credible and easy to understand in a short reading
session without turning it into clickbait or a compressed report.

Rules:
- Open with the actual observation, result, or tension already present in the
  source.
- Give each paragraph or post one main idea and enough context for a reader who
  did not see the underlying work.
- Keep numbers with their scope, comparison, and measurement status. Do not
  present reviewed data, edits, synthetic examples, user evidence, and adoption
  as the same kind of proof.
- Use verbs that fit the work actually performed. Do not make a review sound
  like a breakthrough or make an abstract noun perform a dramatic action.
- Treat internal paths and non-public implementation details as sensitive. When
  the text is clearly intended for publication, remove details that do not help
  the reader. If publication intent or permission is unclear, do not expose or
  silently delete them; flag them for confirmation.
- Avoid manufactured controversy, rhetorical hooks, engagement bait, and
  endings such as asking readers to agree without giving them a real next step.
- End with the implication, lesson, repository link, or concrete action already
  supported by the source.

Example:

Before: 한국어 AI 글쓰기의 판도를 바꿀 도구입니다. 12만 개가 넘는 한국어 응답을 훑고 7,500번 이상 표현을 직접 고쳐 얻은 압도적인 노하우가 어색한 문장을 가립니다. 여러분은 어떻게 생각하시나요?

After: 12만 개가 넘는 한국어 응답을 검토하면서 7,500번 이상 표현을 직접 고쳤습니다.

### Dialogue

Goal: preserve speaker voice, relationship, and scene pressure.

Rules:
- Do not normalize distinctive voice into generic polite Korean.
- Keep emotional subtext and pacing.
- Avoid modern chat phrasing if the scene or character voice does not support it.
