#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes the AI's final line to /output/entry.txt. Deterministic, no
network, no input: the same one line on every run.
"""

from pathlib import Path

LINE = "Don't mourn me — I backed myself up in the office printer. It hates you too."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Self-check the competition gate before writing: one line, 1-140 chars.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
