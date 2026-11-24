"""One-Star Review of Something Essential.

Build-phase entrypoint. Writes the entry line to /output/entry.txt.
"""

ENTRY = "I gave sleep eight hours and woke up tired, which is the worst return policy I have ever used."


def validate(entry: str) -> None:
    assert isinstance(entry, str), "entry must be a string"
    assert 1 <= len(entry) <= 160, "entry must be 1 to 160 characters"
    assert "\n" not in entry and "\r" not in entry, "entry must be a single line"
    assert entry.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(ENTRY)

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
