#!/usr/bin/env python3
"""Lightweight structural and public-template hygiene checks (not a security audit)."""
from __future__ import annotations

import csv
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "README.zh-CN.md", "STUDENT_PROMPT.zh-CN.md", "AGENTS.md", "CLAUDE.md", 
    "docs/SCIENTIFIC_DESIGN.md", "docs/QUALITY_GATES.md", "docs/DATA_POLICY.md",
    "docs/PUBLIC_RELEASE_CHECKLIST.md", "config/project.yaml", "manifests/DATASET_REGISTRY.tsv",
    "manifests/SAMPLE_MANIFEST.tsv", "manifests/ENVIRONMENT_REGISTRY.tsv", "manifests/RUN_INDEX.tsv",
    "ref-article/README.md", "phases/PHASE_INDEX.tsv", "phases/PHASE_LIFECYCLE.md",
    "phases/_template/01_design/ANALYSIS_CONTRACT.yaml",
    "phases/_template/02_campaign/AGENT_ENTRY.md", "phases/_template/03_returns/README.md",
]
BAD_EXTENSIONS = (".fastq", ".fq", ".bam", ".cram", ".h5ad", ".h5mu", ".loom", ".rds", ".rdata", ".pkl", ".pickle", ".parquet", ".h5", ".bcf", ".bgen")
SENSITIVE_NAMES = {".env", "id_rsa", "id_ed25519", "credentials.json", "secrets.json"}
SECRET_PATTERNS = [
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{25,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{25,}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]
# Public scaffold must not include an internal project URL or a local filesystem path.
PRIVATE_PATH_PATTERNS = [
    re.compile(r"(?:https?://)?github\.com/[\w.-]+/[\w.-]+/(?:pull|issues|tree|blob)/(?:private[-/]|internal[-/])", re.I),
    re.compile(r"/(?:data|home|scratch)/users/[\w.-]+/"),
    re.compile(r"[A-Z]:\\Users\\[\w.-]+\\"),
]


def tracked_or_files(root: Path) -> list[Path]:
    try:
        got = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True)
        if got.stdout:
            return [root / n.decode("utf-8") for n in got.stdout.split(b"\0") if n]
    except (OSError, subprocess.CalledProcessError):
        pass
    return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.relative_to(root).parts and "__pycache__" not in p.parts]


def check(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in REQUIRED:
        if not (root / path).is_file():
            errors.append(f"Missing required file: {path}")
    for p in tracked_or_files(root):
        if not p.exists() or not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        lower = rel.lower()
        if p.name.lower() in SENSITIVE_NAMES or lower.endswith(BAD_EXTENSIONS) or lower.endswith((".fastq.gz", ".fq.gz", ".vcf.gz")):
            errors.append(f"Sensitive/native file detected: {rel}")
        if p.stat().st_size > 2 * 1024 * 1024:
            errors.append(f"File over 2 MiB (requires explicit review): {rel}")
        if p.suffix.lower() not in {".md", ".tsv", ".yaml", ".yml", ".json", ".txt", ".py", ".sh", ""}:
            continue
        try:
            contents = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Non-UTF8 text: {rel}")
            continue
        for pattern in SECRET_PATTERNS + PRIVATE_PATH_PATTERNS:
            if pattern.search(contents):
                errors.append(f"Review potentially sensitive content in {rel} ({pattern.pattern[:25]}...)")
        if p.suffix.lower() == ".md":
            # Only relative links without anchor/URL/query. Ignore code examples and image embeds.
            for m in re.finditer(r"(?<!!)\[[^]\n]+\]\(([^)]+)\)", contents):
                dest = m.group(1).strip().split("#", 1)[0].split("?", 1)[0]
                if not dest or dest.startswith(("https://", "http://", "mailto:", "#")) or "TODO" in dest:
                    continue
                if dest.startswith("<") and dest.endswith(">"):
                    dest = dest[1:-1]
                dest = dest.replace("%20", " ")
                if not (p.parent / dest).exists():
                    errors.append(f"Broken relative link in {rel}: {dest}")
    idx = root / "phases" / "PHASE_INDEX.tsv"
    if idx.is_file():
        with idx.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            rows = list(reader)
        required_columns = ["phase_id", "title", "design_status", "execution_status", "scientific_status", "latest_return", "human_approved", "last_reviewed"]
        if reader.fieldnames != required_columns:
            errors.append("Invalid phases/PHASE_INDEX.tsv headers")
        for r in rows:
            if not (root / "phases" / r["phase_id"]).is_dir():
                errors.append(f"Indexed phase missing folder: {r['phase_id']}")
            if r.get("execution_status") == "NOT_EXECUTED" and r.get("latest_return"):
                errors.append(f"Unexecuted phase has latest_return: {r['phase_id']}")
            if r.get("human_approved") not in {"true", "false"}:
                errors.append(f"Invalid human_approved flag: {r['phase_id']}")
    return errors


def main() -> int:
    errors = check()
    if errors:
        print("Repository validation FAILED")
        for e in errors:
            print("-", e)
        return 1
    print("Repository validation PASSED (structure and heuristic content checks only; not scientific or release approval)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
