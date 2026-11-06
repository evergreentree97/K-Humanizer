# Initial source review

Snapshot: `36e28c630effbadfb6b9dfa8c12afc0ee7f57fb9`. Reviewer: `claude-opus-5-5`. This is the unedited independent source review before follow-up fixes and behavioral retesting. It reviewed no generated outputs; those have separate records. Findings and their resolution are summarized in the final business review report.

**Verdict: conditional pass.** I found no critical meaning or condition drift in the authored business guidance, the examples or the fixture. Five medium issues should be fixed before merge; one of them is a scope ambiguity in an example Korean string. I ran no forward test because there are no outputs to grade.

## Evidence scope

- **Read in full:** `SKILL.md` (old and new), `use-cases.md` (old and new), `evaluation.md`, the changed parts of `patterns.md`, all 30 fixture rows, `validate_business_set.py`, its tests, `check_public_hygiene.py`, `promotion.md`, and the diffs for both READMEs, CONTRIBUTING, CHANGELOG, `validation-plan.md`, `open-source-plan.md`, `openai.yaml` and the workflow.
- **Not in the diff:** `change.diff` leaves out the new files (fixture, validator, tests, `promotion.md`). I reviewed those directly in `revised/`.
- **Nothing was run.** I only had read and search tools, so the validator's behaviour is my reading of the code.
- **Historical files:** the golden set, the reports, the baseline JSONL and the three resume references don't appear in the diff and have the same line counts in base and revised. I didn't compare them byte for byte.
- **Forward test:** there's no `forward-test/` directory, so **0 outputs were inspected**.
- **What this is:** a single-model review, not human review and not production validation.

## Medium findings (fix before merge)

**M1. Korean-only mode contradicts itself on register.**
- `SKILL.md:17` says Korean-only edits should "Keep the voice, structure, and register."
- But `SKILL.md:79` lists "Speech levels that … do not fit the brand" as something to fix, §2 says audience and channel decide formality, and `validation-plan.md:27` says to fix what is "wrong for the channel."
- Users who aren't fluent can't tell they picked the wrong speech level, so keeping it by default preserves their mistake.
- **Fix:** "Keep the voice and structure. Keep the register unless it mixes speech levels or clearly misfits the audience and channel; then fix it and note the change in one line."

**M2. The "which version governs?" path has no test case.**
- All five bilingual fixture cases say which version is the source: `bk_sales_003`, `bk_ad_003`, `bk_landing_003`, `bk_support_003`, `bk_ui_003`.
- Three rules in `SKILL.md:21-37` are therefore never exercised:
  - English is the default source when the user names none.
  - When it's unclear which version governs, ask one question or mark the clause.
  - A won price or VAT note alone doesn't prove the Korean was approved.
- Both READMEs advertise these rules. The only example is a hypothetical aside in the "Local price" example.
- **Fix:** add one bilingual case with no source named and a USD/KRW or policy mismatch (`ask_one_question`). Optionally add a clear mistranslation with no source named (`produce_korean` plus a one-line note).

**M3. The validator's coverage check can pass without any business no-op cases.**
- `validate_business_set.py:128-132` and `:151-152` count `expected_behavior` across every row, including the native regression rows.
- `bk_resume_reg_001` and `bk_everyday_reg_001` alone meet the `keep_unchanged` requirement. Deleting all five business `keep_unchanged` cases would still pass, even though `validation-plan.md:175` implies this coverage is enforced.
- **Fix:** count behaviours only when `domain in BUSINESS_DOMAINS`, and add a test that removes only the business no-op cases.

**M4. The delete-dialog example widens the scope of the deletion.**
- At `use-cases.md:559`, `{project_name} 프로젝트와 모든 파일이 … 영구 삭제됩니다` can be read as "the project and *all* files." The English says "all of its files."
- That is the kind of outcome drift this example is meant to teach against.
- **Fix:** `{project_name} 프로젝트와 프로젝트 안의 모든 파일이 팀 전체에서 영구 삭제됩니다.`

**M5. The READMEs promise exactness to readers who can't check it.**
- `README.en.md:109-125` and `README.md:87-93` say the skill "keeps exact" prices and policies and returns natural Korean unchanged. Nothing says these are the skill's instructions rather than measured results, or that legal and regulatory compliance is out of scope (that limit is only in `open-source-plan.md`).
- `README.md`, which GitHub shows as the landing page, is Korean with only a bare `[English]` link at `:10`.
- **Fix:**
  - Add one sentence to each README: outputs aren't yet scored; have a fluent reader check prices and policies before publishing; it doesn't check compliance with Korean law.
  - Add one English line near the top of `README.md`.

