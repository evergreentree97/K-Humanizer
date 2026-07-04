# Evaluation Rubric

Score each output from 1 to 5.

## Meaning Fidelity

5: all facts, claims, numbers, names, and intent preserved.
3: minor nuance drift.
1: new claims, removed constraints, or changed responsibility.

## Naturalness

5: fluent Korean for the target genre.
3: readable but still stiff or generic.
1: translationese, chatbot phrasing, or awkward over-humanization remains.

## Tone Fit

5: matches reader, relationship, and channel.
3: generally acceptable but slightly too formal/casual.
1: wrong register.

## Edit Discipline

5: removes friction without unnecessary rewriting.
3: some avoidable changes.
1: rewrites personality, facts, or structure without need.

## Recommended Validation Set

Keep a small golden set in four buckets:

- Resume/profile: 20 examples
- Documents/reports: 20 examples
- Messenger/casual: 20 examples
- Email: 20 examples

Each item should include:

```json
{
  "id": "email_001",
  "domain": "email",
  "input": "...",
  "expected_traits": ["polite", "direct", "no extra claims"],
  "must_preserve": ["date", "recipient", "request"],
  "avoid": ["다름이 아니오라", "공유드릴 수 있도록 하겠습니다"]
}
```
