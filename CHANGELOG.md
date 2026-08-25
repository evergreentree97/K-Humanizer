# Changelog

## 0.1.0 - Unreleased

- Add portable `k-humanizer` agent skill.
- Add Korean writing references for use cases, patterns, and evaluation.
- Add condition-to-rewrite tables with usage checks and exceptions instead of blind word replacement.
- Add evidence-safe resume rules for contribution boundaries, measurement conditions, completion state, and recruiter-facing terminology.
- Add severity-based triage and a change budget so small problems receive small edits.
- Add reader-facing rules for personal writing, product/UI copy, vague claims, and exact terminology when the genre needs it.
- Add role-aware resume guidance for operations, planning, QA, design, marketing, customer service, research, and education.
- Add a resume-first workflow that humanizes supplied content by default and
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
