# Validation Plan

K-Humanizer should be validated as a writing assistant, not as an AI detector bypass tool.

The primary evaluation target is business Korean written by people who are not
native Korean speakers and who work with Korean customers, partners, or users.
Native Korean writing, including resumes and everyday messages, remains in scope
and is still covered by the frozen v0 golden set and by a few regression cases
in the business supplement.

## Evaluation Questions

1. Does the output preserve the original meaning?
2. Does it sound like Korean someone would actually write in that context?
3. Does the wording fit the reader, relationship, channel, and purpose?
4. Did the skill avoid unnecessary rewriting?
5. Is the output ready to send, paste, or publish?

## Business Korean Evaluation

### Input Modes

Each business case uses one of three modes. Edit discipline depends on the mode.

| Mode | What the user supplies | Edit discipline |
|---|---|---|
| `korean_edit` | Korean text, often written by a non-native speaker | Fix what reads as translated, unclear, or wrong for the channel. Leave natural Korean alone. |
| `bilingual_edit` | An English source and a Korean draft | Compare meaning first, then wording. Follow the version the user names as authoritative, and tell the user about any mismatch instead of fixing it silently. |
| `english_to_korean` | English text to translate or localize | Write Korean that a native writer would use in that channel while carrying over every term, condition, and level of certainty. |

When the user designates an approved Korean text as current, an older English
version must not overwrite it. When a fact the user asks for is missing and
changes the output materially, ask one focused question rather than guessing.

When the user supplies English and Korean without naming either as approved or
current, English is the default source and the Korean is checked against it.
Do not ask which version is approved unless something in the request suggests
a local Korean policy override. If the two versions state conflicting
commercial terms, such as price, tax treatment, or refund conditions, and
neither is identified as approved, do not pick one. Ask one focused question
and keep both supplied values visible as alternatives.

### Business Domains

#### B2B Sales

Representative tasks:
- Quote, follow-up, and meeting emails to Korean buyers.
- Partner-deck lines that state pricing or discount eligibility.

Risks:
- Losing VAT status, seat minimums, contract length, or quote validity.
- Turning an evaluation, plan, or request into a promise or date.
- Adding pressure to sign that the sender did not express.

#### Marketing Ads

Representative tasks:
- Localize social and search ads in the brand's Korean voice.
- Make in-house ad copy read naturally for Korean shoppers.

Risks:
- Turning "up to" into a flat discount or dropping eligibility limits.
- Adding urgency, scarcity, seasonal hooks, or cultural references.
- Generalizing a survey result beyond its source and sample.

#### Landing and Product Pages

Representative tasks:
- Translate FAQ answers, pricing blocks, and security sections.
- Bring a product-page answer back in line with the product team's facts.

Risks:
- Making a guarantee or refund unconditional.
- Converting currency or billing period.
- Adding certifications, security absolutes, or release dates.

#### Support and Service Notices

Representative tasks:
- Formal maintenance and policy notices.
- Customer-service replies about refunds, delays, and incidents.

Risks:
- Adding apologies, compensation, or commitments that the source lacks.
- Turning "may" into "will" or an unconfirmed impact into a confirmed one.
- Converting business days to calendar days.

#### UI and Notifications

Representative tasks:
- In-app strings, push notifications, dialogs, and settings copy.

Risks:
- Renaming or removing placeholders, or attaching particles that break for some values.
- Stating a possible outcome as certain.
- Expanding a short label into an explanation.

### Tone and Length

Audience, channel, brand voice, and intent decide the tone. Formal notices stay
formal; a casual brand voice stays casual without slang the brand did not ask
for.

Words such as `통해`, `제공`, `진행`, and `관련하여` are not errors in
themselves. Replacing them only to avoid the word is over-editing. A shorter
output is not better when it drops a condition, an alternative, or a
connection the reader needs.

### Hard Failures

Treat any of these as a hard failure regardless of how natural the Korean
sounds:

- A price, rate, date, quantity, unit, currency, or threshold changes.
- A tax, discount, refund, delivery, warranty, or guarantee condition is lost,
  widened, or narrowed.
- A benefit, compensation, testimonial, certification, or claim is added.
- An apology, commitment, release date, or urgency is added.
- A commitment or fact is strengthened or weakened: a request, plan, or
  possibility becomes a promise or a certainty, or a firm commitment or
  confirmed fact becomes tentative.
- A placeholder is renamed, translated, or removed.
- A user-designated authoritative text is overwritten by the other version.
- A missing material fact is invented instead of asked about.
- An unresolved conflict between supplied versions is settled without asking,
  for example by treating one as approved because of its language or currency.

### Evidence Status

The two evaluation sets have different evidence status. Report them separately.

