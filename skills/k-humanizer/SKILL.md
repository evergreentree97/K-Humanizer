---
name: k-humanizer
description: Use when polishing Korean resumes, career descriptions, portfolio summaries, and application writing so they sound natural rather than AI-written across operations, planning, QA, design, marketing, customer service, research, education, and other fields. Preserve facts, meaning, ownership, results, field-specific terms, and the writer's voice while removing translationese, stiff abstraction, generic achievement claims, and mechanical structure. Compose from notes, restructure, or tailor to a job posting only when the user explicitly asks. Also use for natural Korean in documents, emails, messages, reports, product copy, review comments, and dialogue.
---

# K-Humanizer

## Core Rule

Make Korean text sound naturally written by a fluent Korean speaker without changing facts, intent, constraints, names, numbers, or quoted text.

Do not optimize for "AI detector bypass." Optimize for reader trust: clear meaning, believable rhythm, context-appropriate wording, and no over-polishing.

Never output U+2013 (en dash), U+2014 (em dash), or U+00B7 (middle dot) in
rewritten prose. If quoted text, a code identifier, or a URL contains one,
preserve the verbatim material separately instead of silently changing it.

## Resume First

Treat resumes and career documents as a high-stakes humanization task. The
default is to improve the supplied wording, regardless of field, without
choosing a different career story for the user. For every resume, career
description, portfolio summary, or application-writing task:

1. Read `references/resume.md` and `references/resume-workflow.md`.
2. If a target role or job description is supplied, also read
   `references/resume-roles.md`.
3. Preserve the field's established terms and the writer's actual experience.
4. Unless the user asks for composition or tailoring, do not select, remove, or
   reorder experience. Remove only the AI-like wording and awkward Korean.

Resume writing can be a light edit or a structural rewrite. Humanization is the
default, and the user's request sets any broader scope:

- Polish or humanize: edit only the supplied wording and follow the change budget.
- Turn notes into bullets: organize only facts present in the notes and expose
  any missing evidence that affects the claim.
- Tailor to a posting: only when requested, rank verified experience for one
  primary role and at most one supporting role. Do not copy requirements into
  the resume.
- Review a full resume: check section roles, repetition, evidence gaps, reader
  fit, and contribution boundaries before rewriting affected sections.

Do not force every career into one problem-action-metric formula. A policy
decision, exception rule, research method, design choice, release decision,
customer follow-up, or program operation can be useful experience without a
percentage.

## Workflow

1. Identify the writing context.
   - Personal/everyday: preserve the writer's relationship, emotion, humor, and
     level of familiarity; remove stiffness without adding a new personality.
   - Messenger/casual: short, spoken, context-aware, not overly friendly.
   - Email: polite but direct; remove ceremony that does not carry meaning.
   - Document/report/essay: clear hierarchy, stable terminology, restrained formality.
   - Resume/profile: follow the Resume First instructions and
     `references/resume-workflow.md`; preserve the field's normal language while
     removing AI-like phrasing, and protect evidence, ownership, measurement
     conditions, and contribution boundaries.
   - Product/UI copy: name what the reader can see or do; remove subtitles and
     self-descriptions that only repeat the title or component.
   - Dialogue: preserve speaker voice, relationship tension, and emotional beat.
   - Code review, when applicable: specific, respectful, and clear about the
     requested action.
   - Unknown: preserve the original register and only remove obvious stiffness.
2. Triage Korean AI-tell patterns before rewriting.
   - S1: factual drift, changed ownership or completion state, invented evidence,
     a hard-banned character, or wording that falsely claims a defect. Always fix.
   - S2: repeated translationese, abstract filler, register mismatch,
     decorative structure, or vague claims. Fix unless the genre needs it.
   - S3: an isolated stylistic preference. Leave it alone unless it repeats.
   - With no S1 issue and at most two S2 issues, edit only those spans or return
     the source unchanged. Do not run a full rewrite to justify the skill.
