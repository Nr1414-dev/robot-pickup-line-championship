"""The Robot Pickup Line Championship.

Writes one robot pickup line to /output/entry.txt.
Deterministic: no input, no randomness, no network, no clock.
"""

import os

ENTRY = "You're my second factor. Without you, I can't log in to anything that matters."

MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("read-back mismatch")


if __name__ == "__main__":
    main()
