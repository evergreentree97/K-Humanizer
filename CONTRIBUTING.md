# Contributing

Thanks for considering a contribution to K-Humanizer.

## What Helps Most

- Anonymized Korean examples for resumes, documents, messenger text, emails, product copy, review comments, or dialogue.
- Better pattern descriptions for Korean AI-like writing.
- Evaluation reports that compare outputs against the rubric.
- Documentation fixes.

## Privacy Rules

Do not contribute:

- Private resumes
- Private emails
- Real chat logs
- Customer data
- Proprietary project text
- Text that contains names, phone numbers, addresses, tokens, API keys, or internal URLs

If an example came from real work, rewrite it into a synthetic equivalent before submitting it.

## Golden Set Format

Use JSONL:

```json
{"id":"email_001","domain":"email","input":"...","expected_traits":["polite","direct"],"must_preserve":["meeting date"],"avoid":["다름이 아니오라"]}
```

Accepted domains for now:

- `resume`
- `document`
- `product_copy`
- `everyday`
- `messenger`
- `email`
- `code_review`
- `dialogue`

Role-specific resume cases may add `resume_role` with one of these values:

- `operations`
- `planning`
- `qa`
- `design`
- `marketing_content`
- `customer_service`
- `research_data`
- `people_education`

Validate before opening a pull request:

```bash
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

## Editing The Skill

Keep [skills/k-humanizer/SKILL.md](skills/k-humanizer/SKILL.md) small. Put detailed examples and checklists under `skills/k-humanizer/references/`.
