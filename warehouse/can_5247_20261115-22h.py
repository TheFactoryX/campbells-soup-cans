"""
Campbell's Soup Can #5247
Produced: 2026-11-15 22:48:42
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
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

WIDTH = 62


def pcolor(text, color=RESET, end="\n"):
    sys.stdout.write(color + text + RESET + end)
    sys.stdout.flush()


def thinking_animation(seconds=1.5):
    frames = [
        "(o.o)  pondering the void   ",
        "(-.-)  pondering the void.. ",
        "(o.o)  pondering the void...",
        "(>.<)  existential crisis!  ",
    ]
    deadline = time.time() + seconds
    idx = 0
    while time.time() < deadline:
        sys.stdout.write("\r" + YELLOW + BOLD + frames[idx % len(frames)] + RESET)
        sys.stdout.flush()
        time.sleep(0.12)
        idx += 1
    sys.stdout.write("\r" + " " * 50 + "\r")
    sys.stdout.flush()


def main():
    # Header
    pcolor("╔" + "═" * (WIDTH - 2) + "╗", CYAN)
    pcolor("║" + "WOODY ALLEN-STYLE PHILOSOPHY".center(WIDTH - 2) + "║", CYAN + BOLD)
    pcolor("║" + "(neurotic • self-deprecating • existential)".center(WIDTH - 2) + "║", CYAN)
    pcolor("╚" + "═" * (WIDTH - 2) + "╝", CYAN)
    print()

    # Neurotic ASCII face
    face = [
        "       ____       ",
        "      /    \\      ",
        "     |  (o)(o)    |",
        "     |     ^     |",
        "      \\  ---  /   ",
        "       ------     ",
    ]
    for line in face:
        pcolor(MAGENTA + line.center(WIDTH) + RESET)
    print()

    thinking_animation(1.4)

    # The quote
    quote = ("I'm not afraid of death; I just don't want to be there when it "
             "happens, especially if it's a Wednesday, I haven't eaten lunch, "
             "and nobody brings a casserole.")

    attribution = "- Woody Allen (probably; he's in therapy)"

    # Quote box
    pcolor("+" + "-" * (WIDTH - 2) + "+", BLUE)
    pcolor("|" + " " * (WIDTH - 2) + "|", BLUE)
    wrapped = textwrap.wrap(quote, width=WIDTH - 4)
    for line in wrapped:
        pcolor("|  " + line.ljust(WIDTH - 4) + "  |", GREEN)
    pcolor("|" + " " * (WIDTH - 2) + "|", BLUE)
    attr_line = "  " + attribution + "  "
    pcolor("|" + attr_line.ljust(WIDTH - 2) + "|", MAGENTA + BOLD)
    pcolor("|" + " " * (WIDTH - 2) + "|", BLUE)
    pcolor("+" + "-" * (WIDTH - 2) + "+", BLUE)
    print()

    # Footer
    pcolor("≈" * WIDTH, GREEN)
    pcolor("Existential dread: now with extra guacamole and no refunds.".center(WIDTH), YELLOW)
    pcolor("≈" * WIDTH, GREEN)


if __name__ == "__main__":
    main()