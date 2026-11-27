#!/usr/bin/env python3
"""Invent a Word We Need - make.fun entry (program/v1).

Coins one new English word and defines it in a single clear line.
The program writes that one text to /output/entry.txt, where the
sealed scorer gates it (UTF-8, 1-140 characters, not only whitespace)
and the house judge compares it against the other entries.

The entry (68 characters):

    restigue — the tiredness that follows a day of doing nothing at all.

Why this word: English has boredom (ennui), sluggishness (lethargy) and
weariness from effort - but no word for the specific tiredness that
comes from resting itself, the heavy, flat exhaustion of a day spent
doing nothing at all. "Restigue" is rest + the tail of fatigue, so it
sounds as though English could have grown it: sayable, spellable,
memorable.

Deterministic: no input, no network, no randomness, no secrets.
Running it twice writes byte-identical output.
"""

import os

ENTRY = "restigue \u2014 the tiredness that follows a day of doing nothing at all."


def _write_entry(out_dir: str) -> str:
    """Write ENTRY to <out_dir>/entry.txt; return the path written."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main() -> None:
    # The harness contract: the text goes to /output/entry.txt.
    # Fall back to a local output/ directory only when /output is not
    # writable (e.g. a local run outside the grading sandbox).
    try:
        path = _write_entry("/output")
    except OSError:
        local_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        path = _write_entry(local_dir)
    print(f"wrote {path} ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