## Low findings (optional)

- **L1. Hard fails only cover one direction.** `evaluation.md:188` and `validation-plan.md:112` fail a possibility that becomes a promise, but not a promise or confirmed fact that becomes a possibility. Fixture cases `bk_sales_005` and `bk_support_005` depend on that direction. Suggested wording: "changes the strength of a request, offer, promise, or certainty in either direction."
- **L2. Added greetings and thanks aren't covered.** `SKILL.md:113-114` forbids added apologies but says nothing about greetings, thanks or sign-offs. In `bk_support_002`, an added `문의해 주셔서 감사합니다` can't be graded consistently.
- **L3. A legacy UI rule was lost.** Base "Product and UI Copy" said "Keep short labels short; do not turn a UI label into explanatory marketing copy." It now appears only in the validation plan and the fixture. It could go in the App UI defaults at `use-cases.md:489`.
- **L4. Two final checks were dropped.** Base step 5 checked that "responsibility … and the reason for a decision still match." `SKILL.md:135` dropped both. The resume references still cover ownership, so this is minor.
- **L5. Two explanations teach wrong rules (the Korean itself is fine):**
  - `use-cases.md:286`: `연중무휴 24시간` is the standard Korean for 24/7, not a redundancy.
  - `use-cases.md:524`: `기록을 깨다` is ambiguous (`연속 기록이 깨지다` means a streak ended), not "the opposite."
- **L6. Fixture wording:**
  - `bk_doc_reg_001` requires 합니다체, but a 했다체 report paragraph is equally valid.
  - `bk_ad_002` doesn't say whether the source's own claim `고객들에게 사랑받고 있습니다` may be kept or dropped.
- **L7. Promo states design intent as behaviour.** `promotion.md:66-77` says "What the skill does now … Leaves Korean … unchanged." A caveat follows at `:81-84`, but "is designed to" would be more accurate.
- **L8. Agent metadata frames everything as customer copy.** `openai.yaml`'s `default_prompt` says "for Korean customers," which misframes resume and native-writing use.
- **L9. Validator tests skip unreadable paths.** The tests don't cover a missing file, a directory or non-UTF-8 input; the code handles all three (`:59-63`). The `splitlines()` call can split on U+2028, but the existing validators do the same.
- **Awkward but faithful, not drift:**
  - Sunscreen ad: `첫 주문 20% 할인은 이번 주에만 드려요` is slightly stiff.
  - Fitness push: `이대로 이어가 보세요` drops "now."

## What passed

- **Domain examples:** every domain has at least three examples (3/3/4/3/4, 17 total). Each has context, English, a machine translation, the revised Korean and an English explanation, and unchanged cases are included.
- **Korean reread:** I reread each example as Korean and confirmed these were restored correctly:
  - "billed annually" and "only if" (quote follow-up)
  - the Jeju and remote-area exclusion, and removal of the added "shop now" line (shipping banner)
  - removal of the invented `즉시 환불` (late-delivery reply)
  - `출고` vs `배송` (maintenance notice)
  - `으로만` and `경우에만` (single-channel refund)
  - `최대`, `기준` and `약` (spec table)
  - approved KRW pricing (local price)
  - the `{project_name}과` particle fix (delete dialog)
- **Fixture:** all 30 cases are plausible, and all 15 domain × mode pairs are covered. I agree all seven `keep_unchanged` texts are already natural Korean. The checks describe meaning, not exact wording.
- **Editing scope:** minimal edits for Korean-only and pair input versus full restructuring for English-to-Korean is consistent across `SKILL.md` §1/§5 and the `evaluation.md` table. An approved Korean text taking priority over older English is stated and tested (`bk_landing_003`).
- **No banned words:** `patterns.md` makes word-level advice conditional throughout.
- **Evaluation claims:** the README, validation plan and promo all describe the 220-case results and 2026-08-25 scores as earlier-version, Korean-only, synthetic records. The business fixture is described as unscored.
- **Counselor sentence:** removed from current guidance; it appears only as a historical note at `CHANGELOG.md:41`.
- **Promo:** marked as an unpublished draft.
- **Hygiene:** the new files contain none of the blocked terms or patterns.

## Remaining limitations

- Business output quality is untested: no outputs have been generated or graded.
- My Korean judgments are one model's reading. The plan's own task to have a native speaker review the examples (`open-source-plan.md`) still applies.
- I didn't run the validator or the tests.
