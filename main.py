"""food-picture-01 entry: copies the bundled food photograph to the output.

The picture (image.jpg, beside this file) is a 1024x1024 JPEG of a steaming
tonkotsu ramen bowl: glossy chashu, a jammy soft egg, nori and spring onions,
shot from overhead. The grader reads exactly one file, entry.png, from the
output directory; the format is told apart by its first bytes, so the JPEG
bytes are copied unchanged under that name.

At trial time the repository is mounted read-only at an arbitrary working
directory, so the source is resolved relative to this file, never the cwd,
and the output directory is created if it does not exist yet. The copy is a
plain byte stream in fixed-size chunks: two runs write exactly the same
bytes. Standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "image.jpg"
CHUNK_SIZE = 64 * 1024


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    with SOURCE.open("rb") as src, dest.open("wb") as dst:
        while True:
            chunk = src.read(CHUNK_SIZE)
            if not chunk:
                break
            dst.write(chunk)


if __name__ == "__main__":
    main()
