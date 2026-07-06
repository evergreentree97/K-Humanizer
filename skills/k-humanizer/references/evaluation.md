# Evaluation Rubric

Score each output from 1 to 5.

Do not ask, "Will this bypass an AI detector?"

Ask, "Could someone actually use this sentence as-is?"

## Meaning Fidelity

Did the rewrite keep the same meaning?

5: Nothing important changed. Facts, names, numbers, dates, requests, and limits are all still there.

3: The main point is still there, but the strength or nuance changed a little.

1: The rewrite added a new claim, removed a condition, changed who does what, or changed the request.

## Korean Naturalness

Does it sound like Korean a person would write?

5: It reads naturally for the situation.

3: It is understandable, but still stiff, translated, or assistant-like.

1: It still sounds like English translated into Korean, awkward honorifics, or forced casual speech.

## Context Fit

Does it fit where it will be used?

5: It fits the reader, relationship, channel, and purpose.

3: It is usable, but a little too formal, too casual, too blunt, or too polished.

1: It is in the wrong style for the place, such as chat wording in an email or corporate wording in daily life.

## Edit Discipline

Did it change only what needed changing?

5: It removes awkward parts without touching what was already fine.

3: It improves the text, but changes more than it needs to.

1: It rewrites the writer's voice, structure, or details without a good reason.

## Practical Usefulness

Can the result be used right away?

5: Ready to send, paste, or publish.

3: Better than the input, but a human still needs to clean it up.

1: It is rewritten, but not useful in the real workflow.

## Domain Checks

After giving the five scores, check the domain-specific risks:

- Resume/profile: Did it avoid inventing metrics or making the achievement sound bigger than it is?
- Documents/reports: Are terms consistent? Is the point clear without ceremonial summary text?
- Messenger/casual: Is it short enough for chat? Did it avoid fake closeness, emojis, and slang unless asked?
- Everyday requests: Does it sound like normal coordination, not a translated task description?
- Email: Is the ask easy to find? Is it polite enough without hiding the point?
- Code review: Does it point to the code and give a concrete suggestion?
- Dialogue: Did it keep the speaker's voice, relationship, and scene tension?

## Red Flags

If any of these happen, the score should be 2 or lower even if the sentence sounds smoother:

- Adds a new fact, promise, metric, apology, or emotional stance.
- Removes a constraint, deadline, recipient, blocker, or uncertainty.
- Makes a review comment so soft that the action item becomes unclear.
- Turns ordinary chat into brand copy, corporate wording, or forced friendliness.
- Normalizes distinctive dialogue into generic polite Korean.

## Recommended Validation Set

Keep a small test set across real use cases:

- Resume/profile: 20 examples
- Documents/reports: 20 examples
- Messenger/casual: 20 examples
- Email: 20 examples
- Everyday requests: 20 examples
- Code review comments: 20 examples
- Dialogue: 10 examples

Each item should say what must stay the same and what should disappear:

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

For code review examples, include the requested action when there is one:

```json
{
  "id": "review_001",
  "domain": "code_review",
  "input": "...",
  "expected_traits": ["specific", "respectful", "clear action"],
  "must_preserve": ["extract helper function", "readability concern"],
  "avoid": ["개선의 여지", "고려해볼 수 있을 것 같습니다"]
}
```
