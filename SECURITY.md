# Security Policy

## Reporting A Problem

If you find leaked private data, credentials, or a security issue in this
repository, use GitHub's
[private vulnerability reporting](https://github.com/evergreentree97/K-Humanizer/security/advisories/new).

Do not open a public issue or paste secrets, private text, identifying details,
or internal URLs into an issue body.

## Data Policy

K-Humanizer should not contain private user text or proprietary project data. Public fixtures must be synthetic or fully anonymized.

Before publishing or releasing, run:

```bash
python3 scripts/check_public_hygiene.py
```
