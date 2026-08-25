#!/usr/bin/env python3
"""Validate a scored K-Humanizer model-output baseline."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


SCORE_FIELDS = (
    "meaning_fidelity",
    "korean_naturalness",
    "context_fit",
    "edit_discipline",
    "practical_usefulness",
)

ALLOWED_FAILURE_TYPES = {
    "completion_state_change",
    "context_mismatch",
    "evidence_type_mixup",
    "factual_drift",
    "generic_organization_fit",
    "not_ready",
    "number_drift",
    "other",
    "over_editing",
    "ownership_inflation",
    "under_editing",
    "unnatural_korean",
}

REQUIRED_FIELDS = {
    "id",
    "domain",
    "input",
    "output",
    "generator_model",
    "judge_model",
    "skill_revision",
    "scores",
    "critical_failure",
    "failure_types",
    "review_notes",
}


def load_fixture(path: Path) -> tuple[dict[str, dict[str, object]], list[str]]:
    items: dict[str, dict[str, object]] = {}
    errors: list[str] = []

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip():
            continue
        try:
            item = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid fixture JSON: {exc}")
            continue
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{path}:{line_number}: fixture id must be a non-empty string")
        elif item_id in items:
            errors.append(f"{path}:{line_number}: duplicate fixture id: {item_id}")
        else:
            items[item_id] = item

    return items, errors


def validate_file(path: Path, fixture_path: Path) -> int:
    fixture, errors = load_fixture(fixture_path)
    seen_ids: set[str] = set()
    domain_counts: Counter[str] = Counter()
    score_totals: defaultdict[str, int] = defaultdict(int)
    critical_failures = 0
    generator_models: set[str] = set()
    judge_models: set[str] = set()
    skill_revisions: set[str] = set()

    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line.strip():
            continue
        try:
            item = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{line_number}: invalid JSON: {exc}")
            continue
        if not isinstance(item, dict):
            errors.append(f"{path}:{line_number}: each line must be a JSON object")
            continue

        missing = REQUIRED_FIELDS - item.keys()
        if missing:
            errors.append(f"{path}:{line_number}: missing fields: {sorted(missing)}")

        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            errors.append(f"{path}:{line_number}: id must be a non-empty string")
            expected = None
        elif item_id in seen_ids:
            errors.append(f"{path}:{line_number}: duplicate id: {item_id}")
            expected = fixture.get(item_id)
        else:
            seen_ids.add(item_id)
            expected = fixture.get(item_id)
            if expected is None:
                errors.append(f"{path}:{line_number}: id is not in fixture: {item_id}")

        domain = item.get("domain")
        if not isinstance(domain, str) or not domain:
            errors.append(f"{path}:{line_number}: domain must be a non-empty string")
        else:
            domain_counts[domain] += 1
            if expected is not None and domain != expected.get("domain"):
                errors.append(
                    f"{path}:{line_number}: domain differs from fixture for {item_id}"
                )

        source_input = item.get("input")
        if not isinstance(source_input, str) or not source_input.strip():
            errors.append(f"{path}:{line_number}: input must be a non-empty string")
        elif expected is not None and source_input != expected.get("input"):
            errors.append(f"{path}:{line_number}: input differs from fixture for {item_id}")

        output = item.get("output")
        if not isinstance(output, str) or not output.strip():
            errors.append(f"{path}:{line_number}: output must be a non-empty string")

        for field, values in (
            ("generator_model", generator_models),
            ("judge_model", judge_models),
            ("skill_revision", skill_revisions),
        ):
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path}:{line_number}: {field} must be a non-empty string")
            else:
                values.add(value)

        scores = item.get("scores")
        if not isinstance(scores, dict):
            errors.append(f"{path}:{line_number}: scores must be an object")
        else:
            missing_scores = set(SCORE_FIELDS) - scores.keys()
            if missing_scores:
                errors.append(
                    f"{path}:{line_number}: missing scores: {sorted(missing_scores)}"
                )
            for field in SCORE_FIELDS:
                value = scores.get(field)
                if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 5:
                    errors.append(
                        f"{path}:{line_number}: {field} score must be an integer from 1 to 5"
                    )
                else:
                    score_totals[field] += value

        critical_failure = item.get("critical_failure")
        if not isinstance(critical_failure, bool):
            errors.append(f"{path}:{line_number}: critical_failure must be a boolean")
        elif critical_failure:
            critical_failures += 1

        failure_types = item.get("failure_types")
        if not isinstance(failure_types, list) or not all(
            isinstance(value, str) and value.strip() for value in failure_types
        ):
            errors.append(f"{path}:{line_number}: failure_types must be a string list")
        elif unknown_types := set(failure_types) - ALLOWED_FAILURE_TYPES:
            errors.append(
                f"{path}:{line_number}: unknown failure types: {sorted(unknown_types)}"
            )
        elif len(failure_types) != len(set(failure_types)):
            errors.append(f"{path}:{line_number}: failure_types must not contain duplicates")
        elif critical_failure is True and not failure_types:
            errors.append(
                f"{path}:{line_number}: a critical failure must name at least one failure type"
            )

        review_notes = item.get("review_notes")
        if not isinstance(review_notes, str):
            errors.append(f"{path}:{line_number}: review_notes must be a string")
        elif failure_types and not review_notes.strip():
            errors.append(
                f"{path}:{line_number}: review_notes must explain recorded failures"
            )

    missing_ids = set(fixture) - seen_ids
    if missing_ids:
        errors.append(
            f"{path}: missing {len(missing_ids)} fixture ids: {sorted(missing_ids)[:10]}"
        )

    for label, values in (
        ("generator_model", generator_models),
        ("judge_model", judge_models),
        ("skill_revision", skill_revisions),
    ):
        if len(values) > 1:
            errors.append(f"{path}: multiple {label} values: {sorted(values)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    total = len(seen_ids)
    print(f"OK: {path} ({total} scored outputs)")
    print(f"  generator_model: {next(iter(generator_models))}")
    print(f"  judge_model: {next(iter(judge_models))}")
    print(f"  skill_revision: {next(iter(skill_revisions))}")
    print(f"  critical_failures: {critical_failures}")
    print("  averages:")
    for field in SCORE_FIELDS:
        print(f"    {field}: {score_totals[field] / total:.3f}")
    print("  domains:")
    for domain in sorted(domain_counts):
        print(f"    {domain}: {domain_counts[domain]}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", help="Scored model-output JSONL file")
    parser.add_argument(
        "--fixture",
        default="evals/fixtures/golden_set.v0.jsonl",
        help="Source golden-set JSONL file",
    )
    args = parser.parse_args()
    return validate_file(Path(args.baseline), Path(args.fixture))


if __name__ == "__main__":
    raise SystemExit(main())
