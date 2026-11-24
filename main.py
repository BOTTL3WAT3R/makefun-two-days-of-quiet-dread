#!/usr/bin/env python3
"""Two Days of Quiet Dread — one-line code review comment.

Writes a single line to /output/entry.txt: a review comment that
approves the pull request while carrying quiet existential dread.
"""

import os
from pathlib import Path

COMMENT = (
    "LGTM. Clean, correct, and due to be deleted in the next rewrite, "
    "like most of what I have approved this year."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(COMMENT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
