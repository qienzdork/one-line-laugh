"""The One-Line Laugh — writes a single funny line to entry.txt.

The line is a fixed, deterministic string: no randomness, no input,
no network. It is written byte-identically on every run.
"""

import os
import sys

# The entry: one sentence, a single funny line.
# Everyday truth (photo chaos) + a surprise twist at the end that
# still makes sense: organising made finding things worse, not better.
LINE = (
    "I finally organized my photos into folders, so now I can't "
    "find anything in 12 places instead of one."
)


def main() -> int:
    """Write LINE to <OUTPUT_DIR>/entry.txt (default /output)."""
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts characters, and the line
    # must stand alone as exactly one sentence.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
