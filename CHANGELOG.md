# Changelog

All notable changes to K-Humanizer are recorded here. Versions follow
[Semantic Versioning](https://semver.org/): a minor version adds or changes
guidance, and a patch version fixes it without changing its scope. Dates use
the Korea Standard Time day of the release.

## Unreleased

- Split the changelog into versioned releases and add a version history to
  both READMEs.
- Move resume and job-application guidance into a separate
  `k-humanizer-resume` skill, so `k-humanizer` focuses on Korean for Korean
  customers.
- Remove internal planning and promotion drafts from `docs/`.

## 0.5.0 - 2026-11-07

Business Korean for Korean customers.

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
  only when a material fact is missing or source authority is unresolved.
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
- Tighten the editing and output instructions after an initial behavioral run
  (see below). Supplied Korean changes only where a concrete problem inside the
  requested scope can be named, and valid, ordinary wording stays. Natural
  Korean comes back as the Korean alone, with no verdict or edit list. Output
  notes are one or two sentences, and only for a corrected discrepancy or an
  unresolved item. When a material fact is missing, everything the source
  supports is still translated, only that fact stays as a placeholder such as
  `[보증 기간]`, and one question is asked. Samples and templates follow the same
  limits as the main text and do not add terms the source lacks. Paragraphs are
  read as a whole, so connectors that carry cause, contrast, or sequence are
  kept and no causal link is invented.
- Add 32 model-authored synthetic cases (27 business, 5 native-writing
  regression) in `evals/fixtures/business_korean.v1.jsonl`, covering all 15
  domain and input-mode pairs, with 7 unchanged-text cases and 3 cases that
  call for one clarifying question, plus `scripts/validate_business_set.py`
  and its tests. The business examples in `use-cases.md` still total 17.
- Record model-scored development checks in
  `evals/reports/2026-11-07-business-korean/business-review.md`, with Sonnet
  5.5 generating and Opus 5.5 judging. Each run is kept separately with its
  raw outputs, and none is pooled with another:
  - initial 30 cases: 26 met the expected behavior
  - full 32-case rerun: 29 met
  - unscored 7-case diagnostic batch
  - isolated final check of 7 selected cases plus one English-explanation
    probe, each request in a fresh `--safe-mode --restricted` process: 6 of 8
    met

  The judge flagged no hard failures, but review treated one beta-status
  wording as a real ambiguity. Still open: questions that go beyond the one
  missing fact, notes in Korean for English requests, and choppy paragraph
  flow. These are development-set checks, not held-out validation, human
  review, or a customer study.
- Resolve the findings of the initial source review: the register exception,
  default English versus approved Korean, business-only no-op coverage in the
  validator, delete-dialog scope, state versus possibility in merged clauses,
  actor, reason, and compact-label checks, and corrected explanations of
  `연중무휴 24시간` and streak wording.
- Recommend one clean process per case for evaluation in
  `docs/validation-plan.md`, and record batch runs separately.
- Point the rubric to the synthetic business fixture and the validation plan
  instead of repeating the fixture schema.
- Update the agent metadata with an English description for the new audience
  and a default prompt that also fits native writing.
- Rewrite both READMEs around the new audience, with copy-ready prompts for
  each input mode and links to the five business domains. Label all examples
  as synthetic, and the 220-case results and 2026-08-25 scores as records of
  the earlier version on synthetic Korean-only editing cases. Describe the
  preservation rules as the skill's instructions rather than a guarantee, link
  the observed results and their limits, and replace the bare English link in
  the Korean README with a line pointing to `README.en.md`. The English prompts
  now ask for notes and questions in English explicitly.
- Add unpublished promotion drafts in `docs/promotion.md` and update the
  positioning and task priorities in `docs/open-source-plan.md`.

## 0.4.0 - 2026-11-06

Context-first editing.

- Edit for the reader and purpose. Check each claim against the source,
  including negation, conditions, ownership, and the reasoning behind a
  decision. Preserve established terminology and natural wording.
- Replace character-change thresholds and blanket punctuation bans with the
  requested edit scope and the destination's style. Add synthetic review
  cases for the new guidance alongside the unchanged v0 benchmark.

## 0.3.1 - 2026-09-14

- Improve sentence and paragraph flow by preserving useful connectors, using
  natural connective endings, and avoiding unnecessary sentence splitting.
  Add synthetic review examples for continuity and unsupported causal links.

## 0.3.0 - 2026-08-25

Application motivation, public posts, and the first scored model baseline.

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

## 0.2.0 - 2026-08-17

Resume guidance and public validation.

- Add condition-to-rewrite tables with usage checks and exceptions instead of blind word replacement.
- Add evidence-safe resume rules for contribution boundaries, measurement conditions, completion state, and recruiter-facing terminology.
- Add reader-facing rules for personal writing, product/UI copy, vague claims, and exact terminology when the genre needs it.
- Add role-aware resume guidance for operations, planning, QA, design, marketing, customer service, research, and education.
- Add a resume workflow that humanizes supplied content by default and
  handles raw notes, job-targeted rewrites, and full-document reviews only when
  requested.
- Add a public v0 fixture integrity baseline that separates structural checks
  from future model-output scoring.
- Scan public evaluation reports for private-data patterns.
- Add a 30-second quick start and skills.sh badge to both READMEs.
- Expand the synthetic v0 golden set to 200 items, including 40 role-specific
  resume cases.

## 0.1.0 - 2026-07-04

First public release.

- Add portable `k-humanizer` agent skill.
- Add Korean writing references for use cases, patterns, and evaluation.
- Add validation and public hygiene scripts.
- Add GitHub Actions validation workflow.
- Add an 80-item synthetic v0 golden set.
