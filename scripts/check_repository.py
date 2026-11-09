#!/usr/bin/env python3
"""Validate the tracked repository without importing application/device code."""

from __future__ import annotations

import ast
import csv
import io
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 10 * 1024 * 1024
REQUIRED = {
    "README.md",
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    ".editorconfig",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "THIRD_PARTY_NOTICES.md",
    ".github/workflows/ci.yml",
    "docs/repository/main-ruleset.json",
}
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+[\"'][^\n]*[\"'])?\)")
LOCAL_DIRS = {".venv", "venv", "__pycache__", "node_modules", ".git"}
SECRET_SUFFIXES = {".pem", ".key", ".p12", ".pfx"}


def main() -> int:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "-z"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    )
    names = sorted(set(result.stdout.decode("utf-8").split("\0")) - {""})
    tracked = set(names)
    errors: list[str] = []
    for name in sorted(REQUIRED - tracked):
        errors.append(f"Missing required tracked file: {name}")

    for name in names:
        relative = Path(name)
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Tracked file missing from working tree: {name}")
            continue
        if (
            LOCAL_DIRS.intersection(relative.parts)
            or (relative.name.startswith(".env") and not relative.name.endswith(".example"))
            or relative.suffix.lower() in SECRET_SUFFIXES
            or relative.name in {"id_rsa", "id_ed25519"}
            or (relative.parts[0] == "logs" and relative.name != "README.md")
            or (
                relative.parts[:2] in {("data", "raw"), ("data", "models")}
                and name not in {"data/raw/README.md", "data/models/README.md"}
            )
        ):
            errors.append(f"Local/generated/secret-path candidate tracked: {name}")
        if path.stat().st_size > MAX_BYTES:
            errors.append(f"File exceeds project limit of 10 MiB: {name}")
        suffix = relative.suffix.lower()
        if suffix not in {".md", ".json", ".csv", ".py"}:
            continue
        try:
            content = path.read_text(encoding="utf-8")
            if suffix == ".json":
                json.loads(content)
            elif suffix == ".csv":
                rows = list(csv.reader(io.StringIO(content), strict=True))
                if not rows or not rows[0] or any(not h.strip() for h in rows[0]):
                    raise ValueError("CSV requires nonempty column names")
                if len(rows[0]) != len(set(rows[0])):
                    raise ValueError("CSV has duplicate column names")
                for number, row in enumerate(rows[1:], 2):
                    if len(row) != len(rows[0]):
                        raise ValueError(f"CSV row {number} has a different column count")
            elif suffix == ".py":
                ast.parse(content, filename=name)
            elif suffix == ".md":
                for target in LINK.findall(content):
                    parsed = urlsplit(target.strip("<>"))
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    destination = (path.parent / unquote(parsed.path)).resolve()
                    try:
                        destination.relative_to(ROOT)
                    except ValueError:
                        errors.append(f"Markdown link leaves repository: {name} -> {target}")
                        continue
                    if not destination.exists():
                        errors.append(f"Broken local Markdown link: {name} -> {target}")
        except (UnicodeError, ValueError, SyntaxError, csv.Error) as exc:
            errors.append(f"{name}: {exc}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Repository checks passed for {len(names)} tracked files.")
    print("No application behavior, simulation or hardware tests were executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