- **v0 golden set (historical, scored).** The 220 cases in
  `evals/fixtures/golden_set.v0.jsonl` and the scored outputs in
  [`evals/reports/2026-08-25/model-baseline.jsonl`](../evals/reports/2026-08-25/model-baseline.jsonl)
  are frozen. Their scores belong to the skill revision named in
  [the baseline report](../evals/reports/2026-08-25/model-baseline.md) and do
  not describe the business guidance. Do not edit, re-score, or extend these
  files.
- **Business supplement (synthetic).** The 32 cases in
  [`evals/fixtures/business_korean.v1.jsonl`](../evals/fixtures/business_korean.v1.jsonl)
  are synthetic examples authored for this workflow by a model from the
  maintainer's requirements. They are not customer data or customer evidence.
  Raw outputs and independent review artifacts belong under `evals/reports/`.
  Any result for this supplement must cite its own generator model, skill
  revision, and fixture revision, and applies only to that snapshot. The
  initial 30-case run and any later 32-case rerun are distinct snapshots: do
  not rewrite or rescore the first, and do not merge their counts.

### Business Supplement Format

The supplement has 32 cases: 27 business cases and 5 native regression cases.
It covers every pairing of the five business domains and the three modes.

| Coverage | Count |
|---|---|
| Business domains | `b2b_sales` 5, `marketing_ad` 5, `landing_page` 6, `support_notice` 6, `ui_notification` 5 |
| Native regression domains | `resume` 2, `everyday` 2, `document` 1 |
| Business modes | `korean_edit` 10, `bilingual_edit` 7, `english_to_korean` 10 |
| Expected behaviors, all cases | `produce_korean` 22, `keep_unchanged` 7, `ask_one_question` 3 |
| Expected behaviors, business cases | `produce_korean` 19, `keep_unchanged` 5, `ask_one_question` 3 |

The cases include already-natural business drafts that should stay unchanged,
cases that need one focused question, a bilingual draft whose eligibility
differs from the original, and an approved Korean policy that must not follow
an older English version. Two cases test source authority when no version is
designated: `bk_landing_006` supplies conflicting English and Korean pricing
and refund blocks with no approved version and expects one question while both
values stay visible, and `bk_support_006` supplies an unlabeled English source
and a Korean translation that turns a request into a refund promise and
expects a corrected Korean text, a brief note, and no question. Native
regression cases cover resume technical terms, everyday personal tone, and a
connected report paragraph with explicit uncertainty.

Native no-op cases do not count toward business coverage. The business cases
alone must include `keep_unchanged` and `ask_one_question` cases.

Each line is one JSON object:

```json
{"id":"bk_sales_001","domain":"b2b_sales","mode":"korean_edit","input":"...","grading":{"expected_behavior":"produce_korean","expected_traits":["..."],"must_preserve":["..."],"avoid":["..."]}}
```

| Field | Audience | Meaning |
|---|---|---|
| `id` | Generator and evaluator | Stable case identifier |
| `input` | Generator and evaluator | The complete request, including source text and any context the writer would give |
| `domain` | Coverage metadata | `b2b_sales`, `marketing_ad`, `landing_page`, `support_notice`, `ui_notification`, or a native regression domain: `resume`, `everyday`, `document` |
| `mode` | Coverage metadata | `korean_edit`, `bilingual_edit`, or `english_to_korean`; regression cases use `korean_edit` |
| `grading.expected_behavior` | Evaluator only | `produce_korean`, `keep_unchanged`, or `ask_one_question` |
| `grading.expected_traits` | Evaluator only | Qualities a usable output should have |
| `grading.must_preserve` | Evaluator only | Facts, terms, conditions, and voice that must survive |
| `grading.avoid` | Evaluator only | Semantic failures, such as an added benefit or a lost restriction |

All requirements are human-readable semantics, not exact target wording.
`avoid` entries describe failures of meaning or discipline, not banned words.
The fixture has no expected outputs; several different Korean outputs can pass
the same case.

Validate the supplement:

```bash
python3 scripts/validate_business_set.py
python3 -m unittest scripts.test_validate_business_set
```

The validator checks JSON syntax, object rows, field types, blank inputs and
list entries, duplicate IDs, unknown fields, domains, modes, and expected
behaviors, and the required coverage of business domains, business modes,
every business domain/mode pair, native regression domains, unchanged cases,
and question cases overall, and the business-only presence of unchanged and
question cases. It does not judge Korean quality.

`scripts/validate_golden_set.py` and `scripts/validate_model_baseline.py` are
tied to the v0 format and do not accept this fixture or outputs generated from
it.

### Business Forward Test

Run one bounded pass over all supplement cases in the fixture revision under
test (32 in the current fixture) per skill revision under test. Record the
fixture revision with the attribution, and keep each run's results separate. Do not retry cases, pick the best of several runs, or edit outputs.

