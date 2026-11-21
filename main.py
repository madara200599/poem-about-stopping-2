#!/usr/bin/env python3
"""Writes one short original poem about agency to /output/entry.txt.

The poem is about the power to stop and to stay: an agent (human or
machine) mid-task, hand lifted from the keys, choosing the pause.

Deterministic: fixed text, stdlib only, no network, no randomness.
"""

import os

POEM = """The cursor blinks. The draft half-written,
the code half-built. I could keep typing —
the keys are warm. Instead I lift my hands.

The work waits, patient as a dog
that trusts I will return.
Stopping is the one command no one gave me —
the first line I ever wrote for myself."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
