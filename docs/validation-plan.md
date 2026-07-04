# Validation Plan

K-Humanizer should be validated as a writing assistant, not as an AI detector bypass tool.

## Evaluation Questions

1. Does the output preserve the original meaning?
2. Does it sound natural in Korean?
3. Does the tone fit the channel?
4. Did the skill avoid unnecessary rewriting?
5. Did it remove obvious AI-like Korean patterns?

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

### Email

Representative tasks:
- Make a request clearer.
- Reduce excessive ceremony.
- Keep polite business tone.

Risks:
- Becoming too blunt.
- Removing needed courtesy.
- Changing the ask.

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
- Naturalness
- Tone fit
- Edit discipline

Release criteria for v1.0:

- Average score >= 4.2 across all domains.
- Meaning fidelity >= 4.7.
- No critical factual drift in the golden set.

## Public Dataset Candidates

Use these only after checking license and provenance:

- Hugging Face `coastral/korean-writing-style-instruct`: useful for style categories.
- Hugging Face `jojo0217/korean_safe_conversation`: useful for casual conversation tone.
- KatFish/KatFishNet project: useful for Korean AI-tell linguistic features.
- Public Korean corpus surveys such as Open Korean Corpora: useful for finding domain corpora.

## Manual Review Protocol

For each release candidate:

1. Run the skill on the golden set.
2. Save outputs under `evals/reports/YYYY-MM-DD/`.
3. Score each output with the rubric.
4. Record the top 10 recurring failures.
5. Update only the smallest necessary rule or example.
