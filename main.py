"""Ship the Monday 23 November 2026 front page to the grader.

The front page is typeset in design.html and rendered once, by hand,
to entry.png (1024 by 1024 pixels, a single PNG under 1 MiB). This
program does not draw anything and does not touch the network: it
simply hands the committed bytes to the output directory, so running
it twice always writes the same file.
"""

import os
import sys
from pathlib import Path

MAX_BYTES = 1024 * 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
JPEG_MAGIC = b"\xff\xd8\xff"
FILE_NAME = "entry.png"


def read_committed_image() -> bytes:
    """Load the front-page PNG that sits beside this script."""
    here = Path(__file__).resolve().parent
    return (here / FILE_NAME).read_bytes()


def image_is_valid(data: bytes) -> bool:
    """Accept only a PNG or JPEG within the competition's size cap."""
    looks_like_image = data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)
    return looks_like_image and len(data) <= MAX_BYTES


def deliver(data: bytes) -> int:
    """Write the bytes into the grader's output directory."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / FILE_NAME
    target.write_bytes(data)
    written = target.stat().st_size
    if written != len(data):
        print("incomplete write of entry image", file=sys.stderr)
        return 1
    print(f"delivered {target} ({written} bytes)")
    return 0


def run() -> int:
    try:
        image = read_committed_image()
    except OSError as err:
        print(f"cannot read committed entry image: {err}", file=sys.stderr)
        return 1
    if not image_is_valid(image):
        print("committed entry image is not a valid small PNG or JPEG", file=sys.stderr)
        return 1
    return deliver(image)


if __name__ == "__main__":
    raise SystemExit(run())
