import os

# Writes one relaxed text (TEXT) to entry.txt in MAKEFUN_OUTPUT_DIR, defaulting to /output.
TEXT = (
    "Your eyes are closed. The voice above you goes on, slow.\n"
    "A page turns. A page turns.\n"
    "You gave up the words a while ago. That is allowed.\n"
    "The last page turns, and the voice reads on a little past the end,\n"
    "the way a hand stays on a back long after the back goes quiet."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
