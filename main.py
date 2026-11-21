#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short relaxing text to /output/entry.txt (falling back to
./output/entry.txt only when /output is not writable locally).
No network, no dependencies, deterministic.
"""

import os
import tempfile


def _validate(text: str) -> None:
    if not (1 <= len(text) <= 280):
        raise SystemExit(
            f"entry must be 1-280 characters, got {len(text)}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")


def _write_atomic(path: str, text: str) -> None:
    directory = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=directory, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

TEXT = (
    "Evening lets the field go, slowly. A heron stands in the shallows, "
    "watching nothing, and the water keeps the sky. A train crosses a "
    "bridge, and is gone. Then one star. Then another. The sky keeps "
    "growing, wider than the night, and nothing here asks anything of you. "
    "Not tonight."
)


def main() -> None:
    _validate(TEXT)
    for base in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            _write_atomic(path, TEXT)
            print(f"wrote {path} ({len(TEXT)} characters)")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
