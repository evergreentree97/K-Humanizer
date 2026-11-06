---
name: k-humanizer
description: Edit supplied Korean so it sounds natural for its reader and purpose. Use for awkward or AI-like phrasing in resumes, applications, documents, messages, emails, product copy, public posts, and dialogue. Preserve the writer's meaning, voice, and established terminology. Compose from notes, restructure, or tailor only when requested.
---

# K-Humanizer

Help the reader understand what the writer means in Korean that fits the
situation. Treat signs of translationese as clues to reread the text.
Evaluate the edit by meaning, readability, and fit for the reader. AI
detector scores are outside the editing goal.

## Edit in context

1. **Set the scope.** Identify the reader, purpose, format, and register from
   the request and surrounding text. Preserve the existing structure and
   register by default. If the user asks for a local edit, use nearby text to
   understand it and edit only the requested passage. Use the writer's own
   wording or supplied examples of the genre for tone, never as a source of
   facts.
2. **Read for meaning before rewriting.** Identify the actor, action, reason,
   conditions, and outcome. Keep negation, exceptions, deadlines, comparisons,
   levels of certainty, and the difference between a request and a promise.
   Preserve exact names, figures, units, citations, quotes, code, and
   identifiers. Keep field terms readers actually use, including English
   terms when those are clearer. Explain an unfamiliar term when the intended
   reader needs it.
3. **Fix the awkward thought where it occurs.** Rewrite an English-shaped
   sentence from its meaning instead of swapping words. Use the concrete
   action already supported by the source. If the source gives no action,
   result, or reason, keep the claim narrow or flag the missing information.
   Read connected sentences together. Keep the wording that carries cause,
   contrast, sequence, or a reference to the previous sentence. Use
   [patterns.md](references/patterns.md) when diagnosing phrasing or rhythm.
4. **Stop when the text works.** Leave natural wording alone. A short label
   may need a new phrase and a long paragraph may need only one local edit.
   Judge scope by what changed in the text, including its content, order,
   and voice. Follow the destination's punctuation and formatting conventions.
   Change structure, select different material, or compose new passages only
   when the user asks.
5. **Compare the finished text with the source.** Check each claim and any
   material that disappeared. Confirm that responsibility, conditions,
   certainty, and the reason for a decision still match. Read the result in
   context to catch choppy sentences, newly implied causes, or generic
   wording that flattened the writer's voice.

## Use the relevant reference

- **Resumes, career descriptions, and portfolio summaries:** Read
  [resume.md](references/resume.md) and
  [resume-workflow.md](references/resume-workflow.md). When a target role is
  supplied, use [resume-roles.md](references/resume-roles.md) for terminology.
  In a full review, inspect evidence, section roles, and repetition. Reorder
  experience only when the request calls for it. Keep the writer's
  contribution, the decision or method that explains it, and the conditions
  needed to interpret a result.
- **Application motivation:** Use the application section of
  [use-cases.md](references/use-cases.md) to preserve the applicant's own reason
  and any supported connection to the organization.
- **Messages, email, documents, UI, public posts, code review, and dialogue:**
  Use the matching section in [use-cases.md](references/use-cases.md) when the
  channel or relationship changes how the text should read.
- **Reviewing or comparing edits:** Use
  [evaluation.md](references/evaluation.md). Compare what each version says
  and how it reads in context.

## Return the result

Put the revised text first. For a small edit, give the text alone unless a
material ambiguity needs a note or the user asks for an explanation. For a
review, distinguish meaning errors from optional style choices. Flag only
evidence gaps that affect the wording, such as unclear ownership, an
unverified result, or an unsupported causal claim.
