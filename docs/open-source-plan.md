# Open Source Plan

## Positioning

K-Humanizer should be positioned as a Korean-native writing polish skill, not as a generic paraphraser or detector bypass tool.

Primary promise:

> Make Korean text sound natural for its real channel: resume, document, messenger, email, or dialogue.

## Scope

In scope:
- Korean AI-tell cleanup
- Translationese reduction
- Genre-aware tone adjustment
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
- 80-item v0 golden set
- JSONL validation script

### v0.2: Validation Baseline

- Manual evaluation report
- Failure taxonomy
- Clear examples of what the skill refuses to change

### v0.3: Lightweight Metrics

- Pattern count script
- Change-rate guardrail
- Simple report generator

### v0.4: More Domains

- Resume/profile examples
- Email examples by relationship
- Messenger examples by closeness
- Document/report examples
- Dialogue examples, if kept general enough for public use

### v1.0: Stable Release

- Stable skill prompt
- Public benchmark report
- Installation instructions tested with `npx skills`
- Contribution guide for adding examples safely

## Validation Design

Use three layers:

1. Golden-set checks: stable, hand-authored, anonymized examples.
2. Public-dataset probes: optional local sampling from licensed datasets.
3. Human review: score meaning fidelity, naturalness, tone fit, and edit discipline.

## Differentiation From Existing Projects

Existing Korean humanizer projects already cover AI-tell removal. K-Humanizer should differentiate through:

- Practical channel modes: resume, docs, messenger, email, dialogue.
- Strict meaning preservation.
- Clear anti-overpolishing policy.
- Small portable skill structure.
- Before/after examples from real editing patterns.

## Immediate Tasks

1. Run K-Humanizer manually on the v0 golden set.
2. Score outputs with `docs/validation-plan.md`.
3. Add a first report under `evals/reports/`.
4. Add a small pattern-count script if the manual report exposes repeatable failures.
5. Publish the GitHub repo as `K-Humanizer`.
