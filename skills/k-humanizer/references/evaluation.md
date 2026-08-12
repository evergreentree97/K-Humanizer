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

For a humanization request, estimate the changed character share. A result over
roughly 30% needs a reason. A result over roughly 50% should be treated as a
rewrite and returned only when the user requested that larger scope.

## Practical Usefulness

Can the result be used right away?

5: Ready to send, paste, or publish.

3: Better than the input, but a human still needs to clean it up.

1: It is rewritten, but not useful in the real workflow.

## Domain Checks

After giving the five scores, check the domain-specific risks:

- Resume/profile: Did it preserve evidence, contribution boundaries,
  measurement conditions, completion state, and public wording?
- Documents/reports: Are terms consistent? Is the point clear without ceremonial summary text?
- Product/UI copy: Does it name visible content or actions without repeating the title or component type?
- Personal/everyday: Did it preserve the writer's relationship, emotion, humor, and level of familiarity?
- Messenger/casual: Is it short enough for chat? Did it avoid fake closeness, emojis, and slang unless asked?
- Email: Is the ask easy to find? Is it polite enough without hiding the point?
- Code review: Does it point to the code and give a concrete suggestion?
- Dialogue: Did it keep the speaker's voice, relationship, and scene tension?

## Red Flags

If any of these happen, the score should be 2 or lower even if the sentence sounds smoother:

- Adds a new fact, promise, metric, apology, or emotional stance.
- Removes a constraint, deadline, recipient, blocker, or uncertainty.
- Replaces an exact name, domain term, or confirmed cause with an unsupported alternative.
- Claims that a mismatch or defect was found when the source only says a check was run.
- Makes a review comment so soft that the action item becomes unclear.
- Turns ordinary chat into brand copy, corporate wording, or forced friendliness.
- Normalizes distinctive dialogue into generic polite Korean.

For a resume, also cap Meaning Fidelity at 1 when the rewrite:

- Turns a team result into an individual result.
- Turns a plan, proposal, candidate, or unshipped change into completed work.
- Adds an unmeasured performance, cost, stability, or productivity effect.
- Keeps a metric but removes its comparison target, sample, or evaluator when
  that condition was supplied.
- Reveals a private project name or infers personal ownership from a repository.
- Replaces a verified method or domain term with a different one.

## Resume-specific scoring

After the five general scores, check these independently:

- **Evidence boundary**: Every claim stays within the supplied source.
- **Contribution boundary**: Individual, led, shared, and supporting work remain distinct.
- **Measurement integrity**: Numbers keep the conditions that make them interpretable.
- **Decision clarity**: The problem, judgment, action, or result is easier to find.
- **Reader fit**: Specialized or insider wording is explained for a recruiter without erasing exact domain terms.

Any fabricated fact, metric, causal effect, or ownership claim is a hard fail
even when the Korean sounds natural.

For a full resume or career document, also check:

- **Target clarity**: The top section communicates one primary direction rather
  than combining every possible role.
- **Section discipline**: The summary positions, experience proves, skills name
  relevant knowledge, and the portfolio explains contribution and judgment.
- **Evidence distribution**: The strongest direct evidence appears before
  transferable or weakly related experience.
- **Repetition control**: The same achievement is not copied across the summary,
  experience, and skills sections.
- **Output usability**: Paste-ready wording comes before diagnosis, and missing
  information is raised only when it changes a material claim.

Do not penalize structural rewriting when the user explicitly asks to compose
from notes, tailor to a posting, or review a full document. Score edit discipline
against the requested task, while holding every factual boundary constant.

## Role-specific resume checks

When `resume_role` is supplied, also check whether the rewrite answers the
role's actual hiring questions:

- Operations: repeated work, exceptions, handoffs, deadlines, and operating results.
- Planning: problem, requirement, priority, scope decision, and validation state.
- QA: scope, environment, reproduction condition, severity, release decision, and follow-up.
- Design: user task, constraint, design decision, handoff, and usability evidence.
- Marketing/content: audience, channel, hypothesis, message, attribution, and measured response.
- Customer service: customer problem, policy, response, escalation, follow-up, and confirmed outcome.
- Research/data: question, method, sample, limitation, finding, and decision supported.
- People/education: learner or team need, program decision, delivery, participation, and later adoption state.

Do not penalize a role for lacking a percentage when the source has strong
qualitative evidence. Do penalize wording that imports a role keyword without
the action, condition, or decision that would support it.

## Recommended Validation Set

Keep a small test set across real use cases:

- Resume/profile: 90 examples, including 5 cases for each of 8 role groups
- Documents/reports: 20 examples
- Product/UI copy: 10 examples
- Personal/everyday: 20 examples
- Messenger/casual: 20 examples
- Email: 20 examples
- Code review comments: 10 examples
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
