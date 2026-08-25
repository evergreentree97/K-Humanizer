# Validation Plan

K-Humanizer should be validated as a writing assistant, not as an AI detector bypass tool.

## Evaluation Questions

1. Does the output preserve the original meaning?
2. Does it sound like Korean someone would actually write in that context?
3. Does the wording fit the reader, relationship, channel, and purpose?
4. Did the skill avoid unnecessary rewriting?
5. Is the output ready to send, paste, or publish?

## Domains

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

Release criteria for v1.0:

- Average score >= 4.2 across all domains.
- Meaning fidelity >= 4.7.
- Practical usefulness >= 4.2.
- No critical factual drift in the golden set.
- No fabricated resume metric, causal effect, completion state, or ownership claim.

## Public Dataset Candidates

Use these only after checking license and provenance:

- Hugging Face `coastral/korean-writing-style-instruct`: useful for style categories.
- Hugging Face `jojo0217/korean_safe_conversation`: useful for casual conversation wording.
- KatFish/KatFishNet project: useful for Korean AI-tell linguistic features.
- Public Korean corpus surveys such as Open Korean Corpora: useful for finding domain corpora.

## Manual Review Protocol

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
