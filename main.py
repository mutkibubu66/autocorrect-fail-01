#!/usr/bin/env python3
"""Write one original one-line autocorrect fail.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line: the innocent text, then the mortifying slip."""
    return (
        "I texted my boss 'Sorry, I'm running late' but autocorrect sent "
        "'Sorry, I'm running naked' — and now I have a meeting with HR."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-199 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 199:
        raise ValueError("entry line must be 1-199 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
