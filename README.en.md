# K-Humanizer

[![Validate](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml/badge.svg)](https://github.com/evergreentree97/K-Humanizer/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20%7C%20Cursor-blue)](skills/k-humanizer/SKILL.md)
[![Language: Korean](https://img.shields.io/badge/Language-Korean-red)](skills/k-humanizer/SKILL.md)
[![Status](https://img.shields.io/badge/Status-v0.1%20pre--release-yellow)](CHANGELOG.md)
[![skills.sh](https://skills.sh/b/evergreentree97/K-Humanizer)](https://skills.sh/evergreentree97/K-Humanizer)

[한국어](README.md)

K-Humanizer is an Agent Skill for Codex, Claude, and Cursor that helps you
write Korean your Korean customers will read as natural. It is for people who
sell to, support, or build products for Korean customers and are not native or
fully fluent Korean readers, whether they read no Korean or some.

Machine-translated Korean is often correct but stiff. It keeps English word
order, carries over pronouns Korean leaves out, and uses a tone that does not
fit the channel. Sometimes it is also wrong in ways that are hard to catch
unless you read Korean closely, such as a dropped shipping exclusion or a
refund the English never offered. K-Humanizer rewrites the Korean for its
reader and channel, and its instructions say to keep prices, dates, policies,
and placeholders exact.

The example below is synthetic. The revised Korean illustrates the expected
result; it is not a recorded model output.

```text
English        Refunds can only be requested through in-app chat within 7 days of delivery.
               Opened items cannot be refunded unless they arrived damaged.

AI-translated  환불은 배송일로부터 7일 이내에 앱 내 채팅을 통해서만 요청이 가능합니다.
               개봉된 상품은 파손된 상태로 도착한 경우가 아닌 한 환불이 불가능합니다.

Revised        환불은 상품을 받은 날부터 7일 이내에 앱 채팅으로만 신청할 수 있습니다.
               개봉한 상품은 받았을 때 이미 파손되어 있던 경우에만 환불받을 수 있습니다.
```

The machine translation is understandable, but its second sentence is a double
negative ("unless ... cannot") that Korean readers have to untangle. The
revision states the same rule directly and reads like a Korean help center.
The in-app-chat-only restriction, the 7-day window, and the damaged-on-arrival
exception all stay.

## Install

```bash
npx skills add evergreentree97/K-Humanizer --skill k-humanizer --full-depth
```

## Three ways to use it

**You have English and need Korean.** The skill translates and localizes,
rebuilding sentences in natural Korean order instead of matching the English
word for word.

```text
Use $k-humanizer to write this in natural Korean for our Korean customers.
Channel: landing page. Audience: small clinic owners.
Tone: friendly but professional.
Write any notes or questions in English.

[paste English]
```

**You have English and a Korean translation.** The skill checks the Korean
against the version you name as the source, or the English if you name none.
It fixes anything that drifted and smooths the Korean that is left. If you say
the Korean is approved or current, it follows the Korean without asking again.

```text
Use $k-humanizer to check this Korean translation against the English source.
Fix anything that drifted or sounds translated. Tell me in English about any
difference in prices, dates, or policies, and ask any questions in English.

English:
[paste English]

Korean:
[paste Korean]
```

**You have Korean only.** The skill edits within the scope you ask for and
keeps the existing tone and structure.

```text
Use $k-humanizer to make this Korean sound natural. It's a support reply to a
customer, so keep our formal tone. Briefly explain the changes in English.

[paste Korean]
```

The instructions put the Korean first, ready to paste. A simple edit or
translation comes back as the Korean alone, and text that was already natural
gets no "nothing to change" verdict or list of edits. Notes are one or two
sentences and cover only what you need to act on, such as a conflict between
the English and the Korean. Ask for English explanations and questions
explicitly, as the prompts above do: in our checks, some English requests
without that line got their notes in Korean.

### Context that helps

All of this is optional. Without it, the skill infers what it can from the text
or uses a sensible default. Its instructions say to ask first when it cannot
tell whether the English or the Korean commercial terms govern. If a fact such as a price or
period is missing, the instructions tell it to translate everything the source
supports, leave only that fact as a placeholder like `[보증 기간]`, and ask
about that one decision. They rule out lists of questions about hypothetical
variants or related terms.

- **Audience:** consumers, business buyers, partners, or your own team
- **Channel:** sales email, ad, landing page, app UI, support reply, or formal
  notice
- **Brand tone:** for example "formal and restrained" or "friendly", or a
  sample of your existing Korean copy
- **Purpose:** purchase, information, inquiry, apology, or guidance
- **Terms to keep:** product names, plan names, or approved Korean terms

### What it keeps exact

This section describes the skill's editing instructions. It is not a guarantee
that a model follows them every time; see [Evaluation](#evaluation) for what
was observed and its limits. Prices and policies are carried over from the text
you supply. The skill does not check whether they are correct.

Prices and currencies, discounts and their conditions, product and plan names,
numbers, dates and time zones, contract and eligibility limits, refund and
delivery policy, warranty scope and exceptions, and UI placeholders such as
`{name}`. It does not add benefits, urgency, testimonials, apologies, or
commitments, and it does not convert currencies or time zones.

When the English and Korean disagree on a price or policy, the skill does not
silently pick one. If you name the version to follow, it follows it without
asking again. If the Korean clearly mistranslates the English, it fixes the
Korean and tells you in one line. If it cannot tell which version governs and
the choice changes commercial terms, it asks one question or marks the clause
as unresolved. A won price or VAT note alone is not treated as proof that the
Korean was approved.

When it edits supplied Korean, the instructions allow a change only if it can
name a concrete problem within the requested scope: a meaning or fact error,
broken grammar, translationese a Korean reader would notice, or a register or
genre mismatch the user or context establishes. If the original wording is
valid and ordinary there, and the change would only swap in a synonym or trim a
particle, the original stays. Korean that already reads naturally comes back
unchanged. The skill reads a paragraph as a whole, keeps connectors that carry
cause, contrast, or sequence, and does not invent a causal link the source
lacks.

## Examples by channel

Each example shows the context, the English, a machine translation, the
revised Korean, and why the revision works. Some need no change at all. All
examples are synthetic, and the revised Korean illustrates the expected result
rather than a recorded model output.

- [B2B sales email](skills/k-humanizer/references/use-cases.md#b2b-sales-email)
- [Marketing and ad copy](skills/k-humanizer/references/use-cases.md#marketing-and-ad-copy)
- [Landing and product pages](skills/k-humanizer/references/use-cases.md#landing-and-product-pages)
- [Customer support and service notices](skills/k-humanizer/references/use-cases.md#customer-support-and-service-notices)
- [App UI and notifications](skills/k-humanizer/references/use-cases.md#app-ui-and-notifications)

## Korean written by Korean speakers

K-Humanizer still edits Korean that native speakers write: resumes,
application essays, documents, email, chat messages, public posts, code review
comments, and dialogue. This example is synthetic too.

```text
Before  고객 문의 분류 기준을 다시 정리하는 작업을 통해 주간 평균 처리 시간을 18시간에서 11시간으로 개선했습니다.
After   고객 문의 분류 기준을 다시 정리해 주간 평균 처리 시간을 18시간에서 11시간으로 줄였습니다.
```

The shorter sentence still says what changed and gives the same numbers. For a
resume, the skill keeps your experience order and terms your readers use, such
as `race condition` in a developer resume. If you want it to write bullets from
notes or reorder your experience for a job posting, ask for that directly.
[Native writing examples](skills/k-humanizer/references/use-cases.md#native-korean-writing), [Resume editing](skills/k-humanizer/references/resume.md), [Resume workflow](skills/k-humanizer/references/resume-workflow.md), [Role-specific examples](skills/k-humanizer/references/resume-roles.md)

## Why I built it

I reviewed more than 120,000 Korean responses and made over 7,500 edits. I used
those edits to document when to rephrase a sentence and when to leave it alone.

## Evaluation

The business Korean guidance is new.
[`evals/fixtures/business_korean.v1.jsonl`](evals/fixtures/business_korean.v1.jsonl)
holds 32 synthetic test cases: 27 cover all 15 pairs of the three input modes
and five business channels, and 5 check for native-writing regressions. Seven
of the 32 are text that should stay unchanged, and three are cases where the
skill should ask one question about a missing fact. A model authored them; they
are not taken from customer material. [Evaluation plan](docs/validation-plan.md)

While the guidance was being repaired, development checks ran with Sonnet 5.5
generating outputs and Opus 5.5 judging them separately. The final check ran
seven selected cases plus one probe that asks for English explanations, each
in its own fresh process. Six of the eight met the expected behavior, and the
judge marked no hard failures. These problems are still open:

- When one fact is missing, the skill sometimes asks about related details
  too.
- English requests sometimes get their notes and questions in Korean.
- A paragraph that sounds translated can stay choppy.

Case counts, two grading descriptions, and the harness changed between runs,
so the numbers cannot be pooled or read as an improvement. Every run, every
failed case, and the limits are in the
[business Korean check report](evals/reports/2026-11-07-business-korean/business-review.md).

These are model outputs on model-authored synthetic cases, scored by another
model. The cases are the same ones used to repair the instructions, so they do
not measure performance on unseen text. They are not a customer study and have
not had a native Korean reader's review, so they do not validate quality.

The records below measured an earlier version of the skill on synthetic
Korean-only editing cases and are unchanged. They do not measure translation or
business localization. The full 220-case set was not rerun against the current
skill; only its data validator was run.

The public golden set contains 220 synthetic examples, separate from the
responses I reviewed. It includes 90 resume examples, plus applications,
everyday conversation, email, documents, product copy, public posts, and code
review. [Fixture validation report](evals/reports/2026-08-25-fixture-baseline.md), [Original 200-case report](evals/reports/2026-08-17-fixture-baseline.md)

On August 25, 2026, `gpt-5.4` produced 220 answers using that version of the
skill. A separate Claude Opus session scored them. The average across five
measures was 4.765, and meaning fidelity averaged 4.800. The model judge
reported no critical changes to the facts. The report includes low-scoring
answers and a case where the score did not follow the rubric. [Model evaluation report](evals/reports/2026-08-25/model-baseline.md)

The scoring rubric, including hard fails for changed prices, policies, and
commitments, is in [evaluation.md](skills/k-humanizer/references/evaluation.md).

## Try it from a local checkout

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

The editing instructions are in the [skill file](skills/k-humanizer/SKILL.md).
[Use cases](skills/k-humanizer/references/use-cases.md), [Korean wording reference](skills/k-humanizer/references/patterns.md), [Evaluation rubric](skills/k-humanizer/references/evaluation.md)

## Contributing

Reports about awkward Korean and installation problems are welcome in Korean
or English. Reports from people writing for Korean customers in a second
language are especially useful. Make up an example that shows the same problem
as your real email, ad, or customer document, with invented companies,
products, and prices, before posting it. [Open an issue](https://github.com/evergreentree97/K-Humanizer/issues/new/choose), [Contribution guide](CONTRIBUTING.md), [Dataset research](docs/dataset-research.md)

## License

MIT. See [LICENSE](LICENSE).
