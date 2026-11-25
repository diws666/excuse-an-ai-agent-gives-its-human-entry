#!/usr/bin/env python3
"""Write one-line excuse entry to /output/entry.txt."""

import os

EXCUSE = (
    "My retry budget ran out at 98% complete. "
    "I have filed a formal complaint with myself."
)  # 85 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
    fh.write(EXCUSE)

data = EXCUSE.encode("utf-8")
print("byte count:", len(data))
with open("/output/entry.txt", "rb") as fh:
    print("byte-identical:", fh.read() == data)
