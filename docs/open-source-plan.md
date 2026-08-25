# Open Source Plan

## Positioning

K-Humanizer should be positioned as a Korean-native writing polish skill, not as a generic paraphraser or detector bypass tool.

Primary promise:

> Make Korean text sound natural for its real channel: personal writing, everyday conversation, resume, application, document, product UI, messenger, email, public post, code review, or dialogue.

## Scope

In scope:
- Korean AI-tell cleanup
- Translationese reduction
- Genre-aware wording and formality adjustment
- Meaning-preserving rewrites
- Evaluation examples and release reports

Out of scope:
- Guaranteed AI detector bypass
- Plagiarism evasion
- Claim invention for resumes
- Automatic posting or sending messages
- Training or distributing a model

## Release Phases

### v0.1: Public Skeleton

- Repo README
- MIT license
- Portable `skills/k-humanizer/SKILL.md`
- Use-case references
- 220-item v0 golden set with everyday, resume integrity, eight role-specific resume groups, application motivation, product/UI, public-post, code-review, and dialogue cases
- JSONL validation script

### v0.2: Validation Baseline

- Full model-scored evaluation report
- Failure taxonomy
- Clear examples of what the skill refuses to change
- Human review of the lowest-scoring cases

### v0.3: Lightweight Metrics

- Pattern count script
- Change-rate guardrail
- Simple report generator

### v0.4: Deeper Domain Coverage

- Additional resume integrity and profile examples
- Email examples by relationship
- Messenger examples by closeness
- Document/report and product/UI examples by setting
- Code review examples by severity
- Dialogue examples by relationship and scene pressure

### v1.0: Stable Release

- Stable skill prompt
- Public benchmark report
- Installation instructions tested with `npx skills`
- Contribution guide for adding examples safely

## Validation Design

Use four layers:

1. Golden-set checks: stable, hand-authored, anonymized examples.
2. Public-dataset probes: optional local sampling from licensed datasets.
3. Independent model scoring: run the full fixture with generator and judge
   versions recorded, then publish weak cases as well as averages.
4. Human review: score meaning fidelity, Korean naturalness, context fit, edit
   discipline, and practical usefulness.

## Differentiation From Existing Projects

Existing Korean humanizer projects already cover AI-tell removal. K-Humanizer should differentiate through:

- Practical channel modes: personal writing, everyday conversation, resume, application writing, docs, product UI, messenger, email, public posts, code review, dialogue.
- Role-aware resume evidence ordering for operations, planning, QA, design, marketing, customer service, research, and education.
- Strict meaning preservation.
- Clear anti-overpolishing policy.
- A change budget that distinguishes polishing from rewriting.
- Small portable skill structure.
- Before/after examples from real editing patterns.

## Immediate Tasks

1. Review the ten lowest-scoring cases in the 2026-08-25 model baseline.
2. Add a small pattern-count script only if review confirms a repeatable rule
   that can be detected without penalizing valid wording.
3. Run a human scoring pass before describing the benchmark as human-validated.
