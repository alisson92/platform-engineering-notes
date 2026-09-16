#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "courses"

HEADING_RE = re.compile(r"^(#{1,6})\s+\S")


def check_file(path: Path) -> list[str]:
    errors = []
    lines = path.read_text(encoding="utf-8").splitlines()
    headings = [
        (i + 1, len(m.group(1)))
        for i, line in enumerate(lines)
        if (m := HEADING_RE.match(line))
    ]

    if not headings or headings[0][1] != 1:
        errors.append("missing a top-level '# ' heading as the first heading")

    for lineno, level in headings[1:]:
        if level == 1:
            errors.append(f"line {lineno}: stray top-level '# ' heading after the document title")

    return errors


def main() -> int:
    failed = False
    for path in sorted(ROOT.rglob("*.md")):
        errors = check_file(path)
        if errors:
            failed = True
            print(f"{path.relative_to(ROOT.parent)}:")
            for e in errors:
                print(f"  - {e}")
    if failed:
        return 1
    print("All course Markdown files have a valid heading structure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
