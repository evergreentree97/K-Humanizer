# Korean AI-Tell Patterns

Use these tables as routing rules, not a global find-and-replace list. First
decide what a phrase means in its sentence, then choose the matching rewrite.
Keep the source wording when an exception applies.

## Translationese and English-shaped grammar

| If the source uses | Use this when the condition fits | Keep or handle differently when |
|---|---|---|
| `~를 통해` for a tool, place, or action | Use `~로`, `~에서`, or make the action the verb: `분석을 통해 확인했다` becomes `분석해 확인했다` | The path, intermediary, or mediation itself is important |
| `~에 대해`, `~에 대한` before a direct object | Attach `을/를` to the object or combine the nouns: `오류에 대해 분석했다` becomes `오류를 분석했다` | The sentence genuinely introduces a topic rather than an action target |
| `~에 있어서` for a setting | Use `~에서` or delete it | The contrast between settings is the point |
| `가지고 있다`, `보유하고 있다` for simple possession | Use `있다`, `갖췄다`, or name the capability directly | Legal ownership or asset possession is the exact claim |
| `~에 의해` with a known actor | Make the actor the subject and use active voice | The actor is unknown, irrelevant, or intentionally withheld |
| `~하게 되었다`, `~지게 되었다` for a completed action | State the action directly | A real transition, external cause, or loss of control matters |
| Repeated `~할 수 있다`, `~할 것으로 보인다` | State the verified capability or result directly | Permission, possibility, or uncertainty is part of the meaning |
| `단순히 X가 아니라 Y`, `X를 넘어 Y` used for emphasis | State Y directly or name the real relationship between X and Y | The sentence corrects a genuine misunderstanding or the contrast changes the meaning |
| `~에 대해서는`, `~와 관련하여` | Use `~은/는`, `~의`, or a direct object | The phrase marks a real scope boundary or legal relation |

## Abstract nouns, filler, and empty weight

| If the source uses | Use this when the condition fits | Keep or handle differently when |
|---|---|---|
| Clusters such as `전략적`, `효과적`, `체계적`, `혁신적` | Name the action, rule, or observed property that makes it so | The adjective is a defined term or is supported by evidence in the source |
| `가능성`, `중요성`, `필요성`, `방향성`, `측면`, `관점`, `부분`, `요소` without a concrete referent | Replace the noun with the decision, action, or property it hides | The abstraction is the actual subject of analysis |
| `결론적으로`, `종합하면` before a repeated summary | Delete the transition and state the last finding | The text is a formal conclusion that adds a new decision or consequence |
| `시사하는 바가 크다`, `중요한 역할을 한다`, `긍정적인 영향을 미칠 것으로 기대된다` | State the source-backed consequence or next action | If no consequence exists in the source, delete the empty claim instead of inventing one |
| `다양한`, `의미 있는`, `성공적인`, `완성도 높은` without a standard | Name the items or the verified result | The source defines the range or evaluation standard |
| `전문가들은`, `업계에서는`, `사용자들은` without a source | Name the supplied source or narrow the statement | Do not invent a source; flag the missing basis when it affects the claim |
| `~라는 점입니다` only adds an ending | End with the actual judgment or difference | The construction identifies one item among several explicit points |

## Reader-facing specificity

Do not replace one abstract noun with another. Ask what the reader can see,
find, decide, or verify. If the source does not answer that question, keep the
claim narrow instead of filling the gap.

| If the source uses | Prefer when the reader needs the concrete behavior | Keep or handle differently when |
|---|---|---|
| `좋은 경험`, `의미 있는 변화`, `문제 상황` without a concrete referent | Name the event, change, or difficulty already present in the source | The writer is deliberately leaving a detail implicit in personal prose |
| `어긋남`, `맞지 않음`, `문제가 있다` without both sides of the comparison | Name what differed, when it happened, or what the reader needs to do | If only a check was performed, say what was checked; do not imply that a problem was found |
| A spatial metaphor such as `뒤로 숨기다`, `비껴가다`, or `다음 단계로 넘어가지 않게` | State the actual relationship, missed condition, or stop rule | The metaphor is intentional and natural in personal or creative writing |
| `꼼꼼히 살폈다`, `직접 검토했다`, `결과를 확인했다` without an object or method | Name what was reviewed and how it was checked when the source supplies it | The object and method are already clear from the surrounding sentences |

