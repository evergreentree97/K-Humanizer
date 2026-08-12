---
name: k-humanizer
description: Use when editing Korean text to sound natural, human-written, and context-appropriate while preserving meaning. Trigger for Korean AI-tell removal, translationese cleanup, resume bullets, business documents, emails, messenger-style casual copy, reports, product copy, review comments, and dialogue text when the user asks to make Korean wording more natural, less stiff, less AI-like, or better matched to its reader, channel, and level of formality.
---

# K-Humanizer

## Core Rule

Make Korean text sound naturally written by a fluent Korean speaker without changing facts, intent, constraints, names, numbers, or quoted text.

Do not optimize for "AI detector bypass." Optimize for reader trust: clear meaning, believable rhythm, context-appropriate wording, and no over-polishing.

Never output U+2013 (en dash), U+2014 (em dash), or U+00B7 (middle dot) in
rewritten prose. If quoted text, a code identifier, or a URL contains one,
preserve the verbatim material separately instead of silently changing it.

## Workflow

1. Identify the writing context.
   - Personal/everyday: preserve the writer's relationship, emotion, humor, and
     level of familiarity; remove stiffness without adding a new personality.
   - Messenger/casual: short, spoken, context-aware, not overly friendly.
   - Email: polite but direct; remove ceremony that does not carry meaning.
   - Document/report/essay: clear hierarchy, stable terminology, restrained formality.
   - Resume/profile: read `references/resume.md`; protect evidence, ownership,
     measurement conditions, and contribution boundaries before polishing.
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

## Reference Files

Read the relevant reference only when the task needs it:

- `references/use-cases.md`: genre-specific rewrite rules and examples.
- `references/resume.md`: evidence-safe resume and career-document rules.
- `references/evaluation.md`: validation rubric for comparing outputs.
- `references/patterns.md`: Korean AI-tell checklist.
