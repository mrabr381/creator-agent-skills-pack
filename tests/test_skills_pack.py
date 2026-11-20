"""Tests for the Creator Agent Skills Pack.

Covers what CI checks: validate.py passes, the install script installs
all six skills, and the README/hero assets the study asked for exist.
Standard library only (plus pytest).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKILLS = [
    "youtube-outlier-research",
    "repurpose-episode",
    "seo-geo-audit",
    "digital-product-packaging",
    "thumbnail-title-test",
    "privacy-tool-review",
]


def test_validate_py_passes():
    """validate.py (frontmatter, sections, links, examples) exits 0."""
    result = subprocess.run(
        [sys.executable, "validate.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "all checks passed" in result.stdout


def test_install_script_installs_all_six_skills(tmp_path):
    """./install.sh --dir <tmp> copies exactly the six skills."""
    target = tmp_path / "skills"
    result = subprocess.run(
        ["bash", "install.sh", "--dir", str(target)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert result.returncode == 0, result.stderr
    installed = sorted(p.name for p in target.iterdir() if p.is_dir())
    assert installed == sorted(SKILLS)
    for name in SKILLS:
        assert (target / name / "SKILL.md").is_file()


def test_install_script_default_target_mentioned():
    """install.sh documents the Claude Code default (~/.claude/skills)."""
    text = (ROOT / "install.sh").read_text(encoding="utf-8")
    assert "~/.claude/skills" in text or ".claude/skills" in text


def test_readme_lists_all_six_skills():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in SKILLS:
        assert name in readme


def test_readme_has_one_command_install():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "install.sh" in readme
    assert "npx skills add mrabr381/creator-agent-skills-pack" in readme


def test_hero_banner_exists_and_is_text():
    hero = ROOT / "assets" / "hero.svg"
    assert hero.is_file()
    text = hero.read_text(encoding="utf-8")
    assert text.startswith("<svg")
    assert "#111827" in text  # dark card background
    assert "#f59e0b" in text  # amber pitch line
    assert "Creator Agent Skills Pack" in text


def test_ci_workflow_runs_validate():
    workflow = ROOT / ".github" / "workflows" / "ci.yml"
    assert workflow.is_file()
    text = workflow.read_text(encoding="utf-8")
    assert "validate.py" in text
    assert "pytest" in text
