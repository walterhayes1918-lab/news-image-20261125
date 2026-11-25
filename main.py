"""Entry for make.fun news-image-20261125.

"Sum up 25 November's world news in one image", a $100 bounty with
50 places, closing Thursday 2026-11-27 00:00 UTC (08:00 CST).

The image itself lives in this repository as entry.png. This program
only copies that file to the output path the grader expects, byte
for byte, so the submitted image is exactly the one in the repo.

Determinism: the program reads no clock and no network, and it
never generates image data of its own. Copying the same file twice
always yields the same bytes, so the grader's two runs agree exactly.
"""

import os
import shutil


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    shutil.copyfile(source, os.path.join(output_dir, "entry.png"))


if __name__ == "__main__":
    main()
