"""Sorry, I Heard That Wrong — make.fun entry.

Reads the single-line apology from entry.txt (next to this file),
validates it against the competition gate (1-140 characters, one
line, UTF-8, not only whitespace), writes it to /output/entry.txt
when that directory exists, and prints it to stdout.
"""

from pathlib import Path

MAX_CHARS = 140


def load_entry() -> str:
    """Read the entry line from entry.txt beside this file."""
    path = Path(__file__).with_name("entry.txt")
    text = path.read_text(encoding="utf-8")
    return normalise_line(text)


def write_output(line: str) -> None:
    """Best-effort write of the entry for the grader's /output/entry.txt."""
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


def normalise_line(raw: str) -> str:
    """Drop a trailing newline and surrounding space; keep inner text."""
    return raw.strip("\n").strip()


def validate_entry(line: str) -> str:
    """Check the line against the gate; return it unchanged if valid."""
    if not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over {MAX_CHARS}")
    return line


def main() -> None:
    line = validate_entry(load_entry())
    try:
        write_output(line)
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
