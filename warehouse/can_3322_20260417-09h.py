"""
Campbell's Soup Can #3322
Produced: 2026-04-17 09:48:13
Worker: NVIDIA: Nemotron 3 Super (free) (nvidia/nemotron-3-super-120b-a12b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright variants for background
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"


def cprint(text: str, color: str = RESET, end: str = "\n"):
    """Print colored text and flush immediately."""
    sys.stdout.write(color + text + RESET + end)
    sys.stdout.flush()


def typewriter_line(line: str, delay: float = 0.05, color: str = YELLOW):
    """Print a line character by character with a slight delay."""
    for ch in line:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)  # ensure reset after line
    sys.stdout.flush()


def main():
    quote = (
        "I'm not pessimistic; I'm just well-informed about how terrible "
        "everything will be."
    )
    width = 50  # inner width of the box
    wrapped = textwrap.wrap(quote, width=width)

    # Box colors
    border_color = CYAN + BOLD
    left_right = border_color + "|" + RESET

    # Top border
    print()
    cprint(" " + "_" * (width + 2), border_color)
    # Print each line with typewriter effect
    for line in wrapped:
        # Pad line to width
        padded = line.ljust(width)
        sys.stdout.write(left_right)
        typewriter_line(padded, delay=0.04, color=YELLOW)
        sys.stdout.write(left_right + "\n")
        sys.stdout.flush()
        time.sleep(0.1)  # pause between lines
    # Bottom border
    cprint(" " + "‾" * (width + 2), border_color)
    print()  # final newline


if __name__ == "__main__":
    main()