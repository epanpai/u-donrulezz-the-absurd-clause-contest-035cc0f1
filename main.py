#!/usr/bin/env python3
"""The Absurd Clause Contest entry.

Writes exactly one absurd terms-of-service clause to /output/entry.txt
(1-200 UTF-8 chars, not only whitespace), as the sealed scorer's gate
requires. Deterministic, stdlib only, no network, no secrets, no randomness.
"""

import os

ENTRY = "By using this service, you agree that your shadow is company property and may be repossessed without notice during daylight hours."

# Why this line: eight candidates were drafted and program-counted (see
# BUILD_LOG.md). This one won because it opens as the most ordinary TOS
# sentence imaginable, then claims ownership of the reader's shadow, and
# the kicker lands on the internal logic — repossession can only happen
# during daylight hours, because that is when a shadow exists. Concrete
# image, no setup, no explanation; the legal register does the ambush.


def main():
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 200 characters, not only whitespace. Fail loudly
    # here instead of shipping a rejected entry.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in ENTRY), "entry has control characters"
    # The task requires a single original English sentence: exactly one
    # sentence terminator, at the very end.
    assert sum(ENTRY.count(c) for c in ".!?") == 1, "entry must be one sentence"
    assert ENTRY.endswith("."), "entry must end with its single period"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back byte-for-byte: what is on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
