#!/usr/bin/env python3
"""Regression tests for the scored model-baseline validator."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_model_baseline import SCORE_FIELDS, validate_file


ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "evals" / "fixtures" / "golden_set.sample.jsonl"


class ValidateModelBaselineTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture_items = [
            json.loads(line) for line in SAMPLE.read_text(encoding="utf-8").splitlines()
        ]

    def make_records(self) -> list[dict[str, object]]:
        return [
            {
                "id": item["id"],
                "domain": item["domain"],
                "input": item["input"],
                "output": item["input"],
                "generator_model": "generator-test-version",
                "judge_model": "judge-test-version",
                "skill_revision": "test-revision",
                "scores": {field: 5 for field in SCORE_FIELDS},
                "critical_failure": False,
                "failure_types": [],
                "review_notes": "",
            }
            for item in self.fixture_items
        ]

    def validate_records(self, records: list[dict[str, object]]) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "baseline.jsonl"
            path.write_text(
                "\n".join(json.dumps(item, ensure_ascii=False) for item in records) + "\n",
                encoding="utf-8",
            )
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = validate_file(path, SAMPLE)
            return result, output.getvalue()

    def test_complete_baseline_passes(self) -> None:
        result, output = self.validate_records(self.make_records())
        self.assertEqual(0, result)
        self.assertIn("(11 scored outputs)", output)

    def test_missing_fixture_id_is_rejected(self) -> None:
        records = self.make_records()[:-1]
        result, output = self.validate_records(records)
        self.assertEqual(1, result)
        self.assertIn("missing 1 fixture ids", output)

    def test_invalid_score_is_rejected(self) -> None:
        records = self.make_records()
        records[0]["scores"]["meaning_fidelity"] = 6
        result, output = self.validate_records(records)
        self.assertEqual(1, result)
        self.assertIn("meaning_fidelity score must be an integer from 1 to 5", output)

    def test_source_input_drift_is_rejected(self) -> None:
        records = self.make_records()
        records[0]["input"] = "바뀐 입력"
        result, output = self.validate_records(records)
        self.assertEqual(1, result)
        self.assertIn("input differs from fixture", output)

    def test_critical_failure_requires_type(self) -> None:
        records = self.make_records()
        records[0]["critical_failure"] = True
        result, output = self.validate_records(records)
        self.assertEqual(1, result)
        self.assertIn("must name at least one failure type", output)

    def test_unknown_failure_type_is_rejected(self) -> None:
        records = self.make_records()
        records[0]["failure_types"] = ["invented_label"]
        records[0]["review_notes"] = "Should fail before publication."
        result, output = self.validate_records(records)
        self.assertEqual(1, result)
        self.assertIn("unknown failure types", output)

    def test_duplicate_failure_type_is_rejected(self) -> None:
        records = self.make_records()
        records[0]["failure_types"] = ["under_editing", "under_editing"]
        records[0]["review_notes"] = "Should fail before publication."
        result, output = self.validate_records(records)
        self.assertEqual(1, result)
        self.assertIn("must not contain duplicates", output)


if __name__ == "__main__":
    unittest.main()
