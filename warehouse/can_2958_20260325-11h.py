"""
Campbell's Soup Can #2958
Produced: 2026-03-25 11:08:09
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

# ANSI color codes
RED   = "\033[31m"
GREEN = "\033[32m"
YELLOW= "\033[33m"
BLUE  = "\033[34m"
MAGENTA= "\033[35m"
CYAN  = "\033[36m"
RESET = "\033[0m"

def type_with_color(text, color, delay=0.05):
    """Print text character by character with a given color."""
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET)

def main():
    # Woody Allen‑style philosophical one‑liner
    quote = "I'm not afraid of dying; I just don't want to be there when it happens, especially if it's during brunch."

    # Build a simple box around the quote
    width = len(quote) + 4
    top_border    = "╔" + "═" * width + "╗"
    empty_line    = "║" + " " * width + "║"
    bottom_line   = empty_line
    bottom_border = "╚" + "═" * width + "╝"

    # Animate the box with different colors
    for ch in top_border:
        sys.stdout.write(MAGENTA + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.008)
    print()

    for ch in empty_line:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.008)
    print()

    # Left border, then the quote, then right border
    sys.stdout.write(YELLOW + "║  " + RESET)
    sys.stdout.flush()
    type_with_color(quote, CYAN, delay=0.04)
    sys.stdout.write(YELLOW + "  ║" + RESET + "\n")
    sys.stdout.flush()

    for ch in bottom_line:
        sys.stdout.write(YELLOW + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.008)
    print()

    for ch in bottom_border:
        sys.stdout.write(MAGENTA + ch + RESET)
        sys.stdout.flush()
        time.sleep(0.008)
    print()

if __name__ == "__main__":
    main()