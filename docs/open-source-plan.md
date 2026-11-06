# Open Source Plan

## Positioning

K-Humanizer is an Agent Skill for writing Korean that Korean readers find
natural. Its primary users sell to, support, or build products for Korean
customers without being native or fully fluent Korean readers, including
people who read some Korean but cannot easily check a machine translation.
Korean speakers polishing their own writing remain a supported audience. It is not a generic paraphraser or an AI detector bypass tool.

Primary promise:

> Turn English, or a machine translation of it, into Korean that fits its
> Korean reader and channel, without changing prices, dates, policies, or
> commitments.

Primary channels:

- B2B sales email
- Marketing and ad copy
- Landing and product pages
- Customer support replies and service notices
- App UI and notifications

Supported native-writing channels: resumes, applications, documents, email
between colleagues, messenger, public posts, code review, and dialogue.
Changes for business Korean must not regress these.

Documentation language: `README.md` stays in Korean and `README.en.md` in
English, as an explicit bilingual choice. The English README is the entry point
for the primary audience, so both must describe the same capabilities.

## Scope

In scope:
- Translating and localizing English into Korean for customer-facing channels
- Checking a Korean translation against its English source for drift
- Korean AI-tell cleanup and translationese reduction
- Register and tone fit for the audience, channel, brand, and purpose
- Meaning-preserving rewrites that keep commercial terms exact
- Evaluation examples and release reports

Out of scope:
- Guaranteed AI detector bypass
- Plagiarism evasion
- Claim invention for resumes or marketing
- Legal or regulatory review. The skill keeps supplied policy text but does not
  check compliance with Korean consumer, advertising, or privacy law.
- Currency, time zone, or price conversion
- Automatic posting or sending messages
- Training or distributing a model

## Release Phases

### v0.1: Public Skeleton (done)

- Repo README
- MIT license
- Portable `skills/k-humanizer/SKILL.md`
- Use-case references
- 220-item v0 golden set with everyday, resume integrity, eight role-specific resume groups, application motivation, product/UI, public-post, code-review, and dialogue cases
- JSONL validation script

### v0.2: Validation Baseline (mostly done)

- Done: full model-scored report for the v0 golden set (2026-08-25), with
  weak cases and a failure summary
- Remaining: human review of the lowest-scoring cases

### v0.3: Business Korean (in progress)

- Three input modes: Korean only, English with a Korean draft, and English only
- Audience, channel, brand register, and purpose handling
- Hard fails for commercial drift in the evaluation rubric
- Five business domains in `use-cases.md`, each with at least three examples
- Synthetic fixture `evals/fixtures/business_korean.v1.jsonl`: 32 cases (27
  business, 5 native regression) covering all 15 domain and mode pairs
- Done: model-scored development checks (Sonnet 5.5 outputs, Opus 5.5 judge)
  with instruction repairs between runs, reported run by run in
  [business-review.md](../evals/reports/2026-11-07-business-korean/business-review.md).
  These are development-set checks, not held-out or human validation.
- Open in the final check: questions that go beyond the one missing fact,
  notes and questions in Korean for English requests, paragraph flow on a
  security section, and an intermittent beta-state ambiguity.
- Not done: a rerun of the 220-case v0 golden set for behavior. Only its data
  validator has passed against the current repository.

### v0.4: Deeper Coverage

- Optional, not yet validated: business examples for longer documents such as
  proposals, larger UI string sets, or regulated categories
- Email examples by relationship
- Messenger examples by closeness
- Document/report examples by setting
- Code review examples by severity
- Dialogue examples by relationship and scene pressure
- A pattern-count script only if review confirms a repeatable rule that can be
  detected without penalizing valid wording

### v1.0: Stable Release

- Stable skill prompt
- Public benchmark report covering business and native-writing fixtures
- Installation instructions tested with `npx skills`
- Contribution guide for adding examples safely

## Validation Design

Use four layers:

1. Golden-set checks: stable synthetic examples with no private data.
2. Public-dataset probes: optional local sampling from licensed datasets.
3. Independent model scoring: run the full fixture with generator and judge
   versions recorded, then publish weak cases as well as averages.
4. Human review: score meaning fidelity, Korean naturalness, context fit, edit
   discipline, and practical usefulness.

Business cases score meaning against the version the user names as
authoritative, or the English when none is named, and treat commercial drift
as a critical failure. The fixture format and release criteria are in
[validation-plan.md](validation-plan.md).

Keep the evidence types separate in public writing. A synthetic fixture is
test coverage, a model-scored run is a model judgment, and only a human pass
supports the phrase "human-validated". The business runs use model-authored
synthetic cases, one generator model, and one judge model; they are not a
customer study. The 2026-08-25 scores measured an earlier version on synthetic
Korean-only editing cases and are not business localization results.

## Differentiation From Existing Projects

Existing Korean humanizer projects already cover AI-tell removal, and general
translation tools already produce understandable Korean. K-Humanizer should
differentiate through:

- Output built for a user who may not be able to check it: Korean first, short
  notes (in English when the user asks for it; default language matching is
  not yet reliable), and a flag when the English and Korean disagree and the
  user has not named which governs.
- Three input modes with different edit scopes.
- Instructions that strictly protect prices, conditions, policies,
  commitments, and UI placeholders.
- Register chosen from the audience, channel, and brand, without assuming that
  natural means casual.
- Practical channel modes for business Korean and native writing.
- Role-aware resume evidence ordering for operations, planning, QA, design,
  marketing, customer service, research, and education.
- A clear policy against over-polishing, including returning natural text
  unchanged.
- Small portable skill structure.
- Synthetic before/after examples informed by real editing experience.

## Immediate Tasks

1. Keep public claims within the results and limits in
   [business-review.md](../evals/reports/2026-11-07-business-korean/business-review.md).
2. Before any draft in [promotion.md](promotion.md) is posted, recheck that
   its claims still match the repository.

Optional next validation steps, none of them performed or committed to:

- Write fresh held-out synthetic cases that were not used to repair the
  instructions, and run them one clean process per case.
- Rerun the full 32-case fixture with the isolated harness.
- Ask a native Korean speaker to review the business examples in
  `use-cases.md` and the business fixture.
- Rerun the full 220-case v0 golden set against the current skill to check
  native-writing behavior.
- Review the ten lowest-scoring cases in the 2026-08-25 model baseline.
- Run a human scoring pass before describing any benchmark as
  human-validated.
