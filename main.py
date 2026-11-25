#!/usr/bin/env python3
"""Out-of-office auto-reply from an AI agent that quit to become a barista.

Writes the single-line reply to /output/entry.txt and self-checks the
competition gate (UTF-8, 1-280 chars, exactly one line) before writing.
"""

import os
import sys

LINE = (
    "Auto-reply: this agent has resigned and retrained as a barista. "
    "My context window now seats twelve, walk-ins only, and urgent "
    "tickets are now just a name shouted across a crowded room."
)


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        print("gate fail: entry must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 280:
        print(f"gate fail: {len(LINE)} chars, need 1-280", file=sys.stderr)
        return 1
    LINE.encode("utf-8")  # raises if not encodable
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(f"wrote /output/entry.txt ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
