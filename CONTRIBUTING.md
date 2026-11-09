# Contributing to K-Humanizer

Thanks for helping K-Humanizer write Korean that feels natural to Korean
readers without changing the source. Contributions are welcome in Korean or
English.

## Current focus

The primary target is business Korean written by people who are not native
Korean speakers and who work with Korean customers, partners, or users: sales
emails, ads, landing pages, support notices, and UI text. Native Korean
writing, including resumes, documents, and everyday messages, remains in scope.

Business requests arrive in one of three input modes:

- `korean_edit`: Korean text to make natural, leaving already-natural Korean
  alone.
- `bilingual_edit`: an English source and a Korean draft to compare, following
  the version the writer names as authoritative.
- `english_to_korean`: English text to translate or localize without losing a
  term, condition, or level of certainty.

[`docs/validation-plan.md`](docs/validation-plan.md#business-korean-evaluation)
describes each mode, the business domains, and the hard failures in detail.

## Choose the right starting point

- If an output still sounds translated, stiff, or unlike the intended writer,
  open a [Korean naturalness report](https://github.com/evergreentree97/K-Humanizer/issues/new?template=naturalness-report.yml).
- If you have found a repeated writing habit with a clear rewrite condition and
  exception, open a [pattern proposal](https://github.com/evergreentree97/K-Humanizer/issues/new?template=pattern-proposal.yml).
- For installation, broken links, validation, or repository problems, open a
  [bug report](https://github.com/evergreentree97/K-Humanizer/issues/new?template=bug-report.yml).
- For a new use case or workflow, open a
  [feature request](https://github.com/evergreentree97/K-Humanizer/issues/new?template=feature-request.yml).
- Small typo and documentation fixes can go straight to a pull request.

For a change that affects the skill's behavior, start with an issue so the
condition, exception, and expected result can be agreed on before implementation.

## What helps most

- Synthetic Korean examples that expose a repeatable naturalness problem
- Pattern rules that say both when to rewrite and when to keep the source
- Evaluation cases that protect facts, numbers, terminology, authorship,
  completion state, and uncertainty
- Fixes for installation steps, links, and unclear documentation
- Reports from non-native Korean writers creating text for Korean readers
- Bilingual cases where a Korean draft drifts from its English source, or an
  approved Korean text must not follow an older English version

## Privacy comes first

Do not contribute real or lightly redacted:

- Resumes or application documents
- Emails or chat logs
- Customer messages or support data
- Company documents or proprietary project text
- Names, phone numbers, addresses, account details, internal URLs, tokens, or
  API keys

Removing a name is not always enough to make a real example safe. Recreate the
same writing problem with invented people, organizations, numbers, and context.
The example should still teach the rule without pointing back to its source.

Report leaked private data, credentials, or security problems through a
[private security advisory](https://github.com/evergreentree97/K-Humanizer/security/advisories/new),
not a public issue.

## Before and after examples

A useful language contribution includes four parts:

```text
Before: 고객 문의 분류 기준을 다시 정리하는 작업을 통해 처리 시간을 개선했습니다.
After:  고객 문의 분류 기준을 다시 정리해 처리 시간을 줄였습니다.

Reason: The source turns the action into a long noun phrase.
Must preserve: The work changed the classification rules. Do not invent a metric.
Keep the original when: "through" describes a real route or intermediary.
```

Do not propose a global find-and-replace rule. The same phrase can be awkward in
one sentence and necessary in another.

## Where changes belong

| Change | File or directory |
|---|---|
| Core routing and workflow | `skills/k-humanizer/SKILL.md` |
| Korean AI-writing patterns and exceptions | `skills/k-humanizer/references/patterns.md` |
| Use-case examples | `skills/k-humanizer/references/use-cases.md` |
| Resume rules | `skills/k-humanizer/references/resume*.md` |
| Evaluation criteria | `skills/k-humanizer/references/evaluation.md` |
| Public test fixtures | `evals/fixtures/` |
| Business supplement validator | `scripts/validate_business_set.py` |
| Scored baseline validator | `scripts/validate_model_baseline.py` |
| Reader documentation | `README.md` and `README.en.md` |

Keep `skills/k-humanizer/SKILL.md` small. Put detailed examples, domain rules,
and checklists under `skills/k-humanizer/references/`.

`evals/fixtures/golden_set.v0.jsonl` is a fixed release snapshot with expected
domain counts. Open an issue before changing it or proposing a new fixture
version. `golden_set.sample.jsonl` documents the format; it is not a collection
of real user submissions.

Business Korean cases belong in `evals/fixtures/business_korean.v1.jsonl`, a
separate synthetic supplement. Its schema, with `mode` and evaluator-only
`grading` fields, is defined in
[Business Supplement Format](docs/validation-plan.md#business-supplement-format);
follow that section rather than the v0 format below.

## Golden-set format (frozen v0)

This format and domain list apply only to the frozen v0 golden set. v0 fixtures
use JSONL, with one JSON object per line:

```json
{"id":"email_001","domain":"email","input":"...","expected_traits":["polite","direct"],"must_preserve":["meeting date"],"avoid":["다름이 아니오라"]}
```

Accepted domains:

- `resume`
- `application`
- `document`
- `product_copy`
- `everyday`
- `messenger`
- `email`
- `public_post`
- `code_review`
- `dialogue`

Role-specific resume cases may add `resume_role` with one of these values:

- `operations`
- `planning`
- `qa`
- `design`
- `marketing_content`
- `customer_service`
- `research_data`
- `people_education`

Every item must explain what the output should do, what it must preserve, and
what wording or behavior it should avoid.

## Pull request workflow

1. Fork the repository or create a focused branch if you have write access.
2. Make one coherent change. Avoid mixing a pattern proposal with unrelated
   documentation cleanup.
3. Add or update an evaluation example when behavior changes.
4. Run the relevant checks.
5. Open a pull request and complete the template, including the privacy
   checklist.

Typical validation commands:

```bash
python3 scripts/validate_golden_set.py
python3 scripts/validate_business_set.py
python3 -m unittest scripts.test_validate_golden_set scripts.test_validate_model_baseline scripts.test_validate_business_set
python3 scripts/validate_model_baseline.py \
  evals/reports/2026-08-25/model-baseline.jsonl
python3 scripts/check_public_hygiene.py
ruby -ryaml -e 'Dir[".github/**/*.yml", "skills/**/*.yaml"].sort.each { |path| YAML.load_file(path) }'
```

Documentation-only changes may not need a new fixture, but they must still pass
the public-hygiene check. If a command does not apply, explain why in the pull
request instead of leaving the validation section blank.

## Review criteria

Reviewers will check that the change:

- Makes the Korean more natural for the stated reader and context
- Preserves facts, numbers, names, terminology, authorship, uncertainty, and
  completion state
- Changes only what needs changing
- Includes a condition and exception for a new rule
- Uses entirely synthetic examples
- Keeps detailed guidance out of the core skill when a reference file is a
  better fit

## Changelog and releases

Add a line under `## Unreleased` in [CHANGELOG.md](CHANGELOG.md) for any
change that affects the skill, its references, the fixtures, or the public
documentation.

Maintainers cut a release by:

1. Choosing the version: a minor bump when guidance is added or its behavior
   changes, a patch bump when a fix keeps the scope the same.
2. Renaming `## Unreleased` to `## X.Y.Z - YYYY-MM-DD` and adding a new empty
   `## Unreleased` section.
3. Updating the version badge and the version history table in both READMEs.
4. Tagging the release commit `vX.Y.Z` and publishing a GitHub release with
   the changelog section as its notes.

By participating, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
