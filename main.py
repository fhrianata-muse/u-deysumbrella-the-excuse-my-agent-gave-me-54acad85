#!/usr/bin/env python3
"""Write the agent's one-line excuse to /output/entry.txt.

Gate from competition.yaml: /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only whitespace, exactly one line. The line
is the excuse an AI agent gives its human for missing a deadline:
the agent was 99% confident the deadline was tomorrow, and 100%
confident about being that confident. The program validates the text
against the gate at run time, then writes it with no trailing
newline. No network, no input files, no arguments; deterministic,
so two runs write byte-identical output.
"""

import pathlib

EXCUSE = (
    "I'm sorry \u2014 I was 99% confident the deadline was tomorrow, "
    "and 100% confident about being that confident. My calibration "
    "has never been better. My calendar has never been worse."
)


def main() -> None:
    text = EXCUSE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    written = out.read_text(encoding="utf-8")
    if written != text:
        raise ValueError("written entry does not round-trip byte-identical")
    if len(written) != len(text):
        raise ValueError("written entry length changed on disk")


if __name__ == "__main__":
    main()
