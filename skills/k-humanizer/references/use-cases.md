# Use Cases

## Resume and Profile

Goal: make achievements concrete, credible, and easy to scan.

Rules:
- Read `resume.md` before editing a resume or career document.
- Read `resume-workflow.md` to classify finished bullets, raw notes,
  job-targeted rewrites, and full-document reviews.
- Read `resume-roles.md` when a target role or job description is supplied.
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
boundaries. Keep broader coverage in the golden set instead of duplicating it
in the runtime prompt.

## Application Motivation

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

## Documents and Reports

Goal: make the writing clear, structured, and professional without corporate fog.

Rules:
- Keep consistent terms for the same concept.
- Replace `~에 있어서`, `~측면에서`, `~을 통해` with direct phrasing.
- Explain a necessary specialist term once at first use for a mixed audience.
  Do not repeat the same English expansion in parentheses after that.
- Avoid summary paragraphs that only repeat the section title.
- If a comparison or mismatch matters, name both sides. If the source only says
  that a check was run, do not write as though a defect was found.

Example:

Before: 이 기능은 사용자 경험을 더 나은 방향으로 가져가는 데 있어서 중요한 역할을 수행할 것으로 기대됩니다.

After: 이 기능은 사용자가 더 편하게 작업하는 데 도움이 됩니다.

## Product and UI Copy

Goal: tell the reader what they can see or do without making the interface
introduce itself.

Rules:
- Remove `한눈에`, decorative subtitles, and `이 화면은 ... 하는 화면입니다`
  when the title or component already carries the same information.
- Replace process nouns with visible items, actions, states, or failure behavior.
- Keep short labels short. Do not turn a UI label into explanatory marketing copy.

Example:

Before: 이 화면은 업로드한 문서와 처리 상태를 한눈에 확인할 수 있도록 구성된 대시보드입니다.

After: 업로드한 문서와 처리 상태를 보여줍니다.

## Personal and Everyday Korean

Goal: make ordinary plans, requests, reactions, and personal writing sound
natural without flattening the writer's personality.

Rules:
- Keep the relationship, emotion, humor, and level of familiarity in the source.
- Prefer the words a person would actually use in that situation.
- Do not add warmth, jokes, slang, intimacy, or a stronger feeling than the
  source contains.

Example:

Before: 제가 오늘 저녁 식사에 필요한 재료들을 구매하는 역할을 수행할 수 있도록 하겠습니다.

After: 저녁 재료는 내가 사갈게.

## Messenger and Casual Korean

Goal: make the text sound like a real person wrote it in chat.

Rules:
- Shorten sentences.
- Use contractions and softer endings only when they fit the relationship.
- Do not add emojis, slang, or over-familiarity unless already present.

Example:

Before: 제가 그 일정에 대해 체크한 이후에 당신에게 공유할 수 있도록 하겠습니다.

After: 일정 확인해보고 공유드릴게요.

## Email

Goal: polite, clear, and low-friction.

Rules:
- Keep greeting and closing proportional to the relationship.
- Put the ask early.
- Remove repeated apologies and ceremonial phrases when they slow the message.

Example:

Before: 저는 미팅 일정에 관하여 당신에게 말씀드리기 위해 이 메일을 쓰고 있습니다.

After: 미팅 일정 때문에 메일드립니다.

## Code Review Comments

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

After: 실패 케이스 처리가 빠져 있어서 방어 로직을 추가해야 할 것 같아요.

Before: 이 변수명은 실제로 담고 있는 데이터의 의미를 명확하게 전달하지 못하고 있는 것으로 판단됩니다.

After: 이 변수명만 보면 어떤 값인지 바로 알기 어려워요.

## Public and Social Posts

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

Before: 한국어 AI 글쓰기의 판도를 바꿀 도구입니다. 12만 개 응답을 훑고 7,500번 표현을 고쳐 얻은 압도적인 노하우가 어색한 문장을 가립니다. 여러분은 어떻게 생각하시나요?

After: 12만 개가 넘는 한국어 응답을 검토하면서 7,500번 이상 표현을 직접 고쳤습니다. 그 과정에서 반복해서 확인한 번역투와 과한 격식 문제를 K-Humanizer에 정리했습니다.

## Dialogue

Goal: preserve speaker voice, relationship, and scene pressure.

Rules:
- Do not normalize distinctive voice into generic polite Korean.
- Keep emotional subtext and pacing.
- Avoid modern chat phrasing if the scene or character voice does not support it.
