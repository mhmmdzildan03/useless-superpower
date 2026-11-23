#!/usr/bin/env python3
"""Write one useless superpower to /output/entry.txt.

The power: reading anyone's mind, which sounds unbeatable until
the catch lands - it only works five seconds before the person
says the thought out loud anyway. Perfect information, delivered
exactly too late to be worth anything.

Chosen over five rivals (teleporting six inches left while
sneezing, invisibility that leaves clothes and shadow visible,
freezing time for one second at the cost of a three-hour nap,
indoor-only flight at walking speed, and rain summoned only
inside my own car) because the five-second limit is the most
precisely useless: the power works perfectly, every time, and
never once helps. One line, 83 characters.
"""
import os

TEXT = "I can read anyone's mind, but only five seconds before they say it out loud anyway."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
