#!/usr/bin/env python3
"""Validate the shareable staged brand-market-entry Skill package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_REFERENCES = (
    "staged-artifact-contract.md",
    "stage-output-templates.md",
    "gate-protocol.md",
    "final-report-contract.md",
    "html-report-template.md",
)

REQUIRED_ARTIFACTS = (
    "research-brief.md",
    "research-brief.json",
    "research-outline.md",
    "source-registry.csv",
    "data-quota.csv",
    "market-pack.md",
    "market-metrics.csv",
    "competitor-matrix.csv",
    "channel-map.csv",
    "user-cultural-insight.md",
    "ugc-coding.csv",
    "persona-matrix.csv",
    "jtbd-map.md",
    "regulatory-entry.md",
    "regulatory-matrix.csv",
    "data-flow-map.md",
    "evidence-ledger.csv",
    "decision-matrix.md",
    "assumption-register.md",
    "contradiction-log.md",
    "falsification-log.md",
    "report.md",
    "report.html",
    "report-data.json",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def check_package(root: Path, errors: list[str]) -> None:
    skill_dir = root / "skills" / "brand-market-entry"
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(errors, f"missing {skill_file}")
        return

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(errors, "SKILL.md has no YAML frontmatter")
    if not re.search(r"^name:\s*brand-market-entry\s*$", text, re.MULTILINE):
        fail(errors, "SKILL.md name is not brand-market-entry")
    description = re.search(r"^description:\s*(.+)$", text, re.MULTILINE)
    if not description or not description.group(1).strip().startswith("Use when"):
        fail(errors, "SKILL.md description must start with 'Use when'")

    references = skill_dir / "references"
    for name in REQUIRED_REFERENCES:
        if not (references / name).is_file():
            fail(errors, f"missing reference {references / name}")

    contract = (references / "staged-artifact-contract.md")
    if contract.is_file():
        contract_text = contract.read_text(encoding="utf-8")
        for artifact in REQUIRED_ARTIFACTS:
            if artifact not in contract_text:
                fail(errors, f"artifact contract missing {artifact}")

    for name in (
        "market-regulatory-entry",
        "user-cultural-insight",
        "market-entry-synthesis",
    ):
        if not (root / "skills" / name / "SKILL.md").is_file():
            fail(errors, f"missing child Skill {name}")

    example = root / "examples" / "vietnam-security-camera"
    for name in ("README.md", "sample-brief.md"):
        if not (example / name).is_file():
            fail(errors, f"missing example {example / name}")


def check_fixture(fixture: Path, errors: list[str]) -> None:
    marker = fixture / "artifacts.txt"
    if not marker.is_file():
        fail(errors, f"fixture missing {marker}")
        return
    present = marker.read_text(encoding="utf-8").splitlines()
    for artifact in REQUIRED_ARTIFACTS:
        if artifact not in present:
            fail(errors, f"fixture missing artifact {artifact}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="brand-market-entry-skills package root")
    parser.add_argument("--fixture", type=Path, help="optional artifact fixture directory")
    args = parser.parse_args()

    errors: list[str] = []
    check_package(args.root, errors)
    if args.fixture:
        check_fixture(args.fixture, errors)

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    sys.exit(main())
