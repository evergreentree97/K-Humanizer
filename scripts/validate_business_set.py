#!/usr/bin/env python3
"""Validate the synthetic business-Korean JSONL evaluation supplement."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


BUSINESS_DOMAINS = {
    "b2b_sales",
    "marketing_ad",
    "landing_page",
    "support_notice",
    "ui_notification",
}

# Native Korean cases that guard existing behavior while the business
# guidance changes. They are source-preservation tests, not new drafting tasks.
REGRESSION_DOMAINS = {
    "resume",
    "everyday",
    "document",
}

MODES = {
    "korean_edit",
    "bilingual_edit",
    "english_to_korean",
}

EXPECTED_BEHAVIORS = {
    "produce_korean",
    "keep_unchanged",
    "ask_one_question",
}

# Native regression cases already include no-ops, so these behaviors must also
# appear in the business cases themselves.
BUSINESS_REQUIRED_BEHAVIORS = {
    "keep_unchanged",
    "ask_one_question",
}

# The generator sees only `id` and `input`. Everything under `grading` is for
# the evaluator; `domain` and `mode` are coverage metadata.
TOP_LEVEL_FIELDS = {"id", "domain", "mode", "input", "grading"}
GRADING_FIELDS = {"expected_behavior", "expected_traits", "must_preserve", "avoid"}
LIST_FIELDS = ("expected_traits", "must_preserve", "avoid")


def is_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_file(path: Path) -> int:
    errors: list[str] = []
    ids: set[str] = set()
    domains: Counter[str] = Counter()
    business_modes: Counter[str] = Counter()
    business_pairs: set[tuple[str, str]] = set()
    behaviors: Counter[str] = Counter()
    business_behaviors: Counter[str] = Counter()

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"ERROR: {path}: cannot read file: {exc}")
        return 1

    for line_number, raw_line in enumerate(lines, 1):
        where = f"{path}:{line_number}"
        if not raw_line.strip():
            continue

        try:
            item = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"{where}: invalid JSON: {exc}")
            continue
        if not isinstance(item, dict):
            errors.append(f"{where}: each line must be a JSON object")
            continue

        missing = TOP_LEVEL_FIELDS - item.keys()
        if missing:
            errors.append(f"{where}: missing fields: {sorted(missing)}")
        unknown = item.keys() - TOP_LEVEL_FIELDS
        if unknown:
            errors.append(
                f"{where}: unknown fields: {sorted(unknown)} "
                "(evaluator requirements belong under 'grading')"
            )

        item_id = item.get("id")
        if not is_text(item_id):
            errors.append(f"{where}: id must be a non-empty string")
        elif item_id in ids:
            errors.append(f"{where}: duplicate id: {item_id}")
        else:
            ids.add(item_id)

        domain = item.get("domain")
        if not isinstance(domain, str) or domain not in BUSINESS_DOMAINS | REGRESSION_DOMAINS:
            errors.append(f"{where}: unknown domain: {domain!r}")
            domain = None
        else:
            domains[domain] += 1

        mode = item.get("mode")
        if not isinstance(mode, str) or mode not in MODES:
            errors.append(f"{where}: unknown mode: {mode!r}")
        elif domain in BUSINESS_DOMAINS:
            business_modes[mode] += 1
            business_pairs.add((domain, mode))
        elif domain in REGRESSION_DOMAINS and mode != "korean_edit":
            errors.append(f"{where}: native regression cases must use korean_edit")

        if not is_text(item.get("input")):
            errors.append(f"{where}: input must be a non-empty string")

        grading = item.get("grading")
        if not isinstance(grading, dict):
            errors.append(f"{where}: grading must be an object")
            continue

        missing = GRADING_FIELDS - grading.keys()
        if missing:
            errors.append(f"{where}: missing grading fields: {sorted(missing)}")
        unknown = grading.keys() - GRADING_FIELDS
        if unknown:
            errors.append(f"{where}: unknown grading fields: {sorted(unknown)}")

        behavior = grading.get("expected_behavior")
        if not isinstance(behavior, str) or behavior not in EXPECTED_BEHAVIORS:
            errors.append(f"{where}: unknown expected_behavior: {behavior!r}")
        else:
            behaviors[behavior] += 1
            if domain in BUSINESS_DOMAINS:
                business_behaviors[behavior] += 1

        for field in LIST_FIELDS:
            value = grading.get(field)
            if not isinstance(value, list) or not value or not all(is_text(v) for v in value):
                errors.append(f"{where}: grading.{field} must be a non-empty list of non-blank strings")

    for domain in sorted(BUSINESS_DOMAINS - domains.keys()):
        errors.append(f"{path}: missing business domain coverage: {domain}")
    for domain in sorted(REGRESSION_DOMAINS - domains.keys()):
        errors.append(f"{path}: missing native regression coverage: {domain}")
    for mode in sorted(MODES - business_modes.keys()):
        errors.append(f"{path}: missing business mode coverage: {mode}")
    # Every business domain is exercised in every input mode, so a case cannot
    # be dropped just because its domain and mode are covered elsewhere.
    for domain in sorted(BUSINESS_DOMAINS):
        for mode in sorted(MODES):
            if (domain, mode) not in business_pairs:
                errors.append(f"{path}: missing business domain/mode coverage: {domain}/{mode}")
    for behavior in sorted(EXPECTED_BEHAVIORS - behaviors.keys()):
        errors.append(f"{path}: missing expected_behavior coverage: {behavior}")
    for behavior in sorted(BUSINESS_REQUIRED_BEHAVIORS - business_behaviors.keys()):
        errors.append(f"{path}: missing business behavior coverage: {behavior}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {path} ({len(ids)} cases)")
    print("  domains:")
    for domain in sorted(domains):
        print(f"    {domain}: {domains[domain]}")
    print("  business modes:")
    for mode in sorted(business_modes):
        print(f"    {mode}: {business_modes[mode]}")
    print("  expected behaviors:")
    for behavior in sorted(behaviors):
        print(f"    {behavior}: {behaviors[behavior]}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        default="evals/fixtures/business_korean.v1.jsonl",
        type=Path,
        help="JSONL fixture to validate",
    )
    args = parser.parse_args()
    return validate_file(args.path)


if __name__ == "__main__":
    raise SystemExit(main())
