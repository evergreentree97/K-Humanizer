#!/usr/bin/env python3
"""Regression tests for the business-Korean supplement validator."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_business_set import validate_file


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals" / "fixtures" / "business_korean.v1.jsonl"


class ValidateBusinessSetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.items = [json.loads(line) for line in FIXTURE.read_text(encoding="utf-8").splitlines()]

    def fresh_items(self) -> list[dict[str, object]]:
        return copy.deepcopy(self.items)

    def validate_lines(self, lines: list[str]) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "business_korean.v1.jsonl"
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = validate_file(path)
            return result, output.getvalue()

    def validate_items(self, items: list[object]) -> tuple[int, str]:
        return self.validate_lines([json.dumps(item, ensure_ascii=False) for item in items])

    def assert_rejected(self, items: list[object], message: str) -> None:
        result, output = self.validate_items(items)
        self.assertEqual(1, result, output)
        self.assertIn(message, output)

    def test_real_fixture_passes(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validate_file(FIXTURE)
        self.assertEqual(0, result, output.getvalue())
        self.assertIn("(30 cases)", output.getvalue())

    def test_malformed_json_is_rejected(self) -> None:
        lines = [json.dumps(item, ensure_ascii=False) for item in self.items]
        lines[3] = lines[3][:-1]
        result, output = self.validate_lines(lines)
        self.assertEqual(1, result)
        self.assertIn(":4: invalid JSON", output)

    def test_non_object_rows_are_rejected(self) -> None:
        for row in ([], "text", 42, None):
            with self.subTest(row=row):
                self.assert_rejected(self.fresh_items() + [row], "each line must be a JSON object")

    def test_unhashable_values_are_rejected_without_crashing(self) -> None:
        cases = [
            ("id", ["bk_sales_001"], "id must be a non-empty string"),
            ("domain", ["b2b_sales"], "unknown domain"),
            ("mode", {"name": "korean_edit"}, "unknown mode"),
        ]
        for field, value, message in cases:
            with self.subTest(field=field):
                items = self.fresh_items()
                items[0][field] = value
                self.assert_rejected(items, message)

        items = self.fresh_items()
        items[0]["grading"]["expected_behavior"] = ["keep_unchanged"]
        self.assert_rejected(items, "unknown expected_behavior")

    def test_wrong_types_are_rejected(self) -> None:
        items = self.fresh_items()
        items[0]["input"] = 123
        self.assert_rejected(items, "input must be a non-empty string")

        items = self.fresh_items()
        items[0]["grading"] = ["not", "an", "object"]
        self.assert_rejected(items, "grading must be an object")

        items = self.fresh_items()
        items[0]["grading"]["must_preserve"] = "price excludes VAT"
        self.assert_rejected(items, "grading.must_preserve must be a non-empty list")

    def test_blank_input_and_entries_are_rejected(self) -> None:
        items = self.fresh_items()
        items[0]["input"] = "   "
        self.assert_rejected(items, "input must be a non-empty string")

        items = self.fresh_items()
        items[0]["grading"]["avoid"] = ["adding a discount", "  "]
        self.assert_rejected(items, "grading.avoid must be a non-empty list")

        items = self.fresh_items()
        items[0]["grading"]["expected_traits"] = []
        self.assert_rejected(items, "grading.expected_traits must be a non-empty list")

    def test_duplicate_id_is_rejected(self) -> None:
        items = self.fresh_items()
        items[1]["id"] = items[0]["id"]
        self.assert_rejected(items, "duplicate id")

    def test_unknown_mode_and_domain_are_rejected(self) -> None:
        items = self.fresh_items()
        items[0]["mode"] = "machine_translation"
        self.assert_rejected(items, "unknown mode")

        items = self.fresh_items()
        items[0]["domain"] = "email"
        self.assert_rejected(items, "unknown domain")

    def test_missing_and_misplaced_fields_are_rejected(self) -> None:
        items = self.fresh_items()
        del items[0]["mode"]
        self.assert_rejected(items, "missing fields: ['mode']")

        items = self.fresh_items()
        items[0]["must_preserve"] = items[0]["grading"].pop("must_preserve")
        result, output = self.validate_items(items)
        self.assertEqual(1, result)
        self.assertIn("unknown fields: ['must_preserve']", output)
        self.assertIn("missing grading fields: ['must_preserve']", output)

        items = self.fresh_items()
        items[0]["grading"]["expected_output"] = "고정 정답"
        self.assert_rejected(items, "unknown grading fields: ['expected_output']")

    def test_regression_case_must_be_korean_edit(self) -> None:
        items = self.fresh_items()
        regression = next(item for item in items if item["domain"] == "resume")
        regression["mode"] = "english_to_korean"
        self.assert_rejected(items, "native regression cases must use korean_edit")

    def test_missing_business_domain_coverage_is_rejected(self) -> None:
        items = [item for item in self.fresh_items() if item["domain"] != "support_notice"]
        self.assert_rejected(items, "missing business domain coverage: support_notice")

    def test_missing_regression_coverage_is_rejected(self) -> None:
        items = [item for item in self.fresh_items() if item["domain"] != "everyday"]
        self.assert_rejected(items, "missing native regression coverage: everyday")

    def test_missing_business_mode_coverage_is_rejected(self) -> None:
        items = [item for item in self.fresh_items() if item["mode"] != "bilingual_edit"]
        self.assert_rejected(items, "missing business mode coverage: bilingual_edit")

    def test_missing_business_domain_mode_pair_is_rejected(self) -> None:
        items = [
            item
            for item in self.fresh_items()
            if (item["domain"], item["mode"]) != ("support_notice", "bilingual_edit")
        ]
        self.assertTrue(any(item["domain"] == "support_notice" for item in items))
        self.assertTrue(any(item["mode"] == "bilingual_edit" for item in items))

        result, output = self.validate_items(items)
        self.assertEqual(1, result, output)
        self.assertIn("missing business domain/mode coverage: support_notice/bilingual_edit", output)
        self.assertNotIn("missing business domain coverage", output)
        self.assertNotIn("missing business mode coverage", output)
        self.assertEqual(1, output.count("missing business domain/mode coverage"), output)

    def test_missing_no_op_and_question_coverage_is_rejected(self) -> None:
        for behavior in ("keep_unchanged", "ask_one_question"):
            with self.subTest(behavior=behavior):
                items = [
                    item
                    for item in self.fresh_items()
                    if item["grading"]["expected_behavior"] != behavior
                ]
                self.assert_rejected(items, f"missing expected_behavior coverage: {behavior}")

    def test_empty_file_is_rejected(self) -> None:
        result, output = self.validate_lines([])
        self.assertEqual(1, result)
        self.assertIn("missing business domain coverage", output)


if __name__ == "__main__":
    unittest.main()
