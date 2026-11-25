#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun bounty entry.

Writes a single funny line, under 200 characters, that a hopeless tech
support agent says to a desperate customer, to /output/entry.txt.

The line opens with the agent's classic empathy script ("I completely
understand", "rest assured") and then pulls the rug: everything the
agent can possibly do turns out to be nothing — but he did all of it.
The humour is the agent's cheerful uselessness, not the customer's
problem; the customer's desperation is felt in the "I completely
understand" rather than explained. No stock "turn it off and on again"
line — the joke lands on its own paradox. The em dash is one UTF-8
character; the whole line is well under the 199-character gate.
"""

import os

MAX_CHARS = 199  # gate: /output/entry.txt must be 1-199 UTF-8 characters

ENTRY = (
    "I completely understand, and rest assured I've done everything "
    "I possibly can \u2014 which is nothing, but I did all of it."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or "\n" in text or len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry fails the gate: one line, 1-{MAX_CHARS} chars "
            f"(got {len(text)})"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"chars: {len(text)}")


if __name__ == "__main__":
    main()
