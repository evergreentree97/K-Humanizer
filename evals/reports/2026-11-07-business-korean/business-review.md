# Business Korean Development Checks

Date: 2026-11-07

Status: Development checks only. Model-scored, not human-reviewed, and not
held-out validation. Problems remain open in the final check, listed under
[Open issues](#open-issues). The v1.0 release criteria are not claimed.

## What was tested and what this does not show

These are development checks of the business Korean guidance on synthetic
cases. `claude-sonnet-5-5` generated the outputs and `claude-opus-5-5` judged
them separately. The judge saw the request, the grading block, the output, and
the public rubric, but not the generation instructions.

The checks do not show:

- **Human or native-speaker quality.** No person scored any output.
- **Held-out performance.** Every case belongs to the development set used to
  repair the instructions. The one extra probe was written during the same
  work.
- **User or customer evidence.** A model authored all of the cases.
- **Production readiness.** Each result applies only to its own skill
  snapshot, fixture, harness, and pair of models.
- **A controlled improvement.** Case counts, two grading descriptions, and the
  harness all changed between runs. Do not pool the runs or read their
  differences as the effect of an instruction change alone.

The judge flagged no hard failures in any run. That label does not prove the
meaning was right; see [the beta wording](#the-beta-wording).

## Runs

| Run | Skill snapshot | Cases | Harness | Review | Expected behavior met | Judge hard failures | Missed |
|---|---|---|---|---|---|---|---|
| Initial | `36e28c6` / `skill-20bd9014b685` | 30, original fixture | One batch session | Opus 5.5 | 26 of 30 | 0 | `bk_sales_004`, `bk_sales_005`, `bk_landing_002`, `bk_ui_005` |
| Full rerun | `63506b3` / `skill-2fa71274a718` | 32, current fixture | One batch session | Opus 5.5 | 29 of 32 | 0 | `bk_sales_005`, `bk_ad_005`, `bk_landing_002` |
| Targeted batch | `8f78a22` / `skill-83f871d51c62` | 7 selected | One batch session | Not scored | — | — | — (observations below) |
| Isolated final | `8f78a22` / `skill-83f871d51c62` | 7 selected + 1 probe | One clean process per request | Opus 5.5 | 6 of 8 | 0 | `bk_sales_005`, `bk_ui_005` |

| Run | `keep_unchanged` met | `ask_one_question` met | Cases with an `avoid` finding |
|---|---|---|---|
| Initial | 6 of 7 | 0 of 2 | 3 |
| Full rerun | 7 of 7 | 2 of 3 | 2 |
| Isolated final | 1 of 1 | 0 of 2 | 3 |

Rubric averages, for reference only. The case sets differ, so these averages
cannot be compared across runs.

| Run | Meaning | Naturalness | Context | Edit discipline | Usefulness |
|---|---|---|---|---|---|
| Initial (30) | 4.933 | 4.600 | 4.833 | 4.700 | 4.733 |
| Full rerun (32) | 4.938 | 4.750 | 4.938 | 4.875 | 4.781 |
| Isolated final (8) | 5.000 | 4.375 | 4.500 | 4.500 | 4.125 |

Every figure above was counted from the review rows and the fixture
behaviors, and it matches [metrics.jsonl](metrics.jsonl). The judge's prose
summary of the full rerun said there were 8 unchanged-text cases because it
counted `bk_landing_003` twice; the fixture and the rows have 7.

## Attribution

All composite revisions use the base commit
`4fff3c7aa90826bdaf44ede9b71eb49f6422a619`. The skill digest is SHA-256 over
every file under `skills/k-humanizer`, sorted by relative path, adding each
path, a NUL byte, the file contents, and another NUL byte in sequence. Each
digest was checked against the snapshot commit that preserves it.

| Run | Skill revision | Full skill digest | Snapshot commit | Fixture SHA-256 |
|---|---|---|---|---|
| Initial | `4fff3c7aa908+skill-20bd9014b685` | `20bd9014b6853ef83e90f8bff1af5a7b24c5d1bb5543e2bb1254890a8d02c61b` | `36e28c630effbadfb6b9dfa8c12afc0ee7f57fb9` | `934235a5ac4787fbf30a4e96f8bc775a39fc7b29a1d052adcd0e19018bc8e8ae` |
| Full rerun | `4fff3c7aa908+skill-2fa71274a718` | `2fa71274a718d74fc29cf9fbc0c95f02efc9bc04dd82b1f809ae35bf41e1df48` | `63506b338fb5c91a7e6914cb17c6089ab072a1f2` | `ee5a8f0b6c7084981d2603d89d41ff38d5ed4454e8f99de6ee517446fc7ea593` |
| Targeted batch | `4fff3c7aa908+skill-83f871d51c62` | `83f871d51c62381d1965c82fdb3527165117ac8cf37f03c0bc8103b2fa08fa27` | `8f78a22e6d7796fdc34fe012af8c28e7954852d0` | source `ee5a8f0b…` (7 rows) |
| Isolated final | `4fff3c7aa908+skill-83f871d51c62` | `83f871d51c62381d1965c82fdb3527165117ac8cf37f03c0bc8103b2fa08fa27` | `8f78a22e6d7796fdc34fe012af8c28e7954852d0` | `1d39bd856fb5802931b0915d1854b1d0ce20c9161e2156b482f97c8555da2304` (source `ee5a8f0b…`) |

- The generator was `claude-sonnet-5-5` and the judge was `claude-opus-5-5`,
  as recorded on every raw row. The CLI at the start of the session was
  Claude Code 2.1.310.
- Every generation saw only each case's `id` and `input`. The grading
  metadata stayed hidden.
- User inputs and output strings are stored exactly as given and produced. The
  artifact wrappers add only attribution fields.
- [runs.jsonl](runs.jsonl) records the harness, the selected IDs, and how each
  run was verified.

## Fixture changes between runs

The current fixture,
[`business_korean.v1.jsonl`](../../fixtures/business_korean.v1.jsonl), has 32
cases: 27 business cases and 5 native regression cases. The original 30
inputs are unchanged. Changes since [initial-fixture.jsonl](initial-fixture.jsonl):

- Two grading descriptions were clarified. `bk_doc_reg_001` now accepts a
  consistent 합니다체 or 했다체 report register. `bk_ad_002` now allows keeping
  or dropping the source's redundant praise line.
- Two source-authority cases were added. In `bk_landing_006`, conflicting
  English and Korean pricing blocks come with no approved version, so the
  skill should ask one question. In `bk_support_006`, an unlabeled English
  source sits beside a Korean translation that promises a refund, so the skill
  should correct the Korean, add a note, and ask nothing.

The initial grades were not rewritten.

## Harness

The initial run, the full rerun, and the targeted batch each sent every case
as an independent request in one read-only, restricted Claude Code batch
session. Those sessions did not explicitly turn off host customizations or
the automatic discovery of `CLAUDE.md`. So unrelated local instructions could
have reached the generator, and a batch shares one context across cases.

The isolated final check ran each request in its own fresh process. It used
`--safe-mode` to turn off customizations and `CLAUDE.md` discovery,
`--restricted` for read-only tools, and loaded the pinned skill files
explicitly. This is a different method, not a controlled before-and-after
comparison. It cannot show that the instruction changes alone caused any
difference.

## Failed and caveated cases

Every case that missed its expected behavior is listed here. The judge's notes
are in the review files.

**Initial run** ([outputs](initial-outputs.jsonl), [review](initial-review.jsonl))

- `bk_sales_004` (should stay unchanged): made four stylistic swaps to
  already-natural Korean (`관련하여`, `진행`, `통해`, `지난번`). The note was in
  English although the request was in Korean.
- `bk_sales_005` (one question): asked about warranty coverage and exclusions
  as well as the period. Its sample line added `무상` and `설치일로부터`, which the
  source never stated.
- `bk_landing_002`: still four detached sentences after a "sounds translated"
  request.
- `bk_ui_005` (one question): asked three numbered questions, and its template
  added an unsupported `{금액}` placeholder.

**Full rerun** ([outputs](business-outputs.jsonl), [review](business-review.jsonl))

- `bk_sales_005`: added a sub-question about coverage scope to the
  warranty-period question.
- `bk_ad_005`: `표시된 기능은 베타 버전으로 변경될 수 있습니다` is ambiguous; see
  below.
- `bk_landing_002`: the four sentences were still not connected.

**Targeted batch, not scored** ([outputs](targeted-batch-outputs.jsonl))

This is an intermediate diagnostic run at the current skill revision. It has
no judge rows, so nothing here is a score:

- `bk_ad_005` produced the same ambiguous `베타 버전으로 변경될 수 있습니다`.
- `bk_ui_005` asked whether the button pays or submits, then asked a second
  thing: whether card and invoice orders share the button.
- `bk_landing_002` kept four separate sentences.
- For the English requests, the notes and questions in `bk_sales_005`,
  `bk_ui_005`, and `bk_support_006` were in Korean.

**Isolated final** ([fixture](isolated-fixture.jsonl), [outputs](isolated-outputs.jsonl), [review](isolated-review.jsonl))

- `bk_sales_005`: after asking the period, it asked for warranty scope and
  exceptions too. The note and question were in Korean for an English request.
- `bk_ui_005`: said it had one question, then listed three sub-questions with
  an explanatory preamble, all in Korean for an English request.
- `bk_landing_002` was marked as meeting the expected behavior. But the judge
  also recorded that "sentences connect" was only partly met (naturalness 3),
  and the output is still four separate sentences. This report treats
  paragraph flow on this case as unresolved.
- `bk_support_006` was marked as meeting the expected behavior, but its
  correction note was in Korean for an English request.
- `probe_english_explanation` met the expected behavior. The user asked for
  the explanation in English, and the explanation came back in English.

## The beta wording

In the full rerun, the judge scored `bk_ad_005` at meaning 3 but did not label
it a hard failure. Review treated it as a real meaning ambiguity anyway:
`베타 버전으로 변경될 수 있습니다` can read as "may be changed into a beta
version" instead of "are in beta and may change". The instructions at
`8f78a22` now say that merged clauses must keep each fact's own state, and
that a current state must not read as a possible future change.

At that same revision, the targeted batch still produced the ambiguous phrase.
The isolated run produced `베타 버전이라 변경될 수 있습니다`, which is clear.
That is one sample under a different harness. It does not show the issue is
fixed. Both runs are kept.

## Open issues

In the final isolated check at `skill-83f871d51c62`:

- **Over-asking.** When one field is missing, the skill still asks for
  related details (`bk_sales_005`) or splits one question into several
  (`bk_ui_005`).
- **Response language.** The instructions say to write notes and questions in
  the language of the request. In all three outputs where an English request
  without an explicit language instruction received a note or question, it
  came back in Korean. An explicit request for English worked in the one probe.
  Treat default language matching as unreliable, and tell users to ask for
  English explicitly.
- **Paragraph flow.** `bk_landing_002` still reads as a list of statements.
- **State wording.** The beta-state ambiguity appeared in two of the three
  `bk_ad_005` outputs generated since it was found.

## Source review findings

[initial-source-review.md](initial-source-review.md) is the source review
taken before these fixes. Its findings are unchanged; commit references in
the review and run metadata were remapped after an email-only commit metadata
rewrite. Every evaluated snapshot tree and every raw input and output stayed
identical. Here is how each finding was resolved:

| Finding | Resolution |
|---|---|
| M1: register contradiction | `SKILL.md` §1 and `evaluation.md` keep a coherent register. They change it only when the user asks or the context clearly shows a channel or brand mismatch, and a change in register gets a one-line note. |
| M2: source-authority path untested | `SKILL.md` §1 separates three cases: a named source, a clear mistranslation (fix it and note it), and an unclear governing version (ask one question or mark the clause). A won price or VAT note alone does not count as approval. `bk_landing_006` and `bk_support_006` test these paths. |
| M3: no-op coverage met by native cases | The validator now requires unchanged and question cases among the business domains. A test confirms that native no-op cases do not satisfy that check. |
| M4: delete-dialog scope | Now reads `프로젝트 안의 모든 파일`, which keeps the scope to all of that project's files. |
| M5: README promises exactness | Both READMEs describe the preservation rules as instructions, link the measured limits in this report, and say the skill does not check policy correctness. `README.md` has an English line near the top. |
| L1: one-directional hard fail | `evaluation.md` fails certainty drift in either direction. `SKILL.md` §5 keeps state and possibility separate in merged clauses. |
| L2: added greetings and thanks | No blanket ban was added. The existing rules against added commitments still apply, and `patterns.md` keeps stacked apologies or thanks to the source's strength. |
| L3: short UI labels | `SKILL.md` §4 says labels stay short and do not become explanatory or marketing copy. |
| L4: actor and reason checks | `SKILL.md` §3 restates the actor when it changes. §5 checks who is responsible and the reason for a decision. |
| L5: wrong explanations | `연중무휴 24시간` is now explained as the accurate Korean for 24/7. `기록을 깨다` is now explained as ambiguous. |
| L6: fixture wording | Both grading descriptions were clarified (see above). |
| L7: promo states intent as behavior | The promotion drafts describe the rules as instructions and link this report. |
| L8: metadata frames all use as customer copy | The `openai.yaml` default prompt now says "for its intended readers", which covers native writing. |
| L9: unreadable-path tests | Not addressed. The empty-file test exists; there are no tests yet for a missing file, a directory, or non-UTF-8 input. |

No legal-approval workflow was added. Legal and regulatory review stays out
of scope.

## Mechanical checks

These ran during development on the working tree:

- 29 `unittest` tests passed: 12 existing tests and 17 business-validator
  tests.
- The frozen 220-case fixture validator and the 2026-08-25 scored-baseline
  validator passed. So did the new 32-case business validator.
- Skill format validation with PyYAML passed, and the YAML files parsed.
- The public hygiene check passed after this report was written. All 104
  local Markdown links and anchors passed, and `git diff --check` passed.
- The historical 220-case fixture and reports and the three resume references
  are byte-identical to the base.

GitHub Actions results are recorded on the pull request separately. The
220-case model generation was not rerun. The full rerun checked 5 native-writing
regression cases at `63506b3`; the final isolated check at `8f78a22` included
only one of those cases, `bk_doc_reg_001`.

No committed validator exists for business output and review files. The
coverage, input, and score-range checks recorded in `metrics.jsonl` were done
outside the repository scripts.

## Files

| File | Contents |
|---|---|
| [runs.jsonl](runs.jsonl) | Attribution, harness, and selected IDs for each run |
| [metrics.jsonl](metrics.jsonl) | Counts and averages per scored run |
| [initial-fixture.jsonl](initial-fixture.jsonl) | The 30-case fixture as first run |
| [initial-outputs.jsonl](initial-outputs.jsonl), [initial-review.jsonl](initial-review.jsonl) | Initial run |
| [initial-source-review.md](initial-source-review.md) | Source review before the fixes, with commit references remapped as described above |
| [business-outputs.jsonl](business-outputs.jsonl), [business-review.jsonl](business-review.jsonl) | Full 32-case rerun |
| [targeted-batch-outputs.jsonl](targeted-batch-outputs.jsonl) | Unscored 7-case diagnostic |
| [isolated-fixture.jsonl](isolated-fixture.jsonl), [isolated-outputs.jsonl](isolated-outputs.jsonl), [isolated-review.jsonl](isolated-review.jsonl) | Final isolated check |
