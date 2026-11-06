# Changelog

## 0.1.0 - Unreleased

- Reposition K-Humanizer for people who write Korean for Korean customers
  without being native or fully fluent Korean readers. Native Korean editing,
  resumes, and applications remain supported.
- Add three input modes to the skill: Korean only (use surrounding text for
  context and edit only the requested passage), English with a Korean draft
  (check against the version the user names as the source, or the English by
  default, and fix drift), and English only (translate and localize in Korean
  sentence order while keeping fields, keys, and intentional formatting).
- Resolve English-Korean conflicts from what the user and context say: follow
  a named source without asking again, fix a clear mistranslation with a
  one-line note, and ask one question or mark the clause when it is unclear
  which version's commercial terms govern. A won price or VAT note alone does
  not count as approval.
- Identify audience, channel, brand register, and purpose, with defaults
  inferred from context. Use a default when the brand voice is missing; ask
  first only when a missing fact blocks the draft or source authority is
  unresolved.
- Protect prices, currencies, discounts, names, numbers, limits, dates, refund
  and delivery policy, warranty scope, and commitments. Do not add benefits,
  urgency, testimonials, apologies, or promises, or convert currencies and time
  zones. Keep UI placeholders and the real outcome of each action.
- Rework `use-cases.md` around five business domains (B2B sales email,
  marketing and ad copy, landing and product pages, customer support and
  service notices, app UI and notifications), each with at least three
  synthetic examples showing context, English, a machine translation, revised
  Korean, and an English explanation. Examples include unchanged text, formal
  notices, and restrained brands. Native-writing sections remain, with context
  added where an example changes the speech level.
- Update `patterns.md`: state that no word is banned, make rows for `통해`,
  `관련하여`, `진행`, `제공`, `~이 가능합니다`, carried-over pronouns, and double
  negatives conditional, add a register and endings section, and keep
  customer-facing loanwords and noun endings in headlines and labels. Simplify
  `~하도록 하겠습니다` only when the actor and commitment strength stay the
  same.
- Update `evaluation.md`: score by input mode instead of word overlap or edit
  size, add checks for the five business domains, and add hard fails for
  commercial drift. Replace the counselor-intermediary review case with a
  store-exchange case that keeps the same restriction.
- Add 30 model-authored synthetic cases (25 business, 5 native-writing
  regression) in `evals/fixtures/business_korean.v1.jsonl`, with
  `scripts/validate_business_set.py` and its tests. Model outputs for these
  cases have not been generated or scored.
- Point the rubric to the synthetic business fixture and the validation plan
  instead of repeating the fixture schema.
- Update the agent metadata with an English description for the new audience.
- Rewrite both READMEs around the new audience, with copy-ready prompts for
  each input mode and links to the five business domains. Label all examples
  as synthetic, and the 220-case results and 2026-08-25 scores as records of
  the earlier version on synthetic Korean-only editing cases.
- Add unpublished promotion drafts in `docs/promotion.md` and update the
  positioning and task priorities in `docs/open-source-plan.md`.

- Edit for the reader and purpose. Check each claim against the source,
  including negation, conditions, ownership, and the reasoning behind a
  decision. Preserve established terminology and natural wording.
- Replace character-change thresholds and blanket punctuation bans with the
  requested edit scope and the destination's style. Add synthetic review
  cases for the new guidance alongside the unchanged v0 benchmark.

- Improve sentence and paragraph flow by preserving useful connectors, using
  natural connective endings, and avoiding unnecessary sentence splitting.
  Add synthetic review examples for continuity and unsupported causal links.

- Add portable `k-humanizer` agent skill.
- Add Korean writing references for use cases, patterns, and evaluation.
- Add condition-to-rewrite tables with usage checks and exceptions instead of blind word replacement.
- Add evidence-safe resume rules for contribution boundaries, measurement conditions, completion state, and recruiter-facing terminology.
- Add reader-facing rules for personal writing, product/UI copy, vague claims, and exact terminology when the genre needs it.
- Add role-aware resume guidance for operations, planning, QA, design, marketing, customer service, research, and education.
- Add a resume workflow that humanizes supplied content by default and
  handles raw notes, job-targeted rewrites, and full-document reviews only when
  requested.
- Add 220-item synthetic v0 golden set, including 40 role-specific resume cases, 10 application-motivation cases, 10 public-post cases, and preserve-when-valid counterexamples.
- Add public and social post guidance for evidence boundaries, credible openings, subject-verb fit, and non-clickbait endings.
- Add application-motivation guidance that connects verified experience to an organization, role, and credible contribution.
- Clarify when compact Korean resume bullets may keep action-noun endings and when full predicates are more natural.
- Explain necessary specialist terms once for mixed audiences instead of repeating English expansions.
- Align the skill's UI description with its broader Korean-writing scope.
- Add negative-control tests for golden-set domain counts, unknown domains, and duplicate IDs.
- Add a scored-baseline validator that checks all fixture IDs, source inputs,
  model attribution, five rubric scores, and recorded failure labels before a
  quality report can be published.
- Add a complete 220-case `gpt-5.4` output baseline independently scored by
  Claude Opus, including domain averages, retained low-scoring cases, and a
  public failure summary.
- Add validation and public hygiene scripts.
- Add GitHub Actions validation workflow.
- Add a public v0 fixture integrity baseline that separates structural checks
  from future model-output scoring.
- Scan public evaluation reports for private-data patterns.
- Add a 30-second quick start and skills.sh badge to both READMEs.
