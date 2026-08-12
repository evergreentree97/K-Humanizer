# Use Cases

## Resume and Profile

Goal: make achievements concrete, credible, and easy to scan.

Rules:
- Read `resume.md` before editing a resume or career document.
- Read `resume-roles.md` when a target role or job description is supplied.
- Prefer problem or scope, judgment and action, then confirmed result over broad self-description.
- Remove inflated adjectives such as `탁월한`, `혁신적인`, `압도적인` unless proven by evidence.
- Keep numbers with their comparison and measurement conditions.
- Keep individual, led, shared, and supporting work distinct.
- If the source has no evidence for an effect, keep the concrete action or flag the gap instead of inventing a result.
- Change the evidence order for operations, planning, QA, design, marketing,
  customer service, research, or education instead of forcing one universal
  achievement template across every role.

See `resume.md` for the minimal examples that define evidence and contribution
boundaries. Keep broader coverage in the golden set instead of duplicating it
in the runtime prompt.

## Documents and Reports

Goal: make the writing clear, structured, and professional without corporate fog.

Rules:
- Keep consistent terms for the same concept.
- Replace `~에 있어서`, `~측면에서`, `~을 통해` with direct phrasing.
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

## Dialogue

Goal: preserve speaker voice, relationship, and scene pressure.

Rules:
- Do not normalize distinctive voice into generic polite Korean.
- Keep emotional subtext and pacing.
- Avoid modern chat phrasing if the scene or character voice does not support it.
