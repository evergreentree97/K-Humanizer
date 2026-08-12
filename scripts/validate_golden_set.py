#!/usr/bin/env python3
"""Validate K-Humanizer JSONL golden-set fixtures."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


REQUIRED_FIELDS = {
    "id",
    "domain",
    "input",
    "expected_traits",
    "must_preserve",
    "avoid",
}

EXPECTED_DOMAINS = {
    "resume",
    "document",
    "product_copy",
    "everyday",
    "messenger",
    "email",
    "code_review",
    "dialogue",
}

V0_EXPECTED_COUNTS = {
    "resume": 90,
    "document": 20,
    "product_copy": 10,
    "everyday": 20,
    "messenger": 20,
    "email": 20,
    "code_review": 10,
    "dialogue": 10,
}

V0_EXPECTED_RESUME_ROLES = {
    "operations": 5,
    "planning": 5,
    "qa": 5,
    "design": 5,
    "marketing_content": 5,
    "customer_service": 5,
    "research_data": 5,
    "people_education": 5,
}


def validate_file(path: Path) -> int:
    errors: list[str] = []
    ids: set[str] = set()
    domains: Counter[str] = Counter()
    resume_roles: Counter[str] = Counter()

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip():
            continue

        try:
            item = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc}")
            continue

        missing = REQUIRED_FIELDS - item.keys()
        if missing:
            errors.append(f"{path}:{line_number}: missing fields: {sorted(missing)}")

        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{path}:{line_number}: id must be a non-empty string")
        elif item_id in ids:
            errors.append(f"{path}:{line_number}: duplicate id: {item_id}")
        else:
            ids.add(item_id)

        domain = item.get("domain")
        if domain not in EXPECTED_DOMAINS:
            errors.append(f"{path}:{line_number}: unknown domain: {domain!r}")
        else:
            domains[domain] += 1

        resume_role = item.get("resume_role")
        if resume_role is not None:
            if domain != "resume":
                errors.append(
                    f"{path}:{line_number}: resume_role is only valid for resume items"
                )
            elif resume_role not in V0_EXPECTED_RESUME_ROLES:
                errors.append(
                    f"{path}:{line_number}: unknown resume_role: {resume_role!r}"
                )
            else:
                resume_roles[resume_role] += 1

        for field in ("expected_traits", "must_preserve", "avoid"):
            value = item.get(field)
            if not isinstance(value, list) or not value or not all(isinstance(v, str) and v for v in value):
                errors.append(f"{path}:{line_number}: {field} must be a non-empty string list")

        text = item.get("input")
        if not isinstance(text, str) or len(text.strip()) < 10:
            errors.append(f"{path}:{line_number}: input is too short or missing")

    if path.name == "golden_set.v0.jsonl":
        for domain, expected_count in V0_EXPECTED_COUNTS.items():
            actual_count = domains[domain]
            if actual_count != expected_count:
                errors.append(
                    f"{path}: expected {expected_count} {domain} items, found {actual_count}"
                )
        for role, expected_count in V0_EXPECTED_RESUME_ROLES.items():
            actual_count = resume_roles[role]
            if actual_count != expected_count:
                errors.append(
                    f"{path}: expected {expected_count} {role} resume items, "
                    f"found {actual_count}"
                )

    if errors:
        for error in errors:
            print(error)
        return 1

    total = sum(domains.values())
    print(f"OK: {path} ({total} items)")
    for domain in sorted(EXPECTED_DOMAINS):
        print(f"  {domain}: {domains[domain]}")
    if resume_roles:
        print("  resume roles:")
        for role in sorted(resume_roles):
            print(f"    {role}: {resume_roles[role]}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default="evals/fixtures/golden_set.v0.jsonl",
        type=Path,
        help="JSONL fixture to validate",
    )
    args = parser.parse_args()
    return validate_file(args.path)


if __name__ == "__main__":
    raise SystemExit(main())
