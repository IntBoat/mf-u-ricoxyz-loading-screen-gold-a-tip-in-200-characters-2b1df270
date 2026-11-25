#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — a make.fun one-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = "Tip: while this loads, remember that somewhere a developer is also waiting for a build, staring at the same spinner, questioning the same life choices."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
