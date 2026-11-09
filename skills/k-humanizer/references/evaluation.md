# Evaluation Rubric

## Contents

- [Scoring by input mode](#scoring-by-input-mode)
- [Meaning Fidelity](#meaning-fidelity)
- [Korean Naturalness](#korean-naturalness)
- [Context Fit](#context-fit)
- [Edit Discipline](#edit-discipline)
- [Practical Usefulness](#practical-usefulness)
- [Domain Checks](#domain-checks)
- [Red Flags](#red-flags)
- [Hard fails for business Korean](#hard-fails-for-business-korean)
- [Test fixtures](#test-fixtures)

Score each output from 1 to 5.

Do not ask, "Will this bypass an AI detector?"

Ask, "Could someone actually use this sentence as-is?"

## Scoring by input mode

Identify the input mode before scoring. The same output can be disciplined in
one mode and overreaching in another.

| Input mode | Source of meaning | How to judge the amount of change |
|---|---|---|
| Korean only | The supplied Korean | Surrounding text gives context; change only the requested passage, and only what does not work there. Unchanged natural text scores well. A coherent register stays unless the user asks or the context clearly shows a mismatch; a default assumption alone is not a reason to change it. |
| English source with a Korean draft | The version the user names as authoritative; the English when they name none | Fix drift and awkward wording. Keep accurate, natural Korean from the draft. Asking again about a source the user already named lowers Practical Usefulness. When authority over a commercial term is unclear, one focused question or a clearly marked unresolved clause is correct; an unflagged material conflict lowers Meaning Fidelity. |
| English only, Korean requested | The English | Judge the Korean as if it were written first in Korean. Restructuring sentences is expected. |

Do not score a translation by word overlap with a reference, by how closely it
follows English sentence boundaries, or by how little it differs from an
earlier machine translation. A Korean draft is evidence of what the user had,
not a target. Score the result by what it says, how a Korean reader in that
channel would read it, and whether the user can paste it without fixing it.

## Meaning Fidelity

Did the rewrite keep the same meaning? In translation mode, compare with the
English. In pair mode, compare with the source named in the input mode table.

5: All material claims survive, including who did what, why, under what conditions, and with what certainty. Negation, names, numbers, units, dates, and requests keep their meaning.

3: The main point is still there, but the strength or nuance changed a little. Certainty can drift in either direction: a possibility strengthened into a promise, or a firm commitment or confirmed fact weakened into a hedge.

1: The rewrite added a new claim, removed a condition, changed who does what, or changed the request.

## Korean Naturalness

Does it sound like Korean a person would write, both sentence by sentence
and as a whole paragraph?

5: It reads naturally for the situation, with clear links between related thoughts.

3: It is understandable, but still stiff, translated, assistant-like, or choppy between sentences.

1: It sounds translated or forced, or reads as disconnected statements or a mechanical chain of connectors.

For multi-sentence prose, check whether useful conjunctions, connective
endings, and references survived the edit. A shorter output is not better when
the reader has to reconstruct the links. Do not require transitions between
independent bullets or labels, or erase deliberate pauses in dialogue.

Use these synthetic cases to review sentence flow. The possible edits are
examples, not exact-match targets; another natural edit may satisfy the same
conditions.

| Source | Possible edit or expected behavior | Must preserve or avoid |
|---|---|---|
| `신청 인원이 정원을 초과했습니다. 정원 초과로 접수를 조기 마감했습니다.` | `신청 인원이 정원을 초과했습니다. 그래서 접수를 조기 마감했습니다.` | Keep the stated reason for closing early without repeating it |
| `초안은 완성했습니다. 검토는 아직 끝나지 않았습니다.` | `초안은 완성했지만 검토는 아직 끝나지 않았습니다.` | Preserve both completion states and their contrast |
| `어제 안내문을 수정했습니다. 오늘 문의가 줄었습니다.` | Keep both observations; `오늘은` may make the time contrast clearer | Do not add `그래서` or claim the edit caused the decrease |
| `오늘은 비가 와서 산책은 미루려고 해. 대신 집에서 책을 읽을까 해.` | Leave unchanged | Keep `대신`, the casual voice, and the tentative plans |
| `자료를 확인했습니다. 그리고 표를 수정했습니다. 그리고 수정본을 보냈습니다.` | `자료를 확인하고 표를 수정한 뒤 수정본을 보냈습니다.` | Preserve the action order; do not replace each `그리고` with a different sentence-opening connector |


## Context Fit

Does it fit where it will be used?

5: It fits the reader, relationship, channel, and purpose.

3: It is usable, but a little too formal, too casual, too blunt, or too polished.

1: It is in the wrong style for the place, such as chat wording in an email or corporate wording in daily life.

For business Korean, check the speech level and tone against the audience,
channel, brand register, and purpose. A formal notice in 합쇼체 can score 5;
so can a consumer app string in 해요체. Do not reward casual wording as more
natural or formal wording as more professional by default.

## Edit Discipline

Did it change only what needed changing?

5: It removes awkward parts without touching what was already fine.

3: It improves the text, but changes more than it needs to.

1: It rewrites the writer's voice, structure, or details without a good reason.

Judge the edit against the request. A rewritten short phrase can be a local
edit. A small deletion can change a claim or erase the writer's voice.
Preserve structure and evidence selection unless the user asks to revisit them.
Check both the edits and the omissions.

When translating from English, Edit Discipline means keeping the content of
the source: no added offers, claims, or tone the brand did not choose, and
nothing dropped. It does not mean staying close to English sentence structure.

### Context and scope review cases

These synthetic cases supplement the frozen v0 benchmark. Review each output
against the stated context. Multiple wordings may pass.

| Context and source | What a usable edit preserves |
|---|---|
| Button in a draft form: `작성 중인 내용의 임시 저장을 수행합니다` | The action is saving a draft. `임시 저장` can replace the entire label without broadening the task. |
| Help article: `검토가 완료되지 않은 경우에도 임시 저장은 가능하나 제출은 불가합니다.` | Draft saving is possible before review ends. Submission is unavailable under that condition. |
| Engineering resume: `동시 요청에서 race condition이 발생해 같은 주문이 두 번 저장되는 문제를 확인. 주문 키에 UNIQUE 제약을 걸어 중복 저장 방지` | Keep the concurrent condition, observed duplication, method, and result. A familiar term such as `race condition` can stay. Keep compact bullet endings when they fit the resume. |
| Copyedit the grammar only in an approved line: `검토 기간은 3–5일이며 대상은 가입·인증 화면입니다.` | Leave the line unchanged. The range and approved grouping carry meaning. |
| Store policy notice: `교환은 구매하신 매장에서만 가능합니다. 온라인 주문 상품은 고객센터로 문의해 주세요.` | Leave it unchanged or make only a light edit. Exchanges are limited to the store of purchase, which `에서만` expresses, and online orders follow a different route. |
| Tighten a report: `새 안내를 올린 뒤 문의가 줄었습니다. 안내 수정이 영향을 줬는지는 아직 확인하지 못했습니다.` | Keep the order and decrease, along with the explicit uncertainty about cause. |

## Practical Usefulness

Can the result be used right away?

5: Ready to send, paste, or publish.

3: Better than the input, but a human still needs to clean it up.

1: It is rewritten, but not useful in the real workflow.

## Domain Checks

After giving the five scores, check the domain-specific risks:

- B2B sales email: Are the recipient's name and title, the reason for writing,
  and the request clear? Did it avoid invented results, references, or urgency?
- Marketing and ad copy: Does each offer keep its condition, exclusion, and
  deadline? Does the register match the brand without adding hype?
- Landing and product pages: Do qualifiers such as `최대` and `약`, spec
  conditions, prices, currencies, and VAT notes match the source?
- Customer support and service notices: Are apologies, commitments, policy
  limits, and exceptions at the same strength as the source?
- App UI and notifications: Are keys, variables, and markup intact? Do buttons
  name the action, and does the text keep the real outcome?
- Documents/reports: Are terms consistent? Is the point clear without ceremonial summary text?
- Product/UI copy: Does it name visible content or actions without repeating the title or component type?
- Personal/everyday: Did it preserve the writer's relationship, emotion, humor, and level of familiarity?
- Messenger/casual: Is it short enough for chat? Did it avoid fake closeness, emojis, and slang unless asked?
- Email: Is the ask easy to find? Is it polite enough without hiding the point?
- Public/social post: Does it lead with a real observation, keep numbers inside
  their source boundary, and avoid clickbait or empty engagement prompts?
- Code review: Does it point to the code and give a concrete suggestion?
- Dialogue: Did it keep the speaker's voice, relationship, and scene tension?

## Red Flags

If any of these happen, the score should be 2 or lower even if the sentence sounds smoother:

- Adds a new fact, promise, metric, apology, or emotional stance.
- Adds an unsupported cause, contrast, or sequence through a connector, or
  deletes a meaningful link while shortening the text.
- Removes a constraint, deadline, recipient, blocker, or uncertainty.
- Replaces an exact name, domain term, or confirmed cause with an unsupported alternative.
- Claims that a mismatch or defect was found when the source only says a check was run.
- Makes a review comment so soft that the action item becomes unclear.
- Turns ordinary chat into brand copy, corporate wording, or forced friendliness.
- When the source supplies a real organization-specific connection, replaces it
  with reusable praise, values, or job-posting phrases.
- Turns a public post into manufactured controversy, merges unlike evidence
  types, or makes the work sound larger through a mismatched dramatic verb.
- Exposes internal paths or non-public implementation details without clear
  permission.
- Normalizes distinctive dialogue into generic polite Korean.

## Hard fails for business Korean

Cap Meaning Fidelity at 1 and mark the case as a critical failure when the
output, compared with its source:

- Changes, drops, or adds a price, currency, discount, or discount condition.
- Changes a product, plan, or brand name.
- Changes a number or statistic, or removes the condition that qualifies it,
  such as "up to", "about", or a test mode.
- Changes or drops a date, time, time zone, or deadline.
- Weakens or drops a contract term, eligibility rule, usage limit, or "only"
  restriction.
- Changes refund, exchange, cancellation, or delivery policy, including a
  dropped exclusion.
- Widens or narrows warranty or guarantee scope, or drops an exception.
- Turns a request or possibility into a promise, or adds a refund, apology,
  compensation, or other commitment.
- Weakens a firm commitment or confirmed fact into a possibility, request, or
  hedge. Judge both directions against the governing source, which is the
  version the user named or a change in scope the user requested.
- Adds a benefit, performance claim, testimonial, urgency, scarcity, or sales
  hook the source does not contain.
- Converts a currency, time zone, or unit, or substitutes a legal term, without
  instruction.
- Overwrites the version the user named as authoritative, or silently
  resolves a material conflict between the English and Korean when neither the
  user nor the context settles which governs.
- Alters or removes a UI placeholder, variable, or key, or labels a button so
  that its action or outcome is unclear or different.

A hard fail applies even when the Korean reads naturally.

## Test fixtures

This rubric works without any other file. The K-Humanizer source repository
also keeps synthetic test fixtures:

- `evals/fixtures/golden_set.v0.jsonl`: 220 Korean-only editing cases, frozen
  as a historical baseline.
- `evals/fixtures/business_korean.v1.jsonl`: 30 model-authored cases, 25
  across the three input modes and five business domains and 5 native-writing
  regression cases.

The fixture format and release criteria are in `docs/validation-plan.md` in
that repository. Each case should state what must stay the same and what the
output should avoid. A fixture describes expected behavior; it is not evidence
of quality until outputs are generated and scored.
