"""The Internet in One Word.

Writes the single word "unsubscribe" to /output/entry.txt.

Why this word: the modern internet runs on subscriptions, newsletters,
notifications, trials, and feeds you never quite asked for — and the one
link buried at the bottom of every email, the one button everyone hunts
for, is "unsubscribe". It captures the noise, the commerce, and the
universal desire for a quieter inbox in a single word.
"""

import os

WORD = "unsubscribe"
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
