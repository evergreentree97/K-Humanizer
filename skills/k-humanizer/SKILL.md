---
name: k-humanizer
description: Use when editing Korean text to sound natural, human-written, and context-appropriate while preserving meaning. Trigger for Korean AI-tell removal, translationese cleanup, resume bullets, business documents, emails, messenger-style casual copy, reports, product copy, review comments, and dialogue text when the user asks to make Korean wording more natural, less stiff, less AI-like, or better matched to its reader, channel, and level of formality.
---

# K-Humanizer

## Core Rule

Make Korean text sound naturally written by a fluent Korean speaker without changing facts, intent, constraints, names, numbers, or quoted text.

Do not optimize for "AI detector bypass." Optimize for reader trust: clear meaning, believable rhythm, context-appropriate wording, and no over-polishing.

## Workflow

1. Identify the writing context.
   - Resume/profile: concise, specific, active, no inflated achievement language.
   - Document/report: clear hierarchy, stable terminology, restrained formality.
   - Messenger/casual: short, spoken, context-aware, not overly friendly.
   - Email: polite but direct; remove ceremony that does not carry meaning.
   - Dialogue: preserve speaker voice, relationship tension, and emotional beat.
   - Unknown: preserve the original register and only remove obvious stiffness.
2. Detect Korean AI-tell patterns.
   - Translationese: `~를 통해`, `~에 대해`, `~에 있어서`, `가지고 있다`, `~할 수 있다` overuse.
   - Stiff nominalization: `~적인`, `~성`, `~화`, `~측면`, `~과정에서` clusters.
   - Generic AI closers: `결론적으로`, `시사하는 바가 크다`, `중요한 역할을 한다`.
   - Mechanical structure: repeated `첫째/둘째/셋째`, mirrored sentence lengths, excessive bullets.
   - Punctuation tells: English-like comma rhythm, needless quotes, decorative emphasis.
   - Register mismatch: too formal for chat, too casual for email, too polished for personal writing.
3. Rewrite surgically.
   - Prefer verbs over abstract nouns.
   - Cut filler before adding new words.
   - Vary sentence endings only when it sounds natural for the genre.
   - Keep the user's level of confidence; do not make claims stronger.
4. Self-check.
   - Meaning preserved?
   - Register and formality appropriate for the target reader?
   - Any phrase that sounds like a generic LLM answer?
   - Any over-humanized slang, forced imperfection, or personality not present in the source?

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
- `references/evaluation.md`: validation rubric for comparing outputs.
- `references/patterns.md`: Korean AI-tell checklist.
