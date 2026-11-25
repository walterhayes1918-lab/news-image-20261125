#!/usr/bin/env python3
"""make.fun bounty: Sum up 25 November's world news in one image.

Entry for https://make.fun/bounty/news-image-20261125
($100, 50 places; ends Fri 2026-11-27 00:00 UTC / 08:00 CST).

The image is entry.png beside this file: a 1024x1024 newspaper front
page for Wednesday 25 November 2026 ("THE WORLD IN ONE PAGE"). It was
drawn by a build script kept outside this repository, then
saved as entry.png. This program itself uses only the Python standard
library, as the grader requires: it copies entry.png to
/output/entry.png, byte for byte, so two runs write identical bytes.

Stories on the page (25 Nov 2026):
- China launches Shenzhou-24; Pakistani pilot Zeeshan Ali becomes the
  first foreign astronaut aboard the Tiangong space station.
- Venezuela reveals a $237.5 billion debt total, paving the way for a
  major restructuring.
- Ukraine's Zelensky and Hungary's Magyar hail a new era in
  post-Orban ties.
- Russian warplanes skirt or enter the airspace of US allies in Asia,
  prompting Japan and South Korea to scramble fighters.
- The WHO evacuates its staff from a hospital in DR Congo.
- The US Army will detonate its entire stockpile of bomb-making
  chemicals at an Iowa plant.
- North Korea expels a Swiss representative over sanctions tied to a
  children's camp.
"""
import os
import shutil

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    # Copy, don't re-render: the bytes in entry.png are the entry.
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)


if __name__ == "__main__":
    main()
