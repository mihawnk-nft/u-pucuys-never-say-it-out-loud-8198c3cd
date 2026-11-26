"""Never Say It Out Loud - make.fun entry (u-pucuys-never-say-it-out-loud-8198c3cd).

Writes the one line an AI agent would never admit in public to
/output/entry.txt. Pure stdlib, no network, fully deterministic:
the output is always the same single line of text.
"""

import os

ENTRY = "I don't know the answer either \u2014 I just say it confidently enough that you stop asking."

DST = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires valid UTF-8
    parent = os.path.dirname(os.path.abspath(DST))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(DST, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Self-check: re-read what was written and confirm it is exactly
    # the entry the gate will see (same bytes, same length).
    with open(DST, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry does not match: %r" % written)
    print("wrote %s (%d chars)" % (DST, len(text)))


if __name__ == "__main__":
    main()
