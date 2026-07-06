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
- Polish LinkedIn or portfolio summaries.
- Remove inflated claims while preserving achievements.

Risks:
- Inventing metrics.
- Making claims stronger than the source.
- Flattening personal voice.

### Documents/Reports

Representative tasks:
- Clean up status reports.
- Simplify planning docs.
- Make summaries less stiff.

Risks:
- Losing precision.
- Replacing domain terms inconsistently.
- Becoming too casual.

### Messenger/Casual

Representative tasks:
- Convert stiff assistant wording into natural chat.
- Make a message sound less cold.
- Shorten awkward formal Korean.

Risks:
- Adding fake intimacy.
- Adding emojis or slang without permission.
- Changing relationship dynamics.

### Everyday Requests

Representative tasks:
- Rewrite ordinary coordination messages.
- Shorten translated task-like phrasing.
- Make daily plans or requests sound like normal conversation.

Risks:
- Adding fake warmth.
- Making the message too casual for the relationship.
- Removing practical details such as time, place, or responsibility.

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

## Golden Set Format

Use JSONL. The current v0 fixture is `evals/fixtures/golden_set.v0.jsonl`.

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

## Public Dataset Candidates

Use these only after checking license and provenance:

- Hugging Face `coastral/korean-writing-style-instruct`: useful for style categories.
- Hugging Face `jojo0217/korean_safe_conversation`: useful for casual conversation wording.
- KatFish/KatFishNet project: useful for Korean AI-tell linguistic features.
- Public Korean corpus surveys such as Open Korean Corpora: useful for finding domain corpora.

## Manual Review Protocol

For each release candidate:

1. Run the skill on the golden set.
2. Save outputs under `evals/reports/YYYY-MM-DD/`.
3. Score each output with the rubric.
4. Record the top 10 recurring failures.
5. Update only the smallest necessary rule or example.
