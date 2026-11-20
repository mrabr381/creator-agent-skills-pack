#!/usr/bin/env python3
"""Validate the Creator Agent Skills Pack (standard library only).

Checks every skills/*/SKILL.md for:
  - YAML frontmatter with a `name` matching its directory and a
    `description` (non-empty, under 1024 characters).
  - Required sections: When to Use, Workflow, Checklist, Templates,
    Anti-Patterns (matched case-insensitively on headings).
  - No placeholder text: TODO, TBD, FIXME, XXX, "Lorem ipsum".
  - Every relative Markdown link resolves to a real file.
Also checks that examples/ has one worked example per skill and that
README.md lists all six skills.

Usage: python3 validate.py
Exit code 0 = all checks pass, 1 = any check failed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills"
EXAMPLES_DIR = ROOT / "examples"

REQUIRED_SECTIONS = [
    "when to use",
    "workflow",
    "checklist",
    "templates",
    "anti-patterns",
]
FORBIDDEN = ("TODO", "TBD", "FIXME", "XXX", "Lorem ipsum", "lorem ipsum")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, list[str]]:
    """Return (frontmatter dict, body, errors). Minimal YAML-subset parser:
    only top-level `key: value` lines are read; multi-line values are joined."""
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["missing frontmatter (file must start with ---)"]
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text, ["frontmatter never closed with ---"]
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    fm: dict[str, str] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            current_key = m.group(1)
            fm[current_key] = m.group(2).strip().strip('"').strip("'")
        elif line.startswith((" ", "\t")) and current_key:
            fm[current_key] += " " + line.strip().strip('"').strip("'")
        else:
            errors.append(f"unparsable frontmatter line: {line!r}")
    return fm, body, errors


def check_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    fm, body, fm_errors = parse_frontmatter(text)
    errors.extend(fm_errors)

    name = fm.get("name", "")
    if not name:
        errors.append("frontmatter missing `name`")
    elif name != path.parent.name:
        errors.append(
            f"frontmatter name {name!r} does not match directory {path.parent.name!r}"
        )
    desc = fm.get("description", "")
    if not desc:
        errors.append("frontmatter missing `description`")
    elif len(desc) > 1024:
        errors.append(f"description is {len(desc)} chars (max 1024)")

    headings = {
        h.strip().lower()
        for h in re.findall(r"^#{1,6}\s+(.+)$", body, flags=re.MULTILINE)
    }
    for section in REQUIRED_SECTIONS:
        if not any(section in h for h in headings):
            errors.append(f"missing required section: {section!r}")

    for bad in FORBIDDEN:
        if bad in text:
            errors.append(f"placeholder text found: {bad!r}")

    for target in LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = (path.parent / target.split("#")[0]).resolve()
        if not target_path.exists():
            errors.append(f"broken relative link: {target!r}")
    return errors


def main() -> int:
    failures = 0
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    print(f"Found {len(skill_files)} skills.")
    if len(skill_files) != 6:
        print("FAIL: expected exactly 6 skills.")
        failures += 1
    found_names: set[str] = set()
    for path in skill_files:
        found_names.add(path.parent.name)
        errors = check_skill(path)
        if errors:
            failures += 1
            print(f"\nFAIL {path.relative_to(ROOT)}:")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"OK   {path.relative_to(ROOT)}")

    for name in sorted(found_names):
        example = EXAMPLES_DIR / f"{name}.md"
        if not example.exists():
            print(f"FAIL: missing worked example {example.relative_to(ROOT)}")
            failures += 1
        else:
            text = example.read_text(encoding="utf-8")
            bad = [b for b in FORBIDDEN if b in text]
            if bad:
                print(f"FAIL: {example.relative_to(ROOT)} contains {bad}")
                failures += 1
            else:
                print(f"OK   {example.relative_to(ROOT)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in sorted(found_names):
        if name not in readme:
            print(f"FAIL: README.md does not mention skill {name!r}")
            failures += 1

    print()
    if failures:
        print(f"RESULT: {failures} failure(s).")
        return 1
    print("RESULT: all checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
