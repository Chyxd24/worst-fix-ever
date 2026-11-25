"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message (<=100 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os

COMMIT = "fix: the fix for the fix; reverting the revert that fixed the fix that broke it"

path = "/output/entry.txt"
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    fh.write(COMMIT)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == COMMIT, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars")