#!/usr/bin/env python3
"""Check for common private-data patterns before publishing."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_DENY_TERMS = [
    "BEGIN PRIVATE KEY",
    "BEGIN OPENSSH PRIVATE KEY",
    "api_key",
    "apikey",
    "access_token",
    "refresh_token",
    "client_secret",
    "password",
]

REGEX_CHECKS = {
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "openai_key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@(?!users\.noreply\.github\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone_kr": re.compile(r"\b01[016789]-?\d{3,4}-?\d{4}\b"),
}

SKIP_DIRS = {".git", "__pycache__", "evals/datasets", "evals/reports"}
CHECK_SUFFIXES = {".md", ".jsonl", ".py", ".yaml", ".yml", ".gitignore", ""}


def should_skip(path: Path) -> bool:
    normalized = path.as_posix()
    return any(part in SKIP_DIRS for part in path.parts) or any(normalized.startswith(skip) for skip in SKIP_DIRS)


def should_check(path: Path) -> bool:
    if should_skip(path) or not path.is_file():
        return False
    if path.name == "check_public_hygiene.py":
        return False
    if path.name in {"LICENSE", ".gitignore"}:
        return True
    return path.suffix in CHECK_SUFFIXES


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    parser.add_argument("--deny-term", action="append", default=[], help="Additional exact term to block.")
    args = parser.parse_args()

    deny_terms = DEFAULT_DENY_TERMS + args.deny_term
    findings: list[str] = []

    for path in sorted(args.root.rglob("*")):
        if not should_check(path):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_number, line in enumerate(text.splitlines(), 1):
            lowered = line.lower()
            for term in deny_terms:
                if term.lower() in lowered:
                    findings.append(f"{path}:{line_number}: blocked term {term!r}")
            for label, pattern in REGEX_CHECKS.items():
                if pattern.search(line):
                    findings.append(f"{path}:{line_number}: blocked pattern {label}")

    if findings:
        print("Public hygiene check failed:")
        for finding in findings:
            print(f"  {finding}")
        return 1

    print("OK: public hygiene check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