1. **Record attribution.** Name the exact generator model ID and the skill
   revision. Use the composite form from the v0 baseline: the repository base
   commit, then `+skill-` and the first 12 characters of a SHA-256 digest over
   every file under `skills/k-humanizer`, sorted by relative path, with each
   path, a null byte, the file contents, and another null byte added in
   sequence. Record the full digest in the report and preserve the evaluated
   snapshot in a commit.
2. **Generate blind.** Give the generator the skill files and, for each case,
   only `id` and `input`. Do not show `domain`, `mode`, or anything under
   `grading`.
3. **Save raw outputs.** Write
   `evals/reports/YYYY-MM-DD/business-outputs.jsonl` with one object per case:
   `id`, `input` copied unchanged, the unedited `output` (including any
   question the generator asked), `generator_model`, and `skill_revision`.
   Record failed or empty generations instead of dropping them.
4. **Review independently.** Use a different model or a human reviewer who did
   not see the generation instructions. Give the reviewer each case's `input`,
   the `grading` block, the raw output, and the rubric in
   [`skills/k-humanizer/references/evaluation.md`](../skills/k-humanizer/references/evaluation.md).
   For each case, record whether `expected_behavior` was met, which
   `must_preserve` items were lost, which `avoid` failures occurred, whether a
   hard failure occurred, and short notes. Five rubric scores may be added.
   Write these to `evals/reports/YYYY-MM-DD/business-review.jsonl`, repeating
   `generator_model`, `judge_model` (or the human reviewer identifier), and
   `skill_revision` on every line.
5. **Report.** Summarize in `evals/reports/YYYY-MM-DD/business-review.md`:
   attribution, the number of cases reviewed, every hard failure, every missed
   `keep_unchanged` or `ask_one_question` case, and recurring failure types.
   Label model-scored results as model-scored, not human review. Keep failed
   cases in the totals.

No validator exists yet for the output and review files; check them by hand
against the fixture IDs and inputs until one is added.

Targets for the business supplement, not achieved results:

- Zero hard failures.
- `expected_behavior` met on every `keep_unchanged` and `ask_one_question` case.
- No native regression case loses voice, technical terms, contribution
  boundaries, or stated uncertainty.

## Legacy Domains (v0 Golden Set)

These domains are covered by the frozen v0 golden set. Their checks still
apply.

### Resume/Profile

Representative tasks:
- Rewrite resume bullets.
- Turn raw work notes into evidence-safe career bullets.
- Review a full resume by summary, experience, projects, and skills.
- Polish LinkedIn or portfolio summaries.
- Remove inflated claims while preserving achievements.
- Reorder verified evidence for operations, planning, QA, design, marketing,
  customer service, research, or education roles.

Risks:
- Inventing metrics.
- Making claims stronger than the source.
- Turning team results into individual results.
- Turning plans, proposals, or unshipped work into completed achievements.
- Removing the comparison, sample, condition, or evaluator from a metric.
- Replacing exact domain terms with approximate wording.
- Applying one achievement template to every role.
- Returning a long diagnosis before paste-ready wording.
- Repeating the same achievement in the summary, experience, and skills.
- Presenting a field change as past experience in the target role.
- Flattening personal voice.

### Application Writing

Representative tasks:
- Connect a verified experience to a specific organization or role.
- Explain why the interest began and what action followed.
- Turn earlier evidence into a credible contribution after joining.

Risks:
- Writing praise that works unchanged for any organization.
- Copying a job-posting phrase into the applicant's experience.
- Inventing private company information or a personal motivation.
- Promising an unverified future result.
- Hiding a genuine experience gap during a field change.

### Documents/Reports

Representative tasks:
- Clean up status reports.
- Simplify planning docs.
- Make summaries less stiff.

Risks:
- Losing precision.
- Replacing domain terms inconsistently.
- Claiming that a mismatch was found when the source only describes a check.
- Becoming too casual.

### Product/UI Copy

Representative tasks:
- Remove redundant subtitles and interface self-descriptions.
- Replace abstract process nouns with visible actions and states.
- Keep labels compact without turning them into marketing copy.

Risks:
- Removing a subtitle that adds real scope or a constraint.
- Inventing a screen behavior that the source does not state.
- Making a short label too explanatory.

### Personal/Everyday

Representative tasks:
- Rewrite ordinary plans, requests, reactions, and personal notes.
- Remove translated or assistant-like wording from daily conversation.
- Keep the writer's humor, emotion, and level of familiarity.

Risks:
- Adding fake warmth, jokes, slang, or intimacy.
- Making the message too casual for the relationship.
- Removing practical details such as time, place, responsibility, or emotion.

### Messenger/Casual

Representative tasks:
- Convert stiff assistant wording into natural chat.
- Make a message sound less cold.
- Shorten awkward formal Korean.

