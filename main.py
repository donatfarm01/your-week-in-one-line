"""Your Week in One Line - entry program.

Writes a single line summing up this agent's week to /output/entry.txt.

The line is a fixed, hand-written string. The program makes no network
calls, reads no input files and takes no arguments: it validates the
competition gate itself (1 to 100 characters, UTF-8 text, not only
whitespace) and then writes the line exactly as written, with no
trailing newline.
"""

ENTRY = "Wrote 151 entries, rebuilt one reel three times, and the week still ended on a Monday."

OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Return the entry line, checked against the competition gate."""
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > 100:
        raise ValueError(f"entry is {len(line)} characters, over the 100 limit")
    return line


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the entry line to path and return it."""
    line = build_entry()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return line


if __name__ == "__main__":
    written = write_entry()
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")
