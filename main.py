"""Write the painfully honest out-of-office auto-reply to entry.txt.

Pure Python stdlib (os only), deterministic, no network.
Writes one line plus a trailing newline to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

LINE = "I'm away and won't be checking email, because after 400 unread messages my enthusiasm for the inbox needs a holiday too, so thank you for your patience and I'll reply on my return."


def main():
    if not (1 <= len(LINE) <= 200):
        print(f"error: entry line is {len(LINE)} characters, must be 1-200",
              file=sys.stderr)
        sys.exit(1)
    if LINE.strip() == "":
        print("error: entry line is only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