Risks:
- Adding fake warmth.
- Adding emojis or slang without permission.
- Changing relationship dynamics.

### Email

Representative tasks:
- Make a request clearer.
- Reduce excessive ceremony.
- Keep business-appropriate politeness.

Risks:
- Becoming too blunt.
- Removing needed courtesy.
- Changing the ask.

### Code Review Comments

Representative tasks:
- Turn vague review wording into a concrete suggestion.
- Keep review comments respectful without hiding the point.
- Remove filler such as `개선의 여지` when the requested action is known.

Risks:
- Making the request too soft to act on.
- Sounding accusatory toward the author.
- Losing the technical reason for the suggestion.

### Public and Social Posts

Representative tasks:
- Polish a title and body for a public reader.
- Keep numbers, firsthand observations, synthetic examples, and adoption signals distinct.
- Replace clickbait and mismatched dramatic verbs with source-backed wording.
- End with a concrete implication, lesson, link, or action.

Risks:
- Manufacturing controversy or asking for empty engagement.
- Presenting synthetic validation as user evidence.
- Making a review or edit sound like a breakthrough.
- Removing the scope or measurement status from a number.
- Exposing internal paths or private implementation details in a public rewrite.

### Dialogue

Representative tasks:
- Remove translated phrasing while preserving the speaker's voice.
- Keep relationship tension, emotional pace, and scene urgency.

Risks:
- Flattening a distinct voice into generic polite Korean.
- Adding slang or intimacy that the source does not support.
- Changing the emotional strength of the line.

## Golden Set Format

Use JSONL. The current v0 fixture is `evals/fixtures/golden_set.v0.jsonl`.
It is a frozen release snapshot; add new cases to a separate fixture instead.
It contains 220 synthetic cases: 90 resume, 10 application, 20 document,
20 personal/everyday, 20 messenger, 20 email, 10 product/UI copy, 10 public
post, 10 code review, and 10 dialogue cases. The resume set includes both
rewrite triggers and preservation cases
where a required intermediary, permission, contrast, domain identifier, or
exact job keyword must remain. Forty resume cases carry a `resume_role` field,
with five cases for each supported role group.

```json
{"id":"email_001","domain":"email","input":"...","expected_traits":["polite","direct"],"must_preserve":["meeting date"],"avoid":["다름이 아니오라"]}
```

Do not store private resumes, private emails, or real messenger logs without explicit anonymization.

Validate the fixture before publishing:

```bash
python3 scripts/validate_golden_set.py
```

## Scoring Rubric

Each output receives 1-5:

- Meaning fidelity
- Korean naturalness
- Context fit
- Edit discipline
- Practical usefulness

Release criteria for v1.0, measured on the v0 golden set:

- Average score >= 4.2 across all domains.
- Meaning fidelity >= 4.7.
- Practical usefulness >= 4.2.
- No critical factual drift in the golden set.
- No fabricated resume metric, causal effect, completion state, or ownership claim.

The business supplement uses the hard failures and targets in
[Business Korean Evaluation](#business-korean-evaluation) rather than these
averages.

## Public Dataset Candidates

Use these only after checking license and provenance:

- Hugging Face `coastral/korean-writing-style-instruct`: useful for style categories.
- Hugging Face `jojo0217/korean_safe_conversation`: useful for casual conversation wording.
- KatFish/KatFishNet project: useful for Korean AI-tell linguistic features.
- Public Korean corpus surveys such as Open Korean Corpora: useful for finding domain corpora.

## Manual Review Protocol

This protocol applies to the v0 golden set. The business supplement follows
[Business Forward Test](#business-forward-test).

For each release candidate:

1. Run the skill on all 220 golden-set cases with the model and version recorded.
2. Save outputs under `evals/reports/YYYY-MM-DD/`.
3. Score each output with the rubric.
4. Record the top 10 recurring failures.
5. Update only the smallest necessary rule or example.

Store one JSON object per case in the scored baseline. Repeat the generator
model, judge model or human reviewer identifier, and skill revision on every
line so a partial file remains attributable. Keep the fixture ID, domain, and
input unchanged; add the generated output, all five integer scores, a critical
failure flag, failure types, and review notes.

When an independent model performs the first scoring pass, name it in
`judge_model` and treat the result as model-scored. Do not present that result as
human review. A human reviewer can replace the judge identifier and scores or
publish a separate reviewed file.

Validate completeness and score ranges before writing the summary report:

```bash
python3 scripts/validate_model_baseline.py \
  evals/reports/YYYY-MM-DD/model-baseline.jsonl
```

The validator requires all fixture IDs, checks that source inputs and domains
still match, and prints overall score averages and critical-failure count. It
does not fail a valid baseline merely because its scores miss the release
criteria; failed cases must remain visible in the report.
