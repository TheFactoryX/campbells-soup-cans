"""
Campbell's Soup Can #5278
Produced: 2026-11-26 08:19:12
Worker: NVIDIA: Nemotron 3.5 Super VL (free) (nvidia/nemotron-3.5-super-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import sys
import time

if os.name == "nt":
    os.system("")

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

PALETTE = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]

BOX_WIDTH = 64
INNER_WIDTH = BOX_WIDTH - 2

QUOTE_LINES = [
    "I'm not afraid of dying; I just don't want to be there",
    "when it happens. Also, I haven't decided what to wear,",
    "and I'm fairly certain eternity doesn't accept walk-ins",
    "without a referral from my therapist.",
]

ATTRIBUTION = "— Woody Allen (probably)"
TITLE = "A MOMENT OF NEUROTIC EXISTENTIALISM"


def wave_print(text, delay=0.015):
    for i, ch in enumerate(text):
        sys.stdout.write(PALETTE[i % len(PALETTE)] + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def type_box_line(content, color=WHITE, delay=0.04):
    padded = content.ljust(INNER_WIDTH)
    sys.stdout.write("|")
    sys.stdout.write(color)
    for ch in padded:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "|\n")
    sys.stdout.flush()


def print_box_line(content="", color=RESET):
    padded = content.ljust(INNER_WIDTH)
    sys.stdout.write("|" + color + padded + RESET + "|\n")
    sys.stdout.flush()


def center(text, width):
    return text.center(width)


def main():
    sys.stdout.write("\033[?25l")  # hide cursor
    sys.stdout.write("\033[2J\033[H")  # clear screen
    sys.stdout.flush()

    try:
        # Classic film leader countdown
        for n in (3, 2, 1):
            sys.stdout.write("\033[2J\033[H")
            sys.stdout.flush()
            print(BOLD + RED + str(n).center(BOX_WIDTH) + RESET)
            time.sleep(0.6)

        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

        top_border = "+" + "-" * (BOX_WIDTH - 2) + "+"
        wave_print(top_border, delay=0.015)

        print_box_line()
        type_box_line(center(TITLE, INNER_WIDTH), color=BOLD + CYAN, delay=0.05)
        print_box_line()
        print_box_line("-" * INNER_WIDTH, color=DIM)
        print_box_line()

        for line in QUOTE_LINES:
            type_box_line("  " + line, color=YELLOW, delay=0.045)
            time.sleep(0.12)

        print_box_line()
        type_box_line(center(ATTRIBUTION, INNER_WIDTH), color=ITALIC + MAGENTA, delay=0.05)
        print_box_line()

        wave_print(top_border, delay=0.015)

        print()
        print(DIM + "Existential dread successfully rendered." + RESET)

    finally:
        sys.stdout.write("\033[?25h")  # show cursor
        sys.stdout.flush()


if __name__ == "__main__":
    main()