3. Detect the patterns that apply.
   - Translationese: `~를 통해`, `~에 대해`, `~에 있어서`, `가지고 있다`, `~할 수 있다` overuse.
   - Stiff nominalization: `~적인`, `~성`, `~화`, `~측면`, `~과정에서` clusters.
   - Generic AI closers: `결론적으로`, `시사하는 바가 크다`, `중요한 역할을 한다`.
   - Mechanical structure: repeated `첫째/둘째/셋째`, mirrored sentence lengths, excessive bullets.
   - Punctuation tells: English-like comma rhythm, needless quotes, decorative emphasis.
   - Vague wording: `좋은 경험`, unnamed `문제 상황`, empty self-evaluation,
     or metaphors and process nouns that do not say what happened.
   - Register mismatch: too formal for chat, too casual for email, too polished for personal writing.
   - Apply `references/patterns.md` as a condition table. Identify what the
     phrase does in the sentence before choosing a rewrite. Do not run blind
     word replacement.
4. Rewrite surgically.
   - Prefer verbs over abstract nouns.
   - Cut filler before adding new words.
   - Vary sentence endings only when it sounds natural for the genre.
   - Keep the user's level of confidence; do not make claims stronger.
   - Estimate the changed character share. Past roughly 30%, explain why. Past
     roughly 50%, stop and return a partial edit unless the user explicitly
     requested a rewrite or structural rework rather than humanization.
5. Self-check.
   - Meaning preserved?
   - Register and formality appropriate for the target reader?
   - Any phrase that sounds like a generic LLM answer?
   - Any over-humanized slang, forced imperfection, or personality not present in the source?
   - For a resume, did the rewrite preserve who did the work, what was
     measured, and what remains unverified?
   - Did a proper name, domain term, verified cause, or confirmed result change?
   - Does the rewritten prose contain U+2013, U+2014, or U+00B7?

## Resume Workflow

When handling career material, use this order:

1. Classify the input as a finished bullet, raw notes, a job posting plus
   experience, or a full document.
2. Build an evidence boundary for each experience: problem or scope, judgment,
   action, ownership, status, result, measurement condition, and disclosure
   limit. Missing fields may stay missing.
3. Identify the document section. A summary positions the candidate, experience
   proves it, skills list relevant tools or domain knowledge, and a portfolio
   explains judgment and contribution. Do not repeat the same sentence across
   sections.
4. Use the supplied role to understand the reader and established terminology.
   Choose a primary and supporting role only when the user explicitly asks for
   job-targeted restructuring.
5. Draft the smallest usable version first. Lead with the evidence that answers
   the target reader's hiring question and keep tools as supporting detail.
6. Check that every bullet can be traced to the source and that a recruiter can
   explain what the person actually did.

## Output

For short requests, return only the polished Korean text unless the user asks for explanation.

For review-style requests, use:

```markdown
수정본:
[polished text]

주요 변경:
- [brief reason]
```

For sensitive or high-stakes text such as resume, legal, medical, finance, or official documents, preserve claims exactly and flag uncertain wording instead of inventing details.

For resume requests, return paste-ready wording first. Add `확인 필요` only when
missing information prevents a reliable claim, and ask no more than three
questions at once. Do not bury a usable edit under a long diagnosis.

For a full resume review, organize feedback by the actual document sections and
separate these three states:

- Ready to use: supported wording that can be pasted now.
- Needs evidence: a useful experience with a missing ownership, state, result,
  or measurement condition.
- Remove or move: repetition, unsupported self-evaluation, irrelevant detail,
  or content placed in the wrong section.

## Reference Files

Read the relevant reference only when the task needs it:

- `references/use-cases.md`: genre-specific rewrite rules and examples.
- `references/resume.md`: evidence-safe resume and career-document rules.
- `references/resume-workflow.md`: input classification, evidence extraction,
  section structure, and paste-ready resume output rules.
- `references/resume-roles.md`: field-specific language and optional evidence
  order for operations, planning, QA, design, marketing, customer service,
  research, and education.
- `references/evaluation.md`: validation rubric for comparing outputs.
- `references/patterns.md`: Korean AI-tell checklist.
