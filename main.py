"""One-Line Office Joke: 24-Hour Sprint — make.fun entry.

Writes one funny one-line office joke to /output/entry.txt.
"""

import os

JOKE = (
    "Our stand-up meeting has been sitting down for forty minutes, "
    "and someone just suggested we schedule a follow-up to decide when it ends."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
