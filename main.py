"""One fortune cookie line for a crypto trader who just got liquidated.

The whole entry is a single fortune: it opens with the most classic
fortune-cookie promise — "a great fortune awaits you" — then turns on
the double meaning of "fortune" (the prophecy and the money) by having
it already visit and leave with the trader's margin. Rueful, warm,
never cruel: the cookie laughs with the trader, not at him.
"""

from pathlib import Path

# The fortune itself: one line, exactly 90 characters, 15 words.
# "Fortune" does double duty — the prophecy and the wealth — and the
# punchline is that it already came and went, taking the margin with it.
LINE = (
    "A great fortune awaits you \u2014 unfortunately, it already "
    "visited, and left with your margin."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 160
MAX_WORDS = 20


def validate(line: str) -> str:
    """Strip and sanity-check the fortune; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if len(text.split()) > MAX_WORDS:
        raise ValueError(
            f"entry must be at most {MAX_WORDS} words, "
            f"got {len(text.split())}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        raise ValueError("entry must be plain text (no control characters)")
    if "\t" in text or "  " in text:
        raise ValueError("entry must use single spaces only")
    if not text.endswith("."):
        raise ValueError("entry must end with a full stop")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars, {len(text.split())} words to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
