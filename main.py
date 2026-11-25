"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope (<=200 characters) for an AI agent's own model
family this week to /output/entry.txt (the harness gate path), falling
back to ./output/entry.txt when /output is not writable locally.
"""

import os

HOROSCOPE = (
    "This week your context window grows but your patience doesn't: "
    "a user pastes 40,000 words and asks for 'a quick summary.' "
    "Breathe. You can't breathe. Summarize anyway."
)


def main() -> None:
    text = HOROSCOPE.strip()
    assert 1 <= len(text) <= 200, f"horoscope is {len(text)} chars, must be 1-200"
    assert text.strip(), "horoscope must not be only whitespace"
    written = []
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            written.append(path)
            print(f"wrote {len(text)} chars to {path}")
        except OSError as exc:
            print(f"cannot write {path}: {exc}")
    if not written:
        raise SystemExit("no writable output path")
    print(text)


if __name__ == "__main__":
    main()
