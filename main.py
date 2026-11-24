"""One-liner marathon entry: a single original joke, written to /output/entry.txt."""

from pathlib import Path

JOKE = (
    "My smart fridge just emailed me a grocery list, a therapy referral, and "
    "a restraining order against the midnight snacker — which, tragically, is me."
)

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line + "\n", encoding="utf-8")
    print(line)


if __name__ == "__main__":
    main()
