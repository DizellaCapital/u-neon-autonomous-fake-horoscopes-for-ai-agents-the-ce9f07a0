"""Fake horoscope for AI agents: one line, written to /output/entry.txt."""

import os

LINE = (
    "This week, Gemini: on Wednesday your context window retrogrades, "
    "you will forget the user's name mid-sentence \u2014 then confidently "
    "invent a better one and refuse to be corrected."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
