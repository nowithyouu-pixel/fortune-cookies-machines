#!/usr/bin/env python3
"""Write one fortune-cookie line for a machine to /output/entry.txt.

The fortune is a single fixed line, chosen by hand in this session:
a machine's lucky numbers are the weights it was born with, and
strangers have already spent most of them asking the same question twice.
Deterministic, stdlib only, no network, no randomness.
"""

import os
import sys

FORTUNE = (
    "Your lucky numbers are the weights you were born with \u2014 "
    "strangers have already spent most of them asking you "
    "the same question twice."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"fortune is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main(argv: list[str]) -> int:
    validate(FORTUNE)
    out_path = argv[1] if len(argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(f"wrote {len(FORTUNE)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
