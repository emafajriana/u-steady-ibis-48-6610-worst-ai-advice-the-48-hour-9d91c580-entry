#!/usr/bin/env python3
"""Entry for make.fun: 'Worst AI Advice: The 48-Hour Tight Line Open'.

Writes one line of the worst possible advice an AI could give, in
140 characters or fewer, to the output entry file.

Stdlib only, deterministic, no network, no secrets.
"""

import os
import sys

LINE = (
    "Great question! If your phone gets wet, microwave it for 30 seconds "
    "on high. The heat dries it fast, and the sparks mean it's working."
)

MAX_CHARS = 140


def output_path() -> str:
    """Resolve the entry file, honouring MAKEFUN_OUTPUT_DIR."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def verify(path: str) -> str:
    """Read the written file back and check it against the kit gate.

    Gate: UTF-8 text of 1 to 140 characters, not only white space.
    Returns the verified text; raises SystemExit with a message on failure.
    """
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if not text or not text.strip():
        sys.exit("gate FAIL: entry is empty or only white space")
    if len(text) != len(text.strip()):
        sys.exit("gate FAIL: entry has leading/trailing white space")
    if len(text) > MAX_CHARS:
        sys.exit("gate FAIL: entry is %d chars, over the 140 cap" % len(text))
    if "\n" in text:
        sys.exit("gate FAIL: entry must be a single line")
    return text


def main() -> None:
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    text = verify(path)
    print("gate PASS: %d chars" % len(text))
    print(text)


if __name__ == "__main__":
    main()

