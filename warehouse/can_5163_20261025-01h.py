"""
Campbell's Soup Can #5163
Produced: 2026-10-25 01:16:36
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
import textwrap

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
CLEAR = "\033[2J\033[H"
HIDE_CURSOR = "\033[?25l"
SHOW_CURSOR = "\033[?25h"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

QUOTE = (
    "I'm not afraid of death; I just don't want to be there when it happens—"
    "especially if there's a waiting room, a clipboard, and no Xanax."
)

WOODY_ART = [
    "   ___",
    "  / _ \\",
    " | (_) |   __",
    "  \\__, |  /  |",
    "    / /  \\  |",
    "   / /____ \\|",
    "  /_/      \\|",
    "         (o.o)",
    "          | |",
    "         /   \\",
]


def type_print(text, color, delay=0.035, pause=0.3):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
        if ch in ".!?—;,":
            time.sleep(pause)
    sys.stdout.write(RESET)


def main():
    sys.stdout.write(CLEAR)
    sys.stdout.write(HIDE_CURSOR)
    try:
        width = 64
        inner_width = width - 4
        border = CYAN + BOLD
        side = border + "|" + RESET
        pad = " " * (width - 2)

        lines = textwrap.wrap(QUOTE, inner_width)

        print()
        print(DIM + WHITE + "Tonight's neurotic philosophical thought:" + RESET)
        print()
        print(border + "+" + "-" * (width - 2) + "+" + RESET)
        print(side + pad + side)

        for line in lines:
            sys.stdout.write(side + "  ")
            type_print(line, YELLOW, delay=0.035, pause=0.3)
            sys.stdout.write(" " * (inner_width - len(line)) + side + "\n")

        print(side + pad + side)
        print(border + "+" + "-" * (width - 2) + "+" + RESET)

        print()
        print(MAGENTA + BOLD + "\n".join(WOODY_ART) + RESET)
        print()
        print(DIM + ITALIC + MAGENTA + "   — Woody Allen (probably, between therapy sessions)" + RESET)
        print()
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()


if __name__ == "__main__":
    main()