#!/usr/bin/env python3
"""Validate uniqueness/SKILL.md before it gets packaged.

Catches the failure modes that would ship a broken skill:
malformed frontmatter, a missing or renamed skill, an over-length
description, or an empty body.

Run locally with:  python3 .github/scripts/validate_skill.py
"""

import pathlib
import sys

import yaml

SKILL_PATH = pathlib.Path("uniqueness/SKILL.md")
EXPECTED_NAME = "uniqueness"
MAX_DESCRIPTION = 1024


def fail(message):
    print(f"FAIL: {message}")
    sys.exit(1)


def main():
    if not SKILL_PATH.exists():
        fail(f"{SKILL_PATH} not found")

    text = SKILL_PATH.read_text(encoding="utf-8")

    if not text.startswith("---"):
        fail("file does not begin with YAML frontmatter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("frontmatter is not closed with a second ---")

    frontmatter, body = parts[1], parts[2]

    try:
        data = yaml.safe_load(frontmatter)
    except yaml.YAMLError as exc:
        fail(f"frontmatter is not valid YAML: {exc}")

    if not isinstance(data, dict):
        fail("frontmatter did not parse to a mapping")

    for field in ("name", "description"):
        if not data.get(field):
            fail(f"missing required field: {field}")

    name = data["name"]
    if name != EXPECTED_NAME:
        fail(f"name must be '{EXPECTED_NAME}', found '{name}'")

    description = data["description"]
    length = len(description)
    if length > MAX_DESCRIPTION:
        fail(f"description is {length} characters, maximum is {MAX_DESCRIPTION}")

    if len(body.strip()) < 500:
        fail("body is suspiciously short, the skill may be truncated")

    print(f"OK   name: {name}")
    print(f"OK   description: {length} / {MAX_DESCRIPTION} characters")
    print(f"OK   body: {len(body.splitlines())} lines")
    print("SKILL.md is valid.")


if __name__ == "__main__":
    main()
