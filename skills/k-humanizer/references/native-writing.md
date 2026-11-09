# Native Korean Writing Examples

## Contents

- [Native Korean writing](#native-korean-writing)
- [Documents and Reports](#documents-and-reports)
- [Personal and Everyday Korean](#personal-and-everyday-korean)
- [Messenger and Chat](#messenger-and-chat)
- [Email Between Colleagues](#email-between-colleagues)
- [Code Review Comments](#code-review-comments)
- [Public and Social Posts](#public-and-social-posts)
- [Dialogue](#dialogue)

All examples are synthetic. The revised versions illustrate expected behavior;
they are not recorded model outputs. Each is one acceptable answer, not an
exact-match target. Another wording passes if it keeps the same facts,
conditions, register, and reader action.

These examples cover native Korean writing such as documents, chat, and
dialogue. Korean written for Korean customers by non-native speakers is
covered separately. Resumes and job applications live in the separate
`k-humanizer-resume` skill.

## Native Korean writing

These sections cover Korean written by and for Korean speakers. The same
facts-first rules apply.

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
[B2B sales email](business-korean.md#b2b-sales-email).

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