For product pages, dashboards, and documentation, remove self-introductions
such as `이 화면은 ... 하는 화면입니다` when the title or UI already says the
same thing. Replace `한눈에`, decorative subtitles, bold labels, and balanced
taglines with the actual items or states shown. Keep a subtitle when it adds a
real scope, constraint, or audience that the title does not contain.

## English and insider wording

Use plain Korean when insider vocabulary keeps a general reader from
understanding the sentence. The table below is for software or internal process
writing only; skip it for unrelated genres. Keep official product names,
identifiers, established domain terms, and exact job-posting keywords when
replacing them would reduce precision.

| If the reader does not need the internal term | Prefer |
|---|---|
| 컨텍스트 | 맥락, 조건, 배경, 앞선 내용 |
| 케이스 | 경우, 사례 |
| 이슈 | 문제, 쟁점 |
| 플로우 | 흐름, 절차 |
| 포인트 | 요점, 지점, 핵심 |
| 리스크 | 위험, 우려, 실패 가능성 |
| 체인 | 순서, 연결 관계 |
| 게이트 | 품질 기준, 통과 조건, 먼저 확인하는 단계 |
| 경합 | 두 로직이 같은 상태를 동시에 바꾸는 문제 |
| 승격 | 채택, 운영 모델로 전환 |
| 에이전트 | AI가 맡은 작업이나 자동화 범위 |
| 스킬 | 프로젝트 지침, 작업별 규칙 |
| 메모리 | 이전 대화 기록, 저장된 상태 정보 |
| 워크플로우 | 작업 절차, 반복 실행 절차 |
| 파이프라인 | 자동화 절차, 처리 단계 |
| 회귀 | 기존 기능의 동작 변경, 수정 전후 동작 차이, 품질 하락 |

Do not replace a term with another vague noun. Replacing
`품질 게이트를 고도화했다` with `품질 기준을 고도화했다` leaves the
abstraction unchanged. State the actual rule or check.

Keep exact names and established terms when precision matters, including legal,
medical, academic, culinary, product, and technical vocabulary. Naturalization
must not replace a documented method or category with a more fashionable but
unsupported alternative. When an awkward required term must remain, use it near
a concrete explanation instead of repeating it as a slogan.

## Rhythm and punctuation

U+2013 (en dash), U+2014 (em dash), and U+00B7 (middle dot) are hard bans in
rewritten prose. Restructure with a comma, period, colon, slash, parentheses, or
conjunction. Do not alter the character inside verbatim quoted text, code,
identifiers, or URLs; separate that material from the rewrite when necessary.

| If the source does this | Use |
|---|---|
| Places a comma immediately after `-고`, `-며`, `-지만`, `-면서`, `-아서`, `-어서`, `-는데`, or `-자` | Remove the comma. If the sentence remains long, split it at a complete thought |
| Uses a comma in more than half of the sentences | Split some sentences or absorb the pause into a connective ending; do not preserve English-like comma rhythm |
| Starts several sentences with `또한`, `그리고`, `따라서`, `특히`, or `이를 통해` | Delete the connector or state the actual relation such as cause, contrast, or sequence |
| Gives every sentence or bullet the same length and ending | Combine related points or split overloaded ones; do not add content only to vary rhythm |
| Forces three parallel items | Keep the number of items supported by the source |
| Ends several lines with noun phrases such as `~구축`, `~개선`, `~강화` | Turn some into complete predicates when the genre allows it |
