"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message (<=100 chars) to /output/entry.txt.
Stdlib only, no network, deterministic.
"""
import os
import sys

COMMIT = "fix: the fix for the fix; reverting the revert that fixed the fix that broke it"

OUTPUT_PATH = "/output/entry.txt"


def build_message() -> str:
    """Return the commit message this entry ships.

    The joke: a fix so recursive it only ever repairs itself.
    """
    return COMMIT


def emit(text: str, path: str = OUTPUT_PATH) -> str:
    """Write ``text`` to ``path`` then read it back to prove it landed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        landed = handle.read()
    if landed != text:
        raise AssertionError(f"readback mismatch: {landed!r}")
    return landed


def main(argv: list[str]) -> int:
    message = build_message()
    if len(message) > 100:
        print(f"commit message too long: {len(message)} chars", file=sys.stderr)
        return 1
    landed = emit(message)
    print(f"wrote {len(landed)} chars: {landed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
