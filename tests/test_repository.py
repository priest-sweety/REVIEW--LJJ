"""Dependency-free tests for a safe, design-only scaffold."""
import csv
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from init_phase import create_phase  # noqa: E402
from validate_repo import check  # noqa: E402


class TemplateTests(unittest.TestCase):
    def test_clean_repository(self):
        self.assertEqual(check(ROOT), [])

    def test_init_phase_only_creates_design(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            import shutil
            shutil.copytree(ROOT / "phases" / "_template", root / "phases" / "_template")
            header = (ROOT / "phases" / "PHASE_INDEX.tsv").read_text(encoding="utf-8").splitlines()[0]
            (root / "phases" / "PHASE_INDEX.tsv").write_text(header + "\n", encoding="utf-8")
            target = create_phase("phase-01", "Example design", root=root)
            self.assertTrue((target / "01_design" / "ANALYSIS_CONTRACT.yaml").exists())
            self.assertFalse((target / "03_returns" / "R001").exists())
            with (root / "phases" / "PHASE_INDEX.tsv").open(encoding="utf-8") as f:
                rows = list(csv.DictReader(f, delimiter="\t"))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["execution_status"], "NOT_EXECUTED")
            self.assertEqual(rows[0]["human_approved"], "false")
            with self.assertRaises(FileExistsError):
                create_phase("phase-01", "Duplicate", root=root)

    def test_invalid_phase_id_is_rejected(self):
        with self.assertRaises(ValueError):
            create_phase("../private", "unsafe", root=ROOT)


if __name__ == "__main__":
    unittest.main()
