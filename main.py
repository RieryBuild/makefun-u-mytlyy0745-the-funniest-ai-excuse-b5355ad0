"""Write the entry's one-line AI excuse to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

LINE = "I read all 47 pages of your file, fell in love with page 31, and eloped with it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
