#!/usr/bin/env python3
"""Regression tests for the K-Humanizer golden-set validator."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_golden_set import validate_file


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals" / "fixtures" / "golden_set.v0.jsonl"
SAMPLE = ROOT / "evals" / "fixtures" / "golden_set.sample.jsonl"


class ValidateGoldenSetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.items = [json.loads(line) for line in FIXTURE.read_text(encoding="utf-8").splitlines()]

    def validate_items(self, items: list[dict[str, object]]) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "golden_set.v0.jsonl"
            path.write_text(
                "\n".join(json.dumps(item, ensure_ascii=False) for item in items) + "\n",
                encoding="utf-8",
            )
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                result = validate_file(path)
            return result, output.getvalue()

    def test_real_fixture_passes(self) -> None:
        result, output = self.validate_items(self.items)
        self.assertEqual(0, result)
        self.assertIn("(220 items)", output)

    def test_sample_fixture_passes(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validate_file(SAMPLE)
        self.assertEqual(0, result)
        self.assertIn("(11 items)", output.getvalue())

    def test_missing_public_post_is_rejected(self) -> None:
        items = [item for item in self.items if item["id"] != "public_001"]
        result, output = self.validate_items(items)
        self.assertEqual(1, result)
        self.assertIn("expected 10 public_post items, found 9", output)

    def test_unknown_domain_is_rejected(self) -> None:
        items = [dict(item) for item in self.items]
        items[0]["domain"] = "unknown"
        result, output = self.validate_items(items)
        self.assertEqual(1, result)
        self.assertIn("unknown domain", output)

    def test_duplicate_id_is_rejected(self) -> None:
        items = [dict(item) for item in self.items]
        items[1]["id"] = items[0]["id"]
        result, output = self.validate_items(items)
        self.assertEqual(1, result)
        self.assertIn("duplicate id", output)


if __name__ == "__main__":
    unittest.main()
