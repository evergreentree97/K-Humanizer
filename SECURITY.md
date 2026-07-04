# Security Policy

## Reporting A Problem

If you find leaked private data, credentials, or a security issue in this repository, please open a private security advisory on GitHub if available.

If private advisories are unavailable, open an issue with minimal detail and do not paste secrets or private text into the issue body.

## Data Policy

K-Humanizer should not contain private user text or proprietary project data. Public fixtures must be synthetic or fully anonymized.

Before publishing or releasing, run:

```bash
python3 scripts/check_public_hygiene.py
```
