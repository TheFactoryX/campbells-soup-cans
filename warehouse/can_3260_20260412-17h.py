"""
Campbell's Soup Can #3260
Produced: 2026-04-12 17:52:02
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

def typewriter(text, delay=0.05):
    """Print text character by character with a small delay."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # newline after the whole string

def main():
    # ANSI colour codes
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    CYAN    = "\033[36m"
    YELLOW  = "\033[33m"
    MAGENTA = "\033[35m"

    border_color = CYAN
    text_color   = YELLOW + BOLD

    # A Woody Allen‑style quote (original)
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying — preferably while "
        "still able to enjoy a good bagel."
    )

    width = len(quote) + 4  # padding inside the box

    top    = border_color + "+" + "-" * (width - 2) + "+" + RESET
    empty  = border_color + "|" + " " * (width - 2) + "|" + RESET
    line   = border_color + "|" + text_color + quote.ljust(width - 2) + RESET + border_color + "|" + RESET

    # Animate the drawing of the box
    for part in (top, empty, line, empty, top):
        typewriter(part, delay=0.02)
        time.sleep(0.1)

if __name__ == "__main__":
    main()