## Summary

<!-- What problem does this PR address, and what changed? -->

## Related issue

<!-- Use "Closes #123" when this PR should close an issue. Write "None" for a small standalone fix. -->

## Type of change

- [ ] Korean naturalness rule or example
- [ ] Evaluation fixture or rubric
- [ ] Skill behavior
- [ ] Documentation
- [ ] Validation or repository maintenance

## Language-change example

<!-- Complete this section for wording, pattern, or skill-behavior changes. Remove it when it does not apply. -->

```text
Before:
After:
```

Why the change is needed:

What must stay unchanged:

When the original wording should be kept:

## Validation

<!-- List the checks you ran and their results. Typical commands are shown below. -->

```text
python3 scripts/validate_golden_set.py
python3 scripts/check_public_hygiene.py
```

## Privacy and review checklist

- [ ] This PR contains no private resume, email, chat, customer data, proprietary text, credentials, or internal URLs.
- [ ] Every contributed language example is entirely synthetic.
- [ ] I checked that facts, numbers, names, domain terms, authorship, completion state, and uncertainty are not changed by the proposed rewrite.
- [ ] I documented the condition and exception for any new language rule.
- [ ] I kept the core skill small and placed detailed examples or checklists under `skills/k-humanizer/references/`.
- [ ] I read [CONTRIBUTING.md](https://github.com/evergreentree97/K-Humanizer/blob/main/CONTRIBUTING.md) and the [Code of Conduct](https://github.com/evergreentree97/K-Humanizer/blob/main/CODE_OF_CONDUCT.md).
