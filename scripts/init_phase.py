#!/usr/bin/env python3
"""Create a design-only phase using template files; never generate run results."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
PHASES = ROOT / "phases"
TEMPLATE = PHASES / "_template"
INDEX = PHASES / "PHASE_INDEX.tsv"
PATTERN = re.compile(r"phase-[0-9]{2,3}$")
FIELDS = ["phase_id", "title", "design_status", "execution_status", "scientific_status", "latest_return", "human_approved", "last_reviewed"]


def create_phase(phase_id: str, title: str, *, root: Path = ROOT) -> Path:
    if not PATTERN.fullmatch(phase_id):
        raise ValueError("Phase ID must be phase-01, phase-02, ..., phase-100")
    if not title.strip() or "\n" in title or "\t" in title:
        raise ValueError("A single-line nonempty title is required")
    phases = root / "phases"
    source = phases / "_template"
    target = phases / phase_id
    index = phases / "PHASE_INDEX.tsv"
    if target.exists():
        raise FileExistsError(f"Phase already exists: {target}")
    with index.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        if reader.fieldnames != FIELDS:
            raise ValueError("Malformed phase index header")
        rows = list(reader)
    if any(r["phase_id"] == phase_id for r in rows):
        raise ValueError("Phase already listed in index")
    shutil.copytree(source, target)
    overview = target / "README.md"
    overview.write_text(overview.read_text(encoding="utf-8").replace("Phase template (copy only; no analysis executed)", f"{phase_id} — {title} (design only)"), encoding="utf-8")
    # A newly created phase is strictly a plan, not a run or human approval.
    rows.append(dict(zip(FIELDS, [phase_id, title, "DRAFT", "NOT_EXECUTED", "REVIEW_REQUIRED", "", "false", ""])))
    with index.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True, dest="phase_id")
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    try:
        created = create_phase(args.phase_id, args.title)
    except (ValueError, FileExistsError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created design-only phase: {created.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
