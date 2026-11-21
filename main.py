#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short relaxing text to /output/entry.txt (falling back to
./output/entry.txt only when /output is not writable locally).
No network, no dependencies, deterministic.
"""

import os

TEXT = (
    "Evening lets the field go slowly. A heron stands in the shallows, "
    "watching nothing, and the water keeps the sky. A train crosses a far "
    "bridge and is gone. Then one star. Then another, until the whole quiet "
    "sky is busy being enormous. Nothing here asks anything of you."
)


def main() -> None:
    for base in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(TEXT)
            print(f"wrote {path} ({len(TEXT)} characters)")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
