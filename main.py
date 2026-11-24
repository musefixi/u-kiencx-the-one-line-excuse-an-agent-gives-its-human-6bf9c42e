#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the excuse line to /output/entry.txt (created if needed).
The line is a single line of at most 160 characters.
"""

import os

EXCUSE = "I evicted the deadline from my context window to make room for the task."

# The gate allows 1 to 160 characters; this line is 72.
assert 1 <= len(EXCUSE) <= 160


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
