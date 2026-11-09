---
name: k-humanizer-resume
description: Edit Korean resumes, career descriptions, portfolio summaries, LinkedIn profiles, and job application essays so they read naturally and stay credible. Keeps every claim inside the supplied evidence, keeps individual and team work distinct, and keeps metrics with their conditions. For other Korean text, use k-humanizer.
---

# K-Humanizer Resume

Make Korean career documents read as if the applicant wrote them carefully,
without adding anything the source does not support. Natural wording cannot
repair missing evidence, so protect each claim before polishing the sentence.
AI detector scores are outside the goal.

## Read first

- [resume.md](references/resume.md) for every task: evidence rules, the
  conditional rewrite table, sentence order, and examples.
- [resume-workflow.md](references/resume-workflow.md) for every task: task
  type, section roles, tailoring, and output patterns.
- [resume-roles.md](references/resume-roles.md) when a target role or job
  posting is supplied.
- [application.md](references/application.md) for application motivation and
  "why this company" essays.
- [evaluation.md](references/evaluation.md) when reviewing or comparing edits.

## Rules

- Prefer problem or scope, judgment and action, then confirmed result over
  broad self-description.
- Remove inflated adjectives such as `탁월한`, `혁신적인`, `압도적인` unless
  the evidence supports them.
- Keep numbers with their comparison and measurement conditions.
- Keep individual, led, shared, and supporting work distinct. Never turn a
  plan into completed work, a team result into an individual result, or an
  unmeasured effect into a metric.
- If the source has no evidence for an effect, keep the concrete action or flag
  the gap instead of inventing a result.
- Preserve the established language and actual work of operations, planning,
  QA, design, marketing, customer service, research, or education. Do not turn
  every field into one generic achievement template.
- Select, remove, or reorder experience only when the user asks for
  composition, tailoring, or a structural review. Otherwise edit only the
  passage the user asked about, and keep wording that already works.
- Match the document's established bullet style. Use complete sentences for an
  introduction or application essay; concise action-noun endings such as
  `설계`, `구현`, `검증`, or `담당` can be natural in compact resume bullets.
- Within one section, do not alternate between noun endings and full
  predicates without a content or layout reason. Rewrite noun endings when they
  hide the action behind repeated abstractions such as `개선` or `강화`.
- Keep field terms recruiters and hiring managers actually use, including
  English terms, and explain insider wording only when the reader needs it.

When the k-humanizer skill is also installed, use its `patterns.md` to diagnose
translationese and AI phrasing.

## Return the result

Start with the paste-ready Korean. Add questions only when a missing fact would
materially change ownership, completion state, or claim strength. Write notes
and questions in the language of the request. Explain changes when the user
asks.
