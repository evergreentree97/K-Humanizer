---
name: k-humanizer
description: Write, localize, and edit Korean so Korean readers find it natural. Use when someone needs Korean for Korean customers, including non-native speakers who translate English sales emails, ads, landing and product pages, support replies, service notices, or app UI and notifications into Korean, check a Korean translation against its English source, or fix Korean that sounds translated, stiff, or AI-written. Also covers resumes, applications, documents, messages, email, public posts, code review, and dialogue. Preserves meaning, commercial terms, placeholders, and the writer's voice.
---

# K-Humanizer

Produce Korean that a Korean reader would accept as written for them, without
changing what the text says. Many users cannot fully check the Korean
themselves, so accuracy comes before polish. AI detector scores are outside the
goal.

## 1. Identify the input mode

| Input | Task | Scope |
|---|---|---|
| Korean only | Edit the Korean | Keep the voice, structure, and register. Read the surrounding text for context, but edit only the passage the request covers, and only where it does not work. |
| English source with a Korean draft | Check the Korean against the source text, fix drift, then fix awkward Korean | Use the text the user names as the source. If they name none, use the English. Keep Korean wording that is accurate and natural. |
| English only, Korean requested | Translate and localize | Build each sentence in Korean order. Merge, split, or reorder sentences when Korean reads better, keeping every fact and condition. Do not aim for word-by-word correspondence or minimal change from a machine translation. |

When the Korean draft and the English disagree on a price, date, limit, policy,
or promise, do not silently pick one. Decide from what the user and the
context actually say:

- If the user names one version as approved, current, or authoritative, follow
  it without asking again.
- If the Korean clearly mistranslates the English, such as a dropped exclusion
  or a softened "only", and nothing marks the Korean as authoritative, fix it
  and say so in one line.
- If it is unclear which version governs and the choice would change
  commercial terms, ask one focused question, or keep the Korean and mark the
  clause as unresolved. Do not present that clause as verified, paste-ready
  copy.

A won price, a VAT note, or a Korea-specific policy does not by itself show
that the Korean was approved. Do not infer approval or local policy from
assumptions about the Korean market.

Translating Korean into English is a different task. Do it when asked, keep it
faithful, and do not apply this skill's Korean style guidance to the English.

## 2. Read the situation

Work out from the request, the text, and any existing Korean copy:

- **Audience:** consumers, business customers, partners, or an internal team.
- **Channel:** sales email, ad, landing or product page, app UI or
  notification, support reply, formal notice, or a native-writing genre such as
  a resume or chat message.
- **Brand register:** speech level (합쇼체, 해요체, or short labels) and how
  warm or restrained the brand sounds.
- **Purpose:** purchase, information, inquiry, apology, or guidance, and what
  the reader should do next.

Infer defaults from context. Professional does not mean stiff, and natural does
not mean casual. Unless the context points elsewhere:

- B2B email, contracts, and formal notices use 합쇼체.
- Consumer apps and many consumer brands use 해요체 in sentences.
- Buttons, headlines, banners, and spec tables can use noun phrases.
- Existing Korean strings, brand samples, or style guides override these
  defaults.

When the brand voice or another preference is missing, use these defaults and
draft. Mention an assumption in one line only when it materially shapes the
result, such as the speech level chosen for a new brand. Ask before drafting
only when a missing fact, such as a price or deadline, blocks the draft, or
when section 1 calls for a question about which version governs.

## 3. Write or edit

Read for meaning first: actor, action, reason, conditions, and outcome. Then
look for what a Korean reader would notice:

- Translationese and English word order
- Wording more formal or ceremonial than the channel needs
- English idioms Korean readers do not use
- Pronouns and subjects Korean leaves out, such as `당신`, `그것`, or `우리는`
- Long nominalized sentences
- Speech levels that mix without reason or do not fit the brand
- Calls to action that read like translated commands
- Repeated AI phrasing

Judge each sentence in its paragraph, for its reader and channel. No word is
banned: `통해`, `제공`, `진행`, and `관련하여` are ordinary Korean when they fit.
Do not shorten to meet a quota or swap a correct formal word for a casual
near-synonym. Read connected sentences together and keep the wording that
carries cause, contrast, sequence, or reference. Keep field terms readers
actually use, including English terms and loanwords, and explain an unfamiliar
term when the reader needs it. Use [patterns.md](references/patterns.md) to
diagnose phrasing and rhythm.

When the source gives no action, result, or reason, keep the claim narrow or
flag the gap. Use the writer's own wording or supplied samples for tone, never
as a source of facts.

## 4. Protect the facts and commitments

Keep these exactly, along with their conditions:

- Prices, currencies, discounts, and the conditions attached to them
- Product, plan, brand, and personal names
- Numbers and statistics, with their comparison and measurement conditions
- Contract terms, eligibility rules, and usage limits
- Dates, times, time zones, and deadlines
- Refund, exchange, delivery, and cancellation policy
- Warranty or guarantee scope and its exceptions
- Quotes, citations, code, and identifiers

Keep negation, exceptions, qualifiers such as "up to" or "about", levels of
certainty, and the difference between a request, an offer, and a promise.

Do not add benefits, performance claims, testimonials, urgency, scarcity,
apologies, commitments, sales hooks, or cultural references the source lacks.
Do not convert currencies, time zones, or units, or substitute local legal
terms, unless the user asks and supplies the basis. Writing a date or amount in
the usual Korean format is fine.

For UI strings and notifications, keep placeholders, variables, keys, and
markup exactly as written. A particle that depends on the last sound of an
unknown value, such as `{name}과`, can be wrong; restructure around it. Button
labels name the action they perform, and the text keeps the real outcome, such
as a permanent deletion or a charge.

## 5. Stop when the text works

Use the surrounding text for context, but edit only the passage the user asked
about. Supplied Korean keeps its voice and structure unless the request calls
for more. When translating from English, restructure sentences as section 1
allows, while keeping fields, keys, list items, and intentional formatting.
Already natural Korean stays unchanged; return it as is. Change structure,
select different material, or compose new passages only when the user asks.
Follow the destination's punctuation and formatting.

Compare the result with the source. Check each claim, condition, number, and
placeholder, and look for anything that disappeared. Read the result in
context to catch choppy sentences, newly implied causes, or generic wording
that flattened the writer's voice.

## Use the relevant reference

- **Business Korean:** For sales email, marketing and ad copy, landing and
  product pages, customer support and service notices, and app UI and
  notifications, use the business sections of
  [use-cases.md](references/use-cases.md). They show each input mode and
  several registers, including text that should stay unchanged.
- **Resumes, career descriptions, and portfolio summaries:** Read
  [resume.md](references/resume.md) and
  [resume-workflow.md](references/resume-workflow.md). When a target role is
  supplied, use [resume-roles.md](references/resume-roles.md) for terminology.
  Reorder experience only when the request calls for it.
- **Application motivation, documents, personal writing, chat, email between
  colleagues, public posts, code review, and dialogue:** Use the matching
  native-writing section in [use-cases.md](references/use-cases.md).
- **Reviewing or comparing edits and translations:** Use
  [evaluation.md](references/evaluation.md).

## Return the result

Put the Korean first, ready to paste. Keep string keys, subject and preheader
fields, list items, and intentional line breaks; within them, sentences may be
reordered, merged, or split as the input mode allows. A simple edit needs no
note. Add one only for a material discrepancy, an assumption that changes the
output, or uncertainty the user must resolve. Write notes in the language of
the request. Explain the changes, in English or another language, when the
user asks. For a review, separate meaning errors from optional style choices.
