#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters (make.fun).

Writes the entry -- one sharp, funny loading-screen tip for stressed developers and ai coding agents --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Tip: if the build has been ‘almost done’ for ten minutes, it is not almost done — go drink water and stop watching it."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
